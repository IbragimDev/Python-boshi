# """Day 22    Volislik vs Polimartizm => """


# class Human:
#     def __init__(self, name, sur_name, id_card, born):
#         self.name = name
#         self.sur_name = sur_name
#         self.id_card = id_card
#         self.born = born

#     def get_info(self):
#         info = f"{self.name} {self.sur_name} "
#         info += f"Id_Card: {self.id_card} born {self.born} year"
#         return info

#     def get_age(self, year):
#         return year - self.born


# class Student(Human):
#     def __init__(self, name, sur_name, Born, id_card, id, location):
#         super().__init__(name, sur_name, Born, id_card, id)
#         self.id = id
#         self.bosqich = 1
#         self.location = location

#     def get_id(self):
#         return self.id

#     def get_bosqich(self):
#         return self.bosqich

#     def get_info(self):
#         info = f"{self.name} {self.sur_name}. "
#         info += f"{self.get_bosqich()} - bosqich. ID_Nomer => {self.id}"
#         return info


# class Location:
#     def __init__(self, viloyat, tuman, kocha, uy_raqam):
#         self.viloyat = viloyat
#         self.tuman = tuman
#         self.kocha = kocha
#         self.uy_raqam = uy_raqam

#     def get_manzil(self):
#         manzil = f"{self.viloyat} vilyati, {self.tuman} tumani "
#         manzil += f"{self.kocha} ko`chasi, {self.uy_raqam} uyda yashaydi"
#         return manzil


# talaba_manzil = Location("Xorazm", "Urganch", "Birdamlik", 22)
# talaba1 = Student("Vali", "Aliyev", 2000, "AB1989562", "DF562158", talaba_manzil)
