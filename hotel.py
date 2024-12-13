class Hotel:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
        self.rooms = []
        self.client = []

    def info(self):
        return f"{self.title} mehmonxonasiga xush kelibsiz."

    def rooms_info(self):
        return self.rooms

    def client_data(self):
        for item in self.client:
            f"Ism: {item}"

class Rooms:
    def __init__(self, number, eco, bus, luk):
        self.number = number
        self.eco = eco
        self.bus = bus
        self.luk = luk
        self.is_activate = False
        self.clients = []

    def data_room(self):
        return f"Room {self.number} - {self.room_type} in room clients: {self.clients}"

    def info_clients(self):
        for item in self.client:
            print(f"Ism: {item.name} phone: {item.phone} id: {item.id}")

    def add_client(self, obj: object):
        self.clients.append(obj)

    def del_client(self, client_id: str):
        self.clients = [client for client in self.clients if client.id != client_id]

class Client:
    def __init__(self, name, phone, id):
        self.name = name
        self.phone = phone
        self.id = id

hotel_1 = Hotel("Hyatt Regency", 5)

xona_1 = Rooms(1, True, False, False)
xona_2 = Rooms(2, True, False, False)
xona_3 = Rooms(3, True, False, False)
xona_4 = Rooms(4, True, False, False)
xona_5 = Rooms(5, True, False, False)
xona_6 = Rooms(6, False, True, False)
xona_7 = Rooms(7, False, True, False)
xona_8 = Rooms(8, False, True, False)
xona_9 = Rooms(9, False, True, False)
xona_10 = Rooms(10, False, True, False)
xona_11 = Rooms(11, False, False, True)
xona_12 = Rooms(12, False, False, True)
xona_13 = Rooms(13, False, False, True)
xona_14 = Rooms(14, False, False, True)
xona_15 = Rooms(15, False, False, True)

hotel_1.rooms.append(xona_1)
hotel_1.rooms.append(xona_2)
hotel_1.rooms.append(xona_3)
hotel_1.rooms.append(xona_4)
hotel_1.rooms.append(xona_5)
hotel_1.rooms.append(xona_6)
hotel_1.rooms.append(xona_7)
hotel_1.rooms.append(xona_8)
hotel_1.rooms.append(xona_9)
hotel_1.rooms.append(xona_10)
hotel_1.rooms.append(xona_11)
hotel_1.rooms.append(xona_12)
hotel_1.rooms.append(xona_13)
hotel_1.rooms.append(xona_14)
hotel_1.rooms.append(xona_15)

def hotel_work():
    while True:
        status = input("Bo`sh xonalarni ko`rish: 1 \nAktiv xonalarni ko`rish: 2 \nChiqish: 0 \n ")
        if status == "1":
            while True:
                room_status = input("Ekonom xonalarni ko`rish: 1 \nBiznes xonalarni ko`rish: 2 \nVIP xonalarni ko`rish: 3 \nXonaga mijoz qo`shish: 4 \nOrtga: 0 \n")
                if room_status == "1":
                    for item in hotel_1.rooms:
                        if not item.is_activate and item.eco:
                            print(f"Ekonom xonamiz: {item.number}")

                if room_status == "2":
                    for item in hotel_1.rooms:
                        if not item.is_activate and item.bus:
                            print(f"Biznes xonamiz: {item.number}")

                if room_status == "3":
                    for item in hotel_1.rooms:
                        if not item.is_activate and item.luk:
                            print(f"VIP xonamiz: {item.number}")

                if room_status == "4":
                    print("Mijozning ma`lumotlarini kiriting: ")
                    ism = input("Ismi: ")
                    phone = input("Telefon raqami: ")
                    id = input("ID ma`lumotlari: ")
                    client = Client(ism, phone, id)
                    room_number = input("Xona raqamini kiriting: ")
                    for room in hotel_1.rooms:
                        if room.number == int(room_number):
                            room.is_activate = True
                            room.add_client(client)
                            print(f"Mijoz {room.number} raqamli xonaga qo`shildi.")
                            print(room.clients)
                elif room_status == "0":
                    break
        if status == "2":
            while True:
                room_status = input("Ekonom xonalarni ko`rish: 1 \nBiznes xonalarni ko`rish: 2 \nVIP xonalarni ko`rish: 3 \nXonaga mijoz qo`shish: 4 \nMijozni o`chirish: 5 \nOrtga: 0 \n")
                if room_status == "1":
                    for item in hotel_1.rooms:
                        if item.is_activate and item.eco:
                            print(f"Ekonom xonamiz: {item.number}")
                if room_status == "2":
                    for item in hotel_1.rooms:
                        if item.is_activate and item.bus:
                            print(f"Biznes xonamiz: {item.number}")
                if room_status == "3":
                    for item in hotel_1.rooms:
                        if item.is_activate and item.eco:
                            print(f"VIP xonamiz: {item.number}")
                if room_status == "4":
                    print("Mijozning ma`lumotlarini kiriting: ")
                    ism = input("Ismi: ")
                    phone = input("Telefon raqami: ")
                    id = input("ID ma`lumotlari: ")
                    client = Client(ism, phone, id)
                    room_number = input("Xona raqamini kiriting: ")
                    for room in hotel_1.rooms:
                        if room.number == int(room_number) and len(room.clients)<3:
                            room.is_activate = True
                            room.add_client(client)
                            print(f"Mijoz {room.number} raqamli xonaga qo`shildi.")
                            print(room.clients)
                        if len(room.clients)>=3:
                            print("Bu xona to`lgan. Boshqa xona tanlang.")
                if room_status == "0":
                    break
        if status == "5":
            client_id = input("Mijoz ID raqamini kiriting: ")
            Rooms.del_client(client_id)
            print("Mijoz o`chirildi.")
        if status == "0":
            break


hotel_work()