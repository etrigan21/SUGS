from typing import Dict, Optional 

from services.database_utils import DatabaseUtils
from models.sensor_query_model import SensorQueryModel

class SensorDataController(): 

    @staticmethod
    def get_sensor_data(query_params: SensorQueryModel) -> Dict:
        results = DatabaseUtils.sensor_query_db(
            query_params=query_params
        )

        return results