# """
# В данной программе считается количество пробелов в строке str_var.
# Задачи
# 1. Заменить пробел на букву 'o'
# 2. Добавить в программу ввод буквы для поиска
# 3. Добавить вывод списка индексов(где находится) буква для поиска
#
# Дополнительно
# 4. Сделать проверку на то, чтобы для поиска использовался 1 символ
# 5. Вывести строку без символов, который ищется
# 6. Сделать программу которая будет спрашивать: Хотите найти ещё один символ?
# """

str_var = "hello, how are you!?"
print(str_var.replace(' ', 'o'))

#answer = 'y'
str_var = "hello, how are you!?"
#while answer == 'y':
for tries in range (1000):
    char_to_find=str(input('Enter char\n'))

    if len(char_to_find) > 1:
        print('Entered >1 value')
        # char_to_find = input('Введите один символ!')

    else:
        print([pos for pos, char in enumerate(str_var) if char == char_to_find])
        print('Количество ', str_var.count(char_to_find))
        print(str_var.replace(char_to_find, ''))
        answer = input('Хотите найти ещё один символ? y/n\n')
        if answer != 'y':
            break