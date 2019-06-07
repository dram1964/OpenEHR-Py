#!/usr/bin/python3

class category():

    __name__ = 'category'

    code = []
    value = []
    terminology = []
    composition = []

    codes = {
            '433' : {'|code' : '433', '|value' : 'event1', '|terminology' : 'openehr' },
            '434' : {'|code' : '434', '|value' : 'event2', '|terminology' : 'openehr' },
            '435' : {'|code' : '435', '|value' : 'event3', '|terminology' : 'openehr' },
            '436' : {'|code' : '436', '|value' : 'event4', '|terminology' : 'openehr' },
    }

    def __init__(self, data=None):
        if data:
            for item in data:
                self.code.append( self.codes[item]['|code'] )
                self.value.append( self.codes[item]['|value'] )
                self.terminology.append( self.codes[item]['|terminology'] )
                self.composition.append( self.codes[item] )

    def read(self, data):
        for item in data:
            self.code.append( item['|code'] )
            self.value.append( item['|value'] )
            self.terminology.append( item['|terminology'] )
            self.composition.append( item )

class composer():
        __name__ = 'composer'

        name = []
        composition = []

        def __init__(self, data=None):
            if data:
                for item in data:
                    self.name.append( item )
                    self.composition.append( { '|name' : item } )

        def read(self, data):
            for item in data:
                self.name.append( item['|name'] )
                self.composition.append( item )

class InformationOrder():
    """
    """
    document_root = 'gel_information_summary_request'
    composition = { document_root : {} }
    category = category()
    composer = composer()

    def set_property(self, data):
        my_property = data.__name__
        self.property = data
        self.composition[self.document_root][my_property] = data.composition

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
        print(i_order.composition)

    def test1():
        """
        Write category composition from category data
        """
        cat1 = category(['433', '434'])
        print(cat1.code)
        print(cat1.value)
        print(cat1.terminology)
        print(cat1.composition)

    def test2():
        """
        Read category data from category composition
        """
        data = [
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
        cat2 = category()
        cat2.read(data)
        print(cat2.code)
        print(cat2.value)
        print(cat2.terminology)
        print(cat2.composition)

    def test3():
        """
        Create information order
        """
        i_order = InformationOrder()
        print(i_order.document_root)
        print(i_order.composition)

    def test4():
        """
        Create information order and add category data
        """
        i_order = InformationOrder()
        cat = category(['433', '435'])
        i_order.set_property(cat)
        print(i_order.category.code)
        print(i_order.category.composition)
        print(i_order.composition)


    def test5():
        """
        Create information order from composition
        containing category data
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
            }
        }
        i_order = InformationOrder()
        i_order.read(data)
        print(i_order.composition)

    def test6():
        """
        Write composer composition from composer data
        """
        compos = composer(['David Ramlakhan', 'John Bunyan'])
        print(compos.name)
        print(compos.composition)

    def test7():
        """
        Read composer data from composer composition
        """
        data = [
            {
                "|name": "William Shakespeare"
            },
            {
                "|name": "John Milton"
            },
        ]
        compos = composer()
        compos.read(data)
        print(compos.name)
        print(compos.composition)

    def test8():
        """
        Create information order and add composer data
        """
        i_order = InformationOrder()
        compos = composer(['David Ramlakhan', 'John Bunyan'])
        i_order.set_property(composer)
        print(i_order.composer.name)
        print(i_order.composer.composition)
        print(i_order.composition)

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
        i_order = InformationOrder()
        i_order.read(data)
        print(i_order.document_root)
        print(i_order.category)
        print(i_order.composer)
        print(i_order.composition)

    def test10():
        """
        Create information order and add category data and composer data
        """
        i_order = InformationOrder()
        cat = category(['433', '435'])
        compos = composer(['David Ramlakhan', 'John Bunyan'])
        i_order.set_property(cat)
        i_order.set_property(compos)
        print(i_order.category.code)
        print(i_order.category.composition)
        print(i_order.composer.name)
        print(i_order.composer.composition)
        print(i_order.composition)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        func = getattr(TestSuite, sys.argv[1])
        func()
