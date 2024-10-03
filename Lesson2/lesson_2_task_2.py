def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

# Выбор года для проверки


year = 2024

# Вызов функции и сохранение результата в переменную
is_leap_year = is_year_leap(year)

# Вывод результата
if is_leap_year:
    print(f'{year} год является високосным')
else:
    print(f'{year} год не является високосным')
