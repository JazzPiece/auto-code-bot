import random

def generate_keypair():
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_e(phi):
        while True:
            e = random.randrange(2, phi)
            if is_prime(e) and phi % e != 0:
                return e

    def find_d(phi, e):
        for d in range(1, phi):
            if (e * d) % phi == 1:
                return d

    p = random.choice([i for i in range(2, 100) if is_prime(i)])
    q = random.choice([i for i in range(2, 100) if is_prime(i)])
    n = p * q
    phi = (p - 1) * (q - 1)
    e = find_e(phi)
    d = find_d(phi, e)
    
    return ((e, n), (d, n))

public_key, private_key = generate_keypair()
print("Public key:", public_key)
print("Private key:", private_key)