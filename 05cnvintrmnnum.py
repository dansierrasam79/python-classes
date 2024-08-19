#convert int to roman numeral
class int_to_rom:
    def __init__(self, num):
        self.num = num
    def int_to_Roman(self):
        val = [1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4,
                1]
        syb = ["M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV",
                "I"]
        roman_num = ''
        i = 0
        while  self.num > 0:
            for _ in range(self.num // val[i]):
                roman_num += syb[i]
                self.num -= val[i]
            i += 1
        return roman_num


first_int_obj = int_to_rom(4000).int_to_Roman()
print(first_int_obj)
