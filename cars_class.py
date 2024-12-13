# class Car:
#     def __init__(self, model, year, price, hours_power):
#         self.model = model
#         self.year = year
#         self.price = price
#         self.hours_power = hours_power
#
#
# car_1 = Car("Nexia", 2015, 7000, 80)
# car_2 = Car("Spark", 2022, 8000, 100)
# car_3 = Car("Nexia 3", 2024, 10000, 120)
# # print(f"{car_1.model} moshinasi {car_1.year} yil, narxi {car_1.price}\
# #  \n{car_2.model} moshinasi {car_2.year} yil, narxi {car_2.price}")
# cars = [car_1, car_2, car_3]
# for i in cars:
#     if i.year > 2015:
#         print(i.model)

class Cards:
    def __init__(self, egasi, raqami, muddati, parol, balans, ):
        self.egasi = egasi
        self.raqami = raqami
        self.muddati = muddati
        self.parol = parol
        self.balans = balans

    def info(self):
        return f"{self.raqami} raqamli karta egasi {self.egasi}."

card_1 = Cards("Xoshimov Azamat", 8600130963634648, "5555", 4567, 1000000000)
card_2 = Cards("Xoshimov Azamatbek", 8600132623455623, "5555", 1235, 1000000000)
card_3 = Cards("Xoshimov Azamatjon", 8600130963635556, "5555", 7123, 1000000000)
card_4 = Cards("Xoshimov Azamatxon", 8600130963638456, "5555", 7723, 100000)
card_5 = Cards("Xoshimov Azamatali", 8600130963634898, "5555", 7700, 0)
card_6 = Cards("Xoshimov AzamatNur", 8600138963634648, "5555", 7567, 10000)
card_7 = Cards("Xoshimov AzamatDur", 8600178963634648, "5555", 7987, 10)
card_8 = Cards("Xoshimov AzamatXonjon", 860018973634648, "5555", 6777, 90000000)
card_9 = Cards("Xoshimov Azamatali", 86001309633214648, "5555", 7727, 3000000000)
card_10 = Cards("Xoshimov Azamatalixon", 8600130987634648, "5565", 8977, 9000000000)

cards = [card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_8, card_10]