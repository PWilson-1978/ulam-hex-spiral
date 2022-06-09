# ulam-hex-spiral
Ulam hexagon spiral in python

I created a variation of the ulam spiral and made it a hexagon with 3 axii.  The primes consistently only appear on the radii that have 5 and 7. I modified the routine to determine if a number is prime by adding a check for the final digit and if it is 5 skip it, and also a check before setting a square root value for the modulo of 6 being 1 or 5 because it does seem that all primes may adhere to that pattern.  I'm trying to check for other patterns in the primes now.

The t version uses an initial list of prime values up to 5,000. If the square root value is higher than that, the routine will add new prime values under that to the list and print them out at the end of the processing.  The check for primes won't be on every number below the square root but will only be the prime numbers.

In the t run, I happened to notice that at least one number was identified as a prime, but didn't appear in the hex drawing.  To avoid a crunch of numbers in the center, I tossed out a few values so that seems to be why it did appear.  I tested the routine and started with a lower number and the number appeared in blue in the hex pattern.

I removed my t version and I think I fixed the issues in the tx version.  Will continue to check and try to improve this.

I may go back eventually and clean up my main program.  The initial positioning could probably be optimized because I was just hastily trying to get a good hexagon, and didn't worry about the start as long as it was working for the end result.  I'm sure I could do a lot more like naming variables better.

In the ulam_primes, I was creating lists of primes and the composites in the 5 and 7 radii lines.  That actually processed quickly so I checked the prime numbers it generated against the list of primes up to 1000 on wikipedia and it looks like those are all correct, so that may actually be a quicker method but I'll still try to check it.  I basically just passed in a number of times to loop and a value to add, and the routine just multiplied the first value by 6 and then added the second.
