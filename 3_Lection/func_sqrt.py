"""
Задние
Сделать функцию, которая определяет: число в аргументе квадрат или нет
"""
def issquare(arg):
    result=(arg**(0.5))
    return float.is_integer(result)

print(issquare(25)) # True
print(issquare(30)) # False
