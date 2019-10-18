import sys


def h_ascii(key, N):
    """ Computes hash value by summing the ascii value of each character
        in the key string

        Parameters
        __________
        key : str
            the string being used to calculate hash value
        N : int
            desired size of hash

        Returns
        _______
        int
            the hash value of the key

        Raises
        ______
        TypeError
            Occurs when either key or N are not of the proper type
        ZeroDivisionError
            Occurs when N is zero and mod cannot be computed
    """

    if not isinstance(key, str):
        raise TypeError('key is not a string')
        sys.exit(1)

    if not isinstance(N, int):
        raise TypeError('N is not an integer')
        sys.exit(1)

    sum = 0
    for char in key:
        sum += ord(char)

    try:
        return sum % N
    except ZeroDivisionError:
        raise ZeroDivisionError('N cannot be zero')
        sys.exit(1)


def h_rolling(key, N, p=53, m=2**64):
    """ Computes hash value by using the polynomial hash algorithm

        Parameters
        __________
        key : str
            the string being used to calculate hash value
        N : int
            desired size of hash

        Returns
        _______
        int
            the hash value of the key

        Raises
        ______
        TypeError
            Occurs when either key or N are not of the proper type
        ZeroDivisionError
            Occurs when N is zero and mod cannot be computed
    """

    if not isinstance(key, str):
        raise TypeError('key is not a string')
        sys.exit(1)

    if not isinstance(N, int):
        raise TypeError('N is not an integer')
        sys.exit(1)

    sum = 0
    for i in range(len(key)):
        sum += ord(key[i]) * p**i
    sum = sum % m

    try:
        return sum % N
    except ZeroDivisionError:
        raise ZeroDivisionError('N cannot be zero')
        sys.exit(1)


def h_hasCode(key, N):
    """ Computes hash value by summing the ascii value of each character
        in the key string multiplied by descending powers of 31

        * algorithm found at :
        https://www.cs.cmu.edu/~adamchik/15-121/lectures/Hashing/hashing.html

        Parameters
        __________
        key : str
            the string being used to calculate hash value
        N : int
            desired size of hash

        Returns
        _______
        int
            the hash value of the key

        Raises
        ______
        TypeError
            Occurs when either key or N are not of the proper type
        ZeroDivisionError
            Occurs when N is zero and mod cannot be computed
    """

    if not isinstance(key, str):
        raise TypeError('key is not a string')
        sys.exit(1)

    if not isinstance(N, int):
        raise TypeError('N is not an integer')
        sys.exit(1)

    sum = 0
    n = len(key)
    for char in key:
        sum += ord(char) * 31**n
        n -= 1

    try:
        return sum % N
    except ZeroDivisionError:
        raise ZeroDivisionError('N cannot be zero')
        sys.exit(1)
