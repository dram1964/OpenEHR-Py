#!/usr/bin/env python3
"""
File: requestor.py 

Package module providing a urllib.request object for interacting with 
the OpenEHR REST API. The requestor object returned by the module
is pre-authenticated to the OpenEHR server with the user_name
and password values from the openehr/conf.py file
"""

import urllib.request
from openehr.conf import service_url, user_name, password
#from ..conf import service_url, user_name, password

def get_requestor():
    """
    Returns a urllib.request object, pre-authenticated to the
    OpenEHR server specified in the openehr/conf.py file.
    """
    requestor = urllib.request

    password_mgr = requestor.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password( 'Think!EHR', service_url, user_name, password )

    handler = requestor.HTTPBasicAuthHandler( password_mgr )

    opener = requestor.build_opener( handler )

    requestor.install_opener( opener )

    return requestor
