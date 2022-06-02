# ulam-hex-spiral
Ulam hexagon spiral in python

I created a variation of the ulam spiral and made it a hexagon with 3 axii.  The primes consistently only appear on the radii that have 5 and 7. I modified the routine to determine if a number is prime by adding a check for the final digit and if it is 5 skip it, and also a check before setting a square root value for the modulo of 6 being 1 or 5 because it does seem that all primes may adhere to that pattern.  I'm trying to check for other patterns in the primes now.

The _t version uses an initial list of prime values up to 5,000. If the square root value is higher than that, the routine will add new prime values under that to the list and print them out at the end of the processing.  The check for primes won't be on every number below the square root but will only be the prime numbers.

In the _t run, I happened to notice that at least one number was identified as a prime, but didn't appear in the hex drawing.  To avoid a crunch of numbers in the center, I tossed out a few values so that seems to be why it did appear.  I tested the routine and started with a lower number and the number appeared in blue in the hex pattern.
