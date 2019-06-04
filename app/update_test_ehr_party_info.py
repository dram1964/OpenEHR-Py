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
    party['firstNames'] = party['firstNames'].swapcase()

    response = update_party_info(party)

    if  response['error']:
        print('Call to update party failed')
        print('Error: ', response['error'])
        print('Message: ', response['error_msg'])
        print(response)
    else: 
        print('Action is', response['action'])
        print('Update can be found at:', response['meta']['href'])
