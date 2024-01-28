from bitarray import bitarray
from typing import Union
from bitarray.util import int2ba


def to_bitarray(data: Union[str, bytes, bitarray, int]) -> bitarray:
  """
  Converts a string, bytes-like object, int, or bitarray to a bitarray.
  """
  if type(data) == bytes:
    x = bitarray()
    x.frombytes(data)
    return x
  elif type(data) == str:
    x = bitarray()
    x.frombytes(data.encode())
    return x
  elif type(data) == int:
    return int2ba(data)
  elif type(data) == bitarray:
    return data
  elif type(data) != bitarray:
    raise TypeError("`data` must be a bitarray or bytes-like object.")


def pad_bitarray_left(ba, size=4):
  # Calculate the number of bits to pad
  pad_size = size - len(ba)

  # Create a new bitarray for padding
  pad = bitarray(pad_size)
  pad.setall(0)

  # Prepend the padding to the original bitarray
  ba[:0] = pad
  return ba


def merge_bitarrays(*bitarrays):
  merged_bitarray = bitarray()

  # Extend the result bitarray with each bitarray in the list
  for ba in bitarrays:
    merged_bitarray.extend(ba)
  return merged_bitarray


def split_bitarray(ba, block_size=4):
  return [
    pad_bitarray_left(ba[i:i + block_size], block_size)
    for i in range(0, len(ba), block_size)
  ]