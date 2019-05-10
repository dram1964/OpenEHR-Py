#!/usr/bin/env python3
import configuration
import urllib.request, urllib.parse, urllib.error
import json

ehr_id = configuration.test_ehrid
service_url = configuration.service_url
user_name = configuration.user_name
password = configuration.password

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password( 'Think!EHR', service_url, user_name, password )

handler = urllib.request.HTTPBasicAuthHandler( password_mgr )

opener = urllib.request.build_opener( handler )

url = service_url + ehr_id

urllib.request.install_opener( opener )

print('Retrieving ', url)

try:
    response = urllib.request.urlopen( url )
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



