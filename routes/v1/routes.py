import json 

from flask import Blueprint, request

from models.sensor_query_model import SensorQueryModel
from models.response_model import ResponseModel, Status
from controller.sensor_data_controller import SensorDataController


v1_bp = Blueprint('v1', __name__, url_prefix='/v1')


@v1_bp.route('/health-check', methods=['GET'])
def health_check(): 
    return {"status": "alive"}

@v1_bp.route('/sensors/<string:sensor_type>', methods=['GET'])
def get_sensor_data(sensor_type):
    try: 
        sensor_data_query = SensorQueryModel(
            deviceType=sensor_type,
            columns= json.loads(request.args.get("columns", []))
        )
        print(sensor_data_query)
        sensor_data =  SensorDataController.get_sensor_data(query_params=sensor_data_query)
        return ResponseModel(status=Status.SUCCESS, result=sensor_data).model_dump_json()
    except Exception as e: 
        return ResponseModel(message=str(e), status=Status.FAILED).model_dump_json(), 500
    