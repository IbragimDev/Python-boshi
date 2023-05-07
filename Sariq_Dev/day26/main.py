"""Day 26 =>   JSON"""

import json

# m = True
# print(m)
# m_json = json.dumps(m)
# print(m_json)

# numbers = (23, 23, 56, 48)
# nums = json.dumps(numbers)
# print((nums))

# bemor = {
#     "name": "Ali",
#     "last_name": "Valiyev",
#     "age": 23,
#     "family": "yes",
#     "children": ("Ahmad", "Umida"),
#     "allergy": None,
#     "dorilar": [
#         {"d_name": "anolgin", "miqdor": 0.5},
#         {"d_nomi": "navakain", "miqdor": 2.5},
#     ],
# }
# """json.dump => json fayl hosil qiladi"""
# bemor_json = json.dumps(bemor, indent=4)

# with open("bemor_json", "w") as f:
#     json.dump(bemor, f)

# """json.loads  => json xolatdan oldindi (asl) xolatiga qaytaradi """
# bemor2 = json.loads(bemor_json)
# print(bemor2)

# filename = "bemor.json"
# with open(filename) as f:
#     bemor = json.load(f)


"""exam     =>  """
data = {"Model": "Malibu", "Rang": "Qora", "Yil": 2020, "Narh": 40000}

json_data = json.dumps(data)
print(json_data)

# 2
# talaba_json = '{"ism":"Hasan","familiya":"Husanov","tyil":2000}'
# talaba = json.loads(talaba_json)
# print(talaba["ism"], talaba["familiya"])

# 3
