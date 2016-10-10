arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)
max_sum = -70
sum = 0
n = len(arr) - 2
k = len(arr[0]) - 2
for i in range(0,n):
    for j in range (0,k):
        sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if(sum>max_sum):
              max_sum=sum
print max_sum
