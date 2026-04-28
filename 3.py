string = "abcabc"
count = 1

arr = list(string)
new=[]
length = len(arr)
start = arr[0]
for i in arr:
    if i == start:
        count +=1
        print (count)