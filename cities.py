#8-5

def describe_city(name, country = "England"):
    print(name.title() + " is in " + country.title() + ".")

describe_city('liverpool')
describe_city('newcastle')
describe_city('prague', country = 'czech republic')