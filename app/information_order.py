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

    def composition(self, data):
        """
        Category data should be provided as a dictionary 
        with the following keys:
        category_data = {
            'code' : '433',
            'value' : 'event',
            'terminology' : 'openehr',
        }
        Default values are contained within this class
        """
        category_data = {
            'code' : '433',
            'value' : 'event',
            'terminology' : 'openehr',
        }
        if data:
            category_data.update(data)

        if self.composition_format == 'FLAT':
            self.flat_composition = {
                "gel_data_request_summary/category|code": category_data['code'],
                "gel_data_request_summary/category|terminology": category_data['terminology'],
                "gel_data_request_summary/category|value": category_data['value'],
            }
            return self.flat_composition

class composition_language(InformationOrder):

    def composition(self, data):
        """
        Language data should be provided as a dictionary with 
        the following keys: 
        language_data = {
            'code' : self.language['code'],
            'terminology' : self.language['terminology'],
        }
        Language data defaults are defined in the InformationOrder class
        """
        language_data = {
            'code' : self.language['code'],
            'terminology' : self.language['terminology'],
        }
        if data:
            language_data.update(data)

        if self.composition_format == 'FLAT':
            self.flat_composition = {
                "gel_data_request_summary/language|code": language_data['code'],
                "gel_data_request_summary/language|terminology" : language_data['terminology'],
            }
            return self.flat_composition

class composition_context(InformationOrder):

    def composition(self, data):
        """
        Context data should be provided in a dictionary 
        with the following keys:
        context_data = {
            'context' : {
                'id' : 'UCLH',
                'namespace' : 'UCLH-NS',
                'scheme' : 'UCLH-SCHEME',
                'name' : 'UCLH NHS Foundation Trust',
            },
            'setting' : {
                'code' : '238',
                'value' : 'other care',
                'terminology' : 'openehr',
            },
            'start_time' : "2018-07-01T00:00:00Z",
        }
        Default values are defined within this class
        """
        context_data = {
            'context' : {
                'id' : 'UCLH',
                'namespace' : 'UCLH-NS',
                'scheme' : 'UCLH-SCHEME',
                'name' : 'UCLH NHS Foundation Trust',
            },
            'setting' : {
                'code' : '238',
                'value' : 'other care',
                'terminology' : 'openehr',
            },
            'start_time' : "2018-07-01T00:00:00Z",
        }
        if data:
            context_data.update(data)
        if self.composition_format == 'FLAT':
            self.flat_composition = {}
            health_care_facility = {
                "gel_data_request_summary/context/_health_care_facility|id": context_data['context']['id'],
                "gel_data_request_summary/context/_health_care_facility|id_namespace": context_data['context']['namespace'],
                "gel_data_request_summary/context/_health_care_facility|id_scheme": context_data['context']['scheme'],
                "gel_data_request_summary/context/_health_care_facility|name": context_data['context']['name'],
            }
            setting = {
                "gel_data_request_summary/context/setting|code": context_data['setting']['code'],
                "gel_data_request_summary/context/setting|terminology": context_data['setting']['terminology'],
                "gel_data_request_summary/context/setting|value": context_data['setting']['value'],
            }
            context_start_time = {
                "gel_data_request_summary/context/start_time": context_data['start_time'],
            }
            for element in [health_care_facility, setting, context_start_time]:
                self.flat_composition.update(element)
            return self.flat_composition

class composition_service(InformationOrder):

    def composition(self, data):
        """
        Service data should be supplied as an array
        of dictionary items with the following keys:
        data = [{
            'service_name' : 'GEL Information data request',
            'service_type' : 'pathology',
            'time' : '2018-07-01T00:00:00Z',
            'state' : ['529', 'scheduled', 'openehr'],
        }]
        No default values are defined for the above items.
        Default values for encoding and language elements are
        defined in the InformationOrder class
        """
        service_data = []
        if data:
            service_data = data
        else:
            print('No Service data provided')

        self.flat_composition = {}
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

    def composition(self, data):
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
        No default values are defined for the above items.
        Default values for encoding and language elements are
        defined in the InformationOrder class
        """
        request_data = []
        if data:
            request_data = data
        else:
            print('No Service Request data provided')

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

    def composition(self, data):
        """
        Territory data should be provided as a dictionary with 
        the following keys: 
        territory = {
            'code' : 'EN',
            'terminology' : 'ISO_3166-1',
        }
        Territory data defaults are defined in the InformationOrder class
        """
        territory = {
            'code' : self.territory['code'],
            'terminology' : self.territory['terminology'],
        }
        if data:
            territory.update(data)

        if self.composition_format == 'FLAT':
            self.flat_composition = {
                "gel_data_request_summary/territory|code": territory['code'],
                "gel_data_request_summary/territory|terminology": territory['terminology']
            }
            return self.flat_composition

class composition_composer(InformationOrder):


    def composition(self, composer_name):
        """
        composer_name parameter should be provided as a string value
        Default value set to the name of the generating class function
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
information_order.add_element(composition_context, None)
information_order.add_element(composition_language, None)
information_order.add_element(composition_category, None)

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

print( json.dumps(information_order.composition, sort_keys=True, indent=4) )

