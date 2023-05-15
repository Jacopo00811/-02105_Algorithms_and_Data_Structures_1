# Given 3 numbers a, b, c, sort them and returns min, mid, max
def sort(a, b, c):
    return min(a, b, c), ((a + b + c) - min(a, b, c) - max(a, b, c)), max(a, b, c)
