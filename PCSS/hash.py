from bitarray import bitarray
from bitarray.util import int2ba
from hashlib import sha256
from random import shuffle, seed


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


def hash(data: str, length: int = 256, block_size: int = 4) -> str:
  """
  Hashes data using the hashing PCSS algorithm.
  The length of the hash is supplied as the length arguemnt and it must be divisible by the block size (which defaults to 4).
  An increased block size results in increased randomness.
  """
  if length % block_size != 0:
    raise ValueError("Length must be a multiple of block_size")
  encoded = bitarray()
  encoded.frombytes(data.encode('utf-8'))
  hash_data = [
    encoded,
    int2ba(len(data)),
    int2ba(length),
    int2ba(encoded.count(1))
  ]
  blocks = []
  for x in hash_data:
    blocks = blocks + split_bitarray(x, block_size)
  emptyblocks = [bitarray(block_size) for _ in range(length)]
  seed((length + block_size + len(data)) * int(blocks[0].to01(), 2))
  for index, i in enumerate(emptyblocks):
    i.setall(0)
    shuffle(blocks)
    for block in blocks:
      i ^= block
    x = bitarray(blocks[min(index, len(blocks) - 1)])
    x.reverse()
    i ^= ~x
    emptyblocks[index] = ~i
  return ''.join('{:x}'.format(int(i.to01(), 2))
                 for i in split_bitarray(merge_bitarrays(*emptyblocks), 4))
