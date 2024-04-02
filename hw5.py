# 1 Hey Twin 

import numpy as np
arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])
filter = np.all(arr[:, 1:] == arr[:,:-1], axis = 1)
print(arr[filter])
# Below is just there (ignore pls)
# number = np.mean(arr1)
# number2 = arr2[0]
# number3 = np.mean(arr3)
# result = np.array([])
# def equalarray(array):
#     result = np.array([])
#     for i in arr1:
#         if i == number:
#             result = np.append(result,i)
#             print(result)

#     for j in arr2:
#         if j == number2:
#             result = np.append(result, j)
#             print(result)
       
#     for k in arr3:
#         if k == number3:
#             result = np.append(result, k)
#             print(result)

    #return (result)    

print(equalarray(arr))




        




# 2 Checkers
x = np.zeros((8, 8), dtype = int)   #dtype meaning data type
x[1::2, ::2] = 1                    #[start:stop:set]
x[::2, 1::2] = 1
print(x)


#1st try (just there ignore pls)
checkboard = np.array[[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]
checkboard[0:8:2]
print  

# 3 I need some space
import numpy as np
sarray = np.char.join(' ', 'Python is cool')
print(sarray)

# 4 Everything is in order

import numpy as np
np.random.seed(12345)
multiarray = np.random.randint(1, 50, (4, 5))
np.sort(multiarray, axis = 0) #isn't doing anything only in print
print(np.sort(multiarray, axis = 0)) # can't put equal in print it's invalid
