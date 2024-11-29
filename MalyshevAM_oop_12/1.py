class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __setattr__(self, name, value):
        if name == "first_name":
            if not isinstance(value, str) or not value.isalpha():
                raise ValueError("Имя должно содержать только буквы")
        elif name == "last_name":
            if not isinstance(value, str) or not value.replace(' ', '').isalnum():
                raise ValueError("Фамилия должна содержать только буквы и цифры")
        elif name == "age":
            if not isinstance(value, int):
                raise ValueError("Возраст должен быть целым числом")
        super().__setattr__(name, value)

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return f"Атрибут '{name}' не существует"

    def __getattr__(self, name):
        if name == "City":
            return "Moscow"
        return None

    def __delattr__(self, name):
        if name in ("first_name", "last_name", "age"):
            raise AttributeError(f"Атрибут '{name}' нельзя удалить")
        super().__delattr__(name)



person = Person("Иван", "Иванов", 30)
try:
    print(person.first_name)
    print(person.City)  
    del person.age
except Exception as e:
    print(e)

try:
    person.last_name = "Иванов123"
except Exception as e:
    print(e)

print(person.some_nonexistent_attr)