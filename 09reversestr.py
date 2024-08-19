# reverse all words in sentence
class reversestr:
    def __init__(self, init_str):
        self.init_str = init_str

    def revstr(self):
        init_list = self.init_str.split(" ")
        final_list = [word[::-1] for word in init_list]
        final_str = ""
        for rev_word in final_list:
            final_str += rev_word + " "
        return final_str.strip()

#Driver code
init_str = "The quick fox jumps over the lazy doggies"
init_obj = reversestr(init_str)
print(init_obj.revstr())
