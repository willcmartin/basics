# Encryption

## Symmetric key cryptography:

- Sender and reciever use same key


## Public-key cryptography:

- Two keys:
    - public key (available to anyone)
    - private key (secret)
- Generated using one-way function

[RSA algorithm] (https://www.quora.com/How-do-you-generate-a-public-and-private-key):
1. Choose large prime numbers p and q (larger = more robust)
2. n = pq and z=(p-1)(q-1)
3. Choose e: e < n, gcd(e,z) = 1 (greatest common divisor = 1),
e and z are prime numbers
4. ed % z = 1 (ed-1 is exactly divisible by z)
5. public key = (n,e), private key = (n, d) 