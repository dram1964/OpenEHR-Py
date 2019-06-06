#!/usr/bin/python3

import json

class InformationOrder:

    composition = {}

    encoding = {
        'code' : 'UTF-8',
        'terminology' : 'IANA_character-sets',
    }

    language = {
        'code' : 'en',
        'terminology' : 'ISO_639-1',
    }
    territory = {
        'code' : 'EN',
        'terminology' : 'ISO_3166-1',
    }

    def __init__(self, composition_format='FLAT'):
        self.composition_format = composition_format

    def add_element(self, element_name, element_data):
        self.composition.update(element_name().composition(element_data))

class composition_category(InformationOrder):

    def composition(self, category_data):
        if self.composition_format == 'FLAT':
            self.flat_composition = {
                "gel_data_request_summary/category|code": "433",
                "gel_data_request_summary/category|terminology": "openehr",
                "gel_data_request_summary/category|value": "event",
            }
            return self.flat_composition

class composition_language(InformationOrder):

    def composition(self, language_data):
        if self.composition_format == 'FLAT':
            self.flat_composition = {
                "gel_data_request_summary/language|code": "en",
                "gel_data_request_summary/language|terminology": "ISO_639-1",
            }
            return self.flat_composition

class composition_context(InformationOrder):

    def composition(self, context_data):
        if self.composition_format == 'FLAT':
            self.flat_composition = {}
            health_care_facility = {
                "gel_data_request_summary/context/_health_care_facility|id": "GOSH",
                "gel_data_request_summary/context/_health_care_facility|id_namespace": "GOSH-NS",
                "gel_data_request_summary/context/_health_care_facility|id_scheme": "GOSH-SCHEME",
                "gel_data_request_summary/context/_health_care_facility|name": "Great Ormond Street",
            }
            setting = {
                "gel_data_request_summary/context/setting|code": "238",
                "gel_data_request_summary/context/setting|terminology": "openehr",
                "gel_data_request_summary/context/setting|value": "other care",
            }
            context_start_time = {
                "gel_data_request_summary/context/start_time": "2018-07-01T00:00:00Z",
            }
            for element in [health_care_facility, setting, context_start_time]:
                self.flat_composition.update(element)
            return self.flat_composition

class composition_service(InformationOrder):

    def composition(self, service_data):
        """
        Service data should be supplied as an array
        of dictionary items with the following keys:
        data = [{
            'service_name' : 'GEL Information data request',
            'service_type' : 'pathology',
            'time' : '2018-07-01T00:00:00Z',
            'state' : ['529', 'scheduled', 'openehr'],
        }]
        If you wish to change the encoding and language values for the
        service_request element, these will need to be changed in the
        Composition's class
        """
        self.flat_composition = {}
        print(len(service_data))
        for service in range(len(service_data)):
            if self.composition_format == 'FLAT':
                service_service = {
                    'gel_data_request_summary/service:' + str(service) + '/service_name' : service_data[service]['service_name'],
                    'gel_data_request_summary/service:' + str(service) + '/service_type' : service_data[service]['service_type'],
                    'gel_data_request_summary/service:' + str(service) + '/time' : service_data[service]['time'],
                }
                service_encoding = {
                    'gel_data_request_summary/service:' + str(service) + '/encoding|code' : self.encoding['code'],
                    'gel_data_request_summary/service:' + str(service) + '/encoding|terminology' : self.encoding['terminology'],
                }
                service_ism_transition = {
                    'gel_data_request_summary/service:' + str(service) + '/ism_transition/current_state|code' : service_data[service]['state'][0],
                    'gel_data_request_summary/service:' + str(service) + '/ism_transition/current_state|terminology' : service_data[service]['state'][2],
                    'gel_data_request_summary/service:' + str(service) + '/ism_transition/current_state|value' : service_data[service]['state'][1],
                }
                service_language = {
                    'gel_data_request_summary/service:' + str(service) + '/language|code' : self.language['code'],
                    'gel_data_request_summary/service:' + str(service) + '/language|terminology' : self.language['terminology'],
                }
                for element in [service_service, service_encoding, service_ism_transition, service_language]:
                    self.flat_composition.update(element)

        return self.flat_composition

