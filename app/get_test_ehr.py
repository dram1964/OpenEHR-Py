#!/usr/bin/python3

from openehr_rest_ehr import get_ehr_by_id
from openehr_conf import test_ehrid

for debug in range(2):
    ehr = get_ehr_by_id( test_ehrid, debug )

    if not ehr:
        print( 'Error retrieving data' )
    else:
        print( 'EHRID: ', ehr['ehrId'] )
        print( 'Subject Id: ', ehr['ehrStatus']['subjectId'] )
        print( 'Modifiable: ', ehr['ehrStatus']['modifiable'] )
