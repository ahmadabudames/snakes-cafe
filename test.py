# list=[]

# list= input("enter a number >")

# print("Array is :",list)

# res = list[::-1] #reversing using list slicing
# # print("Resultant new reversed array:",res)

# def reverseArray(lst):
#     new_lst=lst[::-1]
#     return new_lst


# lst=input("please enter numbers >")
# print(reverseArray(lst))

def binary_search(list, week_to_reach, hard_to_reach , i):
 
    if hard_to_reach >= week_to_reach:

        middel = (hard_to_reach + week_to_reach) // 2
 
        if list[middel] == i:
            return middel
 
        elif list[middel] > i:
            return binary_search(list, week_to_reach, middel - 1, i)
 
        else:
            return binary_search(list, middel + 1, hard_to_reach, i)
 
    else:
        return -1
 
list = [1, 2, 3, 5, 6, 7]
i = 4

result = binary_search(list, 0, len(list)-1, i)
 
if result != 0: 
    
 print(result)
