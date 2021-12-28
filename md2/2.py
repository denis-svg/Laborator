from primes import getPrime


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def message_to_number(message):
    num = "299"
    for c in message:
        n = ord(c)
        if len(str(n)) == 3:
            num += str(n)
        elif len(str(n)) == 2:
            num += "0" + str(n)
        elif len(str(n)) == 1:
            num += "00" + str(n)
    return num


def number_to_message(num):
    s = ""
    for i in range(3, len(num) - 2, 3):
        c = chr(int(num[i] + num[i + 1] + num[i + 2]))
        s += c
    return s


def encrypt(message, e, n):
    return pow(message, e, n)


def decrypt(message, d, n):
    return pow(message, d, n)


message = input()
e = 65537
# e = 17
bits = 1024
p = getPrime(bits)
q = getPrime(bits)
fi = (p - 1) * (q - 1)
while gcd(fi, e) != 1:
    q = getPrime(bits)
    fi = (p - 1) * (q - 1)
n = q * p
d = pow(e, -1, fi)


print(f"""p = {p}\nq = {q}""")
print(f"""{message} = {int(message_to_number(message))}""")
print(f"""public keys {n, e}""")
print(f"""private keys {d}""")
cypher = encrypt(int(message_to_number(message)), e, n)
print(f"""encrypted message {cypher}\n                  {number_to_message(str(cypher))}""")
decrypted_cypher = decrypt(cypher, d, n)
print(f"""decrypted message {decrypted_cypher}\n                  {number_to_message(str(decrypted_cypher))}""")
