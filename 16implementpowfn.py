# implement pow(x,n)
class powerfn:
    def __init__(self,x,n):
        self.x = x
        self.n = n
    def pow_result(self):
        return pow(self.x,self.n)

init_pow = powerfn(2,4)
print(init_pow.pow_result())
