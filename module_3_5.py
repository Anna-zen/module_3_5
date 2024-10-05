

def get_multiplied_digits(number):
    # Преобразуем число в строку для удобства обработки
    str_number = str(number)

    if len(str_number) > 1:
        first = int(str_number[0])

        return first * get_multiplied_digits(int(str_number[1:]))

    else:
        first = int(str_number[0])
        return first




result = get_multiplied_digits ( 23046 )

print(result)

