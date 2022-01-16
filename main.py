# author = Shambazov Ruslan. Russia
intro = ("программа для нахождения наименьшего "
         "общего кратного для двух чисел")
print(intro)


def main():
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))

    spisok = [list(func_a(number1)), list(func_a(number2))]
    # list_num1 = list(func_a(number1))
    # list_num2 = list(func_a(number2))

    objects = func_b(spisok)

    result = func_c(objects)
    # print("НОК чисел :", number1, number2, "равно: ", result)
    print("НОК чисел {0} и {1} равно {2}".format(number1, number2, result))


# Функция разложит на множители число
# возвращает массив(список) с множителями
def func_a(num):
    x = 2
    list_num = []
    while x <= num:
        if (num % x) == 0:
            list_num.append(x)
            num /= x
            # return x
        else:
            x += 1
    return list_num


# нахождение общих множителей чисел
# возвращает словарь
# ключ - значение
# множитель - количество множителей (степень множителя!)
def func_b(spisok):
    objects = {}
    for i in spisok:
        for j in i:
            if j in objects:
                if objects[j] < i.count(j):
                    objects[j] = i.count(j)
            else:
                objects[j] = i.count(j)
    return objects


# получает словарь множитель - степень
# перемножает и возвращает значение НОК
def func_c(objects):
    result = 1
    for item in objects:
        result *= item ** objects[item]
    return result


# while True:
main()
