from passlib.hash import pbkdf2_sha512
from uuid import uuid4, uuid5, uuid1
import hashlib
import random
import time
from bitarray import bitarray

makeid = lambda: hashlib.sha256(str(
        random.randint(-999999999999999999999, 999999999999999999999 + time.
                       time())).encode()
).hexdigest() + hashlib.sha512(str(uuid1()).encode()).hexdigest(
) + str(uuid4()) + str(uuid5(uuid4(), str(uuid1())))


def fill(data, length):
    data.extend([0] * (length - len(data)))
    return data


def encrypt(ba, key):
    if type(ba) != bitarray:
        x = bitarray()
        x.frombytes(ba)
        ba = x
    if type(key) != bitarray:
        x = bitarray()
        x.frombytes(key)
        key = x
    ukey = bitarray()
    ukey.frombytes(
        pbkdf2_sha512.hash(key.tobytes(), rounds=65539,
                           salt=key.tobytes()).encode())
    m = max(len(ba), len(ukey))
    ba = (fill(ba, m) ^ fill(ukey, m))
    ba.bytereverse()
    return ba


def decrypt(encrypted_ba, key):
    if type(encrypted_ba) != bitarray:
        x = bitarray()
        x.frombytes(encrypted_ba)
        encrypted_ba = x
    if type(key) != bitarray:
        x = bitarray()
        x.frombytes(key)
        key = x
    ukey = bitarray()
    ukey.frombytes(
        pbkdf2_sha512.hash(key.tobytes(), rounds=65539,
                           salt=key.tobytes()).encode())
    encrypted_ba.bytereverse()
    m = max(len(encrypted_ba), len(ukey))
    encrypted_ba = (fill(encrypted_ba, m) ^ fill(ukey, m))
    return encrypted_ba


x = bitarray([0] * (32 * 30)).tobytes().decode()
print(x, len(x))
x = encrypt('hiiiiiii'.encode(), ''.encode())
print(x, decrypt(x, ''.encode()).tobytes().decode())
