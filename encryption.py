# 7-7-2020
# encryption

# basic example RSA

# TODO: randomly generate p and q
p = 61
q = 53

n = p*q

z = (p-1)*(q-1)

# 1 < e < z and e is co-prime to z
# common choices: 3, 5, 17, 257, 65537(2^16 + 1)
e = 17

# calculate d using Extended Euclidean Algorithm
# d = (1/e) mod z or ed = 1 mod z
# for more info see:
# https://www.di-mgt.com.au/rsa_alg.html
# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
e = e % z
for d in range(1, z) :
    if (e * d) % z == 1:
        break

# print public and private keys
print("public key: (" + str(n) + ", " + str(e) + ")")
print("private key: (" + str(n) + ", " + str(d) + ")")

# encryption
m_encrypted = 123
c = (m_encrypted**e) % n
print("Encrypted message" + str(c))

# decryption
m_decrypted = (c**d) % n

if m_decrypted == m_encrypted:
    print("Success")
else:
    print("Failed")
