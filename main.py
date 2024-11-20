array = [25,14,69,71,50,3,45,92,16,42]
def  bubble_sort():
 n = len(array)
 for i in range(n-1):
   for j in range (0, n-i-1):
     if array[j] > array[j+1]:
       array[j],array[j+1] = array[j+1],array[j]
     print(array) 