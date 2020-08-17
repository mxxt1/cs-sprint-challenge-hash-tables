def has_negatives(a):
    cache = {}
    result = []
# loop through, check if the negative of current is in the cache.
#if it's in the cache, append the abs val to result
#if not, then add it, you don't pre-pop cache, if the neg exists later, it will find the pos value in cache

    for x in a: 
        if -x in cache:
            result.append(abs(x))
        else:
            cache[x] = x

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


#array of integers, determine if current int has a corresponding negative value returns array of values with a corresponding negative value

# cache
# catch arr
# loop through the list, see if the negative of the current number is in cache. If it is in the cache, then add the absolute value to catch arr
#if it isn't, add it to the cache --> also could just add all to the cache and do lookup --> two loops