#!/usr/bin/python3

from openehr.rest.demographic import get_party_info, add_party_info
from openehr.conf import test_ehrid

party_data = {
    "firstNames": "string", 
    "lastNames": "string", 
    "gender": "MALE", 
    "dateOfBirth": "2012-12-12", 
    "address": {
        "address": "123 Buckingham Palace Road" 
        } 
}

response = add_party_info(party_data)

if response['error']:
    print( response['error_msg'] )
else:
    print('Action is', response['action'] )
    print('New Party info at', response['meta']['href'])
