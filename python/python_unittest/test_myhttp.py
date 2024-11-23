import unittest

from requests.models import Response
import myhttp
from unittest.mock import patch
import json



url = 'http://maps.googleapis.com/maps/api/geocode/json'
params = {'address': "abcd"}
expected_data = {'error_message': 'You must use an API key to authenticate each request to Google Maps Platform APIs. For additional information, please refer to http://g.co/dev/maps-no-account', 'results': [], 'status': 'REQUEST_DENIED'} 


def createGoodMockResp():
    r = Response() 
    r.status_code = 200
    r._content = str.encode(json.dumps(expected_data))
    return r

def createBadMockResp():
    r = Response() 
    r.status_code = 400
    return r




class TestRequests(unittest.TestCase):
    
    def test_get_request(self):
        self.assertEqual(expected_data, myhttp.getRequest(url, params))

    
    def test_myhttp_with_mock(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value = createGoodMockResp()

            data = myhttp.getRequest(url, params)
            mock_get.assert_called_with(url, params=params)
            
            self.assertEqual(expected_data, data)

    def test_myhttp_with_mock_bad_request(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value = createBadMockResp()
            
            with self.assertRaises(Exception):
                myhttp.getRequest('hello'+url, params)
                mock_get.assert_called_with('hello'+url, params=params)




if __name__ == '__main__':
    unittest.main(verbosity=5)
