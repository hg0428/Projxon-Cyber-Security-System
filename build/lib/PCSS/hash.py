from bitarray import bitarray
from hashlib import sha256


def hash(data: str, length: int = 256) -> str:
  encoded = bitarray()
  encoded.frombytes(data.encode('utf-8'))
  blocks = [encoded[i:i + 4] for i in range(0, len(encoded), 4)]
  fourbits = [bitarray(4) for _ in range(length)]
  for index, i in enumerate(fourbits):
    for block in blocks:
      i ^= block
    x = bitarray(blocks[min(index, len(blocks) - 1)])
    x.reverse()
    i ^= ~x
    fourbits[index] = ~i
  return ''.join('{:x}'.format(int(i.to01(), 2)) for i in fourbits)
