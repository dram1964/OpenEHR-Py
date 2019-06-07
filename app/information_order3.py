#!/usr/bin/python3

class category():

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

class InformationOrder():
    """
    {
        "gel_data_request_summary": {
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
        }
    }
    """
    document_root = 'gel_information_summary_request'
    composition = { document_root : {} }
    category = category()

    def set_category(self, data):
       self.category = data
       self.composition[self.document_root]['category'] = data.composition

    def read(self, data):
        self.document_root = list(data.keys())[0]
        self.composition = { self.document_root : {} }

        for item in data[self.document_root].keys():
            if item == 'category':
                self.category.read(data[self.document_root][item])
                self.composition[self.document_root]['category'] = self.category.composition

class TestSuite:

    def test5():
        data = {
            "gel_data_request_summary": {
                "category": [
                    {
                        "|code": "433",
                        "|terminology": "openehr",
                        "|value": "event"
                    }
                ],
            }
        }
        i_order = InformationOrder()
        i_order.read(data)
        print(i_order.document_root)
        print(i_order.category)
        print(i_order.composition)


    def test1():
        cat1 = category(['433', '434'])
        print(cat1.code)
        print(cat1.value)
        print(cat1.terminology)
        print(cat1.composition)

    def test2():
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
        i_order = InformationOrder()
        print(i_order.document_root)
        print(i_order.composition)

    def test4():
        i_order = InformationOrder()
        cat = category(['433', '435'])
        i_order.set_category(cat)
        print(i_order.category.code)
        print(i_order.category.composition)
        print(i_order.composition)

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        func = getattr(TestSuite, sys.argv[1])
        func()
