#!/usr/bin/env python3
"""
openehr_rest_ehr module

Provides functions for interacting with the EHR endpoint
of an OpenEHR REST API
"""

import urllib.parse, urllib.error
import json
from openehr_conf import service_url
from openehr_rest import requestor

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
