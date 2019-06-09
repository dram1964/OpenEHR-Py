#!/usr/bin/python3

class category():

    __name__ = 'category'

    code = ['433']
    value = ['event']
    terminology = ['openehr']
    composition = [
        {
            "|code": "433",
            "|terminology": "openehr",
            "|value": "event"
        },
    ]

    codes = {
            '433' : {'|code' : '433', '|value' : 'event1', '|terminology' : 'openehr' },
            '434' : {'|code' : '434', '|value' : 'event2', '|terminology' : 'openehr' },
            '435' : {'|code' : '435', '|value' : 'event3', '|terminology' : 'openehr' },
            '436' : {'|code' : '436', '|value' : 'event4', '|terminology' : 'openehr' },
    }

    def __init__(self, data=None):
        if data:
            self.code, self.value, self.terminology, self.composition = [], [], [], []
            for item in data:
                self.code.append( self.codes[item]['|code'] )
                self.value.append( self.codes[item]['|value'] )
                self.terminology.append( self.codes[item]['|terminology'] )
                self.composition.append( self.codes[item] )

    def read(self, data):
        self.code, self.value, self.terminology, self.composition = [], [], [], []
        for item in data:
            self.code.append( item['|code'] )
            self.value.append( item['|value'] )
            self.terminology.append( item['|terminology'] )
            self.composition.append( item )

class composer():
        __name__ = 'composer'

        name = ['William Shakespeare']
        composition = [
            {
                "|name": "William Shakespeare"
            },
        ]

        def __init__(self, data=None):
            if data:
                # remove default values
                self.name = []
                self.composition = []
                for item in data:
                    self.name.append( item )
                    self.composition.append( { '|name' : item } )

        def read(self, data):
            self.name = []
            self.composition = []
            for item in data:
                self.name.append( item['|name'] )
                self.composition.append( item )

class InformationOrder():
    """
    """
    document_root = 'gel_information_summary_request'
    category = category()
    composer = composer()
    composition = { document_root : {} }

    def compose(self):
        for item in ( 'category', 'composer'):
            obj_name = getattr(self, item)
            self.composition[self.document_root][item] = obj_name.composition

    def read(self, data):
        self.document_root = list(data.keys())[0]
        self.composition = { self.document_root : {} }

        for item in data[self.document_root].keys():
                my_property = getattr(self, item)
                my_property.read(data[self.document_root][item])
                self.composition[self.document_root][item] = my_property.composition

class TestSuite:

    def test11():
        """
        Create information order with category and composer defaulted
        """
        i_order = InformationOrder()
        i_order.compose()
        print(i_order.composition)

    def test1():
        """
        Write category composition from category data
        """
        categories = ['433', '434']
        print('*** (1): Write categories composition from array of category codes', categories)
        cat1 = category(categories)
        print('Category codes:', cat1.code)
        print('Category values:', cat1.value)
        print('Category terminologies:', cat1.terminology)
        print('Category composition:', cat1.composition)

    def test2():
        """
        Read category data from category composition
        """
        categories = [
            {
                "|code": "433",
                "|terminology": "openehr",
                "|value": "event"
            },
            {
                "|code": "233",
                "|terminology": "special",
                "|value": "event5"
            }
        ]
        print('*** (2): Read category data from category composition', categories)
        cat1 = category()
        cat1.read(categories)
        print('Category codes:', cat1.code)
        print('Category values:', cat1.value)
        print('Category terminologies:', cat1.terminology)
        print('Category composition:', cat1.composition)

    def test3():
        """
        Create information order
        """
        print('*** (3): Create Information Order with no data')
        i_order = InformationOrder()
        print('Document Root:', i_order.document_root)
        print('Information Order composition', i_order.composition)

    def test4():
        """
        Create information order and add category data
        """
        categories = ['433', '434']
        print('*** (4): Create Information Order with category codes array', categories)
        i_order = InformationOrder()
        i_order.category = category(categories)
        i_order.compose()
        print('Information Order category:', i_order.category)
        print('Information Order category codes:', i_order.category.code)
        print('Information Order composition:', i_order.composition)


    def test5():
        """
        Create information order from composition
        containing category data
        """
        categories = {
            "gel_data_request_summary": {
                "category": [
                    {
                        "|code": "433",
                        "|terminology": "openehr",
                        "|value": "event"
                    },
                    {
                        "|code": "234",
                        "|terminology": "openehr",
                        "|value": "event2"
                    }
                ],
            }
        }
        print('*** (5): Create Information Order and read in category composition:', categories)
        i_order = InformationOrder()
        i_order.read(categories)
        print('Information Order category code', i_order.category.code)
        print('Information Order composition:', i_order.composition)

    def test6():
        """
        Write composer composition from composer data
        """
        composers = ['David Ramlakhan', 'John Bunyan']
        compos = composer(composers)
        print('*** (6): Create composer composition from composer name array:', composers)
        print('Composer names:', compos.name)
        print('Composer composition:', compos.composition)

    def test7():
        """
        Read composer data from composer composition
        """
        composers = [
            {
                "|name": "William Shakespeare"
            },
            {
                "|name": "John Milton"
            },
        ]
        print('*** (7): Create composer object from composer composition:', composers)
        compos = composer()
        compos.read(composers)
        print('Composer names:', compos.name)
        print('Composer composition:', compos.composition)

    def test8():
        """
        Create information order and add composer data
        """
        composers = ['David Ramlakhan', 'John Bunyan']
        print('*** (8): Create information order and add composer data', composers)
        i_order = InformationOrder()
        i_order.composer = composer(composers)
        i_order.compose()
        print('Information Order composer names:', i_order.composer.name)
        print('Information Order composer composition:', i_order.composer.composition)
        print('Information Order composition:', i_order.composition)

    def test9():
        """
        Create information order from composition
        containing composer and category data
        """
        data = {
            "gel_data_request_summary": {
                "category": [
                    {
                        "|code": "433",
                        "|terminology": "openehr",
                        "|value": "event"
                    },
                    {
                        "|code": "234",
                        "|terminology": "openehr",
                        "|value": "event2"
                    }
                ],
                'composer' : [
                    {
                        "|name": "William Shakespeare"
                    },
                    {
                        "|name": "John Milton"
                    },
                ]
            }
        }
        print('*** (9): Create Information Order and read category and composer data from composition', data)
        i_order = InformationOrder()
        i_order.read(data)
        print('Information Order document root:', i_order.document_root)
        print('Information Order category:', i_order.category)
        print('Information Order composer:', i_order.composer)
        print('Information Order composition', i_order.composition)

    def test10():
        """
        Create information order and add category data and composer data
        """
        i_order = InformationOrder()
        categories = ['433', '435']
        composers = ['David Ramlakhan', 'John Bunyan']
        print('*** (10): Add category and composer data to Information Order from arrays', categories, composers)
        i_order.category = category(categories)
        i_order.composer = composer(composers)
        i_order.compose()
        print('Information Order category codes:', i_order.category.code)
        print('Information Order category composition:', i_order.category.composition)
        print('Information Order composer names', i_order.composer.name)
        print('Information Order composer composition', i_order.composer.composition)
        print('Information Order composition', i_order.composition)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        func = getattr(TestSuite, sys.argv[1])
        func()
