#!/usr/bin/env python
# i
a = "нМаркіян"            # str
b = 913                          # int
b1 = -12.408                     # float

c = ["мармур", -5, 0.125, "барвінок", a, True, None]   # list 

d = {
    "місто": "Львів",
    "рік": 2025,
    a: b,                        
    "активний": False
}                                # dict

e = ("точка", a, b, b1, None)    # tuple 

f = {"ss", a + "_" , 42} # set 

# ii
print("Перша константа:", True)
print(f"Друга константа (f-string): {None}")
print("Третя константа (Ellipsis):", Ellipsis)

# iii
print(bin(34))
print(complex(75))
print(hex(255))

# iv
#1
letters = ['a', 'C', 'b', 'A', 'd']
appercase_letters = []

for i in range(len(letters)):
    if letters[i].isupper():
        appercase_letters.append(letters[i])

print("Великі літери:", appercase_letters)

#2
numbers = [10, -3, 25, 0, -7, 8, 15]
positive_numbers = []

for i in range(len(numbers)):
    if numbers[i] > 0:
        positive_numbers.append(numbers[i])

print("Позитивні числа:", positive_numbers)

#3
char = '*'
height = 5
width = 10

height = 5
char = "#"

for i in range(1, height + 1):
    print(char * i)


# v
# 1
x = -3
if x < 0:
    print("x від'ємний")
elif x == 0:
    print("x дорівнює нулю")
else:
    print("x додатній")

# 2
cmd = "start"
match cmd:
    case "start":
        print("Запускаю…")
    case "stop":
        print("Зупиняю…")
    case _:
        print("Невідома команда")

# vi
data = {"name": "Nazar"}
try:
    price = data["price"]   # KeyError
    print(price)
except KeyError as e:
    print(f"KeyError: ключ {e!s} відсутній")
finally:
    print("finally: завершили доступ до словника")

# vii
from pathlib import Path
with (Path("lab_3(Basic python)") / "notes.txt").open(encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}) {line.rstrip()}")

# viii
add = lambda a, b: a + b
print(add(2, 3))  # 5
