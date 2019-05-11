#!/usr/bin/env python3
import configuration
from openehr_auth import requestor
import urllib.parse, urllib.error
import json

ehr_id = configuration.test_ehrid
service_url = configuration.service_url

url = service_url + 'ehr/' + ehr_id

print('Retrieving ', url)

try:
    response = requestor.urlopen( url )
except urllib.error.HTTPError as e:
    print( 'HTTP Error: ', e.code )
    print( 'Reason: ', e.reason )
    print( 'Headers: ', e.headers )
except urllib.error.URLError as e:
    print ( 'URL Erorr: ', e.reason )
else:
    data = response.read().decode()
    print( 'Retrieved ', len(data), ' characters' )
    
    try:
        js = json.loads(data)
    except:
        js = None

    if not js:
        print( 'Error retrieving data' )
        print(data)

    print( json.dumps( js, indent=4 ) )



