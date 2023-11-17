from bitarray import bitarray

def hash(data: str, length: int) -> str:
  encoded = [ord(c) for c in data]
  bytes = [0 for _ in range(length)]
  for i in bytes:
    for byte in encoded:
      i ^= byte
    