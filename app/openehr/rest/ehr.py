#!/usr/bin/env python3
"""
File: ehr.py

Package module for interacting with the EHR endpoint of the
OpenEHR REST API

Package can be run from the command line:
python openehr/rest/ehr.py functionname [param[0],...,param[n]]
"""

import urllib.parse, urllib.error
import json
from openehr.conf import service_url, test_ehrid, test_subject_id, default_namespace
from openehr.rest.requestor import run_rest_query

def get_ehr_by_subject_id( subject_id, subject_namespace=default_namespace , debug=False ):
    """
    Queries the ehr REST API endpoint on the OpenEHR server
    for a given subject id in the given subject namespace.
    Query method is GET. Subject id and subject namespace
    should be provided as string objects
    Returns a dictionary response object. If the query is
    successful, response['meta']['href'] will contain
    a link to the ehr on the OpenEHR server
    and response['action'] will be set to 'RETRIEVE'.
    response['ehrId'] will contain the ehr_id for the subject
    and response['ehrStatus'] will contain the remainder of 
    the ehr record
    """
    data = {
        'subjectId' : subject_id,
        'subjectNamespace' : subject_namespace,
    }
    url_values = urllib.parse.urlencode( data )

    url = service_url + 'ehr?' + url_values

    if debug: print('Retrieving ' + url)

    response = run_rest_query(url)
    return response


def get_ehr_by_id( ehrid , debug=False ):
    """
    Queries the ehr/{ehrid} endpoint on the OpenEHR server
    for a given ehrid.
    Query method is GET and ehrid should be provided as a
    string object.
    Returns a dictionary response object. If the query is
    successful, response['meta']['href'] will contain
    a link to the ehr on the OpenEHR server
    and response['action'] will be set to 'RETRIEVE'.
    response['ehrId'] will contain the ehr_id for the subject
    and response['ehrStatus'] will contain the remainder of
    the ehr record
    """
    url = service_url + 'ehr/' + ehrid
    if debug: print('Retrieving ', url)

    response = run_rest_query(url)
    return response

def create_new_ehr( subject_id, subject_namespace=default_namespace, committer_name='OpenEHR-Py', committer_id=1, debug=True):
    """
    Queries the ehr endpoint on the OpenEHR server to
    create a new ehr record.
    Query method is POST and subject_id should be provided as a
    string object.
    Returns a dictionary response object. If the query is
    successful, response['meta']['href'] will contain
    a link to the ehr on the OpenEHR server
    and response['action'] will be set to 'RETRIEVE'.
    response['ehrId'] will contain the ehr_id for the subject
    """

    method = 'POST'
    data = {
        'subjectId' : subject_id,
        'subjectNamespace' : subject_namespace,
    }
    url_values = urllib.parse.urlencode( data )

    url = service_url + 'ehr?' + url_values

    if debug: print('Retrieving ' + url)

    response = run_rest_query(url, method)
    return response

def update_ehr_status( ehrid, ehr_status, debug=True):
    """
    Queries the ehr/{ehrId}/status endpoint on the OpenEHR
    server to update the ehr status for the given ehrid.
    Query method is PUT. ehrid should be provided as a
    string object and ehr_status as a dictionary object
    with the following keys: 'subjectId', 'subjectNamespace',
    'queryable', 'modifiable'.
    Returns a dictionary response object. If the query is
    successful, response['meta']['href'] will contain
    a link to the ehr on the OpenEHR server
    and response['action'] will be set to 'UPDATE'.
    """
    method = 'PUT'
    url = service_url + 'ehr/' + ehrid + '/status'
    headers = {'Content-Type' : 'application/json;charset=UTF-8'}

    if debug: print('Retrieving ' + url)

    response = run_rest_query(url, method, ehr_status, headers)
    return response



if __name__ == '__main__':
    import sys
    import types
    import ehr

    if len(sys.argv) == 1:
        for attr in ehr.__dict__:
            if not attr.startswith('_'):
                if type(getattr(ehr, attr)) == types.FunctionType:
                    print("Available functions: ", attr)
    elif len(sys.argv) > 1:
        try:
            func = getattr(ehr, sys.argv[1])
        except:
            print('Error, unknown function: ', sys.argv[1])
        else:
            print( getattr(ehr, sys.argv[1])( debug=True, *sys.argv[2:] ) )
