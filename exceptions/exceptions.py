class ParameterNotFoundExceptions(Exception):
    """Exception for missing parameters
    
        This can happen if the device type being queried does not exist in the sensor_configs.json file.
    """

class DatabaseException(Exception): 
    """
        Exception for failed initialization of SQLite database
    """