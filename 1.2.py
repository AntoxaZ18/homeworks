'''
Запустить скрипт, после запуска сгенерируются файлы с расширениями. Создать папки с соответсвующими расширениями и рассортировать файлы согласно их расширения 

'''


import random
import string

extensions = ['wav', 'jpg', 'bmp', 'png', 'gif', 'txt', 'xls']

FILE_LENGTH = 10

for i in range(10):
    with open(f'{"".join(random.choice(string.ascii_lowercase) for i in range(FILE_LENGTH))}.{random.choice(extensions)}', 'wb+') as f:
        f.write(b'test_data')

