# 1 Power of a Number

def power(x,y):
    answer = 1
    for i in range(y):
        answer = x * answer     #can also write it as answer*= x
    return answer


# 2 Minimum and Maximum

def min_max(v):
    return(min(v), max(v))


# 3 Check Leap year

def leapyear(x):
    if x % 4 == 0 and x % 100 !=0:
        return True
    elif x % 4 == 0 and x % 100 == 0 and x % 400 == 0:
        return True
    else:
        return False


# 4 Calculate BMI (Body Mass Index)

def BMI(weight, height):
    return weight/height**2


# 5 Rotating Digits

def rotating_digit(x):
    y = x % 10
    h = x // 10
    x = int(str(x)[1:])
    length = len(str(x))
    return ((y*10**length) + h)


# 6 Minimum and Maximum but with Loops
#For Loop 

def min(list):
   min = list[0]
   for l in list:
       if l < min:
           min = l
   return min


def max(list):
    max = list[0]
    for l in list:
        if l > max:
            max = l
    return max


#While Loop

def min(x):
    i = 0
    min = x[i]
    while i < len(x):
        if x[i] < min:
            min = x[i]
        i -= 1
        return min


def max(x):
    i = 0
    max = x[i]
    while i < len(x):
        if x[i] > max:
            max = x[i]
        i -= 1
        return max


# 7 Vowels

def countvowels(x):
    count = 0
    for i in x:
        if i in "aeiouAEIOU":
            count = count + 1
    return count


        
# 8 Digital Root
    
def sum(x):
    if x == 0:
        return 0
    return (x % 10 + sum(int(x/10)))


















