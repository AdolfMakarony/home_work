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

days_of_week = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вc"]


def return_day(day):
    return day['day']


def reformat_date(date_list: list):
    date_list.sort(key=return_day)

    for days in date_list:
        days['day'] = days_of_week[days['day']]
        days['start'] = days['day']
        days['end'] = days['day']
        # days.pop('day')
        d = 0
    for i in range(len(date_list) - 1):

        if date_list[d]['from'] == date_list[d + 1]['from'] and date_list[d]['to'] == date_list[d + 1]['to']:
            date_list[d + 1]['start'] = date_list[d]['start']
            date_list.pop(d)
        else:
            d += 1
    res = []
    for days2 in date_list:
        if days2['start'] != days2['end']:
            days2['day'] = days2['start'] + ' - ' + days2['end'] + ': ' + days2['from'] + ' - ' + days2['to']
        else:
            days2['day'] = days2['start'] + ': ' + days2['from'] + ' - ' + days2['to']
        res.append(days2['day'])

    return print(*res, sep='\n')


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
    },

]))

## На консоле должно быть
# ПН - СР: 11:00 - 23:00
# ЧТ - ПТ: 12:00 - 23:00
# СБ: 10:00 - 23:00
# ВС: 11:00 - 23:00
