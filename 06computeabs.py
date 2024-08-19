# compute abs of -155
import builtins
class computeabs:
    def __init__(self,fn_name,abs_val):
        self.abs = abs_val
        self.func_name = fn_name

    def disp_fn_name(self):
        return self.func_name

    def comp_abs(self):
        return builtins.abs(self.abs)

init_abs = computeabs('abs',-155)
print(help(init_abs.disp_fn_name()))
print(init_abs.comp_abs())
