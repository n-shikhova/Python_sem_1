# Шиховой Натальи

# Задание 1

print("Задание 1")


def Task_1(text):
    text = text.lower()

    d = {}
    for t in text:
        if t in "abcdefghijklmnopqrstuvwxyz":
            d[t] = text.count(t)
    m = max(d.values())
    cont = m
    l = []
    for key in d:
        if d[key] == cont:
            l.append(key)

    l = sorted(l)

    return l[0]


print(Task_1("z zz zz aaa aa bb bbb g gggg L LL LL U"))

# Задание 2

###################################
print("Задание 2")


def Task_2(text):
    count = 0
    res = "Нет последовательности из 3-х слов"
    for i in text.split():
        if i.isalpha():
            count += 1
        else:
            count = 0
        if count >= 3:
            res = "Есть последовательность из 3-х слов"

    return res


print(Task_2("ghjdthrf crjkmrj wdc 2 ghj eio 4"))

# Задание 3

###################################

print("Задание 3")


def Task_3(text):
    prev = ''
    count = 0
    list = []

    for i in text:

        if prev == i or prev == '':
            count += 1

            list.append(count)
            prev = i
        else:

            count = 1
            prev = i

    return max(list)


text = "aaaaaasssssssszzzzzzzzuuuuuuuuuuuuuuuuuuukkkk"

print(Task_3(text))

# Задание 4

###################################

print("Задание 4")


def Task_4(text_str):
    # replace_values = {" ": "", ".": "", ",": "", ":": "", ";": "", "!": "", "?": "", "'": "", '"': ""}
    replace_values = {" ": ""}
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        text_str = text_str.replace(i, j)
    return text_str.upper()


text_str = "Используя функцию replace (), заменяем все пробелы"

# изменяем и печатаем строку

print(Task_4(text_str))

# Задание 5

###################################

print("Задание 5")

mass = [4, 6, 2, 2, 6, 4, 4, 4]


def Task_5(mass):
    res = []
    for i, x in enumerate(mass):
        if i == mass.index(x):
            res.extend([x] * mass.count(x))
    return res


print(Task_5(mass))

# Задание 6

###################################

print("Задание 6")

set_list = [1, 2, 4, 5]

set_int = 3


def Task_6(set_list, set_int):
    res = 0

    for i in set_list:
        if i <= set_int:
            res = i

    return res


print(Task_6(set_list, set_int))

# Задание 7

###################################

print("Задание 7")


def Task_7(x, y):
    checkers = [[0] * 10 for i in range(9)]
    checkers[x][y] = 1
    for i in range(x + 1, 9):
        for k in range(1, 9):

            checkers[i][k] = checkers[i - 1][k - 1] + checkers[i - 1][k + 1]
    res=sum(checkers[8])
    return res



print("Введите значение X")
x = int(input())
print("Введите значение Y")
y = int(input())



print(Task_7(x, y))
