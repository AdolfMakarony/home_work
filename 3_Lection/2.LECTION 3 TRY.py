"""
Данная программ - часть калькулятора, которая расчитвает деление
Необходимо обработать все ошибки, которые могут возникнуть
"""

print("Расчёт деления чисел")
try:
    a = float(input("Числитель: "))
except Exception:
    print('Its not a number!')
    exit()
try:
    b = float(input("Знаменатель: "))
except Exception:
    print('Its not a number!')
    exit()
try:
    print(f"Результат деления: {a / b}")
except ArithmeticError:
    print('Arr error')
    exit()
# except Exception:
#     print('Its not a number!')
