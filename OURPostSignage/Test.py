class test:
    def __init__(self,list1,list2) -> None:
        #print( list1[0],list2[0])
        self.__setattr__(list1[0],list2[0])
        #print(self.__getattribute__(list1[0]))

    def printinfo(self,list1):
        return getattr(self,list1[0])

test1a = test(['Dog'],[1])

#print(test1a.printinfo(['Dog']))

class test2:
    def inputClass(c):
        return c(['Dog'],[1])

test2a = test2.inputClass(test)
#print(test2a.printinfo(['Dog']))

dick = {'Dog':2,'Cat':4}

for i in dick:
    print(dick[i])