class composition_service_request(InformationOrder):

    def composition(self, request_data):
        """
        Service Request data should be supplied as an array 
        of dictionary items with the following keys:
        data = [{
            'narrative' : 'GEL pathology data request',
            'identifier' : '338899LLXX55TT',
            'service_name' : 'GEL Information data request',
            'service_type' : "pathology",
            'expiry_time' : "2018-12-31T00:00:00Z",
            'request_start' : "2011-01-01T00:00:00Z",
            'request_end' :  "2018-01-01T00:00:00Z",
            'request_date' : "2018-07-01T00:00:00",
        }]
        If you wish to change the encoding and language values for the
        service_request element, these will need to be changed in the 
        Composition's class
        """
        self.flat_composition = {}
        for request in range(len(request_data)):
            if self.composition_format == 'FLAT':
                service_request = {
                    'gel_data_request_summary/service_request:' + str(request) + '/expiry_time': request_data[request]['expiry_time'],
                    'gel_data_request_summary/service_request:' + str(request) + '/narrative': request_data[request]['narrative'],
                    'gel_data_request_summary/service_request:' + str(request) + '/requestor_identifier': request_data[request]['identifier'],
                }

                service_request_encoding = {
                    'gel_data_request_summary/service_request:' + str(request) + '/encoding|code': self.encoding['code'],
                    'gel_data_request_summary/service_request:' + str(request) + '/encoding|terminology': self.encoding['terminology'],
                }

                service_request_language = {
                    'gel_data_request_summary/service_request:' + str(request) + '/language|code': self.language['code'],
                    'gel_data_request_summary/service_request:' + str(request) + '/language|terminology': self.language['terminology'],
                }

                service_request_request = {
                    'gel_data_request_summary/service_request:' + str(request) + '/request:0/gel_information_request_details:0/patient_information_request_end_date': request_data[request]['request_end'],
                    'gel_data_request_summary/service_request:' + str(request) + '/request:0/gel_information_request_details:0/patient_information_request_start_date': request_data[request]['request_start'],
                    'gel_data_request_summary/service_request:' + str(request) + '/request:0/service_name': request_data[request]['service_name'],
                    'gel_data_request_summary/service_request:' + str(request) + '/request:0/service_type': request_data[request]['service_type'],
                    'gel_data_request_summary/service_request:' + str(request) + '/request:0/timing': request_data[request]['request_date'],
                    'gel_data_request_summary/service_request:' + str(request) + '/request:0/timing|formalism': 'timing',
                }

                for element in [service_request, service_request_encoding, service_request_language, service_request_request]:
                    self.flat_composition.update(element)

        return self.flat_composition

class composition_territory(InformationOrder):

    def composition(self, territory_code):
        """
        Territory code values are defined in the
        Composition's class
        """
        if self.composition_format == 'FLAT':
            self.flat_composition = {
                "gel_data_request_summary/territory|code": self.territory['code'],
                "gel_data_request_summary/territory|terminology": self.territory['terminology']
            }
            return self.flat_composition

class composition_composer(InformationOrder):


    def composition(self, composer_name):
        """
        composer_name parameter should be provided as a string value
        """
        if not composer_name:
            composer_name = 'openehr-py-' + self.composition_format 
        if self.composition_format == 'FLAT':
            self.flat_composition = {
                "gel_data_request_summary/composer|name": composer_name,
            }
            return self.flat_composition



information_order = InformationOrder('FLAT')
information_order.add_element(composition_composer, None)
information_order.add_element(composition_territory, None)

service_request_data = [
    {
        'narrative' : 'gel cancer data request',
        'identifier' : '553322kkyy33pp',
        'service_name' : 'gel information data request',
        'service_type' : "cancer",
        'expiry_time' : "2019-12-31t00:00:00z",
        'request_start' : "2010-01-01T00:00:00Z",
        'request_end' :  "2019-01-01T00:00:00Z",
        'request_date' : "2019-07-01T00:00:00",
    },
    {
        'narrative' : 'gel pathology data request',
        'identifier' : '553322kkyy33pp',
        'service_name' : 'gel information data request',
        'service_type' : "pathology",
        'expiry_time' : "2019-12-31t00:00:00z",
        'request_start' : "2010-01-01T00:00:00Z",
        'request_end' :  "2019-01-01T00:00:00Z",
        'request_date' : "2019-07-01T00:00:00",
    }
]
information_order.add_element(composition_service_request, service_request_data )
service_data = [
    {
        'service_name' : 'GEL Information data request',
        'service_type' : 'cellular_pathology',
        'time' : '2018-07-01T00:00:00Z',
        'state' : ['529', 'scheduled', 'openehr'],
    },
    {
        'service_name' : 'GEL Information data request',
        'service_type' : 'blood sciences',
        'time' : '2018-07-01T00:00:00Z',
        'state' : ['529', 'scheduled', 'openehr'],
    },
]

information_order.add_element(composition_service, service_data)
information_order.add_element(composition_context, {})
information_order.add_element(composition_language, {})
information_order.add_element(composition_category, {})
print( json.dumps(information_order.composition, sort_keys=True, indent=4) )

