class Cyrillic:
    __uppercases = ['А', 'Ә', 'Б', 'Д', 'Е', 'Ф', 'Г', 'Ғ', 'Ҳ', 'Х', 'Ы', 'И', 'Ж', 'К', 'Қ', 'Л', 'М', 'Н', 'Ң',
                   'О', 'Ө', 'П', 'Р', 'С', 'Т', 'У', 'Ү', 'В', 'Ў', 'Й', 'З', 'Ш', 'Ц', 'Ч', ' ']
    __lowercases = ['а', 'ә', 'б', 'д', 'е', 'ф', 'г', 'ғ', 'ҳ', 'х', 'ы', 'и', 'ж', 'к', 'қ', 'л', 'м', 'н', 'ң',
                   'о', 'ө', 'п', 'р', 'с', 'т', 'у', 'ү', 'в', 'ў', 'й', 'з', 'ш', 'ц', 'ч', ' ']

    def __init__(self, text):
        self.text = text

    @classmethod
    def get_uppercases(cls):
        return cls.__uppercases

    @classmethod
    def get_lowercases(cls):
        return cls.__lowercases

    def isupper(self):
        return all(char in self.__uppercases for char in self.text)

    def islower(self):
        return all(char in self.__lowercases for char in self.text)

    def isdigit(self):
        return self.text.isdigit()

    def isalpha(self):
        return self.text.isalpha() or self.text.isnumeric()

    def swapcase(self):
        return self.text.swapcase()

    def upper(self):
        upper_mapping = dict(zip(self.__lowercases, self.__uppercases))
        return ''.join(upper_mapping.get(char, char) for char in self.text)

    def lower(self):
        lower_mapping = dict(zip(self.__uppercases, self.__lowercases))
        return ''.join(lower_mapping.get(char, char) for char in self.text)
