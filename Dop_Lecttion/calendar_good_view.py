"""
СЛОЖНЫЙ УРОВЕНЬ

Функция должна принимать неотсортированный список из 0-7 элементов.
Если список пуст, он просто возвращает пустой массив.
В противном случае он должен составить
отсортированное удобное для человека расписание
рабочего времени и вернуть его как string.

Формат вывода за один
день должен быть ВС: 11:00 - 23:00.

Если два или более дней недели подряд имеют
одинаковые рабочие часы, они должны быть объединены
и иметь следующий формат: ПН - СР: 11:00 - 23:00.
ИНФОРМАЦИЯ
Метод sort у списка переделывает в сортированный список
По стандарту - идёт сортировка от меньшего к большему,
в алфавите от a до z и тд.
Если мы сортируем список из элементов составных типов данных,
то нам нужно указать по какой логике будет идти сортировка
для этого есть аргумент key. Посмотрите файл list_sort в папке info.
"""

days_of_week = ["Пн:", "Вт:", "Ср:", "Чт:", "Пт:", "Сб:", "ВС:"]

def return_day(day):
    return day['day']


def reformat_date(date_list: list):
    date_list.sort(key=return_day)
    for day_num in date_list:
        day_num['day'] = days_of_week[day_num['day']]
        if day_num['from'] == day_num[-1]['from'] and day_num['to'] == day_num[-1]['from']:
            pass
    # date_list_to_sort=date_list
    # for days in date_list:
    #    if days['from'] == date_list_to_sort['from'] and days['to'] == date_list_to_sort['to']:
    #        print('ok')
    # day_list_sl=slice(date_list(0, 7))
    # print(day_list_sl)
    # for day_num1 in date_list:
    #     days = []
    #     days1=[]
    #     for day_num2 in date_list:
    #         # days=[]
    #         if day_num1['from'] == day_num2['from'] and day_num1['to'] == day_num2['to']:
    #             days.append(day_num2)
    #     # days1.append(days)
    #     days1 = set(days)
    print(date_list)



    # return date_list

print(reformat_date([
    {
        "day": 6,
        "from": "10:00",
        "to": "23:00"
    },
    {
        "day": 0,
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": 1,
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": 2,
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": 3,
        "from": "12:00",
        "to": "23:00"
    },
    {
        "day": 4,
        "from": "12:00",
        "to": "23:00"
    },
    {
        "day": 5,
        "from": "11:00",
        "to": "23:00"
    }
]))

## На консоле должно быть
# ПН - СР: 11:00 - 23:00
# ЧТ - ПТ: 12:00 - 23:00
# СБ: 10:00 - 23:00
# ВС: 11:00 - 23:00
