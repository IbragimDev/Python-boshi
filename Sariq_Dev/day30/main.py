"""Python standart kutubxonasi   => Day30"""
# import datetime as dt

# now = dt.datetime.now()
# print(now)
# print(now.date())
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.date())
# print(now.time())

# day
# today = dt.date.today()
# print(f"Bugungi sana {today}")

# time
# now = dt.datetime.now()
# nt = now.time()
# neext_time = dt.time(16)
# print(f"Hozir vaqt {nt}")
# print(neext_time)

# Sanalar orasidagi farq
# bugun = dt.date.today()
# yoz = dt.date(2023, 6, 1)
# farq = yoz - bugun
# print(f"Yozgacha {farq.days} kun qoldi")

# Farqlar
# now = dt.datetime.now()
# soccer = dt.datetime(2023, 5, 8, 23, 45)
# farq = soccer - now
# seconds = farq.seconds
# minutes = int(seconds / 60)
# hours = int(minutes / 60)
# print(f"Fudbo`l boshlanishiga {farq.days} kun {hours} qoldi")


"""❗❗❗ <==> Modul Math ❗❗❗"""
import math

# eng yaqin butun songa qarab yaxlitlash
# x = 4.5
# print(round(x))
# print(math.ceil(x))
# print(math.floor(x))

# ildiz hisoblash
# x = 100
# print(math.sqrt(x))

# daraja hisoblash
# x = 10
# print(math.pow(x, 1 / 3))

"""❗❗❗ modul pprint ❗❗❗"""
# from pprint import pprint
# import json

# filename = "cv.json"
# with open(filename) as f:
#     bemor = json.load(f)

# pprint(bemor)
# import requests

"""qayeridadir xato bor"""
# r = requests.get("https://api.github.com")
# print(r.json())

"""❗❗❗ modul RegEX ❗❗❗"""
import re

# from words_list import words

word1 = "temir"
word2 = "tomir"
word3 = "taxtalar"

andoza = "^t ... r$"

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))
