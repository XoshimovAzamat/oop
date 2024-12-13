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

def balans():
    while True:
        number = int(input("To`ldirmoqchi bo`lgan karta raqamini kiriting: "))
        bool = True
        for item in cards:
            if item.raqami==number:
                new_balans = int(input("Summani kiriting: "))
                item.balans += new_balans
                #tekshirish uchun print qilindi
                print(f"Karta egasi: {item.egasi}, \nkarta raqami: {item.raqami}, \nMuddati: {item.muddati}, \nbalans: {item.balans}")
                bool = False

        if bool == True:
            print("Karta raqami topilmadi.")

        break

balans()
