#
#
# class Cars:
#     sum_price = 0
#
#     def __init__(self, model, year, color, price):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.price = price
#         Cars.sum_price += self.price
#
#     def get_info(self):
#         return f"Moshina nomi: {self.model}, yili: {self.year}, rangi: {self.color}"
#
#     @classmethod  # class metodni ishlatganimizda classning nomini yozib chaqiramiz funksiyani
#     def get_sum_price(cls):
#         return f"Umumiy narxi: {cls.sum_price}"
#
#
# car1 = Cars("Spark", 2024, "Oq", 7000)
# car2 = Cars("Nexia", 2024, "Oq", 6000)
# car3 = Cars("Nexia3", 2024, "Oq", 9000)
# print(car1.get_info())
# print(Cars.get_sum_price())
from random import randint


class Students:
    def __init__(self, name, year, group):
        self.name = name
        self.year = year
        self.group = group

    @property # getter
    def info(self):
        return self.year
    @info.setter # setter
    def info(self,a):
        if 1920<a<2024:
            self.year = a
        else:
            print("Yilni to`gri kiriting.")


student1 = Students("Xoshimov Azamat", 1999, "n59")
student_2 = Students("Xoshimov Azamatbek", 1996, "n36")
student_3 = Students("Xoshimov Azamatbekjon", 1998, "n26")

student1.info = randint(1910, 2040)
print(student1.info)

