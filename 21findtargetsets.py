
class findzerovals:
    def __init__(self,lst):
        self.lst = lst
        self.target = 0
    def find3vals(self):
        target_list = []
        for i in range(0,len(self.lst)):
            for j in range(0,len(self.lst)):
                for k in range(0,len(self.lst)):
                    if self.lst[i]+self.lst[j]+self.lst[k] == self.target:
                        target_list.append([self.lst[i],self.lst[j],self.lst[k]])
        return target_list
    def removedups(self,lst):
        final_list = []
        for item in lst:
            if sorted(item) not in final_list:
                final_list.append(item)
        return final_list

# Driver code
init_list = [-25, -10, -7, -3, 2, 4, 8, 10]
init_obj = findzerovals(init_list)
final_list = init_obj.find3vals()
print(init_obj.removedups(final_list))
