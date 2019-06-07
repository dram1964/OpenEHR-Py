#!/usr/bin/python

import json

data = {
    "germ_data_request_summary": {
        "_uid": [
            "76d20594-bd4c-45e8-8ffc-cdb786ca0d68::default::2"
        ],
        "category": [
            {
                "|code": "433",
                "|terminology": "openehr",
                "|value": "event"
            }
        ],
        "composer": [
            {
                "|name": "OpenEHR-Perl-STRUCTURED"
            }
        ],
        "context": [
            {
                "_health_care_facility": [
                    {
                        "|id": "GOSH",
                        "|id_namespace": "GOSH-NS",
                        "|id_scheme": "GOSH-SCHEME",
                        "|name": "Great Ormond Street"
                    }
                ],
                "setting": [
                    {
                        "|code": "238",
                        "|terminology": "openehr",
                        "|value": "other care"
                    }
                ],
                "start_time": [
                    "2018-07-01T00:00Z"
                ]
            }
        ],
        "language": [
            {
                "|code": "en",
                "|terminology": "ISO_639-1"
            }
        ],
        "service": [
            {
                "encoding": [
                    {
                        "|code": "UTF-8",
                        "|terminology": "IANA_character-sets"
                    }
                ],
                "ism_transition": [
                    {
                        "current_state": [
                            {
                                "|code": "529",
                                "|terminology": "openehr",
                                "|value": "scheduled"
                            }
                        ]
                    }
                ],
                "language": [
                    {
                        "|code": "en",
                        "|terminology": "ISO_639-1"
                    }
                ],
                "service_name": [
                    "GEL Information data request"
                ],
                "service_type": [
                    "pathology"
                ],
                "time": [
                    "2018-07-01T00:00Z"
                ]
            }
        ],
        "service_request": [
            {
                "_uid": [
                    "3695726c-53df-4a97-a4ab-6fe65ef25334"
                ],
                "encoding": [
                    {
                        "|code": "UTF-8",
                        "|terminology": "IANA_character-sets"
                    }
                ],
                "expiry_time": [
                    "2018-12-31T00:00Z"
                ],
                "language": [
                    {
                        "|code": "en",
                        "|terminology": "ISO_639-1"
                    }
                ],
                "narrative": [
                    "GEL pathology data request"
                ],
                "request": [
                    {
                        "gel_information_request_details": [
                            {
                                "patient_information_request_end_date": [
                                    "2018-01-01T00:00Z"
                                ],
                                "patient_information_request_start_date": [
                                    "2011-01-01T00:00Z"
                                ]
                            }
                        ],
                        "service_name": [
                            "GEL Information data request"
                        ],
                        "service_type": [
                            "pathology"
                        ],
                        "timing": [
                            {
                                "|formalism": "timing",
                                "|value": "2018-07-01T00:00:00"
                            }
                        ]
                    }
                ],
                "requestor_identifier": [
                    "834y5jkdk-ssxhs"
                ]
            }
        ],
        "territory": [
            {
                "|code": "ES",
                "|terminology": "ISO_3166-1"
            }
        ]
    }
}

