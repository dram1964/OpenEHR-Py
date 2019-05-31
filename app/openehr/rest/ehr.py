#!/usr/bin/env python3
"""
openehr.rest.ehr module

Provides functions for interacting with the EHR endpoint
of an OpenEHR REST API
"""

import urllib.parse, urllib.error
import json
from openehr.conf import service_url, test_ehrid
from openehr.rest.requestor import get_requestor as _get_requestor

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
    elif len(sys.argv) == 3:
        if sys.argv[1] == 'get_ehr_by_id':
            print( get_ehr_by_id(sys.argv[2]) )
        else:
            print('Unknown function: ', sys.argv[1] )
