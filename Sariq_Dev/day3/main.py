# cars = ["BMW", "mers", "toyota"]
# print(cars)
# cars[0] = "Onix"
# print(cars)

# append() => array ichiga (oxiriga) qo`shadi
# cars = ["BMW", "mers", "toyota"]
# cars.append("KIA")
# print(cars)

# insert() => list(array) hohlagan yeriga qo`shish imkonini beradi
# cars = ["BMW", "mers", "toyota"]
# cars.insert(2, "MAN")
# print(cars)

# vagitables = []
# vagitables.append("tomato")
# vagitables.append("potato")
# vagitables.append("Banana")
# vagitables.append("kiwi")
# print(vagitables)
# del vagitables[0]
# print(vagitables)
# vagitables.insert(0, "tomatoes")
# print(vagitables)
# # vagitables.remove("kiwi")
# print(vagitables)
# # print(len(vagitables))

# age = ["kiwi", "tom", "Jerry", "Nike", "Nik", "tom"]
# age.remove("tom")
# print(age)

# bozor = ["yog", "un", "go`sht", "banana", "kiwi"]
# ten = bozor.pop(3)
# print("bozordan", bozor, "topa olmadim")
# print("men bozordan", ten, "sotib oldim")

#1  exam
# name = ["Ali", "Vali", "G`ani"]
# print("Salom", name[0], "bugun fudbo`lga boramizmi")
# print(name[1], "bugun mashina sotib olamizmi")
# print(name[2], "bugun kadega boramizmi")

#2
# numbers = [12, 23, 15 ,26, -4, 465, 456, 456, 416, 465, 45]
# numbers[0] = 2000
# numbers.remove(456)
# numbers.append(5)
# numbers.insert(5, 66)
# print(len(numbers))
# print(numbers)

#3
# t_shaxslar = ["navoi", "Buxoriy", "Xorazmiy", "Beruniy"]
# z_shaxslar = ["Ali", "Umid", "Temur", "Hasan aka"]
# # human = t_shaxslar.pop(2)

# print("Men tarixiy shaxslardan",t_shaxslar[2], "bilan ko`rishishni hohlardim", 
#       "zamonaviy shaxslardan esa", z_shaxslar[3], "bilan suhbatlashishni hohlardim" )
 
#3
# friends = []
# friends.append("Anvar")
# friends.append("Dima")
# friends.append("Do`sya")
# friends.append("Akmal")
# friends.append("Suhrob")
# friends.remove("Akmal")


# friends.append("Ruzi")
# friends.insert(3, "Azad")
# print(friends)

#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
# mehmonlar = []
# mehmonlar.append(friends.pop(3))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(0))
# print("\nKelgan mehmonlar: ", mehmonlar)