
def SieveOfEratosthenes(num): 

    p = 2

    while (p * p <= num): 

        p = sieve(p)

 
    # Print all prime numbers
    for p in range(2, num+1):
       if prime[p]:
           plist.append(p)
           #print(p)


def sieve(p):

    # If prime[p] is not
    # changed, then it is a prime
    if (prime[p] == True):
 
        # Updating all multiples of p
        # set may be more efficient
        for i in range(p * p, num+1, p):
            prime[i] = False
    p += 1
    return p

           
##############
print("Enter number:")
num = int(input())

#list for storing result prime values from activity
plist = []

#boolean array
prime = [True for i in range(num+1)]

SieveOfEratosthenes(num)

print(plist)
