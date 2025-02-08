from pydantic import BaseModel
from typing import List, Dict

class SensorModel(BaseModel): 
    type: str
    parameters: List[str]
    deviceNames: List[str]

    @staticmethod
    def fromJson(src: Dict):
        print(f'raw_json: {src}')
        return SensorModel(
            type=src['type'], 
            parameters=src['parameters'], 
            deviceNames=src['deviceNames']
        )