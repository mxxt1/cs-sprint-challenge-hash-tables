def get_indices_of_item_weights(weights, length, limit):
# cache for indexing 

    cache = {}
#loop through the weights values and index them in the cache
# cache[weights[i]] = i --> key:index

    for i in range(length):
        cache[weights[i]] = i


# loop through the weights, subtract current weight from the limit and then see if 2nd value is present in the dict, if it is, return the structured tuple or none

    for j in range(length):
        sec_val = limit-weights[j]

        if sec_val in cache:
            #return in the order (max(first val index, second val index), min("","")) j=first val, cache[second] --> sec index
            return (max(j,cache[sec_val]),min(j, cache[sec_val]))



    return None


    # Find the combination of two elements in weights that equal the limit value, and return tuple containing the index of those two values, where the largest of the two values is at 0 position and smaller is at 1 position 
