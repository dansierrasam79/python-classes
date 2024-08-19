class getclassName:
    def __init__(self,init_name):
        self.init_name = init_name
        
    def displayclassName(self):
        return self.init_name

init_obj = getclassName("Daniel")
second = type(init_obj).__name__
print(second)
