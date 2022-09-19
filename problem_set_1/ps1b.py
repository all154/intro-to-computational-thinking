###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Aloisio Valério
# Collaborators:
# Time: 1h30
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    max_weight = egg_weights[len(egg_weights) - 1]

    if target_weight < egg_weights[1]:
        return target_weight
    try:
        return memo[target_weight]
    except KeyError:
        for i in range(len(egg_weights)):
            if target_weight < egg_weights[i]:
                number_of_larger_eggs = int(target_weight/egg_weights[i-1])
                result = number_of_larger_eggs +\
                    dp_make_weight(egg_weights, target_weight - number_of_larger_eggs * egg_weights[i-1], memo)
                memo[target_weight] = result
                return result
        
        if target_weight >= max_weight:
            number_of_larger_eggs = int(target_weight/max_weight)
            result = number_of_larger_eggs +\
                dp_make_weight(egg_weights, target_weight - number_of_larger_eggs * max_weight, memo)
            memo[target_weight] = result
            return result
            

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected output: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    weights = [75, 65, 150, 32, 95, 427, 54, 121]

    for weight in weights:
        n = weight
        print("n = " + str(weight))
        print("Actual output:", dp_make_weight(egg_weights, n))
        print()

