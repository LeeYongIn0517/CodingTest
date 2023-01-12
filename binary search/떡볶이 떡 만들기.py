n,m = int(input().split())
array = list(map(int, input().split()))
array.sort()
def search_binary(array, target, start, end, sum_record):
    