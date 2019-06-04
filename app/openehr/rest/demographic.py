#!/usr/bin/env python3
"""
File: demographic.py 

Package module for interacting with the Demographic endpoint of the
OpenEHR REST API

Package can be run from the command line:
python openehr/rest/demographic.py functionname [param[0],...,param[n]]
"""

import urllib.parse, urllib.error
from openehr.conf import service_url, test_ehrid
from openehr.rest.requestor import run_rest_query


def add_party_info( party_data, debug=True):
    """
    Queries the demographics/party REST API endpoint
    on the OpenEHR server to add new party information.
    Query method is POST and party data should be provided
    as a dictionary object
    Returns a dictionary response object. If the query is 
    successful, response['meta']['href'] will contain
    a link to the party information on the OpenEHR server 
    and response['action'] will be set to 'CREATE'
    """
    method = 'POST'
    url = service_url + 'demographics/party'
    headers = {'Content-Type' : 'application/json;charset=UTF-8'}

    response = run_rest_query(url, method, party_data, headers)
    return response


def update_party_info( party_data, debug=True ):
    """
    Queries the demographics/party REST API endpoint
    on the OpenEHR server to update existing party 
    information.
    Query method is PUT and party data should be provided
    as a dictionary object
    Returns a dictionary response object. If the query is 
    successful, response['meta']['href'] will contain
    a link to the party information on the OpenEHR server 
    and response['action'] will be set to 'UPDATE'
    """
    method = 'PUT'
    url = service_url + 'demographic/party'
    url = service_url + 'demographics/party'
    headers = {'Content-Type' : 'application/json'}

    response = run_rest_query(url, method, party_data, headers)
    return response


def get_party_info( ehrid, debug=False ):
    """
    Queries the demographics/ehr/{ehrid}/party endpoint 
    to retrieve party information for the specified ehrid.
    Query method is GET and erhid should be specified as
    a string value. 
    If the query is successful, response['meta']['href'] will 
    contain a link to the party information on the OpenEHR server 
    and response['action'] will be set to 'RETRIEVE'. 
    response['party'] will contain the party information in 
    a dictionary object
    """
    url = service_url + 'demographics/ehr/' + ehrid + '/party'
    if debug: print('Retrieving ', url)

    response = run_rest_query(url)
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
