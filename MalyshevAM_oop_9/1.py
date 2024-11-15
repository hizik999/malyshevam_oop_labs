class SeparateText:
    def __init__(self, text):
        print("Старт инициализатора в классе SeparateText")
        self.splitword = text.split()
        print("Конец инициализатора в классе SeparateText")


class CountWorld(SeparateText):
    def __init__(self, text):
        print("Старт инициализатора в классе CountWorld")
        super().__init__(text)
        self.word_count = len(self.splitword)
        print("Конец инициализатора в классе CountWorld")


class Unique(SeparateText):
    def __init__(self, text):
        print("Старт инициализатора в классе Unique")
        super().__init__(text)
        self.unic = set(text)
        print("Конец инициализатора в классе Unique")


class Describer(CountWorld, Unique):
    def __init__(self, text):
        print("Старт инициализатора в классе Describer")
        super().__init__(text)
        print("Конец инициализатора в классе Describer")

    def print_info(self):
        print("Список слов:", self.splitword)
        print("Количество слов:", self.word_count)
        print("Уникальные символы:", self.unic)


# Пример использования
text = "Пример текста для обработки текста"
describer = Describer(text)
describer.print_info()
