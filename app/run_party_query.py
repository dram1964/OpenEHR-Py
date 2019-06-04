#!/usr/bin/python3

from openehr.rest.demographic import party_query

party = {
    "maxHits" : 10,
    "parameters" : "gender=MALE"
}

response = party_query(party)

print(response)

party = {
    "maxHits" : 10,
    "parameters" : "gender=MALE&firstNames=Test"
}

response = party_query(party)

print(response)
