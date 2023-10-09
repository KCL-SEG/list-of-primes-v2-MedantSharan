"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    nums = []
    isprime = []
    primes = []
    for i in range(999999):
        nums.append(i)
        isprime.append(True)
    for i in range(999999):
        if i==0 or i==1:
            continue
        else:
            if(isprime[i]):
                primes.append(nums[i])
                for j in range(2*i, 999999, i):
                    isprime[j] = False
            else:
                continue
    if number_of_primes <= 0:
        raise ValueError
    for i in range(number_of_primes):
        list.append(primes[i])

    return list
