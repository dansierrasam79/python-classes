# find indices of target value

class targetval:
    def __init__(self,target,lst):
        self.target = target
        self.lst = lst

    def find_targt_set(self):
        final_list = []
        for i in range(0, len(self.lst)):
            for j in range(0, len(self.lst)):
                if self.lst[i] + self.lst[j] == self.target:
                    final_list.append([self.lst.index(self.lst[i]),self.lst.index(self.lst[j])])
        return final_list

    def remove_duplicates(self,lst):
        final_list = []
        for item in lst:
            if sorted(item) not in final_list:
                final_list.append(item)
        return final_list

#Driver code
init_list = [10,20,10,40,50,60,70]
target = 50
init_object = targetval(target,init_list)
target_set = init_object.find_targt_set()
final_list = init_object.remove_duplicates(target_set)
print(final_list)
