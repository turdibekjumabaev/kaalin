class KaalinLatin:
    __uppercases = ['A', 'Á', 'B', 'D', 'E', 'F', 'G', 'Ǵ', 'H', 'X', 'Í', 'I', 'J', 'K', 'Q', 'L', 'M', 'N', 'Ń',
                    'O', 'Ó', 'P', 'R', 'S', 'T', 'U', 'Ú', 'V', 'W', 'Y', 'Z', 'Sh', 'C', 'Ch']
    __lowercases = ['a', 'á', 'b', 'd', 'e', 'f', 'g', 'ǵ', 'h', 'x', 'ı', 'i', 'j', 'k', 'q', 'l', 'm', 'n', 'ń',
                    'o', 'ó', 'p', 'r', 's', 't', 'u', 'ú', 'v', 'w', 'y', 'z', 'sh', 'c', 'ch']

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
        return char.isalpha()

    def swapcase(self, text):
        return ''.join(c.lower() if c.isupper() else c.upper() for c in text)

    def to_upper(self, text):
        upper_mapping = dict(zip(self.__lowercases, self.__uppercases))
        return ''.join(upper_mapping[char] if char in upper_mapping else char for char in text)

    def to_lower(self, text):
        lower_mapping = dict(zip(self.__uppercases, self.__lowercases))
        return ''.join(lower_mapping[char] if char in lower_mapping else char for char in text)

    def to_latin(self, text):
        pass