# day -> 14 => Funksiya or function

# def give_me(ism):
#     """Foydalanuvchiga salom beruvchi va ismini aytuvchi function"""
    # print(f"Salom aleykum, qonday {ism.title()} makkammi")

# give_me('Hasan')
# give_me('Dima')    
# print(give_me.__doc__) => Funksiya tavsifi haqida

# def send_name(firstName, lastName ):
#     print(f"Foydalanuvchi ismi: {firstName.title()}")
#     print(f"Foydalanuvchi familiyasi: {lastName.title()}")
    
# send_name("Dima", "Bilan")

# def find(born, now = 2023):
#     print(f"siz {now - born} yoshdasiz")
    
# find(2000, 2023)
# find(1996)

# Amaliy ->

# def find(born, name, now = 2023):
#     print(f"Salom aleykum, qonday {name.title()} yoshingni isoplimismi")    
#     print(f"siz {now - born} yoshdasiz")
# find(1997, "Abdulla" )

# 2
# def find_num(num, num2):
#     print(num ** 2)
#     print(num ** 3)
# find_num(6, 6)

# mood

# def find_num():
#     num = int(input("Hohlagan soningizi kiriting: "))
#     kvadrat = num ** 2
#     kub = num ** 3
#     print(f"Kiritilgan sonning kvatrati: {kvadrat} ")
#     print(f"Kiritilgan sonning kubi: {kub} ")
# find_num()

# 3
# def find_num(num):
#     # num = int(input("Hohlagan soningizi kiriting: "))
#     if num % 2 == 0:
#         print(f"Kiritilgan raqam => {num} va u juft")
#     else:
#         print(f"Kiritilgan raqam => {num} va u toq")
# find_num(8)

# 4
# def findNum(num, num2):
#     if num > num2:
#         print(f'{num} katta {num2} dan')
#     elif num == num2:
#         print(f"{num} teng {num2} ga" )
#     else:
#         print(f'{num2} katta {num} dan')
# findNum(-999, 0)

# 5
# def getNum(x,y):
#     print(f"{x} ning {y} darajasi {x**y} ga teng")
# getNum(4, 4)

# 6
# def getNum(x,y=2):
#     print(f"{x} ning {y} - darajasi {x**y} ga teng")
# getNum(-999)

# 7
# def getNum(num):
#     for n in range(2, 11):
#         if not num % n:
#             print(f"{num} {n} ga qoldiqsiz bo`linadi")
# getNum(99)    