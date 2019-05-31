#!/usr/bin/env python3
"""
File: openehr.conf
Package module holding configuration settings for the
openehr package. 
Package can be run from the command line:
python openehr/conf.py [setting[0],...,setting[n]
With no arguments returns a list of configured settings
With arguments returns the value for the setting
"""

test_ehrid = '33b11502-9e5c-41f0-9cea-93b851c85b67'
test_uid = '1c11d0b2-d9fa-4fac-b5f4-e9b44aa4bf10::default::2'
test_subject_id = '3333333333'

service_url = 'http://thinkehr:8081/rest/v1/'
user_name  = 'admin'
password = 'admin'

if __name__ == '__main__':
    import sys
    import conf
    if len( sys.argv ) == 1:
        print('Configured attributes: ')
        print( [attr for attr in conf.__dict__ if not attr.startswith('__')] )
    else:
        for attr in sys.argv[1:]:
            if attr in conf.__dict__:
                print('%s is %s' % (attr, getattr(conf, attr)))
            else:
                print('Unconfigured setting %s' % attr)
