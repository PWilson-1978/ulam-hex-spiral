# ulam-hex-spiral
Ulam hexagon spiral in python

I created a variation of the ulam spiral and made it a hexagon with 3 axii.  The primes consistently only appear on the radii that have 5 and 7. I modified the routine to determine if a number is prime by adding a check for the final digit and if it is 5 skip it, and also a check before setting a square root value for the modulo of 6 being 1 or 5 because it does seem that all primes may adhere to that pattern.  I'm trying to check for other patterns in the primes now.

The _t version of this routine opens and converts prime numbers up to 5,000 to a list and will append to the list in the processing.  Also, uses this list to iterate through the prime checking routine.  I've included the text file containing the prime values.
