from random import randint


first_name = str(input('Введите фамилию: '))
lastname = str(input('Введите имя: '))
age = int(input('Введите возраст: '))
wt = float(input('Введите вес: '))
comment = str(input('Недуг со слов пациента: '))

print(first_name,'', lastname, ' вы записаны к врачу!', '\n','Ваш возраст: ', age, '\n', 'Ваш вес: ', wt, '\n', 'Ваш недуг: ', comment, '\n' 'Номер вашего талона', randint(0, 100))