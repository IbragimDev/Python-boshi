# Day 13 -> while => ro`yhatlar, lists`

print("Keling yaqin do`stlaringizni ro`yhatini tuzamiz")
names = []
n = 1
while True:
    text = f"{n} da do`stingizni ismini kiriting: "
    name = input(text)
    names.append(name)
    result = input("Yana ism qo`shmoqchimisiz (yes/no)")
    n += 1
    if result != 'yes':
        break

# print("Do`stlaringiz ro`yhati:")
# for name in names:
#     print(name.title())

#                   while yordamida lug`at hosil qilish => 
# frinds = {}
# ishora = True
# while ishora:
#     name = input("Do`stlaringiz ismini kiriting: ")
#     age = input(f"{name.title()}ning yoshini kiriting: ")
#     frinds[name] = int(age)
 
#     answer = input("Yana ma`lumot qo`shasizmi (yes/no)")
#     if answer != "yes":
#         ishora = False
    
# for name, age in frinds.items():
#     print(f"{name.title()} {age} yoshda")

# while/for yordamida listdan ma`lumot o`chirish =>
# cars = ["bmw", 'nexia', "jentra", "nexia", "mers", 'toyota', "nexia", "nexia"] 
# while 'nexia' in cars:
#     cars.remove('nexia')
#     print(cars)

# cars = ["bmw", 'nexia', "jentra", "nexia", "mers", 'toyota', "nexia", "nexia"] 
# for car in cars:    car => nexia
#     cars.remove('nexia')
#     print(cars)

# students = ['anvar', 'dima', 'fezot', 'azik', 'bekjan']
# res_students = {}
# while students:
    # student = students.pop()
    # baho = input(f"{student.title()}ning bahosini kiriting: ")
    # print(f'{student.title()} baholandi')
    # res_students[student] = int(baho)


# talabalar = ['anvar', 'dima', 'fezot', 'azik', 'bekjan']
# res_students = {}
# while talabalar:
    # talaba = talabalar.pop()
    # baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    # print(f'{talaba.title()} baholandi')
    # res_students[talaba] = int(baho)

# Amaliy ->
# e_bozor = []
# n = 1
# while True:
#     text = f"{n} - mahsulot nomimi kiriting: "
#     bazar = input(text)
#     e_bozor.append(bazar)
#     result = input("Yana mahsulot qo`shmoqchimisiz (yes/no)")
#     n += 1
#     if result != 'yes':
#         break
    
# print(f"Siz zakas qildingiz {e_bozor}")

# 2
# e_bozor = {}
# ishora = True
# while ishora:
#     text = input("Mahsulot nomimi kiriting: ")
#     prise = input(f"{text.title()}ning narxini kiriting: ")
#     answer = input("Yana ma`lumot qo`shasizmi (yes/no)")
#     if answer != "yes":
#         ishora = False
        
# for text, prise in e_bozor.items():
#     print(f"{text.title()} {prise} so`m")
 
procudts = {}
while True:
    procudts_name = input("Mahsulotlar nomini kiriting(dastur to`xtashi uchun 'stop deb yozing)")
    if procudts_name == 'stop':
        break
