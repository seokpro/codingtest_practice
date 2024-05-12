def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        #mid값=target값인 경우
        if array[mid] == target:
            return mid
        #mid값 > target값인 경우
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
#상근이 카드 갯수 입력
n = int(input())
#상근이 카드 값을 공백으로 구분해 입력
array = list(map(int, input().split()))
array.sort()
#정수 갯수 입력
m = int(input())
#상근이 카드와 대조할 카드 값 입력
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('1', end =' ')
    else:
        print('0', end=' ')