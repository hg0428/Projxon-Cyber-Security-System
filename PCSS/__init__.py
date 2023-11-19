from passlib.hash import pbkdf2_sha512
from uuid import uuid4, uuid5, uuid1
import hashlib
import random
import time
from bitarray import bitarray
from typing import Union

makeid = lambda: hashlib.sha256(
  str(
    random.randint(-2**512, 2**512 + time.time())
  ).encode()).hexdigest() + hashlib.sha512(str(uuid1()).encode()).hexdigest(
  ) + str(uuid4()) + str(uuid5(uuid4(), str(uuid1())))


def fill(data: bitarray, length: int) -> bitarray:
  data.extend([0] * (length - len(data)))
  return data


def encrypt(data: Union[str, bytes, bitarray],
            key: Union[str, bytes, bitarray, None] = None,
            final_key: Union[bitarray, None] = None,
            rounds=None,
            salt=None) -> bitarray:
  """
  Encrypts data using an advanced method including XOR encrytion and byte and bit reversal.
  `salt` will defualt to the key.
  """
  if type(data) == bytes:
    x = bitarray()
    x.frombytes(data)
    data = x
  elif type(data) == str:
    x = bitarray()
    x.frombytes(data.encode())
    data = x
  elif type(data) != bitarray:
    raise TypeError("`data` must be a bitarray or bytes-like object.")
  if final_key == None:
    if key == None:
      raise ValueError("Either key OR final_key must be provided.")
    if type(key) == bytes:
      x = bitarray()
      x.frombytes(key)
      key = x
    elif type(key) == str:
      x = bitarray()
      x.frombytes(key.encode())
      key = x
    elif type(key) != bitarray:
      raise TypeError("`key` must be a bitarray or bytes-like object.")
    final_key = bitarray()
    if rounds == None:
      rounds = (int(key[:15].to01(), 2) + 100) * 2
    final_key.frombytes(
      pbkdf2_sha512.hash(key.tobytes(),
                         rounds=rounds,
                         salt=salt if salt else key.tobytes()).encode())
  if len(final_key) > len(data):
    final_key = final_key[-len(data):]
    #TODO: CHAGE THIS BECAUSE THIS DISREGARDS THE END, which is the most important. The rounds only seems to effect the end of it.
    # final_key = final_key[:len(data)]
  while len(final_key) < len(data):
    final_key += final_key[:max(len(data) - len(final_key), len(final_key))]
  data ^= final_key
  data.bytereverse()
  data.reverse()
  return data


def decrypt(encrypted_data: Union[str, bytes, bitarray],
            key: Union[str, bytes, bitarray, None] = None,
            final_key: Union[bitarray, None] = None,
            rounds=None,
            salt=None) -> bitarray:
  """
  Decrypts data that was encrypted using the PCSS.encrypt function. Parameters that do not match will generate an incorrect output.
  """
  if type(encrypted_data) == bytes:
    x = bitarray()
    x.frombytes(encrypted_data)
    encrypted_data = x
  elif type(encrypted_data) == str:
    x = bitarray()
    x.frombytes(encrypted_data.encode())
    encrypted_data = x
  elif type(encrypted_data) != bitarray:
    raise TypeError(
      "`encrypted_data` must be a bitarray or bytes-like object.")
  if final_key == None:
    if key == None:
      raise ValueError("Either key OR final_key must be provided.")
    if type(key) == bytes:
      x = bitarray()
      x.frombytes(key)
      key = x
    elif type(key) == str:
      x = bitarray()
      x.frombytes(key.encode())
      key = x
    elif type(key) != bitarray:
      raise TypeError("`key` must be a bitarray or bytes-like object.")
    if rounds == None:
      rounds = (int(key[:15].to01(), 2) + 100) * 2
    final_key = bitarray()
    final_key.frombytes(
      pbkdf2_sha512.hash(key.tobytes(),
                         rounds=rounds,
                         salt=salt if salt else key.tobytes()).encode())
  encrypted_data.reverse()
  encrypted_data.bytereverse()
  if len(final_key) > len(encrypted_data):
    final_key = final_key[-len(encrypted_data):]
    #TODO: CHAGE THIS BECAUSE THIS DISREGARDS THE END, which is the most important. The rounds only seems to effect the end of it.
    # final_key = final_key[:len(encrypted_data)]
  while len(final_key) < len(encrypted_data):
    final_key += final_key[:max(
      len(encrypted_data) - len(final_key), len(final_key))]
  encrypted_data ^= final_key
  return encrypted_data


def bitarray_to_text(data: bitarray) -> str:
  return data.tobytes().rstrip(b'\x00').decode()


# x = encrypt('hiiiiiii'.encode(), ''.encode())
# print(x, decrypt(x, ''.encode()).tobytes().decode())
