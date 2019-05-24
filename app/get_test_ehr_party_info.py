#!/usr/bin/python3

from openehr_rest_ehr import get_ehr_by_id
from openehr_rest_demographic import get_party_info
from openehr_conf import test_ehrid

party = get_party_info( test_ehrid, 0 )
if not party:
    print('No party data found for %s' % test_ehrid)
else:
    for key in party.keys(): print( key , party[key] )

    print( 'Party ID: ', party['party']['id'] )
    print( 'Name: ', party['party']['firstNames'], ' ',  party['party']['lastNames'] )
    print( 'Gender: ', party['party']['gender'] )
    print( 'Date of Birth: ', party['party']['dateOfBirth'] )
