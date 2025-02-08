from flask import Flask

from services.database_utils import DatabaseUtils
from config import file_settings
from services.mqtt_service import MQTTService
from routes.v1.routes import v1_bp


app = Flask(__name__)

app.register_blueprint(v1_bp)

if __name__ == "__main__":
    DatabaseUtils.create_table_from_configs(overwrite=file_settings.overwrite_db)
    MQTTService()

    app.run(debug=True)