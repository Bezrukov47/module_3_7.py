# РЕКУРСИЯ. РЕКУРСИВНОЕ УМНОЖЕНИЕ ЦИФР.

def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) <= 1:
        return int(str_number) if str_number != '0' else 1  # Возвращаем 1 вместо 0 для умножения

    first = int(str_number[0])
    if first == 0:  # Игнорируем нули
        return get_multiplied_digits(int(str_number[1:])) # Возвращаем число.

    return first * get_multiplied_digits(int(str_number[1:])) # Bыполняем умножение возвращенного числа на очередное число.
# Примеры  вызова функции (из задания)
result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)