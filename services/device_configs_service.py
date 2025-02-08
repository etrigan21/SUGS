from sys import path 
import os
import json

from typing import Dict, List, Union

from exceptions.exceptions import ParameterNotFoundExceptions
from models.sensor_models import SensorModel

class DeviceConfigHelper():

    def read_config(self,config_path: str) -> Dict:
        data = None
        with open(config_path, 'r', encoding='utf-8') as file: 
            data = json.loads(file.read())
        return data
    

    def convert_raw_to_sensor_model(self, raw_jsons: Dict) -> List[SensorModel]:
        print(raw_jsons)
        return [SensorModel.fromJson(raw_json) for raw_json in raw_jsons]


    def __init__(self, sensor_config: Union[List[Dict], str] = os.path.abspath(os.path.join(os.path.dirname(__file__), "../mounted_device_configs/sensor_configs.json"))):
        if isinstance(sensor_config, str):
            self.raw_json: Dict = self.read_config(sensor_config)
        else: 
            self.raw_json: Dict = sensor_config
        self.sensor_configs: List[SensorModel] = self.convert_raw_to_sensor_model(raw_jsons=self.raw_json)
        

    def get_sensor_types(self):
        return [sensor_config.type for sensor_config in self.sensor_configs]
    

    def get_parameters_for_type(self, sensor_type: str) -> List[str]: 
        config = next(filter(lambda configs: configs.type  == sensor_type, self.sensor_configs), None)
        if config == None: 
            raise ParameterNotFoundExceptions("Parameter not found")
        return config.parameters