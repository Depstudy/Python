
#Task 1:
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
with open('my_file.txt', 'a') as new_f:
    text = None
    while text != '':
        text = input('Введите текст:')
        new_f.writelines(text + '\n')
'''
#Task 2:
# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open('my_file.txt') as new_f:
    words = 0
    for lines, line in enumerate(new_f, 1):
        words = len(line.split())
        print(f'Количество слов в строке {lines}: {words}')
    print(f'Количество строк в данном файле: {lines}')
'''