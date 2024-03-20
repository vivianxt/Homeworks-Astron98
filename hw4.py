# 2 List slicing and striding
#2.1

varlist = list(range(0,51))
print(varlist)

#2.2
lis = [2, 3, 4]
#square(lis)
#The error: that seems to be present here is that we simply cannot type
# square and think it will square the list, our square is not defined
# Fixing: by including a for loop we can use the i**2 which will define 
# that we are squaring our list the right way.

def lis(x):
    ans = []
    for i in x:
        ans = ans + [i**2]
    return ans
print(lis([2, 3, 4]))

#2.3
#Error: I kept getting an error for some reason when I had my list before my functio
#Fix: I decided to have it after my function which for some reason fixed it

def twolists(listA, listB):
    ans = []
    for i in listA:
        if i%2 != 0:
            ans.append(i)
        #return ans
    for i in listB:
        if i%2 != 0:
            ans.append(i)
    return ans

list1 = range(1,11)
list2 = range(20,31)
print(twolists(list1, list2))   

# 3.1 Part 1
#Error: It wouldn't want to take my list and put it into a 2D list
#fix: I changed putting it into a range without [] and with ()

import numpy as np
myArray = np.array([range(1, 6), range(6,11), range(11,16), range(16,21), range(21, 26)])
print(myArray)

#3.2
#Error: it wouldnt run my code because of my string to replace the #'s divisible by three
#Fix: I opted for putting a data type in the myArray part to let it run.

import numpy as np
myArray = np.array([np.arange(1, 6), np.arange(6,11), np.arange(11,16), np.arange(16,21), np.arange(21, 26)], dtype = 'object') 
def myArray2(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]%3 == 0:
                arr[i][j] = '?'
    return arr
print(myArray2(myArray))

#4
#Error: function wouldn't run when I tried it with a for loop
#Fix: I opted for in putting a set into my list.

dubllist = [1, 1, 2, 3, 4, 4]
def dublist(x):
    set(x)
    return list(set(x))
print(dublist(dubllist))

