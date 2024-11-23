import requests

def getRequest(url='', params={}):
    r = requests.get(url, params=params)
    data = {}
    # print (r.status_code, r.ok)
    if r.ok and 199 < r.status_code < 300:
        data = r.json()
    else:
        raise Exception("Bad Response from server")

    return data


def getRequest2():
    headers = {'test': 'hello_test_header'}
    response = requests.get("https://kite.com", headers=headers)

    print(response.headers)



if __name__ == '__main__':
    url = 'http://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': "abcd"}
    getRequest(url, params)
    getRequest2()
