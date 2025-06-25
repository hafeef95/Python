list1=[1,4,6,9,]
total=sum(list1)
print(total)
def func(list2):
    
    total=0
    for list in list2:
        total+=list
    return total
list2=[2,4,6,8,9,8]
func(list2)