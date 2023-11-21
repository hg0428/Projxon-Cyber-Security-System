from PCSS import encrypt, decrypt, makeid, bitarray_to_text
from PCSS.hash import hash

print(f"""
Hash of Hi!: {hash("Hi!", 256)}
Hash of Hello_World!: {hash("Hello_World!", length=256)}
Hash of Hello_World! : {hash("Hello_World! ", length=256)}
Hash of Hello World: {hash("Hello World", length=256)}
Hash of Password#123: {hash("Password#123", length=256)}
Hash of AAAAAAAAAAAA: {hash("AAAAAAAAAAAA", length=256)}
Hash of AAAAAAAAAAAB: {hash("AAAAAAAAAAAB", length=256)}
Hash of !#!#!#!#!#!#!#!#: {hash("!#!#!#!#!#!#!#!#", length=256)}
""")

# Output:
"""
Hash of Hi!: 293bcd0b497216b999a7e81e2b7cd7530017f44dd53472710d2b44bfea670227
Hash of Hello_World!: 23c5fc4b5f59a9ebb20c3a88de653214fba07b382c4e0acfe09b76e6b0073cf3
Hash of Hello_World! : 74d6ae99037683397fadda7da65afa72c0560d6e64319d0c86abe2301b46146d
Hash of Hello World: cc65180fbca2636fd269c3830dfc3903679f394d10a233ceae9bf9ac5c26a177
Hash of Password#123: 491d11b7e30323855c9c8fe742c947ee9c4f718f602b0275620bf9c4937dbd1a
Hash of AAAAAAAAAAAA: 4f14559045890891b74ec030af9d4530097aedd29ed850444b74bc2559730180
Hash of AAAAAAAAAAAB: 54314d9b51864195a0d4c7f2e0c3b1d623554a6c68d0a40593430b526e982b29
Hash of !#!#!#!#!#!#!#!#: b3ff1bf0a9f3411e4ce8b95cabbb352d34eb42a7640b67a366f2044daee68235
"""
x = 'Hello Everyone!'
print('Hash works?', hash(x) == hash(x))  # True

## Encryption

text = "Hello World!"
key = "key"

# Encrypt the text
encrypted_bitarray = encrypt(text, key)
print(encrypted_bitarray)

# Decrypt the bitarray
decrypted_bitarray = decrypt(encrypted_bitarray, key)

# Convert it back to a string.
decrypted_text = bitarray_to_text(decrypted_bitarray)

print(decrypted_text, text == decrypted_text)
# Hello World! True

print(makeid())
# 3fbe99d84c1b9255565c79d758bebba6e011ba2ca0795c5c50d22519adaf99050e74cb261933091fc4c52d6a7581c3681557e4adf495b1cd1314579e962791efc6d5ceb9133de75cd25a20a99d50cf4b7bf927f61dfa298d69d573da101f26a973241224-a5eb-49fa-828b-f86b89d9a4745480679b-4d20-5b8a-a72b-268877dc086a
# ids will vary.
