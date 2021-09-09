name = input('Введите имя: ')
print(f'Ваше имя {name.capitalize()}')

user_info = {}
user_info['first_name'] = 'Екатерина'
user_info['last_name'] = 'Данилова'
print(user_info['first_name'])

user_info = {
    'first_name':'',
    'last_name':''
}
user_info['first_name'] = input('Введите ваше имя: ')
user_info['last_name'] = input('Введите вашу фамилию: ')
print(f"Привет {user_info['first_name']} {user_info['last_name']}")