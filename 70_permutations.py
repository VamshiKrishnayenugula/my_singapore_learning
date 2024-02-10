"""Permutations of a string are different orders in which we can 
arrange the elements of the string. For example, given an "ABC" 
string, we can rearrange it into ["ABC," "ACB," "BAC," "BCA," 
"CAB," "CBA."]. In Python, the easiest way to find permutations 
of a string is to use itertools. Itertools has a permutation class. 
Here is how we can do it, using itertools."""

from itertools import permutations

def get_per(s):
    permu =[]

    for i in permutations(s):
        permu.append(''.join(i))

    return permu

print(get_per('abc'))