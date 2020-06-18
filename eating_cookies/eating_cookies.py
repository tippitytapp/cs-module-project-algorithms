

                            #### TESTS PASSING... OBJECTIVE COMPLETE ####


'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # if n < 0:
    #     return 0
    # elif n <= 1:
    #     return 1
    # else:
    #     permutations = eating_cookies( \
    #         n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    #     return permutations
##### SEANS SOLUTION #####
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)


def eating_large_cookies(n, cache):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache[n] > 0:
        return cache[n]
    else:
        cache[n] =  eating_large_cookies(n-3, cache) + eating_large_cookies(n-2, cache) + eating_large_cookies(n-1, cache)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
