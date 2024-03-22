class KaalinNumber:
    __ones = ["", "bir", "eki", "úsh", "tórt", "bes", "altı", "jeti", "segiz", "toǵız", "on", "on bir", "on eki", "on úsh", "on tórt", "on bes", "on altı", "on jeti", "on seginz", "on toǵız"]
    __tens = ["", "", "jigirma", "otız", "qırıq", "eliw", "alpıs", "jetpis", "seksen", "toqsan"]

    def __init__(self):
        pass

    def to_word(self, number):
        if number < 20:
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
        elif number < 100000:
            ten_thousand_digit = number // 1000
            remainder = number % 1000
            if remainder == 0:
                return f"{self.__ones[ten_thousand_digit]} mıń"
            else:
                return f"{self.__ones[ten_thousand_digit]} mıń {self.to_word(remainder)}"
        else:
            return "San shegaradan asıp ketti"