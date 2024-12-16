# def f1():
#     a = 0
#
#     def f2():
#         nonlocal a
#         a += 1
#         return a
#
#     return f2
# count1 = f1()
# print(count1())
# print(count1())
# print(count1())
# print(count1())
# import json
# from collections import namedtuple
# a = {
#     ism : "Azamat",
#     fam : "Xoshimov",
#     phone : "+998900199921"
# }
# Person = namedtuple("Person", ["ism", "fam", "phone"])
# info = Person(ism=None, fam=None, phone=None)
# # print(info.ism)
# # print(info.fam)
# # print(info.phone)

# def my_name(func):
#     def get_name():
#         return f"Bu {func()}ning funksiyasi."
#     return get_name
#
# @my_name
# def inp_name():
#     name = "Azamat"
#     return name
# print(inp_name())

def list_sum(func):
    def get_sum(*args, **kwargs):
        print(f"{func.__name__} funksiyasi ishladi.")
        result = func(*args, **kwargs)
        print("Natija: ", result)
    return get_sum

@list_sum
def add(a: list):
    return sum(a)
a = [1, 2, 3, 4, 5]
add(a)
