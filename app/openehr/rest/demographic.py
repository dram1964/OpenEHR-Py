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
from openehr.conf import service_url, test_ehrid
from openehr.rest.requestor import run_rest_query


def add_party_info( party_data, debug=True):
    method = 'POST'
    url = service_url + 'demographics/party'
    headers = {'Content-Type' : 'application/json;charset=UTF-8'}

    response = run_rest_query(method, url, party_data, headers)
    return response




def update_party_info( party_data, debug=True ):
    method = 'PUT'
    url = service_url + 'demographic/party'
    url = service_url + 'demographics/party'
    headers = {'Content-Type' : 'application/json'}
    #party_data = urllib.parse.urlencode(party_data)
    #party_data = party_data.encode('ascii')

    response = run_rest_query(method, url, party_data, headers)
    return response


def get_party_info( ehrid, debug=False ):
    """
    Sends a REST query to the demographics/ehr/{ehrid}/party endpoint 
    and returns the response as a JSON object representing the 
    party info for the specified ehrid
    """
    method = 'GET'
    url = service_url + 'demographics/ehr/' + ehrid + '/party'
    if debug: print('Retrieving ', url)

    response = run_rest_query(method, url, None, None)
    return response

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
