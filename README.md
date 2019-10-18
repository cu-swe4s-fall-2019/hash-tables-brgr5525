# Hash tables

## hash functions
- h_ascii : sums the ascii values of the characters in the key
- h_rolling : calculates the hash value following the polynomial rolling hash
    algorithm
- h_hasCode : similar to h_ascii, but also multiplies the ascii value of
    each character by decreasing powers of 31 before summing

## hash tables
- LinearProbe : will look for the next open slot when a collision occurs
- QuadraticProbe : instead of looking at each additional slot to place the
    value, will look at the slots in powers of 2
    ex. when the first collision occurs it will check the initial hash plus
        1^2, then it will look at 2^2 and so on
- ChainedHash : will simply create a list at each slot that contains every
    value that was hashed to that location
