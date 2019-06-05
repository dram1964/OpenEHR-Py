#!/usr/bin/python3

from openehr.rest.demographic import party_get_query, party_post_query

#query = {
#    "maxHits" : 10,
#    "parameters" : "gender=MALE"
#}
#
#response = party_get_query(query)
#
#print(response)

query = [
    { "key" : "gender", "value" : "MALE" }, 
] 
response = party_post_query(query, 10)
print(response)

query = [
    { "key" : "gender", "value" : "MALE" }, 
] 
response = party_post_query(query, 0)
for party in response['parties']:
    print(party['id'], party['lastNames'])
    if 'partyAdditionalInfo' in party:
        additional = party['partyAdditionalInfo']
        for info in additional:
            if info['key'] == 'ehrId':
                print("Ehrid: ", info['value'])
