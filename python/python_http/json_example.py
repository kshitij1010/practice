import os
import datetime
import json



'''
Notes:

- String:
* json.loads(s): Load JSON data from a string (Load as dictionary)
* json.dumps(j): Output JSON object as string

- File:
* json.load(f): Load JSON data from file or file-like object (Load as dictionary)
* json.dump(j, f): Write JSON object to file or file-like object


'''

sample_json_read_file = os.path.join(os.path.dirname(__file__), 'sample.json')
sample_json_write_file = os.path.join(os.path.dirname(__file__), 'write_test.json')


# Sample JSON

def mock_json_str():
    temp = """
            {
                "type": "test",
                "flag": null,
                "time": "%s",
                "active": true,
                "list": ["elem1√", "elem2∫", "elem3ƒ", "elem4¬˚∆"]
            }"""%(str(datetime.datetime.now()))

    return temp

def mock_json_dict():
    temp = {
        "type": "test",
        "flag": None,
        "time": "%s"%(str(datetime.datetime.now())),
        "active": True,
        "list": ["elem1√", "elem2∫", "elem3ƒ", "elem4¬˚∆"]
    }

    return temp



########## Reading JSON from string or file as dictionary object 

def read_json_from_file(file_path):
    f = open(file_path, 'r') # or open(file_path, 'r', encoding='utf-8')
    data = json.load(f) # json.loads would return dictionary or array of dictionary based on the input
    f.close()

    print ('\n')
    for d in data:
        print ('id:', d['id'], ', name:', d['first_name'], d['last_name'], ', email:', d['email'], ', city:', d['city'], ', flag:', d['flag'])

    return data


def read_json_from_str(s):
    data = json.loads(s)
    print ('\n')
    print (
        'type:', data['type'],
        ', time:', data['time'],
        ', flag:', data['flag'],
        ', active:', data['active'],
        ', list:', data['list']
    )
    return data



########## Converting dictionary to JSON

def convert_to_json(d):
    # ensure_ascii=False will make sure that non-ascii/unicode chars are not escaped
    data = json.dumps(d, ensure_ascii=False)
    print ('\n')
    print (json.dumps(d))
    print ('\n')
    print (data)
    return data


def convert_to_json_and_write_to_file(d, file_path):
    f = open(file_path, 'w')
    # ensure_ascii=False will make sure that non-ascii/unicode chars are not escaped
    data = json.dump(d, f, ensure_ascii=False)
    f.close()
    return data



if __name__ == '__main__':
    
    read_json_from_file(sample_json_read_file)
    read_json_from_str(mock_json_str())
    
    convert_to_json(mock_json_dict())
    convert_to_json_and_write_to_file(mock_json_dict(), sample_json_write_file)
