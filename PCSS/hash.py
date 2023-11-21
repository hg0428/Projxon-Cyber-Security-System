from bitarray import bitarray
from bitarray.util import int2ba
from random import shuffle, seed, randint
import base64
from typing import Union
from .util import to_bitarray, merge_bitarrays, pad_bitarray_left, split_bitarray
import math


def hash(data: Union[str, int, bitarray, bytes],
         length: int = 256,
         block_size: int = 2,
         affected_area: int = 0.5,
         output: str = "hex") -> Union[bitarray, str, int, bytes]:
  """
  Hashes data using the hashing PCSS algorithm.
The length of the hash is supplied as the length arguemnt and it must be divisible by the block size (which defaults to 4).
An increased block size results in increased randomness.

`affected_area` is the number of input blocks used in the output block calculation. If it is an integer, it represents a concrete value, and if it is between 0 and 1 it is proportional to the number of blocks. This value is very particular, be careful!

Output can be "hex", "bitarray", "bytes", "base64", "base64-bytes", or "int".
  """
  if length % block_size != 0:
    raise ValueError("Length must be a multiple of block_size")
  encoded = to_bitarray(data)
  hash_data = [encoded, int2ba(length), int2ba(encoded.count(1))]
  blocks = []
  for x in hash_data:
    blocks = blocks + split_bitarray(x, block_size)
  emptyblocks = [bitarray(block_size) for _ in range(int(length / block_size))]
  seed((affected_area + (length + block_size) * int(blocks[0].to01(), 2)) *
       int(blocks[-1].to01(), 2) + int(encoded.to01(), 2))
  if affected_area > 0 and affected_area < 1:
    affected_area = math.floor(affected_area * len(blocks))
  for index, i in enumerate(emptyblocks):
    i.setall(0)
    shuffle(blocks)
    x = randint(0, len(blocks) - affected_area - 1)
    for block in blocks[x:x + affected_area]:
      i ^= block
    x = bitarray(blocks[min(index, len(blocks) - 1)])
    x.reverse()
    i ^= ~x
    emptyblocks[index] = ~i
  merged = merge_bitarrays(*emptyblocks)
  if output == "hex":
    return ''.join('{:x}'.format(int(i.to01(), 2))
                   for i in split_bitarray(merged, 4))
  elif output == 'bitarray':
    return merged
  elif output == 'bytes':
    return merged.tobytes()
  elif output == 'base64':
    return base64.b64encode(merged.tobytes()).decode('utf-8')
  elif output == 'base64-bytes':
    return base64.b64encode(merged.tobytes())
  elif output == 'int':
    return int(merged.to01(), 2)
