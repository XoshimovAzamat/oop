from random import randint, random


class Auto_salon:
    def __init__(self, nomi, tel, lokatsiya, email):
        self.nomi = nomi
        self.tel = tel
        self.lokatsiya = lokatsiya
        self.email = email
        self.baza = []

    def __str__(self):
        return self.baza


    @property
    def info_name(self):
        return f"Avto salon nomi: {self.nomi}"
    @info_name.setter
    def info_name(self, new_name):
        new_name = input("Yangi nomini kiriting: ")
        self.nomi = new_name
    @property
    def info_phone(self):
        return f"Avto salon raqami: {self.tel}"
    @info_phone.setter
    def info_phone(self, new_tel):
        new_tel = int(input("Yangi telefon raqamni kiriting: "))
        self.tel = new_tel
    @property
    def info_location(self):
        return f"Manzili: {self.lokatsiya}"
    @info_location.setter
    def info_location(self, new_loc):
        new_loc = input("Yangi manzilni kiriting: ")
        self.lokatsiya = new_loc
    @property
    def info_email(self):
        return f"Pochta manzili: {self.email}"
    @info_email.setter
    def info_email(self, new_email):
        new_email = input("Yangi pochta kiriting: ")
        self.email = new_email



salon_1 = Auto_salon("Azam Motors", 900199921, "Toshkent shahar Sergili tumani", "azammotors@gmail.com")


class Cars:
    def __init__(self, model, name, year, color, price):
        self.model = model
        self.name = name
        self.year = year
        self.color = color
        self.price = price

    @property
    def car_model(self):
        return f"Moshina modeli: {self.model}"
    @car_model.setter
    def car_model(self, new_model):
        new_model = input("Yangi modelni kiriting: ")
        self.model = new_model
    @property
    def car_name(self):
        return f"Moshina nomi: {self.name}"
    @car_name.setter
    def car_name(self, new_name):
        new_name = input("Yangi nom kiriting: ")
        self.name = new_name
    @property
    def car_year(self):
        return f"Moshina yili: {self.year}"
    @car_year.setter
    def car_year(self, new_year):
        new_year = int(input("Yilni kiriting: "))
        self.year = new_year
    @property
    def car_color(self):
        return f"Moshina rangi: {self.color}"
    @car_color.setter
    def car_color(self, new_color):
        new_color = input("Rangini kiriting: ")
        self.color = new_color
    @property
    def car_price(self):
        return f"Moshina narxi: {self.price}"
    @car_price.setter
    def car_price(self, new_price):
        new_price = int(input("Narxini kiriting: "))
        self.price = new_price

car_1 = Cars("Gm","Nexia", 2015, "Oq", 7000)

car_2 = Cars("Gm","Nexia1", 2020, "Oq", 7000)

car_3 = Cars("Gm","Spark", 2020, "Oq", 8000)

car_5 = Cars("Gm","Cobalt", 2024, "Choco", 14000)

car_7 = Cars("Gm","Jentra", 2024, "Qora", 14000)

car_9 = Cars("Gm","BMW", 2024, "Oq", 50000)


cars = [car_1, car_2, car_3, car_5, car_7,  car_9,]
for item in cars:
    while True:
        salon_1.baza.append(item)
        break
while True:
    status = input("Assalomu alaykum. Moshinalarni ko`rish uchun: 1 "
                   "\nMoshina nomini o`zgartirish uchun: 2 "
                   "\nMoshina modelini o`zgartirish uchun: 3"
                   )
    if status == '1':
        for i in range(len(salon_1.baza)):
            print(salon_1.baza[i].model, salon_1.baza[i].year, salon_1.baza[i].color, salon_1.baza[i].price)

    if status == '2':
        for i in range(len(salon_1.baza)):
            print(salon_1.baza[i].model, salon_1.baza[i].year, salon_1.baza[i].color, salon_1.baza[i].price)
        edit_name = input("Qaysi moshina nomini o`zgartirasiz: ")
        count = 0
        for i in range(len(salon_1.baza)):
            if salon_1.baza[i].model == edit_name:
                salon_1.baza[i].car_model= None
    if status == '3':
        for i in range(len(salon_1.baza)):
            print(salon_1.baza[i].model, salon_1.baza[i].year, salon_1.baza[i].color, salon_1.baza[i].price)
        edit_name = input("Qaysi moshina nomini o`zgartirasiz: ")
        count = 0
        for i in range(len(salon_1.baza)):
            if salon_1.baza[i].name == edit_name:
                salon_1.baza[i].car_name= None
    # status1 = input(
    #     f"Qaysi avtosalon bazasini ko`rmoqchisiz? {salon_1.nomi} bazasini ko`rish: 1")
    # rangi = input("Bazadan qanday rangdagi moshinalarni ko`rmoqchisiz? ")
    #
    # # print(salon_1.baza[0].model)
    # if status1 == "1":
    #     count = 0
    #     for i in range(len(salon_1.baza)):
    #         if salon_1.baza[i].color == rangi:
    #             print(salon_1.baza[i].model, salon_1.baza[i].year, salon_1.baza[i].color, salon_1.baza[i].price)
    #             count += 1
    #     # for i in range(len(salon_1.baza)):
    #     #     print(salon_1.baza[i].model, salon_1.baza[i].year, salon_1.baza[i].color, salon_1.baza[i].price)
    #
    # if status1 == "2":
    #     count2 = 0
    #     for i in range(len(salon_2.baza)):
    #         if salon_2.baza[i].color == rangi:
    #             print(salon_2.baza[i].model, salon_2.baza[i].year, salon_2.baza[i].color, salon_2.baza[i].price)
    #             count2 += 1
    #     if count2 == 0:
    #         print("Afsuski, bu rangdagi moshina topilmadi.")
    #
    # #     for i in range(len(salon_2.baza)):
    # #         print(salon_2.baza[i].model, salon_2.baza[i].year, salon_2.baza[i].color, salon_2.baza[i].price)
