
cache = {}


def intersection(arrays):
    # cache
    # populate cache with the ints in the zero array in array of arrays, value is the count
    #loop through other arrays and check if the ints are in the cache, if so += 1
    # if the count is equal to the length of the array of arrays, then add it to the intersection catch array

    result = []

    for num in arrays[0]:
        cache[num] = 1

    for i in range(1,len(arrays)):
        for j in arrays[i]:
            if j in cache:
                cache[j] += 1
            if cache[j] == len(arrays):
                result.append(j)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))


    # given array of arrays of ints, find the intersecting values across all provided arrays and return the common ints as array (order doesn't matter)