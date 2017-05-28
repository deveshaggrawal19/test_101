from urllib import request
import json
import sys


print("Running Endpoint Tester....\n")
address = input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://127.0.0.1:5000':   ")
if address == '':
    address = 'http://localhost:5000'


# Making a POST Request
print("Making a POST Request for /post_location...")
try:
    url = address + "/post_location"
    headers = {"Content-type": "application/json","Accept": "application/json"}
    params = json.dumps({'name': 'new_test_user', 'lat': '40.1245', 'lng': '73.1546'}).encode('utf8')
    req = request.Request(url, data=params, headers=headers)
    response = request.urlopen(req)
    print(response.read().decode('utf8'))
    if response.status != 200:
        raise Exception('Received an unsuccessful status code of %s' % response.status)
except Exception as err:
	print("Test 1 FAILED: Could not make POST Request to web server")
	print(err)
	sys.exit()
else:
	print("Test 1 PASS: Succesfully Made POST Request to /post_location")


# Making a GET Request
print("Making a GET request to /get_using_postgres...")
try:
    url = address + "/get_using_postgres?"+'lat=%s&lng=%s' %(40.124, 73.1546)
    headers = {"Content-type": "application/json","Accept": "application/json"}
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    print(response.read().decode('utf8'))
    if response.status != 200:
        raise Exception('Received an unsuccessful status code of %s' % response.status)
except Exception as err:
	print("Test 2 FAILED: Could not make GET Request to web server")
	print(err)
	sys.exit()
else:
	print("Test 2 PASS: Succesfully Made GET Request to /get_using_postgres")

# Making a GET Request
print("Making a GET request to /get_using_self...")
try:
    url = address + "/get_using_self?"+'lat=%s&lng=%s' %(40.124, 73.1546)
    headers = {"Content-type": "application/json","Accept": "application/json"}
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    print(response.read().decode('utf8'))
    if response.status != 200:
        raise Exception('Received an unsuccessful status code of %s' % response.status)
except Exception as err:
	print("Test 3 FAILED: Could not make GET Request to web server")
	print(err)
	sys.exit()
else:
	print("Test 3 PASS: Succesfully Made GET Request to /get_using_self")
