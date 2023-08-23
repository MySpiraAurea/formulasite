#{%if<условие>%}
#    <фрагмент при исполнении условия>
#{%enfif%}

from jinja2 import Template

cities = [{'id': 1, 'city': 'Москва'},
          {'id': 5, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Смоленск'},
          {'id': 11, 'city': 'Калуга'},]

# условие проверяет id больше 6
# Далее идет проверка elif для Москвы и  выводится тэг <option>
#Если нет, то печатает просто имя города (условие else)
link = '''<select name="cities"> 
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{%elif c.city == 'Москва' -%}
    <option>{{c['city']}}</option>    
{%else -%}
    {{c['city']}}
{%endif -%}
{% endfor -%}
</select'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)
