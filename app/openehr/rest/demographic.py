#!/usr/bin/env python3
"""
File: demographic.py 

Package module for interacting with the OpenEHR Demographic API

Package can be run from the command line:
python openehr/rest/demographic.py functionname [param[0],...,param[n]]
With no arguments runs the get_party_info function for the test_ehrid
value defined in the system configuration file (openehr/conf.py).
"""

import urllib.parse, urllib.error
import json
from openehr.conf import service_url, test_ehrid
from openehr.rest.requestor import get_requestor as _get_requestor

def add_party_info( party_data, debug=True):
    requestor = _get_requestor()

    req = requestor.Request
    url = service_url + 'demographics/party'
    data = json.dumps(party_data)
    data = data.encode('ascii')
    headers = {'Content-Type' : 'application/json;charset=UTF-8'}

    req = req(url, data, headers)

    try:
        response = requestor.urlopen( req )
    except urllib.error.HTTPError as e:
        response = e.read().decode()
        return {
            'error' : e.code,
            'error_msg' : 'HTTP Error: ' + e.reason,
            'response' : response,
            'party' : None,
            'meta' : None,
            'action' : None,
        }
    except urllib.error.URLError as e:
        return {
            'error' : 1,
            'error_msg' : 'URL Error: ' + e.reason,
            'party' : None,
            'meta' : None,
            'action' : None,
        }
    else:
        data = response.read().decode()
        if debug: print( 'Response Code: %s' % response.getcode() )
        if debug: print( 'Retrieved %s characters' % len(data) )

        try:
            js = json.loads(data)
        except:
            return { 
                'error' : 2,
                'error_msg' : 'Error converting response to JSON',
                'response' : data,
                'party' : None,
                'meta' : None,
                'action' : None,
            }
        else:
            return {
                'error' : 0,
                'party' : js['meta']['href'],
                'meta' : js['meta'],
                'action' : js['action'],
            }

def update_party_info( ehrid, party_data, debug=True ):
    """
    Sends a REST query to the demographics/party end point
    to update exising party info
    """
    url = service_url + 'demographics/party'
    party = {"id": "772", "version": 50, "firstNames": "Test Tester", "lastNames": "Test-Patient", "gender": "MALE", "dateOfBirth": "1950-01-01", "address": {"id": "772", "version": 50, "address": "21 Winding Road, London, NW1 2PG"}, "partyAdditionalInfo": [{"id": "2924", "version": 0, "key": "ehrId", "value": "33b11502-9e5c-41f0-9cea-93b851c85b67"}, {"id": "2923", "version": 0, "key": "uk.nhs.nhs_number", "value": "3333333333"}]}
    data = urllib.parse.urlencode(party)
    data = data.encode('ascii')

    headers = {'Content-Type' : 'application/json'}
    requestor = _get_requestor()
    req = requestor.Request
    req.method = 'PUT'
    req = req(url, data, headers)

    try:
        response = requestor.urlopen( req )
    except urllib.error.HTTPError as e:
        response = e.read().decode()
        return {
            'error' : e.code,
            'error_msg' : 'HTTP Error: ' + e.reason,
            'response' : response,
            'party' : None,
            'meta' : None,
            'action' : None,
        }
    except urllib.error.URLError as e:
        return {
            'error' : 1,
            'error_msg' : 'URL Error: ' + e.reason,
            'party' : req,
            'meta' : None,
            'action' : None,
        }
    else:
        data = response.read().decode()
        if debug: print( 'Response Code: %s' % response.getcode() )
        if debug: print( 'Retrieved %s characters' % len(data) )

        try:
            js = json.loads(data)
        except:
            return { 
                'error' : 2,
                'error_msg' : 'Error converting response to JSON',
                'response' : data,
                'party' : None,
                'meta' : None,
                'action' : None,
            }
        else:
            js['error'] = 0
            return js


def get_party_info( ehrid, debug=False ):
    """
    Sends a REST query to the demographics/ehr/{ehrid}/party endpoint 
    and returns the response as a JSON object representing the 
    party info for the specified ehrid
    """
    url = service_url + 'demographics/ehr/' + ehrid + '/party'
    if debug: print('Retrieving ', url)
    requestor = _get_requestor()

    try:
        response = requestor.urlopen( url )
    except urllib.error.HTTPError as e:
        return {
            'error' : e.code,
            'error_msg' : 'HTTP Error: ' + e.reason,
            'party' : None,
            'meta' : None,
            'action' : None,
        }
    except urllib.error.URLError as e:
        return {
            'error' : 1,
            'error_msg' : 'URL Error: ' + e.reason,
            'party' : None,
            'meta' : None,
            'action' : None,
        }
    else:
        data = response.read().decode()
        if debug: print( 'Response Code: %s' % response.getcode() )
        if debug: print( 'Retrieved %s characters' % len(data) )

        try:
            js = json.loads(data)
        except:
            return { 
                'error' : 2,
                'error_msg' : 'Error converting response to JSON',
                'party' : None,
                'meta' : None,
                'action' : None,
            }
        else:
            js['error'] = 0
            return js

if __name__ == '__main__':
    import sys
    import types
    import demographic

    if len(sys.argv) == 1:
        for attr in demographic.__dict__:
            if not attr.startswith('_'):
                if type(getattr(demographic, attr)) == types.FunctionType:
                    print("Available functions: ", attr)
    elif len(sys.argv) > 1:
        try:
            func = getattr(demographic, sys.argv[1])
        except:
            print('Error, unknown function: ', sys.argv[1])
        else:
            print( getattr(demographic, sys.argv[1])( debug=True, *sys.argv[2:] ) )
