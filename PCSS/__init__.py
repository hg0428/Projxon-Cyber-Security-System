from passlib.hash import pbkdf2_sha512
from passlib.utils.binary import ab64_decode
from uuid import uuid4, uuid5, uuid1
import hashlib
import random
import time
from bitarray import bitarray
from typing import Union
from .util import to_bitarray

makeid = lambda: hashlib.sha256(
  str(random.randint(-2**512, 2**512 + time.time())).encode()).hexdigest(
  ) + hashlib.sha512(str(uuid1()).encode()).hexdigest() + str(uuid4()) + str(
    uuid5(uuid4(), str(uuid1())))


def process_key(key: Union[str, bytes, bitarray, int, None],
                salt=None,
                rounds=None) -> bitarray:
  """
  Process a key for encryption or decryption
  """
  key = to_bitarray(key)
  final_key = bitarray()
  if rounds == None:
    rounds = (int(key[:15].to01(), 2) + 100) * 2
  x = pbkdf2_sha512.hash(key.tobytes(),
                         rounds=rounds,
                         salt=salt if salt else key.tobytes()).split('$')[-1]
  final_key.frombytes(ab64_decode(x))
  return final_key


def encrypt(data: Union[str, bytes, bitarray, int],
            key: Union[str, bytes, bitarray, int, None] = None,
            final_key: Union[bitarray, None] = None,
            rounds=None,
            salt=None) -> bitarray:
  """
  Encrypts data using an advanced method including XOR encrytion and byte and bit reversal.
  `salt` will defualt to the key.
  """
  data = to_bitarray(data)
  if final_key == None:
    if key == None:
      raise ValueError("Either key OR final_key must be provided.")
    else:
      key = to_bitarray(key)
      final_key = process_key(key, salt, rounds)
  if len(final_key) > len(data):
    final_key = final_key[-len(data):]
  while len(final_key) < len(data):
    final_key += final_key[:max(len(data) - len(final_key), len(final_key))]
  data ^= final_key
  data.bytereverse()
  data.reverse()
  return data


def decrypt(encrypted_data: Union[str, bytes, bitarray, int],
            key: Union[str, bytes, bitarray, int, None] = None,
            final_key: Union[bitarray, None] = None,
            rounds=None,
            salt=None) -> bitarray:
  """
  Decrypts data that was encrypted using the PCSS.encrypt function. Parameters that do not match will generate an incorrect output.
  """
  encrypted_data = to_bitarray(encrypted_data)
  if final_key == None:
    if key == None:
      raise ValueError("Either key OR final_key must be provided.")
    else:
      key = to_bitarray(key)
    if rounds == None:
      rounds = (int(key[:15].to01(), 2) + 100) * 2
    final_key = process_key(key, salt, rounds)
  encrypted_data.reverse()
  encrypted_data.bytereverse()
  if len(final_key) > len(encrypted_data):
    final_key = final_key[-len(encrypted_data):]
  while len(final_key) < len(encrypted_data):
    final_key += final_key[:max(
      len(encrypted_data) - len(final_key), len(final_key))]
  encrypted_data ^= final_key
  return encrypted_data


def bitarray_to_text(data: bitarray) -> str:
  """
  Converts a bitarray to a string.
  """
  return data.tobytes().rstrip(b'\x00').decode()


# x = encrypt('hiiiiiii'.encode(), ''.encode())
# print(x, decrypt(x, ''.encode()).tobytes().decode())
