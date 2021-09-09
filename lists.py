a = [1, 5, 8, -6, 0]
print(a[3])
print(a[2:4]) #последний индекс не включается

a.append(99)
print(a)

a = [1, 2, 3]
b = [4, 5, 6]
c = a+b
print(c)

for i in c:
    print(i)

capitals = ['Краснодар', 'Москва', 'Ростов', 'Минск']
capitals.reverse()
print('Обратный список:', capitals)

scores = [1, 2, 3]
scores = reversed(scores)
print(scores)

numbers = [1, 2, 3, 4]
print(list(reversed(numbers)))

numbers = [1, 2, 3, 4]
for i in reversed(numbers) :
    print(i)

numbers = [1, 5, 3, 6] 
print(sorted(numbers))

capitals = ['Краснодар', 'Москва', 'Ростов', 'Минск']
print(sorted(capitals))