def heapify(arry, n, i):
    largest = i  
    l = 2 * i + 1 
    r = 2 * i + 2  

    if l < n and arry[i] < arry[l]:
        largest = l

    if r < n and arry[largest] < arry[r]:
        largest = r
   
    if largest != i:
        arry[i], arry[largest] = arry[largest], arry[i]  

        heapify(arry, n, largest)


def heap_sort(arry):
    n = len(arry)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arry, n, i)

    for i in range(n - 1, 0, -1):
        arry[i], arry[0] = arry[0], arry[i]
        heapify(arry, i, 0)

    return arry


data = input("Enter input (space):").split(" ")

sorted_arry = heap_sort(data)

print("Sorted Data", sorted_arry)
