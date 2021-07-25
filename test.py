# arr=[]

# arr= input("enter a number >")

# print("Array is :",arr)

# res = arr[::-1] #reversing using list slicing
# print("Resultant new reversed array:",res)

def reverseArray(lst):
    new_lst=lst[::-1]
    return new_lst


lst=input("please enter numbers >")
print(reverseArray(lst))