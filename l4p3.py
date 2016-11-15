def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    n = float(len(L))
    if n == 0:
        return float('NaN')
    lengths = [len(str) for str in L]
    mean = sum(lengths) / n
    squaredDev = [(l - mean) ** 2 for l in lengths]
    variance = sum(squaredDev) / n
    return variance ** 0.5

def stdDev(nums):
    n = float(len(nums))
    if n == 0:
        return float('NaN')
    mean = sum(nums) / n
    if mean == 0:
        return float('NaN')
    squaredDev = [(num - mean) ** 2 for num in nums]
    variance = sum(squaredDev) / n
    stdDev = variance ** 0.5
    covariance = stdDev / mean
    return covariance

nums = [10, 4, 12, 15, 20, 5]
print stdDev(nums)
