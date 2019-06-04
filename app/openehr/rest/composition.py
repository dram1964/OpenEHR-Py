#!/usr/bin/env python3
"""
File: composition.py

Package module for interacting with the Composition endpoint
of the OpenEHR REST API

Package can be run from the command line:
python openehr/rest/composition.py [functionname] [param[0],...,param[n]]
"""

import urllib.parse, urllib.error
import json
from openehr.conf import service_url, test_uid
from openehr.rest.requestor import run_rest_query

def get_composition_by_uid( composition_id=test_uid, response_format='FLAT', include_meta='true', debug=1):
    """
    Queries the composition/{uid} endpoint to retrieve composition
    data for the given composition uid, in the specified response format.
    Query method is GET and composition uid should be specified as a
    string value. Response format should be one of [FLAT|STRUCTURED|RAW]
    If the query is successful, response['meta']['href'] will
    contain a link to the compostion on the OpenEHR server and
    response['meta']['precedingHref'] will contain a link to the
    preceding version of the composition. The composition uid will
    be held in response['compositionUid'] and the composition itself
    will be in response['composition']. Additional keys for the response
    object include: 'format', 'templateId', 'deleted', 'lastVersion',
    'ehrId' and 'lifecycleState'.
    """
    data = {
        'format' : response_format,
        'meta'   : include_meta
    }
    url_values = urllib.parse.urlencode(data)

    url = service_url + 'composition/' + composition_id + '?' +  url_values
    if debug: print('Retrieving', url)

    response = run_rest_query(url)
    return response


if __name__ == '__main__':
    import sys
    import types
    import composition

    if len(sys.argv) == 1:
        for attr in composition.__dict__:
            if not attr.startswith('_'):
                if type(getattr(composition, attr)) == types.FunctionType:
                    print("Available functions: ", attr)
    elif len(sys.argv) > 1:
        try:
            func = getattr(composition, sys.argv[1])
        except:
            print('Error, unknown function: ', sys.argv[1])
        else:
            print( getattr(composition, sys.argv[1])(debug=True, *sys.argv[2:] ) )
