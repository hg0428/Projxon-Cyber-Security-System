from passlib.hash import pbkdf2_sha512
from uuid import uuid4, uuid5, uuid1
import hashlib
import random
import time
from bitarray import bitarray

makeid = lambda: hashlib.sha256(
    str(
        random.randint(-999999999999999999999, 999999999999999999999 + time.
                       time())).encode()).hexdigest() + hashlib.sha512(
                           str(uuid1()).encode()).hexdigest() + str(uuid4(
                           )) + str(uuid5(uuid4(), str(uuid1())))


def fill(data: bitarray, length: int) -> bitarray:
    data.extend([0] * (length - len(data)))
    return data


def encrypt(ba, key) -> bitarray:
    if type(ba) == bytes:
        x = bitarray()
        x.frombytes(ba)
        ba = x
    elif type(ba) != bitarray:
        raise TypeError("`ba` must be a bitarray or bytes-like object.")
    if type(key) == bytes:
        x = bitarray()
        x.frombytes(key)
        key = x
    elif type(key) != bitarray:
        raise TypeError("`key` must be a bitarray or bytes-like object.")
    ukey = bitarray()
    ukey.frombytes(
        pbkdf2_sha512.hash(key.tobytes(), rounds=65539,
                           salt=key.tobytes()).encode())
    m = max(len(ba), len(ukey))
    ba = (fill(ba, m) ^ fill(ukey, m))
    ba.bytereverse()
    return ba


def decrypt(encrypted_ba, key) -> bitarray:
    if type(encrypted_ba) == bytes:
        x = bitarray()
        x.frombytes(encrypted_ba)
        encrypted_ba = x
    elif type(encrypted_ba) != bitarray:
        raise TypeError(
            "`encrypted_ba` must be a bitarray or bytes-like object.")
    if type(key) == bytes:
        x = bitarray()
        x.frombytes(key)
        key = x
    elif type(key) != bitarray:
        raise TypeError("`key` must be a bitarray or bytes-like object.")
    ukey = bitarray()
    ukey.frombytes(
        pbkdf2_sha512.hash(key.tobytes(), rounds=65539,
                           salt=key.tobytes()).encode())
    encrypted_ba.bytereverse()
    m = max(len(encrypted_ba), len(ukey))
    encrypted_ba = (fill(encrypted_ba, m) ^ fill(ukey, m))
    return encrypted_ba


# x = bitarray([0] * (32 * 30)).tobytes().decode()
# print(x, len(x))
# x = encrypt('hiiiiiii'.encode(), ''.encode())
# print(x, decrypt(x, ''.encode()).tobytes().decode())
