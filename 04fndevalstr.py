# display valid strings if containing "()" "{}" "[]"

class evalvalstr:
    def __init__(self,init_str):
        self.init_str = init_str

    def fndvalstr(self):
        def_str_lst = ["()","{}","[]"]
        init_str_lst = []
        count = 0
        init_str_lst  = [self.init_str[i:i+2] for i in range(0,len(self.init_str),2)]
        for i in range(0,len(self.init_str)):
            if self.init_str[i:i+2] in def_str_lst:
                count += 1
        if count == len(init_str_lst):
            return True
        else:
            return False

#Driver code
init_str_obj = evalvalstr("(){}[]")
print(init_str_obj.fndvalstr())
sec_str_obj = evalvalstr("()[{)}")
print(sec_str_obj.fndvalstr())
thrd_str_obj = evalvalstr("()")
print(thrd_str_obj.fndvalstr())
