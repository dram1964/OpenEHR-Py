#!/usr/bin/python3

from openehr.rest.demographic import get_party_info
from openehr.conf import test_ehrid

response = get_party_info( test_ehrid, 0 )

if  response['error']:
    print('Call to get party failed for %s' %  ehr)
    print('Error: ', response['error'])
    print('Message: ', response['error_msg'])
else: 
    print('Action is', response['action'])
    print('Party located at', response['meta']['href'])
    print('Party data', response['party'])
