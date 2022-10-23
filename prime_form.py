# Python code
# from youtube video url https://www.youtube.com/watch?v=j5s0h42GfvM
# complex formula to identify prime number reliably

import math

def prime(n):
    return 1 + sum([
        math.floor(pow(n/sum([
            math.floor(pow(math.cos(math.pi * (math.factorial(j - 1) + 1)/j), 2))
            for j in range(1, i+1)
        ]), 1/n))
        for i in range(1, pow(2, n)+1)
    ])


'''
(* Mathematica code *)

prime[n_] := 1 + Sum[Floor[(n/Sum[Floor[Cos[Pi ((j - 1)! + 1)/j]^2], {j, 1, i}])^(1/n)], {i, 1, 2^n}]
'''