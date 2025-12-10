#1-misol
a = int(input())
b = int(input())

if a < b:
    print("Kichigi:", a)
elif b < a:
    print("Kichigi:", b)
else:
    print("Ikkalasi teng")

#2-misol
k = int(input())

if k == 1:
    print("Dushanba")
elif k == 2:
    print("Seshanba")
elif k == 3:
    print("Chorshanba")
elif k == 4:
    print("Payshanba")
elif k == 5:
    print("Juma")
elif k == 6:
    print("Shanba")
elif k == 7:
    print("Yakshanba")
else:
    print("Xato!")

#3-misol
h = input().lower()

if h in "aoiue":
    print("Unli")
else:
    print("Undosh")

#4-misol
p = input()

if len(p) >= 6:
    print("Parol qabul qilindi")
else:
    print("Parol juda qisqa")

#5-misol
gol = int(input())

if gol >= 3:
    print("Zo‘r o‘yin!")
elif gol == 2:
    print("Yaxshi o‘yin")
elif gol == 1:
    print("Qoniqarli")
else:
    print("Yomon natija")

#6-misol
a = int(input())
b = int(input())

o = (a + b) / 2

if o > 0:
    print("O‘rtacha musbat:", o)
else:
    print("O‘rtacha manfiy:", o)

#7-misol
a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180:
    print("To‘g‘ri uchburchak")
else:
    print("Uchburchak emas")

#8-misol
n = int(input())

if n % 3 == 0:
    print("3 ga bo‘linadi")
else:
    print("3 ga bo‘linmaydi")

#9-misol
t = int(input())

if t >= 30:
    print("Issiq")
elif t >= 15:
    print("Yoqimli")
elif t >= 0:
    print("Sovuq")
else:
    print("Juda sovuq")

#10-misol
n = int(input())  # masalan 123

if 100 <= n <= 999:
    b = n // 100
    o = (n // 10) % 10
    y = n % 10
    print(y, o, b, sep="")
else:
    print("Uch xonali son emas!")
