class SeparateText:
    def __init__(self, text):
        print("Старт инициализатора в классе SeparateText.__init__()")
        self.splitword = text.split()
        print("Конец инициализатора в классе SeparateText.__init__()")


class CountWorld(SeparateText):
    def __init__(self, text):
        print("Старт инициализатора в классе CountWorld.__init__()")
        super().__init__(text)
        self.word_count = len(self.splitword)
        print("Конец инициализатора в классе CountWorld.__init__()")


class Unique(SeparateText):
    def __init__(self, text):
        print("Старт инициализатора в классе Unique.__init__()")
        super().__init__(text)
        self.unic = set(text)
        print("Конец инициализатора в классе Unique.__init__()")


class Describer(CountWorld, Unique):
    def __init__(self, text):
        print("Старт инициализатора в классе Describer.__init__()")
        CountWorld.__init__(self, text)
        Unique.__init__(self, text)
        print("Конец инициализатора в классе Describer.__init__()")

    def print(self):
        print("Список слов:", self.splitword)
        print("Количество слов:", self.word_count)
        print("Множество уникальных символов:", self.unic)


# Пример использования
text = "Hello world! Hello Python!"
describer = Describer(text)
describer.print()
