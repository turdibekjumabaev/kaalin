class KaalinCyrillic:
    __uppercases = ['А', 'Ә', 'Б', 'Д', 'Е', 'Ф', 'Г', 'Ғ', 'Ҳ', 'Х', 'Ы', 'И', 'Ж', 'К', 'Қ', 'Л', 'М', 'Н', 'Ң',
                   'О', 'Ө', 'П', 'Р', 'С', 'Т', 'У', 'Ү', 'В', 'Ў', 'Й', 'З', 'Ш', 'Ц', 'Ч']
    __lowercases = ['а', 'ә', 'б', 'д', 'е', 'ф', 'г', 'ғ', 'ҳ', 'х', 'ы', 'и', 'ж', 'к', 'қ', 'л', 'м', 'н', 'ң',
                   'о', 'ө', 'п', 'р', 'с', 'т', 'у', 'ү', 'в', 'ў', 'й', 'з', 'ш', 'ц', 'ч']

    def __init__(self):
        pass

    @classmethod
    def get_uppercases(cls):
        return cls.__uppercases

    @classmethod
    def get_lowercases(cls):
        return cls.__lowercases

    def is_upper(self, char):
        return char in self.__uppercases

    def is_lower(self, char):
        return char in self.__lowercases

    def is_digit(self, char):
        return char.isdigit()

    def is_alpha(self, char):
        return char.isalpha() or char.isnumeric()

    def swapcase(self, text):
        return ''.join(c.lower() if c.isupper() else c.upper() for c in text)

    def to_upper(self, text):
        upper_mapping = dict(zip(self.__lowercases, self.__uppercases))
        return ''.join(upper_mapping[char] if char in upper_mapping else char for char in text)

    def to_lower(self, text):
        lower_mapping = dict(zip(self.__uppercases, self.__lowercases))
        return ''.join(lower_mapping[char] if char in lower_mapping else char for char in text)

    def to_cyrillic(self, text):
        pass