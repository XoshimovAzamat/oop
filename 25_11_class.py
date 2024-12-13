# Single (ta ota 1 ta bola)
class One:
    def __init__(self, name):
        self.name = name

class Two(One):
    def __init__(self, name, mame):
        super().__init__(name)
        self.mame = mame


#Multiple (2 ta ota 1 ta bola)
class One_1:
    def __init__(self, bame):
        self.bame = bame

class Two_1(One, One_1):
    def __init__(self, name, bamee, dame):
        super().__init__(name, bamee)
        self.dame = dame

#Multilevel (bobo, ota, bola)
class Two_2(One, Two):
    def __init__(self, name, mame, fame):
        super().__init__(name, mame)
        self.fame = fame

#Hierarchical (1 ta ota, 2 ta bola)
class Two_3(One):
    def __init__(self, name, fame):
        super().__init__(name)
        self.fame = fame

class Three(One):
    def __init__(self, name, kame):
        super().__init__(name)
        self.kame = kame

#Hybrid (aralash)
exem = Two_2("ali", "vali", "hali")
print(exem.name)
print(exem.mame)
print(exem.fame)

# class Example:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#     def info(self):
#         return f"Ismim: {self.name}"
#
# class Xwyz(Example):
#     def __init__(self, name, phone, age):
#         super().__init__(name, phone)
#         self.age = age
#






