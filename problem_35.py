'''
Given an array of strictly the characters 'R', 'G', and 'B', 
segregate the values of the array so that all the Rs come first, 
the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''


def sort_rgb(arr):
    start_pos = 0
    end_pos = len(arr)-1

    for n in arr:
        if n == 'R':
            start_pos += 1
        else:
            break

    for n in reversed(arr):
        if n == 'B':
            end_pos -= 1
        else:
            break

    idx = start_pos

    while idx < len(arr) and start_pos < end_pos and idx <=end_pos:
        if arr[idx] == 'B':
            tmp = arr[idx]
            arr[idx] = arr[end_pos]
            arr[end_pos] = tmp
            end_pos -= 1
        elif arr[idx] == 'R':
            tmp = arr[idx]
            arr[idx] = arr[start_pos]
            arr[start_pos] = tmp
            start_pos += 1
            idx += 1
        else:
            idx += 1
        

    return arr 
        


assert sort_rgb(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R','R','R','G','G','B','B'] 
