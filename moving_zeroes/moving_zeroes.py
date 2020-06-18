

                            #### TESTS PASSING... OBJECTIVE COMPLETE ####

'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    for i, v in enumerate(arr):
        if v == 0:
            p = v
            arr.remove(p)
            arr.append(p)


    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")