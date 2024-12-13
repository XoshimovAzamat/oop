from datetime import datetime
from dbm import error


class Students:
    yigindi = 0
    talaba_soni = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Students.yigindi += self.age
        Students.talaba_soni += 1

    def info_age(self):
        return f"{self.name} {datetime.now().year - self.age} yilda tug`ilgan."# self. bilan yozilgani instans metod

    def info_nimadir(self):
        return f"{self.name} talaba."

    @classmethod
    def yigindi_ga(cls):
        return f"Umumiy yoshlar yig`indisi: {cls.yigindi}" # cls class ichidagi o`zgaruvchilar bilan ishlaydi
    @classmethod
    def talabalar_soni(cls):
        return f"Umumiy talabalar soni: {cls.talaba_soni}"

    @staticmethod
    def summ(a: list):
        return f"Massiv elementlari yig`indisi: {sum(a)}" #static metodi clasga bog`liq emas, tashqaridan argument olib ishlashdi
    @staticmethod
    def biron_nima(a: list):
        return f'Eng kattasi: {max(a)}'


student_1 = Students("Xoshimov Azamat", 25)
student_2 = Students("Xoshimov Azamatbek", 26)
student_3 = Students("Xoshimov Azamatbekjon", 27)
print(Students.yigindi_ga())
a1 = [1, 2, 3, 4, 6, 5, 8, 9]
print(Students.summ(a1))
print(Students.biron_nima(a1))
