from json import dumps
from faker import Faker
import collections
import jsonMockConfig as conf

database = []
filename = '1M'
fileNum =conf.mocker['filenum']
lines = conf.mocker['lines']
fake     = Faker() # <--- Forgot this
for i in range(fileNum):
    for x in range(lines):
        database.append(collections.OrderedDict([
            ('last_name', fake.last_name()),
            ('first_name', fake.first_name()),
            ('street_address', fake.street_address()),
            ('email', fake.email())
        ]))

    with open(conf.mocker['destination'] +conf.mocker['filename'] + str(i) + '.json', 'w') as output:
        output.write(dumps(database, indent=4))

print ("Done")