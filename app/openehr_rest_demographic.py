#!/usr/bin/env python3
"""
openehr_rest_demographic module

Provides functions for interacting with the Demographic endpoint
of an OpenEHR REST API
"""

import urllib.parse, urllib.error
import json
from openehr_conf import service_url
from openehr_rest import requestor

def get_party_info( ehrid , debug=False ):
    """
    get_party_info( ehrid, debug=False )  -> ehr_json object

    Sends an erhid to the ehr/{ehrid} endpoint and returns 
    the response as a JSON object representing the EHR identified 
    by the supplied ehrid. Optional debug argument forces 
    more output if True
    """
    url = service_url + 'demographics/ehr/' + ehrid + '/party'
    print('Retrieving ', url)

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
