'''
Посчитать в файле war and peace и вывести в терминал

1. Количество символов
2. Количество строк
3. Количество уникальных слов
4. Количество знаков препинания 

'''
import string

FILE_PATH = '1_1_task.txt'

symbol_counter = 0
line_counter = 0
unique_words = set()
punctuation_counter = 0 


with open(FILE_PATH, encoding='utf8') as f:
    for line in f:
        line = line.lower()
        line_counter += 1
        line_len = len(line)
        symbol_counter += line_len
        

        for point in string.punctuation:
            if point in line:
                line = line.replace(point, '')

        punctuation_counter += line_len - len(line)
        unique_words = unique_words | set(line.split())


print(f'Количество символов: {symbol_counter}\nКоличество строк: {line_counter}\nКоличество уникальных слов: {len(unique_words)}\nКоличество знаков препинания: {punctuation_counter}\n')