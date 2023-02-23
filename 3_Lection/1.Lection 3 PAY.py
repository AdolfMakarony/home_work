"""
В данной программе указывается количество часов, которые отработал человек в неделю
Программа должна расчитать сколько человеку должна быть оплата
"""

hours = int(input('Введите количество отработанных часов: '))
standart_hours = 40  # стандартное количество часов в неделю
standart_hour_pay = 600  # оплата в рублях в час
over_percent = 15  # повышение стандартной ставки
result_pay = 0  # результат, куда нужно записать итоговую оплату в неделю

if hours >= standart_hours:
    standart_hour_pay += standart_hour_pay * over_percent / 100
#    result_pay = standart_hour_pay * hours
#else:
#    result_pay = standart_hour_pay * hours

result_pay = standart_hour_pay * hours
#  -----------------------------------

print(f"Работнику необходимо оплатить {result_pay} рублей.")
