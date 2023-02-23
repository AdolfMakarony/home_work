"""
Данная программ - часть калькулятора, которая расчитвает деление
Необходимо обработать все ошибки, которые могут возникнуть
"""

print("Расчёт деления чисел")
try:
    a = float(input("Числитель: "))
    b = float(input("Знаменатель: "))
    try:
        print(f"Результат деления: {a / b}")
    except ArithmeticError:
        print('Arr error')
except Exception:
    print('Its not a number!')
