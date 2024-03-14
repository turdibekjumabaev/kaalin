class KaalinNumber:
    __ones = ["", "bir", "eki", "úsh", "tórt", "bes", "altı", "jeti", "segiz", "toǵız"]
    __tens = ["", "", "jigirma", "otız", "qırıq", "eliw", "alpıs", "jetpis", "seksen", "toqsan"]

    def __init__(self):
        pass

    def to_word(self, number):
        if number < 10:
            return self.__ones[number]
        elif number < 100:
            ten_digit = number // 10
            one_digit = number % 10
            if one_digit == 0:
                return self.__tens[ten_digit]
            else:
                return f"{self.__tens[ten_digit]} {self.__ones[one_digit]}"
        elif number < 1000:
            hundred_digit = number // 100
            remainder = number % 100
            if remainder == 0:
                return f"{self.__ones[hundred_digit]} júz"
            else:
                return f"{self.__ones[hundred_digit]} júz {self.to_word(remainder)}"
        elif number < 10000:
            thousand_digit = number // 1000
            remainder = number % 1000
            if remainder == 0:
                return f"mıń"
            else:
                return f"{self.__ones[thousand_digit]} mıń {self.to_word(remainder)}"
        else:
            return "Number out of range"

    def base2to8(self, number):
        decimal_number = int(number, 2)
        octal_number = oct(decimal_number)[2:]
        return octal_number

    def base2to10(self, number):
        decimal_number = int(number, 2)
        return decimal_number

    def base8to2(self, number):
        decimal_number = int(number, 8)
        binary_number = bin(decimal_number)[2:]
        return binary_number

    def base8to10(self, number):
        decimal_number = int(number, 8)
        return decimal_number

    def base8to16(self, number):
        decimal_number = int(number, 8)
        hexadecimal_number = hex(decimal_number)[2:]
        return hexadecimal_number

    def base2to16(self, number):
        decimal_number = int(number, 2)
        hexadecimal_number = hex(decimal_number)[2:]
        return hexadecimal_number

    def base10to2(self, number):
        return bin(number)[2:]

    def base10to8(self, number):
        return oct(number)[2:]

    def base10to16(self, number):
        return hex(number)[2:]