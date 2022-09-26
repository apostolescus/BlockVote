from phe import paillier, EncryptedNumber
import json


def generate_keys():
    global pubkey, privkey, nsquare
    pubkey, privkey = paillier.generate_paillier_keypair(n_length=32)
    nsquare = pubkey.nsquare
    return (pubkey, privkey)


def get_nsquare():
    return nsquare


def decrypt(number):
    enc_add = EncryptedNumber(pubkey, number, exponent)
    results = privkey.decrypt(enc_add)
    return results


def encrypt(pubkey, number):
    global exponent
    encrypted = pubkey.encrypt(number)
    exponent = encrypted.exponent
    encrypted = encrypted.ciphertext(False)
    return encrypted


def add_numbers(num1, num2):
    add = (num1 * num2) % (nsquare)
    return add


def test():
    num1 = 0
    num2 = 0
    num3 = 1

    pub, priv = generate_keys()

    enc1 = encrypt(pub, num1)
    enc2 = encrypt(pub, num2)
    enc3 = encrypt(pub, num3)

    print(enc1)
    print(enc2)
    print(enc3)

    ad1 = add_numbers(enc1, enc2)
    ad2 = add_numbers(ad1, enc3)

    final = decrypt(ad2)
    print(final)


# test()
