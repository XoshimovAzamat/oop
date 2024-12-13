import re

class EditName:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        print("EditName class ning get metodi ishladi.")
        return instance.__dict__.get("name", None)

    def __set__(self, instance, value):
        check_name = r"^[A-Za-z\s'`‘’ʼ]+$"
        if re.match(check_name, value):
            instance.__dict__["name"] = value
        if not isinstance(value, str):
            raise ValueError("Str kiriting!")
        if value.capitalize()!=value:
            return ValueError("Boshiga katta harf kiriting!")
        print("EditName class ning set metodi ishladi.")

    def __delete__(self, instance):
        raise AttributeError("Name attribute cannot be deleted!")


class EditPhone:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        print("EditPhone class ning get metodi ishladi.")
        return instance.__dict__.get("phone", None)

    def __set__(self, instance, value):
        check_name = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        if re.match(check_name, value):
            instance.__dict__["phone"] = value
        if not isinstance(value, int):
            raise ValueError("Raqam kiriting!")
        print("EditPhone class ning set metodi ishladi.")

    def __delete__(self, instance):
        raise AttributeError("Name attribute cannot be deleted!")


class EditEmail:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        print("EditEmail class ning get metodi ishladi.")
        return instance.__dict__.get("email", None)

    def __set__(self, instance, value):
        check_name = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
        if re.match(check_name, value):
            instance.__dict__["email"] = value
        if not isinstance(value, str):
            raise ValueError("Namuna: geon@ihateregex.io kabi kiriting!")
        print("EditEmail class ning set metodi ishladi.")

    def __delete__(self, instance):
        raise AttributeError("Name attribute cannot be deleted!")

class EditID:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        print("EditID class ning get metodi ishladi.")
        return instance.__dict__.get("ID", None)

    def __set__(self, instance, value):
        check_name = r"^[A-Z]{2}\d{7}$"
        if re.match(check_name, value):
            instance.__dict__["ID"] = value
        if not isinstance(value, None):
            raise ValueError("Namuna: AA1234567 kabi kiriting!")
        print("EditID class ning set metodi ishladi.")

    def __delete__(self, instance):
        raise AttributeError("Name attribute cannot be deleted!")

class EditUserName:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        print("EditUserName class ning get metodi ishladi.")
        return instance.__dict__.get("ID", None)

    def __set__(self, instance, value):
        check_name =  r"^[a-zA-Z0-9_]{5,32}$"
        if re.match(check_name, value):
            instance.__dict__["ID"] = value
        if not isinstance(value, str):
            raise ValueError("Namuna: username123 kabi kiriting!")
        print("EditUserName class ning set metodi ishladi.")

    def __delete__(self, instance):
        raise AttributeError("Name attribute cannot be deleted!")


class Student:
    name = EditName()
    phone = EditPhone()
    email = EditEmail()
    id = EditID()
    user_name = EditUserName()

    def __init__(self, name, phone, email, id, user_name):
        self.name = name
        self.phone = phone
        self.email = email
        self.id = id
        self.user_name = user_name


