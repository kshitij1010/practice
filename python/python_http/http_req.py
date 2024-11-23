import requests
import datetime
import json


'''
Notes:

Diff Content-Type:
- 'text/plain;charset=UTF-8'
- 'application/json' or 'application/problem+json
- 'application/xml'


'''


url_mockbin = 'http://mockbin.org/bin/9f84b0c2-e3d2-4aa8-b1c2-3fa15678be9d?foo=bar&foo=baz' # Bin Identifier: 9f84b0c2-e3d2-4aa8-b1c2-3fa15678be9d
url_httpbin_get = 'https://httpbin.org/get'
url_httpbin_header = 'https://httpbin.org/headers'
url_httpbin_post = 'https://httpbin.org/post' # this would return the request info as content in resp



# Creates sample json to post
def mock_json():
    temp = {
        'type': 'test',
        'time': '{}'.format(datetime.datetime.now()),
        'flag': None,
    }

    return json.dumps(temp)


# Parse received headers in resp
def parse_headers(headers):
    print ('\n')
    print ('Headers (Date)              :', headers.get('Date', "Header not found"))
    print ('Headers (Connection)        :', headers.get('Connection', "Header not found"))
    print ('Headers (Content-Type)      :', headers.get('Content-Type', "Header not found"))


def parse_status(resp):
    print ('\n')
    print ('Status (Request URL)     :', resp.url)
    print ('Status (Status Code)     :', resp.status_code)
    print ('Status (Status Reason)   :', resp.reason)
    print ('Status (Encoding)        :', resp.encoding)
    print ('Status (Time Elapsed)    :', resp.elapsed)
    print ('Status (Is redirect)     :', resp.is_redirect)


# Parse received Contents/data in resp
def parse_content(resp):
    print ('\n')
    # print ('Data (Raw - as bytes)               :', resp.content)
    # print ('Data (Raw - as a str)               :', resp.text)

    # try:
    #     data_in_dict = resp.json()
    #     print ('Data (in dict form)            :', data_in_dict)
    #     print ('Data (in dict form) [foo key]  :', data_in_dict['foo'])
    # except:
    #     print ('No JSON data found')
    
    if 'application/json' in resp.headers.get('Content-Type'):
        data_in_dict = resp.json()
        print ('Data (in dict form)                 :', data_in_dict)
        print ('Data (in dict form) [foo key]       :', data_in_dict.get('foo', "foo key not found in content"))
        print ('Data (in dict form) [success key]   :', data_in_dict.get('success', "success key not found in content"))
        print ('Data (in dict form) [data key]      :', data_in_dict.get('data', "data key not found in content"))
        data = data_in_dict.get('data')
        d = json.loads(data)
        print (type(d))
    else:
        print ('No JSON data found')


# Perform HTTP request
def do_req(url, method='GET', custom_header=False):
    r = None
    headers = {}
    if custom_header:
        headers = {
            "Custom": "this is for testing custom header"
        }
    
    if method.upper() == 'GET':
        r = requests.get(url=url, headers=headers)
    else:
        r = requests.post(url=url, json=mock_json(), headers=headers)

    if r is None:
        raise Exception("HTTP request failed from our end!!!!")
    
    parse_status(r)
    parse_content(r)
    parse_headers(r.headers)
        


if __name__ == '__main__':
    # do_req(url_httpbin_header, "get")
    # do_req(url_httpbin_header, "get", True)
    do_req(url_httpbin_post, "post")
    do_req(url_httpbin_post, "post", True)
