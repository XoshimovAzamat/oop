class Texnikalar:
    def __init__(self, brand, model, typee):
        self.brand = brand
        self.model = model
        self.typee = typee
    def info(self):
        return f"Brandi: {self.brand}, Modeli: {self.model}, Turi: {self.typee}"

class PK(Texnikalar):
    def __init__(self, brand, model, typee, video_card, ram, displey):
        super().__init__(brand, model, typee)
        self.video_card = video_card
        self.ram = ram
        self.displey = displey

    def info(self):
        return f"Brandi: {self.brand}, Modeli: {self.model}, Turi: {self.typee}, Video karta: {self.video_card}, Ram: {self.ram}, Displey: {self.displey}"

class TV(Texnikalar):
    def __init__(self, brand, model, typee, size, displey):
        super().__init__(brand, model, typee)
        self.size = size
        self.displey = displey

    def info(self):
        return f"Brandi: {self.brand}, Modeli: {self.model}, Turi: {self.typee}, Ekran: {self.size}, Disepley: {self.displey}"

class Phone(Texnikalar):
    def __init__(self, brand, model, typee, size, sim_count):
        super().__init__(brand, model, typee)
        self.size = size
        self.sim_count = sim_count

    def info(self):
        return f"Brandi: {self.brand}, Modeli: {self.model}, Turi: {self.typee}, Ekran: {self.size}, Sim: {self.sim_count}"

class Texnika:
    def __init__(self, brand, model, tipe):
        self.brand = brand
        self.model = model
        self.tipe = tipe
    def info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Turi: {self.tipe}"

class Cars(Texnika):
    def __init__(self, brand, model, tipe, battery_life, chargin_time):
        super().__init__(brand, model, tipe)
        self.battery_life = battery_life
        self.chargin_time = chargin_time

    def info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Turi: {self.tipe}, Batareya quvvati: {self.battery_life}, Quvvatlash vaqti: {self.chargin_time}"

class Moto(Texnika):
    def __init__(self, brand, model, tipe, motor, color):
        super().__init__(brand, model, tipe)
        self.motor = motor
        self.color = color

    def info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Turi: {self.tipe}, Ot kuchi: {self.motor}, Rangi: {self.color}"

class Fura(Texnika):
    def __init__(self, brand, model, tipe, motor, height, long, wieght):
        super().__init__(brand, model, tipe)
        self.motor = motor
        self.height = height
        self.long = long
        self.wieght = wieght

    def info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Turi: {self.tipe}, Motor: {self.motor}, Balandligi: {self.height}, Uzunligi: {self.long}, Og`irligi: {self.wieght}"





