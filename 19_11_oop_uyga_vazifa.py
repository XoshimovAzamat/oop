import re
from random import randint


class Students:
    def __init__(self, name, year, tg_user, phone, email, pass_seria):
        self.name = name
        self.year = year
        self.tg_user = tg_user
        self.phone = phone
        self.email = email
        self.pass_seria = pass_seria

    @property
    def name_info(self):
        return f"Talaba ismi: {self.name}"

    @name_info.setter
    def name_info(self, new_name):
        chesk_name = r"^[a-zA-Zа-яА-ЯёЁўЎқҚҳҲғҒ]+ [a-zA-Zа-яА-ЯёЁўЎқҚҳҲғҒ]+$"
        new_name = input("Yangi ism va familiya kiriting: (namuna: Ali Valiyev)")
        if re.match(chesk_name, new_name):
            self.name = new_name
            print(f"Talabaning ismi {self.name} ga o`zgartirildi.")
        else:
            print("Ism va familiyani to`g`ri kiriting.")

    @property
    def year_info(self):
        return f"Talabaning tug`ilgan yili: {self.year}"

    @year_info.setter
    def year_info(self, new_year):
        new_year = int(input("Yilni kiriting: "))
        if 1920 < new_year < 2024:
            self.year = new_year
            print(f"Talabaning yili {self.year}ga o`zgartirildi.")
        else:
            print("Yilni to`g`ri kiriting.")

    @property
    def tg_user_info(self):
        return f"Telegram user: {self.tg_user}"

    @tg_user_info.setter
    def tg_user_info(self, new_tg_user):
        check_user = r"^@?[a-zA-Z0-9_]{5,32}$"
        new_tg_user = input("tg user kiriting: ")
        if re.match(check_user, new_tg_user):
            self.tg_user = new_tg_user
            print(f"Talabaning tg useri {self.tg_user} ga o`zgartirildi.")
        else:
            print("Noto`g`ri. ")

    @property
    def phone_info(self):
        return f"Telefon raqami: {self.phone}"
    @phone_info.setter
    def phone_info(self, new_phone):
        check_phone = r"^\+?998[-\s()]?\d{2}[-\s()]?\d{3}[-\s]?\d{2}[-\s]?\d{2}$"
        if re.match(check_phone, new_phone):
            self.phone = new_phone
            print(f"Talabaning tel raqami {self.phone} ga o`zgartirildi.")
        else:
            print("Noto`g`ri.")

    @property
    def email_info(self):
        return f"Talabaning email manzili: {self.email}"
    @email_info.setter
    def email_info(self, new_email):
        check_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(check_email, new_email):
            self.email = new_email
            print(f"Talabaning email manzili {self.email} ga o`zgartirildi.")
        else:
            print("Noto`g`ri. ")

    @property
    def pass_info(self):
        return f"Passport raqami: {self.pass_seria}"
    @pass_info.setter
    def pass_info(self, new_pass):
        check_pass = r"^[A-Z]{2}\d{7}$"
        if re.match(check_pass, new_pass):
            self.pass_seria = new_pass
            print(f"Talabaning passport ma`lumoti {self.pass_seria} ga o`zgartirildi.")
        else:
            print("Noto`g`ri.")

    # @property  # getter
    # def info(self):
    #     return self.year
    #
    # @info.setter  # setter
    # def info(self, a):
    #     if 1920 < a < 2024:
    #         self.year = a
    #     else:
    #         print("Yilni to`gri kiriting.")


student1 = Students("Xoshimov Azamat", 1999, "@azamatxoshimov", +998900199921, "azamat@gmail.com", "AA1234567")
# student1.info = randint(1910, 2040)
# print(student1.info)
student1.year_info = None # None berganim, funksiyani ichida input bilan yangi ma`lumotni  o`zi so`raydi



