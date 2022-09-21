#2. Write a Python program to multiplies all the items in a list.



def multiplyList(myList):
        result=1
        for x in myList:
            result=result*x
        return result
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1),multiplyList(list2))
