# day15 -> qiymat qaytaruvchu function

# def avto_info(kompaniya, model, rang, yil, karobka, narx=None):
#     avto = { 'kompaniya':kompaniya,
#              'model':model,
#              'rang':rang,
#              'yil':yil,
#              'karobka':karobka,
#              'narx':narx}
#     return avto
# avto1 = avto_info('GM', 'Malibu', 'qora', 2022, 'mexanika') 
# avto2 = avto_info('Mers', 'Gelik', 'qora', 2023, 'avtomat', 150000)
# avtos = [avto1, avto2]
# print('Salomda bor bo`lgan avtamabillar: ')
# for avto in avtos:
#     if avto['narx'] is not None:
#         narx = avto['narx'] 
#     else:
#         narx = 'nomalum'
#     print(f"{avto['rang']} {avto['model']}. Narx: {narx}")


# def oraliq(min, max, qadam):
#     """funksiyamiz 2 son oralig'idagi sonlarni ro'yxat ko'rinishida qaytarsin."""
#     sonlar = [] # bo'sh ro'yxat
#     while min < max:
#         sonlar.append(min)
#         min += 1
#         min += qadam
#     return sonlar
# print(oraliq(0, 11, 1))
# print(oraliq(11, 20, 1))
# print(oraliq(0, 21, 2))

# def avto_info(kompaniya, model, rang, yil, karobka, narx=None):
#     print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting ",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
    # Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    # avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    # javob = input("Yana avto qo'shasizmi? (yes/no): ")
    # if javob!='yes':
    #     break
    
# amaliy ->

