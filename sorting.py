from random import randint

def bubble_sort(lst: list) -> list:
    sorted = False
    while sorted == False:  
        sorted = True
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                sorted = False  
    return lst

def insertion_sort(lst: list) ->list:
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i] < lst[j]:
                lst.insert(j, lst.pop(i))
                break
    return lst

def merge_sort(lst: list) -> list:
    def wrapper(lst: list, left: int, right: int) -> list:
        if (left < right):
            mid = left + int((right-left)/2)
            wrapper(lst, left, mid)
            wrapper(lst, mid+1, right)
            i, j = left, mid+1
            while i < j and j < right+1:
                if lst[i] > lst[j]:
                    lst.insert(i, lst.pop(j))
                    j += 1
                i += 1
        return lst
    return wrapper(lst, 0, len(lst)-1)

def quick_sort(lst: list) -> list:
    def wrapper(lst: list, left: int, right: int) -> list:
        if left < right:
            i, j = left, right
            while True:
                while i < j and lst[j] >= lst[left]:
                    j -= 1
                while i < j and lst[i] <= lst[left]:
                    i += 1
                if i == j:
                    lst[left], lst[i] = lst[i], lst[left]
                    break
                lst[i], lst[j] = lst[j], lst[i]
            wrapper(lst, left, i-1)
            wrapper(lst, i+1, right)
        return lst
    return wrapper(lst, 0, len(lst)-1)

algorithms = [bubble_sort, insertion_sort, merge_sort, quick_sort]
for algorithm in algorithms:
    name = algorithm.__name__.replace('_', ' ').capitalize()
    print(f"  *** {name} ***\n")
    for j in range(3):
        numbers = [randint(-99, 99) for _ in range(randint(5,10))]
        print(f" Randomised numbers: {str(numbers)}")
        print(f" Sorted numbers:     {algorithm(numbers)}\n")
