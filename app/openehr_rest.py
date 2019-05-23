#!/usr/bin/env python3
"""
openehr_rest module

Provides a requestor object to submit Queries 
to OpenEHR REST API. The requestor object is 
a urllib.request object which has been 
pre-authenticated to the OpenEHR REST server 
from values stored in the openehr_conf module
"""

import urllib.request
import openehr_conf

requestor = urllib.request

service_url = openehr_conf.service_url
user_name = openehr_conf.user_name
password = openehr_conf.password

password_mgr = requestor.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password( 'Think!EHR', service_url, user_name, password )

handler = requestor.HTTPBasicAuthHandler( password_mgr )

opener = requestor.build_opener( handler )

requestor.install_opener( opener )
