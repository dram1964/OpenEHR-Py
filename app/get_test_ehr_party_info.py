#!/usr/bin/python3

from openehr.rest.ehr import get_ehr_by_id
from openehr.rest.demographic import get_party_info
from openehr.conf import test_ehrid

ehr = test_ehrid
ehr = ehr.replace('33', '44')

response = get_party_info( ehr, 0 )

if response['error']:
    print('Call to get party failed for %s' %  ehr)
    print('Error: ', response['error'])
    print('Message: ', response['error_msg'])
else:
    party = response['party']
    meta = response['meta']
    action = response['action']
    print(party, meta, action, sep='\n')

response = get_party_info( test_ehrid, 0 )

if  response['error']:
    print('Call to get party failed for %s' %  ehr)
    print('Error: ', response['error'])
    print('Message: ', response['error_msg'])
else: 
    party = response['party']
    meta = response['meta']
    action = response['action']
    print(party, meta, action, sep='\n')
