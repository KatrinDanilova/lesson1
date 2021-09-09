a = 'привет'
b = a.upper() 
print(b)

a = 'Hello!'
b = a.lower() 
print(b)

a = 'катюшка!'
print(a.capitalize())

f = '   Катя '
print(f)
print(f.strip())

a = 'Привет'
print(a.replace('и', 'а').upper())

a = 'learn.python.uz'
print(a.split('.'))

a = 'Введите почту чтобы зарегистрироваться'
print(a.split(' '))

age = 26
message = 'Вам ' + str(age) + ' лет'
print(message)

age = 26
message = 'Вам %s лет' %age
print(message)

age = 26
birth_year = 1990
message = 'Вам {} лет. Вы родились в {} году.'.format(age, birth_year)
print(message)

age = 26
birth_year = 1990
message = 'Вам {1} лет. Вы родились в {0} году.'.format(birth_year, age)
print(message)

password = 'asDf1'
for symbol in password:
    print(symbol, symbol.isalpha())

password = 'asDf1'
print(password, password.isalpha())

