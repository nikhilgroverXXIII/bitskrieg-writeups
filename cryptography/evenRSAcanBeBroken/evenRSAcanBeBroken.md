# evenRSAcanBeBroken

## Approach
On connecting to the program using netcat, we obtain the values of n,e and the ciphertext. On inspecting the python file given to us, we realize that we need to find the 2 primes p and q such that p*q=n. On looking closer, I found that n is an even number, so one of the primes is 2 and the other prime is n/2. 

## Solution
Since p = 2 and q = n/2, p-1 = 1. So phi = q. On writing a python script to solve for the message in decimal form to reverse the RSA encryption, we obtain the flag in decimal form. Then i just asked claude to convert it into hex and then into ASCII values to obtain the flag.

## Flag
academy{tw0_1$_pr!m39cf1fb4f}

## Takeway
RSA encryption can be broken if we know the 2 primes which constitute n.
