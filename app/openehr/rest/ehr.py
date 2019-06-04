#!/usr/bin/env python3
"""
File: ehr.py 

Package module for interacting with the OpenEHR EHR API

Package can be run from the command line:
python openehr/rest/ehr.py functionname [param[0],...,param[n]]
With no arguments runs the get_ehr_by_id function for the test_ehrid
value defined in the system configuration file (openehr/conf.py).
"""

import urllib.parse, urllib.error
import json
from openehr.conf import service_url, test_ehrid, test_subject_id, default_namespace
from openehr.rest.requestor import run_rest_query

def get_ehr_by_subject_id( subject_id, subject_namespace=default_namespace , debug=False ):
    """
    get_ehr_by_subject_id( subject_id, subject_namespace, debug) -> ehr_json object
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
    get_ehr_by_id( ehrid, debug=False )  -> ehr_json object

    Sends an erhid to the ehr/{ehrid} endpoint and returns 
    the response as a JSON object representing the EHR identified 
    by the supplied ehrid. Optional debug argument forces 
    more output if True
    """
    url = service_url + 'ehr/' + ehrid
    if debug: print('Retrieving ', url)

    response = run_rest_query(url)
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
