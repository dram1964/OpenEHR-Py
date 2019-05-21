#!/usr/bin/python3

from rest_ehr import get_ehr_by_id
import configuration

ehrid = configuration.test_ehrid

ehr = get_ehr_by_id(ehrid)

if not ehr:
    print( 'Error retrieving data' )
else:
    print( 'EHRID: ', ehr['ehrId'] )
    print( 'Subject Id: ', ehr['ehrStatus']['subjectId'])
    print( 'Modifiable: ', ehr['ehrStatus']['modifiable'])
