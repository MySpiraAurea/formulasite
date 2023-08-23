#{%macro list_users(list_of_user)-%}
#<ul>
#{% for u in users -%}
#    <li>{{u.name}}{{caller(u)}} вызывается специальный метод caller от u
#{%-endfor%}
#</ul>
#{%-endmacro%}
#
#-------------------------------------
#
#{%call(user)list_users(users)%} call вызывается caller при помощи list_users, те вместо caller , будет блок call
#    <ul>
#    <li>age: {{user.age}}
#    <li.weight>: {{user.weight}}
#    </ul>
#{%endcall-%%}

from jinja2 import Template

persons = [
    {'name': 'Алексей', 'old': 18, 'weight': 78.5},
    {'name': 'Николай', 'old': 28, 'weight': 82.3},
    {'name': 'Иван', 'old': 33, 'weight': 94.8},
]

# формируем макроопределение list_users и передаем ему списокlist_of_user
# внутри макроопределения формируем список <ul>
# внутри тега <ul> будут формироваться теги <li> при помощи цикла for для каждого человека
#вместо вызова макроса будем вызывать метод call
html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}}{{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{%endcall -%}    
'''

tm = Template(html)
msg = tm.render(users=persons)

print(msg)

