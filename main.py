# author = Shambazov Ruslan. Russia
intro = ("программа для нахождения наименьшего "
         "общего кратного для любого количества чисел")
print(intro)


def main():
    numb = int(input("Введите количество чисел: "))
    spisok_a = func_d(numb)
    spisok = []
    for item in spisok_a:
        spisok.append(list(func_a(item)))

    objects = func_b(spisok)

    result = func_c(objects)
    # print("НОК чисел :", number1, number2, "равно: ", result)
    # print("НОК чисел {0} и {1} равно {2}".format(number1, number2, result))
    print("НОК чисел")
    for item in spisok_a:
        print(item)
    print("равно", result)


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


def func_d(numb):
    i = 1
    spisok = []
    while i <= numb:
        spisok.append(int(input("Введите очередное число: ")))
        i += 1
    return spisok


# while True:
main()
