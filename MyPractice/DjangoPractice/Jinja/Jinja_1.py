from jinja2 import Template

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

person = Person("Федор", 28)

tm = Template("Привет, меня зовут {{ p.get_age() }}, мне {{ p.get_name()  }} лет")
msg = tm.render(p=person)

print(msg)

from jinja2 import Template #импортируем класс Template из библиотеки Jinja

name = "Федор"
age = 28

tm = Template("Привет, меня зовут {{ n }}. Мне {{ a }} лет")  #в фигурных скобках стоят ссылки на переменные name и age
msg = tm.render(n=name, a = age)  # указатель будет ссылаться на переменную name

print(msg)