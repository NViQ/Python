import random
import time
a = 'abcdefghijklmnopqrstuvwxyz'
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c = '0123456789'
d = '[]{}()*\,-!?'
all = a + b + c + d
length = int(input('Введите длину пароля '))
password = ''.join(random.sample(all, length))
print('Идет генерация пароля...')
time.sleep(3)
print('Пароль готов ')
print(password)