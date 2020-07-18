# 7-7-2020
# encryption

# basic example RSA

# TODO: randomly generate p and q
p = 61
q = 53

n = p*q

z = (p-1)*(q-1)

# TODO: calculate e
e = 17

# TODO: calculate d
d = 2753

print("public key: (" + str(n) + ", " + str(e) + ")")
print("private key: (" + str(n) + ", " + str(d) + ")")

# encryption
m_encrypted = 123
c = (m_encrypted**e) % n
print(c)

# decryption
m_decrypted = (c**d) % n

if m_decrypted == m_encrypted:
    print("Success")
else:
    print("Failed")
