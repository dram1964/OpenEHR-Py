#!/usr/bin/env python3
"""
File: composition.py 

Package module for interacting with the OpenEHR Composition API

Package can be run from the command line:
python openehr/rest/composition.py [functionname] [param[0],...,param[n]]
With no arguments runs the xxxx function for the test_ehrid
value defined in the system configuration file (openehr/conf.py).
"""

import urllib.parse, urllib.error
import json
from openehr.conf import service_url, test_uid
from openehr.rest.requestor import get_requestor as _get_requestor

def get_composition_by_uid( composition_id=test_uid, response_format='FLAT' , include_meta='true', debug=1):
    """
    get_composition_by_uid( composition_id, format, meta) -> composition_json object
    """
    data = {
        'format' : response_format,
        'meta'   : include_meta
    }
    url_values = urllib.parse.urlencode(data)

    url = service_url + 'composition/' + composition_id + '?' +  url_values
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
            composition = json.loads(data)
            return composition
        except:
            return None


if __name__ == '__main__':
    import sys
    import types
    import composition

    if len(sys.argv) == 1:
        for attr in composition.__dict__:
            if not attr.startswith('_'):
                if type(getattr(composition, attr)) == types.FunctionType:
                    print("Available functions: ", attr)
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'get_composition_by_uid':
            print( get_composition_by_uid( ) )
    elif len(sys.argv) == 3:
        if sys.argv[1] == 'get_composition_by_uid':
            print( get_composition_by_uid(sys.argv[2]) )
        else:
            print('Unknown function: ', sys.argv[1] )
    elif len(sys.argv) == 4:
        if sys.argv[1] == 'get_composition_by_uid':
            print( get_composition_by_uid(sys.argv[2], sys.argv[3]) )
        else:
            print('Unknown function: ', sys.argv[1] )
    elif len(sys.argv) == 5:
        if sys.argv[1] == 'get_composition_by_uid':
            print( get_composition_by_uid(sys.argv[2], sys.argv[3]), sys.argv[4] )
        else:
            print('Unknown function: ', sys.argv[1] )
