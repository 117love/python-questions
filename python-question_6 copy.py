# ******************************************************************************
#   問題 6: 辞書の操作                                                             
#                                                                             
#   辞書 person から、キー "age" の値を出力してください。                        
# ******************************************************************************

def check_number(num):
    if num % 2 == 0:
        print("偶数です")
    else:
        print("奇数です")

def dog(a, b):
    if a > b:
        return a - b
    else:
        return b - a

def japan (a, b):
    if b != 0:
        return a / b
    else:
        return 0

def apple(a, b):
    if a * b > 100:
        return a * b
    else:
        return a + b

def carrot(a, b):
    if a < b:
        return a ** 2
    else:
        return b ** 2

try:
    x = int(input("1つ目の整数を入力してください： "))
    y = int(input("2つ目の整数を入力してください： "))
except ValueError:
    print("整数を入力してください")
else:
    r1 = dog(x, y)
    r2 = japan(x, y)
    r3 = apple(x, y)
    r4 = carrot(x, y)
    total = int(r1 + r2 + r3 + r4)
    print("最終結果:", total)
    check_number(total)