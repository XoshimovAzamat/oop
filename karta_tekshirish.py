from random import randint

class Cards:
    def __init__(self, egasi, raqami, muddati, parol, balans, ):
        self.egasi = egasi
        self.raqami = raqami
        self.muddati = muddati
        self.parol = parol
        self.balans = balans
        self.phone = None

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


def bankamad():
    status = False
    bool1 = False
    card = None
    while True:
        raqam = int(input("Karta raqam kiriting: "))
        for i in cards:
            if raqam == int(i.raqami):
                count = 0
                while count < 3:
                    count += 1
                    password = int(input("parol kiriting: "))
                    if password == i.parol:
                        status = True
                        card = i
                        break
                    else:
                        print("parol xato")
                else:
                    bool1=True
                    print("Karta bloklandi.")
                    break
            if status == False and bool1 == False:
                print("Bunday karta topilmadi.")
            if status or bool1:
                break
        if status:
            while True:
                statuss = input("Balansni ko`rish: 1 \nParolni almashtirish: 2 \nPul qo`shish: 3 \nSMS xabarnoma yoqish: 5 \nChiqish: 0")
                if statuss == "1":
                    print(card.balans)
                if statuss == "2":
                    new_pass = int(input("Yangi parol kiriting: "))
                    card.parol = new_pass
                if statuss == "3":
                    new_balans = int(input("Pul kiriting: "))
                    card.balans += new_balans
                if statuss == "5":
                    sms_count = 0
                    while sms_count<3:
                        sms_count += 1
                        phone = int(input("Telefon raqamini kiriting: "))
                        kod = randint(1000, 9999)
                        print(kod)
                        tek_kod = int(input(f"{phone} raqamiga yuborilgan kodni kiriting: "))
                        if kod == tek_kod:
                            card.phone = phone
                            print(f"SMS xabarnoma {phone}ga ulandi.")
                            break
                        else:
                            print("Kod noto`g`ri!")
                    else:
                        print("Urinishlar soni ko`payib ketdi. Iltimos keyinroq yana urinib ko`ring.")

                if statuss == "0":
                    print("Rahmat, kartangizni oling.")
                    break
        break
bankamad()