# Day7 =>
# day = input("Bugun qaysi kun ")
# gradus = int(input("Havo harorati qanday ? "))

# if (day.lower() == "yakshnba" or day.lower() == "shanba") and gradus >= 25:
#     print("Bassenynga keetik")
# elif (day.lower() == "yakshnba" or day.lower() == "shanba") and gradus < 25:
#     print("Uyda dam olamiz")
# else:
#     print("Hozir ish kuni")

# prise = 20000
# tea = True
# salat = False

# if tea and salat:
#     prise += 5000
# elif tea or salat:
#     prise += 5000
    
# print(f"Jami summa {prise} ga teng 😁")

# prise = 12000
# tea = 1
# salat = 0
# non = 1
# kompot = 1
# cola = 1

# if tea:
#     print("Mijoz tea sotib oldi")
#     prise += 3000
    
# if salat:
#     print("Mijoz salat sotib oldi")
#     prise += 5000
    
# if non:
#     print("Mijoz non sotib oldi")
#     prise += 3500
    
# if kompot:
#     print("Mijoz kompot sotib oldi")
#     prise += 3500
    
# if cola:
#     print("Mijoz kompot sotib oldi")
#     prise += 2200
    
# print(f"Jami narx {prise} bo`ldi")

# menu = ["osh", "manti", "kozonkabob", "iqra", 'baliq', "somsa", "shashlik"]

# ovqat = input("Nima buyurtma qilasiz ? ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Afsuski bunday ovqat bizda yo`q")

# menu = ["osh", "manti", "kozonkabob", "iqra", 'baliq', "somsa", "shashlik"]
# zakas = ["osh", "manti", "kozonkabob", "barak", "iqra"]

# if zakas:
#     for taom in zakas:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Uzr {taom} bizda bunaqa taom yo`q")
# else:
#     print("Siz hech nima zakas bermadingiz")

# Amaliyot =>

# even_numbers = int(input("hohlagan soningizni yozing "))

# if even_numbers % 2 == 0:
#     print("Rahmat")
# else:
#     print("Bu son juft emas blki toq")

# 2
# age = int(input("Yozinshizni kiriting "))

# if age <= 4 or age >= 60:
#     print("Muzeyga kirish sizga bepul")
# elif age <= 18:
#     print("Muzeyga kiring siz uchun 10 000 so`m")
# elif age > 18:
#     print("Muzeyga kirish sizga 20 000 so`m")

# 3
# num = int(input("Istalgan sonni kiriting "))
# num1 = int(input("Istalgan sonni kiriting "))

# if num == num1:
#     print(f"{num} teng {num1} ga")
# elif num > num1:
#     print(f"{num} katta {num1} dan")
# else:
#     print(f"{num1} katta {num} dan")

# 4

# WARMING ⚠⚠⚠
# products = ["olma", "banan", "uzum", "nok", "qovun", "behi", "anor", "shaftoli", "mandarin", "anjir"]
# savat = []

# for i in range(5):
#     mahsulot = input(f"Savatga {i+1}-mahsulotni qo'shing: ")
# savat.append(mahsulot)

# for mahsulot in savat:
#     if mahsulot in products:
#         print(f"{mahsulot} do'konimizda bor")
#     else:
#         print(f"{mahsulot} do'konimizda yo'q")

# 5

# mahsulotlar = ["olma", "banan", "uzum", "qovun", "shaftoli"]
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []

# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni kiriting: "))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print("Quyidagi mahsulotlar do'konimizda yo'q: ")
# for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# 6
# admins = ["anvar", "bek", "coder", "dima", "umar"]
# login = input("Login kiriting ")

# if login.lower() in admins:
#     print("Login band boshqa login tanlang")
# else:
#     print(f"xush kelibsiz {login}")

# 7
# num = int(input("Hohlagan son kiriting "))

# if num % 2 == 0:
#     print(f"Siz kiritgan son => {num}  <= va u 2 qoldiqsiz bo`linadi")
#     if num % 10 == 10:
#         print(f"Siz kiritgan son => {num} <= 10 qoldiqsiz bo`linadi")
#     else:
#         print(f"Siz kiritgan son =>  {num} <= 10 qoldiqli bo`linadi")
# else:
#     print(f"Siz kiritgan son: {num} 2 qoldiqli bo`linadi")
    
    # 2 yol
# son = int(input("Butun son kiriting: "))
# for i in range(2, 11):
#     if son % i == 0:
#         print(f"{son} soni {i} ga qoldiqsiz bo'linadi")
