# Will Martin
# 7-7-2020
# encryption

import random
import math

# basic example of RSA encryption
# works for integers with digits up to ~5

# TODO: expand encryption beyond one integer
# user input for number to encrypt
m_encrypted = int(input("Number to encrypt: "))
m_bits = m_encrypted.bit_length()

# arbitrarily making bit length n > m
n_bits = m_bits + 2


# TODO: simplify generation of p and q
# https://www.di-mgt.com.au/rsa_alg.html
rand = (random.getrandbits(math.ceil(n_bits/2)))
if (rand % 2) == 0:
    rand = rand + 1

p = None
q = None

while p is None:
    for i in range(2, rand):
        if (rand % i) == 0:
            # rand is not prime
            rand += 2
            break
    else:
        # rand is prime
        p = rand

rand = (random.getrandbits(math.ceil(n_bits/2)))
if (rand % 2) == 0:
    rand = rand + 1

while q is None:
    if rand > 1:
        for i in range(2, rand):
            if (rand % i) == 0:
                # rand is not prime
                rand += 2
                break
        else:
            # rand is prime
            q = rand
            if q == p:
                q = None
                rand += 2
    else:
        rand += 2

# p = 61
# q = 53

print("p = " + str(p))
print("q = " + str(q))

n = p*q

z = (p-1)*(q-1)

# choose e
# 1 < e < z and e is co-prime to z
# common choices: 3, 5, 17, 257, 65537(2^16 + 1)
e = 17

# calculate d using Extended Euclidean Algorithm
# d = (1/e) mod z or ed = 1 mod z
# for more info see:
# https://www.di-mgt.com.au/rsa_alg.html
# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
e = e % z
for d in range(1, z):
    if (e * d) % z == 1:
        break

# print public and private keys
print("public key: (" + str(n) + ", " + str(e) + ")")
print("private key: (" + str(n) + ", " + str(d) + ")")

# encryption
c = (m_encrypted**e) % n
print("Encrypted message: " + str(c))

# decryption
# fails when when m_encrypted digits ~>5
# most likely caused by very large numbers calculated below
m_decrypted = (c**d) % n

if m_decrypted == m_encrypted:
    print("Success")
else:
    print("Failed")
