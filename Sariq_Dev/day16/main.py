# def avto_info(kompaniya, model, rangi, yili, karobka, narx=None):
#     avto = {
#         "kompaniya": kompaniya,
#         "model": model,
#         "rangi": rangi,
#         "yili": yili,
#         "karobka": karobka,
#         "narx": narx,
#     }
#     return avto


# avto1 = avto_info("mers", "gelik", "qora", 2023, "avtomar")
# avto2 = avto_info("mers", "mybax", "qora", 2023, "avtomar", 220000)
# avtos = [avto1, avto2]
# print(f"bor mashinalar \n {avto1}, \n {avto2}")


# def oraliq(min, max):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#         return sonlar


# print(range(0, 10))
# print(range(10, 21))


# def summa(*numbers):
#     res = 0
#     for num in numbers:
#         res += num
#     return res


# print(summa(2, 3, 5, 6, 8))
# print(summa(2, 93, 55, 60, 80))
# print(summa(2, 3, -56985, 6, 855))
# print(summa())


# def summa(*numbers):
#     return sum(numbers)
# print(summa(2, 93, 55, 60, 80))


# def summa(x, y, *numbers):
#     return x + y + sum(numbers)
# print(summa(2, 93, 55, 60, 80))

# args usslida moslashuvchan funksiya => ^^


# def avto_info(company, model, **infos):
#     infos["company"] = company
#     infos["model"] = model
#     return infos


# avto1 = avto_info("GM", "kamaro", yil=2000, rang="dark")
# avto2 = avto_info("GM", "malibu", yil=2023, rang="white", prise=20000)

# kwargs usulidagi function => ^

# exam =>


# def summa(x, y, *numbers):
#     return x * y * sum(numbers)


# print(summa(2, 93, 55, 60, 80))


def multiply(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma


print(multiply(4, 5, 6))
