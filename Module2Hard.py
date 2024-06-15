import random

number = random.randrange(3, 20)
print(f'The first stone number: {number}')
result = ''
for i in range(1, number):
    for k in range(1, number):
        if number % (i + k) == 0 and i < k:  # второе условие для исключения повтора чисел с переменой их места
            result += str(i) + str(k)
print(f'The passkey for the second stone: {result}')
