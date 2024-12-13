class Cards:
    def __init__(self, number, balans):
        self.number = number
        self._balans = balans

class Card(Cards):
    def __init__(self, number, balans, date, passw):
        super().__init__(number, balans)
        self.date = date
        self.__passw =  passw

card_1 = Card(9860, 1320000, 1222, 5711)
