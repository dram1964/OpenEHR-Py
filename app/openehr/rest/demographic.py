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

def party_get_query( data, debug=True ):
    """
    Queries the demographics/party/query endpoint
    to retrieve party information based on the data
    specified with two keys: 'maxHits' which should
    have an integer value specifying the maximum 
    number of party records to return and; 'parameters'
    which should be a string specified as
    'key1=value1&key2=value2...keyn=valuen'
    Query method is GET
    If the query is successful, response['meta']['href'] will
    contain a link to the query results on the OpenEHR server
    and response['action'] will be set to 'RETRIEVE'.
    response['parties'] will contain an array of dictionary
    party objects returned from the query
    """
    method = 'GET'
    url_values = urllib.parse.urlencode( data )
    headers = {'Content-Type' : 'application/json'}

    url = service_url + 'demographics/party/query/?' + url_values
    if debug: print('Retrieving ', url)

    response = run_rest_query(url, method, False, headers)
    return response

def party_post_query( data, limit=10, debug=True ):
    """
    Queries the demographics/party/query endpoint
    to retrieve party information based on the filters
    provided. Query method is POST and the query is provided
    in the first parameter as an array of dictionary items
    containing two keys: 'key' and 'value'.
    For example: [ {"key" : "lastNames",
    "value" : "Wilson" },...]. 'limit' is specified as an
    integer value to limit the number of results returned:
    set this value to '0' if no limit is required.
    If the query is successful, response['meta']['href'] will
    contain a link to the query results on the OpenEHR server
    and response['action'] will be set to 'RETRIEVE'.
    response['parties'] will contain an array of dictionary
    party objects returned from the query
    """
    method = 'POST'
    headers = {'Content-Type' : 'application/json'}
    url = service_url + 'demographics/party/query'

    if limit:
        limit = { "maxHits" : limit }
        url_values = urllib.parse.urlencode( limit )
        url = url + '?' + url_values
    if debug: print('Retrieving ', url)

    response = run_rest_query(url, method, data, headers)
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
