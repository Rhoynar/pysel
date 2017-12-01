employee = {
    'id' : 12345,
    'name' : 'John Doe',
    'ssn' : 86749380484,
    'contact' : {
        'phone_number': '+1 (765) 836-7493',
        'address': '123, Main St',
        'city': 'Denver',
        'state': 'CO',
        'zipcode': 80012
    },
    'manager' : {
        'id' : 8346746,
        'name' : 'Manager Joe',
    },
    'department' : {
        'id' : 1234,
        'name' : 'Human Resources'
    }
}

import pprint
pprint.pprint(employee)
