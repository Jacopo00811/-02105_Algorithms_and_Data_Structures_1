matrix = [[1, 2, 3], 
          [4, 10, 5], 
          [6, 2, 0]]

def findPeak(matrix):
    start = 0 
    end = len(matrix)
   
    while (start <= end):
        mid = int((start + end)/2)
        current_row = 0

        for r in range(len(matrix)):
            current_row = r if matrix[r][mid] >= matrix[current_row][mid] else current_row

        is_left =  mid-1 >= start and matrix[current_row][mid-1] > matrix[current_row][mid]
        is_right = mid + 1 <= end and matrix[current_row][mid+1] > matrix[current_row][mid]
               
        # When a peak is found
        if (not is_left and not is_right) :
            return [current_row, mid]
        elif (is_right):
            start = mid+1
        else:
            end = mid-1
     
    return [ -1, -1 ]


print(findPeak(matrix))
 





























