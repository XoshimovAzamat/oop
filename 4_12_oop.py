class EditName:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get("name", None)
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("str kiriting.")
        instance.__dict__["name"] = value

    def __delete__(self, instance):
        raise AttributeError("haaa")

class EditID:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get("ID", None)
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Noto`g`ri.")
        instance.__dict__["ID"] = value

    def __delete__(self, instance):
        raise AttributeError("vahaaaa")


class Student:
    name = EditName()
    id = EditID()
    def __init__(self, name, id):
        self.name = name
        self.id = id

student1 = Student("Azamat", "AA1234567")
print(student1.name)
student1.name = "Ali"
print(student1.name)
print(student1.id)
student1.id = "DD9999999"
print(student1.id)