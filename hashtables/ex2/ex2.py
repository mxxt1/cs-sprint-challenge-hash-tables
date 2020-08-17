#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
     
    route = [None] * length
    cache = {}

    # add the source --> dest relationships to cache
    for x in tickets:
        cache[x.source] = x.destination

    #store the next destination
    dest = None


    for i in range(0, length):
        #for i=0, start the cycle --> dest = destination of first ticket, then reassign dest to destination of subsequent ticket
        # None to LAX
        #set dest=LAX
        #push to route
        #Lax --> SFO, set dest sfo, etc...
        if i == 0:
            route[i] = cache["NONE"]
            dest = route[i]
        else:
            route[i] = cache[dest]
            dest = cache[dest]

    return route


# unsorted array of tickets, containing source and destination. Put the sequence in order, such that destination = source. Starting ticket has source None, ending ticket has destination None

# create catch array to hold sorted
# Find the starting ticket (source = none)
# add the destination to the catch array 
# find the next ticket where dest = source, push the destination 
# repeat

# actually that's dumb
# create a dict, loop through the tickets, and add source:dest
#loop through the range, set the destination to corresponding value in dict, set the destination as the value from dict