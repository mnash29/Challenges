"""Problem #1408 [Hard]

Given a list, sort it using this method: reverse(lst, i, j),
which reverses lst from i to j.
"""
import random

def reverse(lst, i, j) -> list:
    """Reverse list from i to j

    Args
    ----
    lst : list
        The list to reverse
    i : int
        The starting index
    j : int
        The ending index

    Returns
    -------
    list
        The list with reversed section
    """
    if not lst or len(lst) == 0:
        return lst

    lst[i:j+1] = lst[j:i-1:-1]

    return lst

sample = random.sample(range(10, 30), 10)
print("Reversing: ", sample)
reversed = reverse(sample, 2, 6)
print("Output: ", reversed)