class InformationOrder:
    """
    Holds InformationOrder data
    """
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

    document_root = 'gel_data_request_summary'
    uids = []
    categories = [{ '|code': '433', '|terminology': 'openehr', '|value': 'event'}]
    composers = [{'|name': 'OpenEHR-Py-STRUCTURED'}]
    languages = [ { "|code": language['code'], "|terminology": language['terminology']} ]
    territories = [ { "|code": "EN", "|terminology": "ISO_3166-1" } ]
    contexts = [
            {
                "_health_care_facility": [
                    {
                        "|id": "UCLH",
                        "|id_namespace": "UCLH-NS",
                        "|id_scheme": "UCLH-SCHEME",
                        "|name": "UCLH NHS Foundation Trust"
                    }
                ],
                "setting": [ { "|code": "238", "|terminology": "openehr", "|value": "other care" } ],
                "start_time": [ "2018-07-01T00:00Z" ]
            }
    ]
    services = [
            {
                "encoding": [ { "|code": "UTF-8", "|terminology": "IANA_character-sets" } ],
                "ism_transition": [ { "current_state": [ { "|code": "529", "|terminology": "openehr", "|value": "scheduled" } ] } ],
                "language": [ { "|code": "en", "|terminology": "ISO_639-1" } ],
                "service_name": [ "GEL Information data request" ],
                "service_type": [ "pathology" ],
                "time": [ "2018-07-01T00:00Z" ]
            }
    ]
    service_requests = [
            {
                "_uid": [ "3695726c-53df-4a97-a4ab-6fe65ef25334" ],
                "encoding": [ { "|code": "UTF-8", "|terminology": "IANA_character-sets" } ],
                "expiry_time": [ "2018-12-31T00:00Z" ],
                "language": [ { "|code": "en", "|terminology": "ISO_639-1" } ],
                "narrative": [ "GEL pathology data request" ],
                "request": [
                    {
                        "gel_information_request_details": [
                            {
                                "patient_information_request_end_date": [ "2018-01-01T00:00Z" ],
                                "patient_information_request_start_date": [ "2011-01-01T00:00Z" ]
                            }
                        ],
                        "service_name": [ "GEL Information data request" ],
                        "service_type": [ "pathology" ],
                        "timing": [ { "|formalism": "timing", "|value": "2018-07-01T00:00:00" } ]
                    }
                ],
                "requestor_identifier": [ "834y5jkdk-ssxhs" ]
            }
    ]

    def add_category(self, data):
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
        if data:
            self.categories = [data]

    def add_composer(self, data):
        """
        composer_name parameter should be provided as a string value
        Default value set to the name of the generating class function
        """
        if data:
            self.composers = [{'|name': data }]
    def add_language(self, data):
        """
        Language data should be provided as a dictionary with
        the following keys:
        language_data = {
            'code' : 'es',
            'terminology' : 'ISO_639-1',
        }
        Language data defaults are defined in the InformationOrder class
        """
        if data:
            self.languages = [ data ]

    def write(self, data):
        composition = {}
        composition[self.document_root] = {}
        composition[self.document_root]['_uid'] = []
        composition[self.document_root]['_uid'].extend(self.uids)
        composition[self.document_root]['category'] = []
        composition[self.document_root]['category'].extend(self.categories)
        composition[self.document_root]['composer'] = []
        composition[self.document_root]['composer'].extend(self.composers)
        composition[self.document_root]['context'] = []
        composition[self.document_root]['context'].extend(self.contexts)
        composition[self.document_root]['language'] = []
        composition[self.document_root]['language'].extend(self.languages)
        composition[self.document_root]['service'] = []
        composition[self.document_root]['service'].extend(self.services)
        composition[self.document_root]['service_request'] = []
        composition[self.document_root]['service_request'].extend(self.service_requests)
        composition[self.document_root]['territory'] = []
        composition[self.document_root]['territory'].extend(self.territories)

        return composition

    def read(self, data):
        self.document_root = list(data.keys())[0]
        self.uids = data[self.document_root]['_uid']
        self.categories = data[self.document_root]['category']
        self.composers = data[self.document_root]['composer']
        self.contexts = data[self.document_root]['context']
        self.languages = data[self.document_root]['language']
        self.services = data[self.document_root]['service']
        self.service_requests = data[self.document_root]['service_request']
        self.territories = data[self.document_root]['territory']

compos1 = InformationOrder()
compos1.add_category({ 'code' : '435', 'value' : 'special_event', 'terminology' : 'openehr', } )
compos1.add_composer('David Ramlakhan')

composition = compos1.write(None)
print(json.dumps(composition, indent=4))

compos2 = InformationOrder()
compos2.read(data)
print(compos2.document_root)
print(compos2.uids)
print(compos2.categories)
print(compos2.composers)
print(compos2.contexts)
print(compos2.languages)
print(compos2.services)
print(compos2.service_requests)
print(compos2.territories)
