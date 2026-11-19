n = int(input())
name = []
address = []
region = []
people = []

class Person:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

for _ in range(n):
    name_value, address_value, region_value = input().split()
    name.append(name_value)
    address.append(address_value)
    region.append(region_value)
    people.append(Person(name_value, address_value, region_value))

result = people[0]

for person in people:
    if person.name > result.name:
        result = person

print("name", result.name)
print("addr", result.address)
print("city", result.region)