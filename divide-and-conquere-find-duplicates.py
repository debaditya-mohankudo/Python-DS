#O(nlogn)?
def find_duplicates(L):
    if len(L) == 0:
        return
    item = L[0]
    L1 = [num for num in L if num < item]
    L2 = [num for num in L if num > item]
    print(item, len(L) - len(L1) - len(L2))
    find_duplicates(L1)
    find_duplicates(L2)

a = [1, 3, 5, 11, 13, 40, 15, 2, 3, 11, 1]
find_duplicates(a)
1 2
3 2
2 1
5 1
11 2
13 1
40 1
15 1

