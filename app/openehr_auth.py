#!/usr/bin/env python3

import urllib.request
import configuration

requestor = urllib.request

service_url = configuration.service_url
user_name = configuration.user_name
password = configuration.password

password_mgr = requestor.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password( 'Think!EHR', service_url, user_name, password )

handler = requestor.HTTPBasicAuthHandler( password_mgr )

opener = requestor.build_opener( handler )

requestor.install_opener( opener )