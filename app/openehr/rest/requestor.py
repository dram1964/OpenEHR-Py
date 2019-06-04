#!/usr/bin/env python3
"""
File: requestor.py 

Package module providing a urllib.request object for interacting with 
the OpenEHR REST API. The requestor object returned by the module
is pre-authenticated to the OpenEHR server with the user_name
and password values from the openehr/conf.py file
"""

import urllib.request
import json
from openehr.conf import service_url, user_name, password

def run_rest_query(url, method='GET', data=False, headers=False):
    requestor = get_requestor()
    req = requestor.Request
    req.method = method

    if data:
        data = json.dumps(data)
        data = data.encode('ascii')
        if headers:
            req = req(url, data, headers)
        else:
            req = req(url, data)
    else:
        req = req(url)

    try:
        response = requestor.urlopen( req )
    except urllib.error.HTTPError as e:
        response = { "error" : e.code, 'error_msg' : 'HTTP Error: ' + e.reason}
        response_body = e.read().decode()
        if response_body:
            response.update( json.loads(response_body) )
    except urllib.error.URLError as e:
        response = { "error" : e.code, 'error_msg' : 'URL Error: ' + e.reason}
    else:
        response = response.read().decode()
        if response:
            response = json.loads(response)
            response['error'] = False
            response['error_msg'] = False
        else:
            response = {'error' : 1, 'error_msg' : 'Response error: no data returned'}

    return response

def get_requestor():
    """
    Returns a urllib.request object, pre-authenticated to the
    OpenEHR server specified in the openehr/conf.py file.
    """
    requestor = urllib.request

    password_mgr = requestor.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password( 'Think!EHR', service_url, user_name, password )

    handler = requestor.HTTPBasicAuthHandler( password_mgr )

    opener = requestor.build_opener( handler )

    requestor.install_opener( opener )

    return requestor
