# day -> 11 -> Nesting
# car0 = {
#     "model":"cobalt",
#     "year":2021,
#     "narx": 12000,
#     "probeg":12000,
#     "rang":"black"
# }

# car1 = {
#     "model":"malibu",
#     "year":2020,
#     "narx": 15000,
#     "probeg":6000,
#     "rang":"oq"
# }

# car2 = {
#     "model":"kia",
#     "year":2021,
#     "narx": 20000,
#     "probeg":120,
#     "rang":"black"
# }

# cars = [car0, car1, car2]

# for car in cars:
#     print(f"{car['model'].title()}, {car['year']} year, "
#           f"{car['rang']} rang, {car['narx']}, $ ")
#     print(cars['narx'])
    
# asaka = []
# for n in range(10):
#     new_car = {
#         'rang':'black',
#         'year': 2023,
#         'km': 0,
#         'narx':25000,
#         'model':'kia',
#         'karobka':'avto'
#     }
#     asaka.append(new_car)
    
# for kia in asaka[:3]:
#     kia['rang'] = "oq"

# for kia in asaka[3:6]:
#     kia['rang'] = "qizil"

# for kia in asaka[6:]:
#     kia['rang'] = "yashil"
#     kia["karobka"] = "mexanika"

# for kia in asaka:
#     if kia["karobka"] == "avto":
#         kia["narx"] = 40000
#     else:
#         kia["narx"] = 36000
            
# print(asaka)

# devs = {
#     "ali":["c++", "python"],
#     "vali":["java", "js"],
#     "husan":["php", "ruby"],
#     "madina":["java", "react"],
#     "guli":["C#", "html", "css"]
# }
# for ism, tillar in devs.items():
#     print(f"\n{ism.title()} tillarni biladi:") 
#     for til in tillar:
#         print(til.upper())
        # print(f"{til.upper()} ", end="")
        
# friends = {
#     "ali":{
#         "last_name":"valiyev",
#         "born":2000,
#         "degree":"o`rta - maxsus",
#         "skills":["html", "css", "js"]
#         },
#     "vali":{
#         "last_name":"aliyev",
#         "born":2001,
#         "degree":"o`rta - maxsus",
#         "skills":["html", "css", "js", "ruby", "sql"]
#         },
#     "maryam":{
#         "last_name":"husanova",
#         "born":1998,
#         "degree":"oliy",
#         "skills":["html", "css", "js", "python", "nodejs"]
#     }
# }
# for ism, info in friends.items():
#     print(f"\n {ism.title()} {info['last_name'].title()}, "
#         f"{info['born']} - yilda tug`ilgan. "
#         f"Ma`lumoti: {info['degree']}. \n"
#         "Quyidagi dasturlash tillarini biladi: ")
#     for til in info:
#         print(til.upper())

# Amaliy ->
# people = {
#     'isaak': {
#        "lastName":"Nyuton",
#         "born": 1642,
#         "city":"london",
#         "skill":"fizika"
#     },
#     'ali':{
#         "lastName":"muhammad",
#         "born":"1928",
#         "city":"usa",
#         "skill":"boks"
#     },
#     'erkin':{
#         "lastName":"vohidov",
#         "born":"1956",
#         "city":"farg`ona",
#         "skill":"adabiyot"
#     }
# }
# for ism, info in people.items():
#     print(f"\n {ism.title()} {info['lastName'].title()}, "
#         f"{info['born']} - yilda {info['city']} shaxrida tug`ilgan. "
#         f"{info['skill'].title()} sohasi bo`yicha mutaxasis bo`lgan. \n")

# 2