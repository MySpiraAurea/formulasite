from jinja2 import Environment, FileSystemLoader, FunctionLoader

persons = [
    {'name': 'Алексей', 'old': 18, 'weight': 78.5},
    {'name': 'Николай', 'old': 28, 'weight': 82.3},
    {'name': 'Иван', 'old': 33, 'weight': 94.8},
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader) #создаем класс окружения со ссылкой на загрузчик

tm = env.get_template('page.html')
msg = tm.render(domain='http://proproprogs.ru', title='Про Jinja')

print(msg)