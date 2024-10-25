class DataBase:
    _instance = None

    def __new__(cls, user, psw, port):
        if cls._instance is None:
            cls._instance = super(DataBase, cls).__new__(cls)
            return cls._instance
        else:
            raise Exception("Экземпляр DataBase уже существует.")

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def __str__(self):
        return f"Подключение к БД: {self.user}, {self.psw}, {self.port}"

    def connect(self):
        print(f"Подключение к БД: {self.user}, {self.psw}, {self.port}")

    def __del__(self):
        print("Закрытие соединения с БД")

    def get_data(self):
        return "Данные из базы данных"

try:
    db1 = DataBase('root', '1234', 80)
    print(db1)
    db1.connect()
    print(db1.get_data())

    db2 = DataBase('admin', '5678', 81)
except Exception as e:
    print(e)

try:
    print(db2)
except NameError:
    print("db2 не существует.")
