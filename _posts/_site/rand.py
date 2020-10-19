import random

def randnum(arr, freq):
    sum = 0
    aux = []
    count = 0
    for i in freq:
        sum+=i
        for j in range(i):
            aux.append(arr[count])
        count+=1
    print(aux[random.randint(0,sum-1)])


randnum([10, 30, 20, 40], [1,6, 2, 1])
