from contextlib import contextmanager

import sqlite3
from typing import Dict

from services.device_configs_service import DeviceConfigHelper
from config import file_settings
from services.file_utils import FileUtils
from exceptions.exceptions import DatabaseException
from models.sensor_models import SensorModel
from models.sensor_query_model import SensorQueryModel

#In order to save processing power since this project might be ran on raspberry pi zero, the database chosen is SQLite

class DatabaseUtils(): 

    @staticmethod
    @contextmanager
    def db_session(db_path: str): 
        conn = sqlite3.connect(db_path)
        conn.execute('PRAGMA journal_mode=WAL;')
        try: 
            yield conn 
        finally: 
            conn.close()


    def create_table_sql_from_field_array(config: SensorModel):
        fields = ["id", "deviceName", *config.parameters]
        sql_fields = []

        for field in fields: 
            if field == "id": 
                sql_fields.append('id INTEGER PRIMARY KEY AUTOINCREMENT')
            elif field == "deviceName": 
                sql_fields.append('deviceName TEXT')
            else: 
                sql_fields.append(f'{field} REAL')

        merged_sql_fields = ", ".join(sql_fields)
        table_name = config.type
        create_table_sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({merged_sql_fields});'
        return create_table_sql


    @staticmethod
    def create_table_from_configs(overwrite: bool = False):
        try: 
            FileUtils.create_path(directory=file_settings.operations_path)

            if overwrite: 
                DatabaseUtils.delete_database()

            deviceConfigHelper = DeviceConfigHelper()

            for config in deviceConfigHelper.sensor_configs: 
            
                create_table_sql = DatabaseUtils.create_table_sql_from_field_array(config=config)

                with DatabaseUtils.db_session(file_settings.database_path) as conn: 
                    conn.execute(create_table_sql)
                    conn.commit()

        except Exception as e:
                raise DatabaseException(str(e))


    @staticmethod
    def delete_database():
        FileUtils.delete_file(file_path=file_settings.database_path)

    
    @staticmethod
    def insert_sensor_data(table_name: str, insert_params: Dict, db_path: str = file_settings.database_path): 
        try: 
            with DatabaseUtils.db_session(db_path=db_path) as conn: 
                values_clause = ", ".join(["?" for _ in range(len(insert_params))])
                query = f'INSERT INTO {table_name} ({", ".join(insert_params.keys())}) VALUES ({values_clause})'
                values = insert_params.values()

                conn.cursor().execute(query, tuple(values))
                conn.commit()

        except sqlite3.Error as e: 
            #ToDo: Add logging here database exceptions needs to halt the program since the whole system will be useless if it cannot insert data to the db. 
            raise DatabaseException(str(e))
            

    @staticmethod
    def sensor_query_db(query_params: SensorQueryModel, db_path: str = file_settings.database_path): 
        try: 
            with DatabaseUtils.db_session(db_path=db_path) as conn: 
                select_fields = ", ".join(query_params.columns)
                query = f'SELECT {select_fields} FROM {query_params.deviceType}'

                if query_params.query: 
                    #Might be risky but this will only be used in select queries 
                    query += f'WHERE {query_params}'                

                if query_params.limit: 
                    query += f' LIMIT {query_params.limit}'

                query+= ";"

                print(query)

                conn.cursor().execute(query)
                query_results = conn.cursor().fetchall()

                return query_results
            
        except sqlite3.Error as e: 
            raise DatabaseException(e)