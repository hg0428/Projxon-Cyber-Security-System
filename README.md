# What is it?
A fast and unbreakable encrytion system.
This library has 4 functions, `makeid`, `encrypt`, `decrypt`, and `bitarray_to_text`.

`makeid` will generate a long, virtually collision-proof identifier.

These tools can be very useful in login systems.

It also includes a (probably insecure) custom hash function in `PCSS.hash`.
# Installation
You can install it with pip.
`pip install Projxon-Cyber-Security-System`


# Usage

## Encyrpt and Decrypt
```py
from PCSS import encrypt, decrypt, makeid, bitarray_to_text
from PCSS.hash import hash

print(f"""
Hash of Hello_World!: {hash("Hello_World!")}
Hash of Hello_World! : {hash("Hello_World! ")}
Hash of Hello World: {hash("Hello World")}
Hash of Password#123: {hash("Password#123")}
Hash of AAAAAAAAAAAA: {hash("AAAAAAAAAAAA")}
Hash of !#!#!#!#!#!#!#!#: {hash("!#!#!#!#!#!#!#!#")}
""")
# Output:
"""
Hash of Hello_World!: 133e15fbd573507fd63714d032547698badcfe1032547698badcfe1032547698badcfe1032547698badcfe1032547698badcfe1032547698badcfe1032547698badcfe1032547698badcfe1032547698badcfe1032547698badcfe1032547698badcfe1032547698badcfe1032547698badcfe1032fe1032547698badcfe1032
Hash of Hello_World! : 6ac3ec8eac8ea90aafcaeda5832107654ba98fedc32107654ba98fedc32107654ba98fedc32107654ba98fedc32107654ba98fedc32107654ba98fedc32107654ba98fedc32107654ba98fedc32107654ba98fedc32107654ba98fedc32107654ba98fedc32107654ba9854ba98fedc32107654bfeecddc32107654ba98fedc3
Hash of Hello World: 026b0426c4c941a2c762056789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123ef0123456789abcdef0455766789abcdef012345182439abcdef01234567
Hash of Password#123: 7ad07a98bc5ffa9e967052b89efcd23016745ab89efcd23016745ab89efcd23016745ab89efcd23016745ab89efcd23016745ab89efcd23016745ab89efcd23016745ab89efcd23016745ab89efcd23016745ab89efcd2301cd23016745ab89efcd26775445ab89efcd2301673a061b89efcd230164f5bacd23016745ab89efb
Hash of AAAAAAAAAAAA: 4fa183e5c7290b6d4fa183e56789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789ab6789abcdef012345678cddfeef0123456789abcd90acb123456789abce5f106789abcdef0123d6e0f789abcdef01234567
Hash of !#!#!#!#!#!#!#!#: 5a781e34d2f096bc5a781e34d2f096bcdef89ab45670123cdef89ab45670123cdef89ab45670123cdef89ab45670123cdef89ab45670123cdef89ab45670123cdef23cdef89ab45670123c899baab45670123cdef89d4e8f5670123cdef8a1b5423cdef89ab456792a4b3cdef89ab456700d165ef89ab45670123cdef7067ccc
"""

# Encode it so that we have a bytes object to pass to encrypt
text = "Hello World!"
key = "key"
# Encode it so that we have a bytes object to pass to encrypt

encoded_text = text.encode()
encoded_key = key.encode()

# Encrypt the text
encrypted_bitarray = encrypt(encoded_text, encoded_key)
print(encrypted_bitarray)
print(bitarray_to_text(encrypted_bitarray))

# Decrypt the bitarray
decrypted_bitarray = decrypt(encrypted_bitarray, encoded_key)

# Convert it back to a string.
decrypted_text = bitarray_to_text(decrypted_bitarray)

print(decrypted_text, text == decrypted_text)
# Hello World! True

```


## Generate id
```py
from PCSS import makeid

print(makeid()) 
# 3fbe99d84c1b9255565c79d758bebba6e011ba2ca0795c5c50d22519adaf99050e74cb261933091fc4c52d6a7581c3681557e4adf495b1cd1314579e962791efc6d5ceb9133de75cd25a20a99d50cf4b7bf927f61dfa298d69d573da101f26a973241224-a5eb-49fa-828b-f86b89d9a4745480679b-4d20-5b8a-a72b-268877dc086a
# ids will vary.
```
These ids are garunteed to be unique, the chance of collision is about 1 / (2.42721841x10^229).
For refernce, the number of atoms in the universe is estimated to be 10^78.

