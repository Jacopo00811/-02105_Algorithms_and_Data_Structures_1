import Heap as hp

def HeapSort(array):
    heap = hp.MaxHeap()
    # Build heap
    for item in array:
        heap.insert(item)

    for i in range(heap.n, 1, -1):
        heap.swap(1,i)
        heap.n -= 1
        heap.bubbleDown(1)

    return heap.h[1:]

# Sort a given array
someArray = list(map(int, input().split()))
print(HeapSort(someArray))