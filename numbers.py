import math

a = 2
b = 3.5
print('a+b={}'.format(a+b)) #addition 
print('a-b={}'.format(a-b)) #subtraction
print('a*b={}'.format(a*b)) #multiplication
print('a/b={}'.format(a/b)) #division

b=3
print('a**b={}'.format(a**b)) #exponentiation

a = 9
a = math.sqrt(a)
print(a)

print(math.sqrt(9))
print(math.sin(1))
print(math.cos(1))

a = 12.789
b = - 10.235
c = 10.3
print(math.ceil(0.02)) #округление вверх
print(math.ceil(a)) #округление вверх
print(math.floor(a)) #округление вниз
print(math.copysign(a, b)) #возвращает число, имеющее модуль такой же, как и у числа X, а знак - как у числа Y.
print(math.fabs(b))  #модуль числа
print(math.factorial(3)) #факториал
print(math.fmod(3,2)) #остаток от деления X на Y.
print(math.frexp(a)) #возвращает мантиссу и экспоненту числа
print(math.fsum([a,b])) #сумма всех членов последовательности. Эквивалент встроенной функции sum(), но math.fsum() более точна для чисел с плавающей точкой
print(sum([a,b])) #сумма (math не нужен)
c='a'
print(math.isfinite(a)) #является ли X числом.
print(math.isfinite(7.896))

print(math.isnan(0))
print(math.isnan(a)) #является ли X NaN (Not a Number - не число)
print(math.isnan(5))

print(math.modf(3.567)) #возвращает дробную и целую часть числа X. Оба числа имеют тот же знак, что и X.
print(math.trunc(a)) #усекает значение X до целого.
print(math.pow(2, 3)) #2**3 возведение в степень

print(math.pi)
print(math.e)

print(round(a))