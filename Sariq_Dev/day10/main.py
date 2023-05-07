# day 10 =>  Lug`atlar bn ishlash

# student = {
#     "ism" : "vali",
#     "last_name" : "aliyev",
#     "kurs":2,
#     "fakultet":"Fiz-mat",
#     "city":"urganch"
# }
# # print({student["ism   "]})

# print(student.items())
# for key, value in student.items():
#     print(f"Kalit:{key}")
#     print(f"Qiymat:{value}")
    
# phones = {
#     "ali":"iphone x",
#     "vali":"iphone 11",
#     "olim":"samsung a52",
#     "anvar":"Redmi 7"
# }
# for key, value in phones.items():
#     print(f"{key.title()}ning telefoni {value}")

# cars = {
#     "mers":"mybax",
#     "bmw":"m2",
#     "hyundai":"sanata",
#     "kia":"k5",
#     "chevrolet":"malibu"
# }
# print(cars.keys())
# print("Do`kondagi bor mashinalar:")
# for car in cars:
#     print(car.title())
    
# .keys() -> dictionary ichidagi keys olinadi, \n .values() yordamida esa valular olnadi (:nuqtadan keyinkila value hisoblanadi)

# cars = {
#     "mers":2000,
#     "bmw":3000,
#     "hyundai":2500,
#     "kia":5000,
#     "chevrolet":500
# }
# bozorlik = ["bmw", "kia", "malibu", "nexia", "porch"]
# for buy in cars:
#         if buy in bozorlik:
#             print(f"{buy.title()} {cars[buy]} dollar")
            
# for buyum in cars:
#     if buyum in bozorlik:
#         print(f"Iltimos salonga {buyum} ham olib keling")

# print("salomdagi cars ")
# for car in sorted(cars):
#     print(car.title())

# toys = {"ball", "bike", "moto", "doll", "ball"}
# print(toys)

# Amaliyot ->

# python_dic = { 
#     "boolen":"Mantiqiy qiymat", 
#     "float":"kasr son",
#     "for":"biron amalni qayta - qayta bajarish amali",
#     "if":"shart operatori (agar degan ma`noni bildiradi)",
#     "integer":"butun son",
#     "[]":"bu katta qavslar list deb ataladi",
#     "title()":"har bir so`zni bosh harf bulan yozadi",
#     "strip":"so`zdagi mavjud bo`shliqni olib tashlaydi",
#     "keys()":"lug`atdagi keylarni olib beradi",
#     "value":"lug`atdagi valularni olib beradi",
#     "set()":"lug`atdagi takrorlangan so`zlarni olib tashlaydi olib beradi"
# }
# for words in sorted(python_dic):
#     print(f"{words.title()} - {python_dic[words]}")
 
#  2
# countryes = {
    
# "Afghanistan": "Kabul",
# "Albania" :"Tirana", 
# "Algeria":"Algiers", 
# "Andorra" :	"Andorra la Vella", 
# "Angola":"Luanda", 
# "Bahamas":"Nassau",
# "Bahrain":"Manama",
# "Barbados":"Bridgetown",
# "Austria": "Vienna",
# "USA":"Washington",
# "Uk":"london",
# "Kazak":"astana"
# }
# for country in countryes.keys():
#     print(country)
# for country in countryes.values():
#     print(country)
    
# 3
# davlat = input("Qaysi davlatni poytaxtini bilishni hohlaysi ? ").upper()
# if davlat in countryes:
#     capital = countryes[davlat]
#     print(f"{davlat}ning poytaxti: {capital}")
# else:
#     print("Bizda bunday ma'lumot yo'q")

# 4
# menu = {
#     'osh': 15000,
#     'shashlik': 12000,
#     'somsa': 8000,
#     'manti': 10000,
#     'lag\'mon': 14000,
#     'salat': 9000,
#     'choy': 3000,
#     'non': 2500,
#     'shorva': 11000,
#     'kebab': 13000
# }

# buyurtmalar = []
# for i in range(3):
#     taom = input(f"{i + 1}-taomni kiriting: ")
#     if taom in menu:
#         narh = menu[taom]
#         buyurtmalar.append((taom, narh))
#     else:
#         print(f"Bizda {taom} yo'q")

# if buyurtmalar:
#     print("Sizning buyurtmalariz:")
#     jami_narh = 0
#     for taom, narh in buyurtmalar:
#         print(f"{taom.capitalize()} - {narh} so'm")
#         jami_narh += narh
#     print(f"Jami narh: {jami_narh} so'm")
# else:
#     print("Siz hech qanday taom buyurtmaganingiz uchun rahmat!")

