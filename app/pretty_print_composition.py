#!/usr/bin/python3

from openehr.rest.composition import get_composition_by_uid
import sys
import json

if len(sys.argv) >= 2:
    composition_id = sys.argv[1]
    print('Retrieving Composition:', composition_id)
    response = get_composition_by_uid(*sys.argv[1:])
    print( json.dumps(response['composition'], sort_keys=True, indent=4) )
