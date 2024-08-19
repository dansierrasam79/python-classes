#work with strings
class workwithstrs:
    def __init__(self):
        self.init_str = ""

    def get_str(self):
        self.init_str = input("Enter a word:")
        print("Input accepted")

    def prnt_str(self):
        print(self.init_str)

    
init_obj = workwithstrs()
init_obj.get_str()
print("Printing accepted string...")
init_obj.prnt_str()
