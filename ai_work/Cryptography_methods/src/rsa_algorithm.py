def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi:
        if is_prime(e):
            break
        e += 1
    for d in range(1, phi):
        if (e * d) % phi == 1:
            break
    return ((e, n), (d, n))

p = 61
q = 53
public_key, private_key = generate_keypair(p, q)
print("Public key:", public_key)
print("Private key:", private_key)