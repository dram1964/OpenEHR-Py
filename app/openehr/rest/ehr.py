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
from openehr.rest.requestor import get_requestor as _get_requestor

def get_ehr_by_subject_id( subject_id=test_subject_id, subject_namespace=default_namespace , debug=True ):
    """
    get_ehr_by_subject_id( subject_id, subject_namespace, debug) -> ehr_json object
    """

    #http://localhost:8081/rest/v1/ehr?subjectId=3333333333&subjectNamespace=uk.nhs.nhs_number
    url = service_url + 'ehr?subjectId=' + subject_id + '&subjectNamespace=' + subject_namespace
    if debug: print('Retrieving ' + url)
    requestor = _get_requestor()

    try:
        response = requestor.urlopen( url )
    except urllib.error.HTTPError as e:
        print( 'HTTP Error: ', e.code )
        print( 'Reason: ', e.reason )
        print( 'Headers: ', e.headers )
    else:
        data = response.read().decode()
        if debug: print( 'Response Code: %s' % response.getcode() )
        if debug: print( 'Retrieved %s characters' % len(data) )

        try:
            ehr = json.loads(data)
            return ehr
        except:
            return None


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
    requestor = _get_requestor()

    try:
        response = requestor.urlopen( url )
    except urllib.error.HTTPError as e:
        print( 'HTTP Error: ', e.code )
        print( 'Reason: ', e.reason )
        print( 'Headers: ', e.headers )
        return None
    except urllib.error.URLError as e:
        print ( 'URL Error: ', e.reason )
        return None
    else:
        data = response.read().decode()
        if debug: print( 'Response Code: %s' % response.getcode() )
        if debug: print( 'Retrieved %s characters' % len(data) )

        try:
            ehr = json.loads(data)
            return ehr
        except:
            return None

if __name__ == '__main__':
    import sys
    import types
    import ehr

    if len(sys.argv) == 1:
        for attr in ehr.__dict__:
            if not attr.startswith('_'):
                if type(getattr(ehr, attr)) == types.FunctionType:
                    print("Available functions: ", attr)
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'get_ehr_by_id':
            print( get_ehr_by_id( test_ehrid ) )
        if sys.argv[1] == 'get_ehr_by_subject_id':
            print( get_ehr_by_subject_id( test_subject_id, default_namespace, 1 ) )
    elif len(sys.argv) == 3:
        if sys.argv[1] == 'get_ehr_by_id':
            print( get_ehr_by_id(sys.argv[2]) )
        if sys.argv[1] == 'get_ehr_by_subject_id':
            print( get_ehr_by_subject_id( sys.argv[2], default_namespace, 1 ) )
        else:
            print('Unknown function: ', sys.argv[1] )
