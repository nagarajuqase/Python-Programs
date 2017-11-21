'''d = {'dict1': {'foo': 1, 'bar': 2}, 'dict2': {'baz': 3, 'quux': 4}}
print d
print d.keys()
print d.values()
print d.values()[0]
print d.values()[0].values()
print d.items()
print d['dict1']
print d['dict1']['foo']

dictVal = [v for (k, v) in d.values()]
print dictVal

for keys, values in d.values():
    print keys,values

for keys, values in d.items():
    for k, v in values.items():
        print v

for keys, values in d.items():
    print keys, values

d1 = {'abc':10, 'bcd':20}
d2 = {'xyz':40, 'mno':30}
d3 = {'first':d1, 'second':d2}
print d3'''

data = {
    "FirstName": "Bhairav",
    "MiddleName": "S",
    "LastName": "Ram",
    "DateOfBirth": "09-01-1984",
    "Contact": {
        "Phone": 9988776655,
        "Email": "bhairav@gmail.com"
    },
    "Address": [
        {
            "Type": "Office",
            "ZipNumber": 560056,
            "Street": "Nagarbhavi Road",
            "City": "Bangalore",
            "Country": "India"
        },
        {
            "Type": "Home",
            "ZipNumber": 560004,
            "Street": "Gandhi Bazaar Road",
            "City": "Chennai",
            "Country": "India"
        }
    ]
}

for i in data['Address']:
    for k in i.keys(), i.values():
        print k