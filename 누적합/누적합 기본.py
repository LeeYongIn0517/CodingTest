arr = [0,7,6,3,2,1]
for i in range(1,len(arr)):
   arr[i] = arr[i-1] + arr[i]
print(arr[5]-arr[3]) #인덱스 4~5의 누적합 예시, 답은 3