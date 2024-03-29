# ulam-hex-spiral
Ulam hexagon spiral in python

I created a variation of the ulam spiral and made it a hexagon with 3 axii.  The primes consistently only appear on the radii that have 5 and 7. I modified the routine to determine if a number is prime by adding a check for the final digit and if it is 5 skip it, and also a check before setting a square root value for the modulo of 6 being 1 or 5 because it does seem that all primes may adhere to that pattern.  I'm trying to check for other patterns in the primes now.

The t version uses an initial list of prime values up to 5,000. If the square root value is higher than that, the routine will add new prime values under that to the list and print them out at the end of the processing.  The check for primes won't be on every number below the square root but will only be the prime numbers.

In the t run, I happened to notice that at least one number was identified as a prime, but didn't appear in the hex drawing.  To avoid a crunch of numbers in the center, I tossed out a few values so that seems to be why it did appear.  I tested the routine and started with a lower number and the number appeared in blue in the hex pattern.

I removed my t version and I think I fixed the issues in the tx version.  Will continue to check and try to improve this.

I may go back eventually and clean up my main program.  The initial positioning could probably be optimized because I was just hastily trying to get a good hexagon, and didn't worry about the start as long as it was working for the end result.  I'm sure I could do a lot more like naming variables better.

In the ulam_primes, I was creating lists of primes and the composites in the 5 and 7 radii lines.  That actually processed quickly so I checked the prime numbers it generated against the list of primes up to 1000 on wikipedia and it looks like those are all correct, so that may actually be a quicker method but I'll still try to check it.  I basically just passed in a number of times to loop and a value to add, and the routine just multiplied the first value by 6 and then added the second.

I modifed the method I used to obtain prime numbers in ulamprimes2.py.  That just uses multiples of 6 and either adds or subtracts 1 to attempt that as a prime value.  I need to change the area where the iteration between 2 and the value of the square root is done to use just the list of prime numbers, and I will do that in a different version.

ulam_n1 - This replaces what I tried with ulam_tx version.  I used lambda function to replace some of the defined functions, used an *arg to enable an optional parameter on a function to enable it to skip some lines when it runs for a different condition.  This routine generates prime numbers within the user defined ranges entered at the start.  Adds values to list - slistp that starts with a list of primes up to 100.  This routine will also add any new primes that are within the square root value of the prime range.  Need to test changing the lists to sets because this routine really seems to slow when larger groupings are used.  If you use some of the things I did in a different language, you might not run into the same lag problems as some of the python uses do.  So far, for loops and lists are on my list of the not so great things in python.

ulam_nt - Changed most of the lists to sets to see if the routine would run quicker.  Will keep trying to use different containers to determine which might be the best for this routine.  Also, instead of printing the lists to the screen, writes out a file with a name in the format of ulam_nt_[date]_[time].txt.

Added prime_form to show python-esk code for a complex formula to reliably identify prime numbers that I found as a youtube video.

Ulam_nt1 - a version I worked on to see if it would run faster.  I think it actually ran a minute slower for a range based on my childhood phone number 8169319011 to 1000.  I think this version took 15 minutes and the old nt version took 13-14 minutes.  I'll try to compare the differences.


