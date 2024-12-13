class Card:
    def __init__(self, card_number, user_name, phone, balance,  password):
        self.card_number = card_number
        self.user_name = user_name
        self.phone = phone
        self.balance = balance
        self.password = password


class User:
    def __init__(self, user_name, phone, user_id, cards):
        self.user_name = user_name
        self.phone = phone
        self.user_id = user_id
        self.cards = []


class Hotel:
    def __init__(self, name, balance, price):
        self.name = name
        self.balance = 0
        self.price = price
        self.clients = []


hotel_1 = Hotel("Hyatt", None, 100)
hotel_2 = Hotel("Hilton", None, 150)

card1 = Card(98600101, "Azam Azamov", 998887799,100000000,  5711)
card2 = Card(98600102, "Azam Azamov", 998887799,100000000,  5711)
card3 = Card(98600103, "Azam Azamov", 998887799,100000000,  5711)
card4 = Card(98600104, "Ali", 998887788, 10000000, 4455)
card5 = Card(98600105, "Ali", 998887788, 10000000, 4455)
card6 = Card(98600106, "Ali", 998887788, 10000000, 4455)
card7 = Card(98600107, "Vali", 998887700, 10000000, 1112)
card8 = Card(98600108, "Vali", 998887700, 10000000, 1112)
card9 = Card(98600109, "Vali", 998887700, 10000000, 1112)
card10 = Card(98600110, "Vali", 998887700, 10000000, 1112)

user1 = User("Azam Azamov", 998887799, "AA9566565", None)
user2 = User("Ali", 998887788, "AD1234567", None)
user3 = User("Vali", 998887700, "AB7654321", None)
users = [user1, user2, user3]


user1.cards.append(card1)
user1.cards.append(card2)
user1.cards.append(card3)

user2.cards.append(card4)
user2.cards.append(card5)
user2.cards.append(card6)

user3.cards.append(card7)
user3.cards.append(card8)
user3.cards.append(card9)
user3.cards.append(card10)


def work_hotel():
    while True:
        status = input("Assalomu alaykum. Mehmonxonani tanlang: \nHyatt: 1 \nHilton: 2  ")
        while True:
            if status == "1":
                work_1 = input("Mijozlarni ro`yhatini ko`rish: 1 \nMijoz qo`shish: 2 \nMehmonxona balansini ko`rish: 3 \nChiqish: 0 ")
                if work_1 == "1":
                    for item in hotel_1.clients:
                        print(f"Mijoz: {item.user_name}, ID: {item.user_id}")
                    id_client = input("To`liq ma`lumot uchun ID raqam kiriting: ")
                    for item in hotel_1.clients:
                        if id_client == item.user_id:
                            print(f"Mijoz: {item.user_name}, tel: {item.phone}, ID: {item.user_id} ")
                            pay_card = int(input("Karta raqam kiriting: "))
                            for card in item.cards:
                                if pay_card == card.card_number:
                                    pass_card = int(input("Parol kiriting: "))
                                    if pass_card == card.password:
                                        print(f"Mablag`ingiz: {card.balance}")

                            break
                        else:
                            print("Bunday ID raqamli mijoz topilmadi.")
                if work_1 == "2":
                    pl_client = input("Mijoz qo`shish uchun ID raqam kiriting: ")
                    for item in users:
                        if item.user_id == pl_client:
                            day_cn = int(input("Necha kun turasiz: "))
                            print("Iltimos to`lovni amalga oshiring:")
                            pay_card = int(input("Karta raqam kiriting: "))
                            for card in item.cards:
                                if pay_card == card.card_number:
                                    pass_card = int(input("Parol kiriting: "))
                                    if pass_card == card.password:
                                        if card.balance> day_cn * hotel_1.price:
                                            card.balance -= day_cn * hotel_1.price
                                            hotel_1.balance += day_cn * hotel_1.price
                                            hotel_1.clients.append(item)
                                            print(f"{item.user_name} qo`shildi.")
                                            print(f"Hisobingizda: {card.balance} qoldi.")
                                            break

                                        else:
                                            print("Mablag` yetarli emas.")
                                            break
                                else:
                                    print("Karta topilmadi.")
                                    break
                        else:
                            print("ID raqam topilmadi.")
                            break
                if work_1 == "3":
                    print(hotel_1.balance)
                if work_1 == "0":
                    break
work_hotel()