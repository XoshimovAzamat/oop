# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def info(self):
#         return f"Brand: {self.brand}, Modeli: {self.model}, Yili: {self.year}"
#
#
# class BMW(Car):
#     def __init__(self, brand, model, year, color, price):
#         super().__init__(brand,model,year)
#         self.color = color,
#         self.price = price
#
# class Chevrolet(Car):
#     def __init__(self, brand, model, year, color, price):
#         super().__init__(brand, model, year)
#         self.color = color
#         self.price = price
#
# bmw = BMW("BMW", "x6", 2024, "Qora", 100000)
# print(bmw.info())
class Univesity:
    def __init__(self, name, loc, email):
        self.name = name
        self.loc = loc
        self.email = email

    def univer_info(self):
        return f"Universitet nomi: {self.name}, Manzili: {self.loc}, Pochta: {self.email}"

class Staff(Univesity):
    def __init__(self, name, loc, email, first_name, last_name, age):
        super().__init__(name, loc, email)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def staff_info(self):
        return f"Ish joyi: {self.name}, Ismi: {self.first_name}, Familiya: {self.last_name}, Yoshi: {self.age}"

class Student(Staff):
    def __init__(self, name, first_name, last_name, age, group):
        super().__init__(name, first_name, last_name, age)
        self.group = group

    def student_info(self):
        return  f"O`qish joyi: {self.name}, Ism: {self.first_name}, Familiya: {self.last_name}, Yoshi: {self.age}, Guruh: {self.group}"


class Teacher(Staff):
    def __init__(self, name, first_name, last_name, age, position, fan):
        super().__init__(name, first_name, last_name, age)
        self.position = position
        self.fan = fan

    def teacher_ingo(self):
        return f"Ish joyi: {self.name}, Ism: {self.first_name}, Familiya: {self.last_name}, Yoshi: {self.age}, Darajasi: {self.position}, Fani: {self.fan}"

class Other_staff(Staff):
    def __init__(self, name, first_name, last_name, age, position):
        super().__init__(name, first_name, last_name, age)
        self.position = position
    def other_staff_info(self):
        return f"Ish joyi: {self.name}, Ism: {self.first_name}, Familiya: {self.last_name}, Yoshi: {self.age}, Darajasi: {self.position}"

class Subject(Univesity):
    def __init__(self, name, titel):
        super().__init__(name)
        self.titel = titel

    def subject_info(self):
        return f"Universitet nomi: {self.name}, fani: {self.titel}"


class Computer(Subject):
    def __init__(self, name, soni, tizimi, xolati):
        super().__init__(name)
        self.soni = soni
        self.tizimi = tizimi
        self.xolati = xolati

    def comp_info(self):
        return f"Qayerniki: {self.name}, Soni: {self.soni}, Tizim: {self.tizimi}, Xolati: {self.xolati}"


class Model(Computer):
    def __init__(self, soni, turi, xolati):
        super().__init__(soni, xolati)
        self.turi = turi

    def model_info(self):
        return f"Soni: {self.soni}, Xolati: {self.xolati}, Turi: {self.turi}"

univer1 = Univesity("Nizomiy", "Bunyodkor 17", "nizmoy@gmail.com")
xodim1 = Staff("TATU", "Azamat", "Xoshimov", 25)
student1 = Student("Nizomiy", "Azam", "xoshimov", 25, "N59")
teacher1 = Teacher("Najot Ta`lim", "Ali", "vali", 25, "Oliy", "Python")
other_staff1 = Other_staff("Nizomiy", "Azam", "Azamov", 25, "Oliy")
subject  = Subject("Najot ta`lim", "Python")
comp1 = Computer("Najot ta`lim", 30, "erp", "yangi")
model1 = Model(30, "HP", "Yangi")
univer1.univer_info()
xodim1.staff_info()
student1.student_info()
teacher1.teacher_ingo()
other_staff1.other_staff_info()
subject.subject_info()
comp1.comp_info()
model1.model_info()




