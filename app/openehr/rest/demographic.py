#!/usr/bin/env python3
"""
openehr.rest.demographic module

Provides functions for interacting with the Demographic endpoint
of an OpenEHR REST API
"""

import urllib.parse, urllib.error
import json
from openehr.conf import service_url, test_ehrid
from openehr.rest.requestor import get_requestor as _get_requestor

def get_party_info( ehrid=test_ehrid , debug=False ):
    """
    get_party_info( ehrid, debug=False )  -> ehr_json object

    Sends an erhid to the ehr/{ehrid} endpoint and returns 
    the response as a JSON object representing the EHR identified 
    by the supplied ehrid. Optional debug argument forces 
    more output if True
    """
    url = service_url + 'demographics/ehr/' + ehrid + '/party'
    print('Retrieving ', url)
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
            js['error'] = 0
            return js
        except:
            return { 
                'error' : 2,
                'error_msg' : 'Error converting response to JSON',
                'party' : None,
                'meta' : None,
                'action' : None,
            }

if __name__ == '__main__':
    import sys
    import types
    import demographic

    if len(sys.argv) == 1:
        for attr in demographic.__dict__:
            if not attr.startswith('_'):
                if type(getattr(demographic, attr)) == types.FunctionType:
                    print("Available functions: ", attr)
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'get_party_info':
            print( get_party_info() )
    elif len(sys.argv) == 3:
        if sys.argv[1] == 'get_party_info':
            print( get_party_info(sys.argv[2]) )
        else:
            print('Unknown function: ', sys.argv[1] )
