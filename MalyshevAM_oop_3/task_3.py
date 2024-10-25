class Vagon:
    numbers = {}

    def __new__(cls, name, number):
        if not name.startswith("vagon_"):
            raise ValueError("Имя должно начинаться с 'vagon_'")
        real_name = name[6:]
        instance = super(Vagon, cls).__new__(cls)
        cls.numbers[real_name] = number  
        setattr(instance, f'v{real_name}', number)
        return instance


try:
    v1 = Vagon("trone_1", 1)
    print("Объект v1 создан успешно.")
    print("Содержимое словаря numbers:", Vagon.numbers)
except ValueError as e:
    print(e)
