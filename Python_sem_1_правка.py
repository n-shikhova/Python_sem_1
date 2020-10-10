# Шиховой Натальи

# Задание 1

print("Задание 1")
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(arr[0], arr[2], arr[-2])

# Задание 2

print("\n Задание 2")
N: int = 3
if len(arr) - 1 < N:
    print(-1)
else:
    print(arr[N] ** N)

# Задание 3
print("\n Задание 3")
sber = list('сбербанк')
symbol = 'б'


def LinearSearch(lys, element):
    k: int = 0
    for i in range(len(lys)):
        if lys[i] == element:
            if k == 0:
                k: int = 1
            elif lys[i] == element and k == 1:
                return i
    return -1


print(LinearSearch(sber, symbol))

# Задание 4

print("\n Задание 4")
arr = int(101100110100)
Count = 0
while arr % 10 == 0:
    arr //= 10
    Count += 1
print(Count)

# Задание 5

print("\n Задание 5")
stroka = "проверка"
print(stroka[::-1])

# Задание 6
print("\n Задание 6")
arr = [1, 1, 1]
n = arr[1]
flag = False
for element in arr:
    if (element != n):
        flag = True
print(flag)

# Задание 7

# импорт библиотеки
print("\n Задание 7")
import re


def password(passwd):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{16}$"

    # составление регулярных выражений

    pat = re.compile(reg)

    # поиск регулярных выражений

    mat = re.search(pat, passwd)

    if mat:

        print("Пароль надежный")

    else:

        print("Пароль не надежный")


if __name__ == '__main__':
    password("PassWord12345678")
    password("PassWord12")
    password("PassWord12345678@")

# Задание 8
print("\n Задание 8")

arr = [7, 6, 5, 4, 3, [2, 4], [[10, 5], 8],[23,"hi"]]

def list_open(arr, l=[]):
    for i in arr:
        if type(i) == list:
            list_open(i)
        else:
            l.append(i)

    return l
print(list_open(arr))


# Задание 9
print("\n Задание 9")

stats = {'нулевой': 35, 'первый': 3, 'второй': 5}

M: int = 0
key = ''
for i in stats:
  if stats[i] > M:
    M = stats[i]
    key = i
if key:
    print(key)


#10
print("\n Задание 10")

arr = [1, 2, 3, 1, 3]
arr_2 = [i for i in arr if arr.count(i) > 1]
if arr_2:
    print(arr_2)
else:
    print('Нет повторяющихся элементов')
