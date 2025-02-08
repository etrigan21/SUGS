
from typing import Any, Dict 
import paho.mqtt.client as mqtt

from config import mqtt_config
from services.device_configs_service import DeviceConfigHelper
from services.payload_helper import PayloadHelper
from services.database_utils import DatabaseUtils

class MQTTService(): 


    def __init__(self):
        self.client: mqtt.Client = mqtt.Client()
        self.client.username_pw_set(mqtt_config.USERNAME, mqtt_config.PASSWORD)
        self.deviceHelper: DeviceConfigHelper = DeviceConfigHelper()
        self.client.on_connect = self.on_connect
        self.client.on_message= self.on_message
        self.client.connect(mqtt_config.HOST, mqtt_config.PORT)
        self.client.loop_start()


    def on_connect(self,client: mqtt.Client, userdata: object, flags: Dict[str, Any], rc: int) -> None: 
        #The topics used by the mqtt is based on the sensor type. This way, parsing would be easier. 
        print(f'Server connected to MQTT')
        topics = self.deviceHelper.get_sensor_types()
        for topic in topics: 
            print(f'topic: {topic}')
            client.subscribe(topic=topic)


    def on_message(self, client: mqtt.Client, userdata: object, msg: mqtt.MQTTMessage) -> None: 
        print(f'topic: {msg.topic}, payload: {msg.payload.decode()}')
        #once the message is received, parse the data 
        #Since the payload can vary, it might be difficult to create a class for it. It's better to parse it as is. 
        try: 
            sensor_type_params = self.deviceHelper.get_parameters_for_type(sensor_type=msg.topic)
            parsed_payload = PayloadHelper.convert_payload_to_dict(payload=msg.payload.decode(), parameters=sensor_type_params)
            table_name = parsed_payload['type']
            del parsed_payload['type']
            #this parsed_payload must be stored in the database
            DatabaseUtils.insert_sensor_data(
                table_name=table_name, 
                insert_params=parsed_payload
            )

            #ToDo: Add decision making based on the bounds set in mounted_device_configs. Currently, only the solenoid valves are the moving parts.
            # Still waiting from the feedback from the agricultural engineer on how to correctly handle the irrigation of a small scale setup. 
            # Possible to use the clientId from the client to identify which valve should be opened
        
        except Exception as e: 
            print(f'exception')
            #ToDo: Handle this exception with logging and possibly notification to client
    
