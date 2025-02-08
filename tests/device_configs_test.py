import unittest

from services.device_configs_service import DeviceConfigHelper

class PayloadHelperTest(unittest.TestCase):
    

    def test_device_sensor_types(self): 

        deviceConfigHelper: DeviceConfigHelper = DeviceConfigHelper(sensor_config=[{
            "type": "soilSensing", 
            "parameters": ["soilMoisture", "temperature", "humidity"], 
            "deviceNames": ["A", "B"]
        }])
        

        self.assertListEqual(deviceConfigHelper.get_parameters_for_type('soilSensing'), ["soilMoisture", "temperature", "humidity"])

        deviceConfigHelper: DeviceConfigHelper = DeviceConfigHelper(sensor_config=[
            {
                "type": "soilSensing", 
                "parameters": ["soilMoisture", "temperature", "humidity"], 
                "deviceNames": ["A", "B"]
            }, 
            {
                "type": "weedHeight", 
                "parameters": ["height"], 
                "deviceNames": ["C"]
            }
        ])
        
        self.assertListEqual(deviceConfigHelper.get_parameters_for_type('soilSensing'), ["soilMoisture", "temperature", "humidity"])
        self.assertListEqual(deviceConfigHelper.get_parameters_for_type('weedHeight'), ["height"])

    def test_get_sensor_types(self): 

        deviceConfigHelper: DeviceConfigHelper = DeviceConfigHelper(sensor_config=[{
            "type": "soilSensing", 
            "parameters": ["soilMoisture", "temperature", "humidity"], 
            "deviceNames": ["A", "B"]
        }])
        

        self.assertListEqual(deviceConfigHelper.get_sensor_types(), ["soilSensing"])

        deviceConfigHelper: DeviceConfigHelper = DeviceConfigHelper(sensor_config=[
            {
                "type": "soilSensing", 
                "parameters": ["soilMoisture", "temperature", "humidity"], 
                "deviceNames": ["A", "B"]
            }, 
            {
                "type": "weedHeight", 
                "parameters": ["height"], 
                "deviceNames": ["C"]
            }
        ])
        
        self.assertListEqual(deviceConfigHelper.get_sensor_types(), ["soilSensing","weedHeight"])



if __name__ == "__main__": 
    unittest.main()