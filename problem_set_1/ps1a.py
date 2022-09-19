###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Aloisio Valério
# Collaborators: None
# Time: 2h30

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows = {}
    
    file = open(filename, encoding="utf-8")

    for line in file:
        line = line.strip('\n')
        split_line = line.split(",")
        cows[split_line[0]] = int(split_line[1])

    file.close()

    return cows


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = []
    
    cows_copy = dict(sorted(cows.items(),key= lambda x:x[1], reverse = True))
    
    while (bool(cows_copy)):
        single_trip = greedy_single_trip(cows_copy, limit)
        trips.append(single_trip)

        for cow in single_trip:
            del(cows_copy[cow])
    
    return trips

def greedy_single_trip(cows, limit):
    '''
    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of containing the names of cows transported on a particular trip
    '''
    trip = []
    total_weight = 0

    for cow in cows:
        if cows[cow] + total_weight <= limit:
            total_weight += cows[cow]
            trip.append(cow)
    
    return trip

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = []

    for partition in get_partitions(cows):
        valid_trips = 0
        for trip in partition:
            if (not is_trip_valid(cows, trip, limit)):
                break

            valid_trips += 1

            if len(partition) == valid_trips:
                return partition

def is_trip_valid (cows, trip, limit):
    '''
    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    trip - a list with cows in the trip
    limit - weight limit of the spaceship (an int)
    
    Returns:
    Boolean - True if trip is under weight limit and false otherwise
    '''
    total_weight = 0

    for cow in trip:
        total_weight += cows[cow]
    
    return total_weight < limit
     
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows('ps1_cow_data.txt')

    start = time.time()
    greedy = greedy_cow_transport(cows)
    end = time.time()

    greedy_time = end - start

    print("Number of trips in Greedy algorithm: " + str(len(greedy)))
    print("Time spent: " + str(greedy_time))
    
    start = time.time()
    brute_force = brute_force_cow_transport(cows)
    end = time.time()

    brute_force_time = end - start

    print("Number of trips in Brute Force algorithm: " + str(len(brute_force)))
    print("Time spent: " + str(brute_force_time))

if __name__ == '__main__':
    compare_cow_transport_algorithms()