#!/usr/bin/python3

from openehr.rest.ehr import get_ehr_by_id, update_ehr_status
from openehr.conf import test_ehrid

response = get_ehr_by_id( test_ehrid )

if not response:
    print( 'Error retrieving data' )
else:
    print(response)
