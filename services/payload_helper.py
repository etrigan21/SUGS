from typing import List

class PayloadHelper(): 

    @staticmethod
    def convert_payload_to_dict(payload: str, parameters: List[str]):
        """
            This method converts the comma separated payload into a dict 

            sample payload: 
            
            "sensorTypeA;A;0.4;30;0.3"

            sample parameters: 

            ["soilMoisture", "temperature", "humidity"]

            returns: 
            {
                "type": "sensorTypeA", 
                "deviceName": "A", 
                "soilMoisture": 0.4, 
                "temperature": 30, 
                "humidity": 0.3
            }
        """

        complete_params = ["type", "deviceName", *parameters]

        body = {}
        split_payload = payload.split(";")
        for i in range(0, len(complete_params)): 
            if complete_params[i] == "type" or complete_params[i] == "deviceName":
                body[complete_params[i]] = split_payload[i]
            else: 
                body[complete_params[i]] = float(split_payload[i])
        return body

