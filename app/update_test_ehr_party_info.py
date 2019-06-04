#!/usr/bin/python3

from openehr.rest.demographic import get_party_info, update_party_info
from openehr.conf import test_ehrid

ehr = test_ehrid

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

party['firstNames'] = 'Test Tester'
print('After update: ', party)

response = update_party_info( test_ehrid, party )

if  response['error']:
    print('Call to update party failed for %s' %  ehr)
    print('Error: ', response['error'])
    print('Message: ', response['error_msg'])
    print(response)
else: 
    party = response['party']
    meta = response['meta']
    action = response['action']
    print(party, meta, action, sep='\n')
