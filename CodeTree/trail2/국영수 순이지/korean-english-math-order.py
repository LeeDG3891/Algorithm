n = int(input())
name = []
korean = []
english = []
math = []
people = []

class Person:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

    people.append(Person(student_info[0], int(student_info[1]), int(student_info[2]), int(student_info[3])))

people.sort(key = lambda x: (-x.korean, -x.english, -x.math))

for person in people:
    print(person.name, person.korean, person.english, person.math)