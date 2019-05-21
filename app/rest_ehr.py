#!/usr/bin/env python3

import urllib.parse, urllib.error
import json
import configuration
from openehr_auth import requestor

service_url = configuration.service_url

def get_ehr_by_id( ehrid ):
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
