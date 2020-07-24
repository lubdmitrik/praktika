import random
def randomize(arr):
    for i in range(0,10):
        arr.append(random.randint(0,100))
    return arr

def indexer(arr,indexing):
    for i in range(len(arr)):
        if arr[i] == indexing:
            return print('індекс',i)

def sorting(arr):
    arr.sort()
    return arr

def poslidov(arr):
    z = 0
    a = (len(arr))
    for i in range (1,a):
      
      if arr[i-1] >= arr[i]:
        z = z+1
    if z == 9 :
          print ('Послідовність від більшого до меншого')
    else: 
          print ('Послідовність від меншого до більшого')    	

def lowest(arr):
    print (arr[0],arr[1],arr[2],arr[3],arr[4])

def biggest(arr):
  	print (arr[-1],arr[-2],arr[-3],arr[-4],arr[-5])

def avg(arr):
	k = (sum(arr)/len(arr))
	print (k)

def deletdouble(arr):
    return print("Видалення дублікатів",list(set(arr)))
