import unittest

from services.payload_helper import PayloadHelper

class PayloadHelperTest(unittest.TestCase):
    

    def test_convert_payload_to_dict(self): 
        self.assertDictEqual(PayloadHelper.convert_payload_to_dict("weedHeight;X1;0.4;0.1;30", ['height','temperature', 'humidity']), {
            'type': 'weedHeight', 
            'deviceName': 'X1', 
            'height': 0.4, 
            'temperature': 0.1, 
            'humidity': 30
        })


if __name__ == "__main__": 
    unittest.main()