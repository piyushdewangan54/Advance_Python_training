from jinja2 import Template

# name = input("Enter Name")
# tm = Template("Hello {{name}}")
# msg = tm.render(name=name)
#
# print(msg)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

person = Person('Peter', 24)
tm = Template("My name is {{per.getName()}} and I am of {{per.getAge()}}")
msg = tm.render(per=person)
print(msg)