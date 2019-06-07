#!/usr/bin/python

import json

data = {
    "germ_data_request_summary": {
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
    }
}

class InformationOrder():
    """
    Holds InformationOrder data
    """

    class category:
        code = ''
        value = ''
        terminology = ''
        composition = ''

        lookup = {
            '433' : {'|code' : '433', '|value' : 'event1', '|terminology' : 'openehr' },
            '434' : {'|code' : '434', '|value' : 'event2', '|terminology' : 'openehr' },
            '435' : {'|code' : '435', '|value' : 'event3', '|terminology' : 'openehr' },
            '436' : {'|code' : '436', '|value' : 'event4', '|terminology' : 'openehr' },
        }

        def __init__(self, code):
            self.code = self.lookup[code]['|code']
            self.value = self.lookup[code]['|value']
            self.terminology = self.lookup[code]['|terminology']
            self.composition = self.lookup[code]

        def compose(self):
            self.composition = self.lookup[self.code]
            return self.composition

        def set_code(self, code):
            self.__init__(code)

    class composer:
        name = ''
        composition = ''

        def __init__(self, data):
            self.name = data
            self.composition = { '|name' : data }

        def compose(self):
            return self.composition

        def set_name(self, data):
            self.__init__(data)

    composition = {}

    document_root = 'gel_data_request_summary'
    uids = []
    categories = [ category('433') ]
    composers = [ composer('OpenEHR-Python') ]

    def set_item(self, item_name, object_name, data ):
        if data:
            self.item_name = []
            for item in data:
                self.item_name.append( object_name(item))

    def set_category(self, data):
        """
        Category data should be provided as a an 
        array of strings with each string being a valid
        category code
        """
        if data:
            self.categories = []
            for item in data:
                self.categories.append( self.category(item) )

    def set_composer(self, data):
        """
        composer_name parameter should be provided as a string value
        Default value set to the name of the generating class function
        """
        if data:
            self.composers = []
            for item in data:
                self.composers.append( self.composer(item) )

    def write_document_root(self):
        self.composition[self.document_root] = {}

    def write_category(self):
        self.composition[self.document_root]['category'] = []
        for category in self.categories:
            self.composition[self.document_root]['category'].append(category.composition)

    def write_composer(self):
        self.composition[self.document_root]['composer'] = []
        for composer in self.composers:
            self.composition[self.document_root]['composer'].append(composer.composition)

    def write(self):
        self.write_document_root()
        self.write_category()
        self.write_composer()


    def read(self, data):
        def read_categories(data):
            categories = []
            for item in data:
                item_obj = category( item['|code'])
                categories.append(item_obj)
            return categories

        def read_composers(data):
            composers = []
            for item in data:
                item_obj = composer( item['|name'])
                composers.append(item_obj)
            return composers


        self.document_root = list(data.keys())[0]
        self.categories = read_categories( data[self.document_root]['category'] )
        self.composers = read_composers( data[self.document_root]['composer'] )


compos1 = InformationOrder()
#compos1.set_category(['433', '434'])
compos1.set_item('categories', compos1.category, ['433', '434'])
compos1.set_composer(['David Ramlakhan', 'John Duncan'])
compos1.write()
print('Compos1:', json.dumps(compos1.composition, indent=4))

#compos2 = InformationOrder()
#compos2.read(data)
#composition = compos2.write()
#print('Compos2:',  json.dumps(composition, indent=4) )
