import self as self


class Test1:
    def getval(self):
        arr1 = [1,2,3,4]
        print([i+1 for i in arr1])
        # arr2=[]
        # arr1=[1,2,3,4]
        # for i in arr1:
        #     arr2.append(i+1)
        # print(arr2)


obj = Test1
obj.getval(self)
