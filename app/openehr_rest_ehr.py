#!/usr/bin/env python3
"""
openehr_rest_ehr module

Provides functions for interacting with the REST API
of an OpenEHR system
"""

import urllib.parse, urllib.error
import json
import openehr_conf
from openehr_auth import requestor

service_url = openehr_conf.service_url

def get_ehr_by_id( ehrid ):
    """
    get_ehr_by_id( ehrid )  -> ehr_json object

    Submits a query to the OpenEHR REST API. Sends an erhid to the 
    ehr/{ehrid} endpoint and returns the response as a JSON object
    representing the EHR identified by the supplied ehrid
    """
    url = service_url + 'ehr/' + ehrid
    print('Retrieving ', url)

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
        print( 'Response Code: %s' % response.getcode() )
        print( 'Retrieved %s characters' % len(data) )

        try:
            ehr = json.loads(data)
            return ehr
        except:
            return None
