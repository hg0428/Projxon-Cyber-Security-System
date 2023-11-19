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
Hash of Hi!: {hash("Hi!")}
Hash of Hello_World!: {hash("Hello_World!")}
Hash of Hello_World! : {hash("Hello_World! ")}
Hash of Hello World: {hash("Hello World")}
Hash of Password#123: {hash("Password#123")}
Hash of AAAAAAAAAAAA: {hash("AAAAAAAAAAAA")}
Hash of !#!#!#!#!#!#!#!#: {hash("!#!#!#!#!#!#!#!#")}
""")
# Output:
"""
Hash of Hi!: 32aa253325323f2f7a22f52313272b77335b11b25327aab12772a3522522bf77322223233227222ff2ff3b33332a27252b3ff323127b2335ba752f2a1f3b22122b2b23522522af3f22f522a735f273112332f722b227f122b22111f22222532f75327172332271377a2ffb3322232ba22f3bf2223322f73ab12f52f52a1ab332
Hash of Hello_World!: 0c1c55cb50099c5305199d9500932925530517975755d00b20cc222909550305039275050005905205d7770530c5c0953d50cd9559155729c39101352395c7cc5971b700d925d3d5570500d1c725992c957d500b555950352521dd7b3c505d759d057377005550252b552335d0171071092dd5000959005d53c75170520c5297
Hash of Hello_World! : 117eb51b771a2557be7fbd710b2231e1e1775227ff13b217e551137e7f55977ddee73e70b0922232a21e773777bb1e155170150172b9713f7f273a3d32737db5ee29af755f75711fb7bf59729efadb12eff722177777e2725e2be7129055075050b55535270302e252213ef752d10b7772b7ba27e5772773732f1f7579777107
Hash of Hello World: d9ed49a56eea69bc42ce69e89c25bc828bee5d7ece576e6bbb76b94eee779e575daba4be8ece2e8899e2e2bec978b87d7d79a972225e246b687ede897bb556a7e6e8abaebaee6ee282eb45beee4ee5858a8e2e2bcbdbcb84ceee845ee565769cde5ee99958a296e9eee87d774ce82beb8eeaeedceeeb8ec4b8d929e88eebcbea
Hash of Password#123: acae4c46684ec4cefccce6c61c2e6c330fe4fcc8c12cec2004a4acaec3ea2c0448e8ee464ca2ceee6ca2eea62acaa230e6feccaeadcefeec2ee318ccc382ec6c4ecdee46e2cc664ece2eeaeee424c1eee6cece68e2e0e64ee46dfee8ceccc6eccfc26eecc6eeeceee28aa2a41c1f22ac63ee46660ec8c48c2e4ce6aecea4aeea
Hash of AAAAAAAAAAAA: b0a0aa00abba00a80a0aaa0a0b089a0aa8ba080aaaaa0bb00b00909a0aaa08ba0800aa0a000aa0a0baa8a00a8b0a000a80ab0a0aaa0aa09a08a00a8a98aa0000aa0a0abbaa0a080aaaba0b000a0aaa90aaa0ab00aaaaab8a9a90aaa080a0aaaaaa0aa88ab0aaa09a90aa088aa0a0a0aa0a00aa00baaab0aaa808a0aba000a008
Hash of !#!#!#!#!#!#!#!#: beab626ee6e6b66e666bbea622ae26622efafaee2e2b6ae66eeeeeee22ae6626aea62beeee26eefb222ee622ea6eee66ea66e2ee22e6a66e2ae2666f6ee6fee6e2eeb6226622e2a6e2ebf666ee62a2bb2eeeee6a26eee6e2eeeee262ae2e6afa66e2eee6e66e62e626e2aa22ebbea6ee26e6a2abbe26eee62226eeee6a6b6e62
"""
x = 'Hello Everyone!'
print('Hash works?', hash(x) == hash(x))  # True

## Encryption

text = "Hello World!"
key = "key"

# Encrypt the text
encrypted_bitarray = encrypt(text, key)
print(encrypted_bitarray)
print(bitarray_to_text(encrypted_bitarray))

# Decrypt the bitarray
decrypted_bitarray = decrypt(encrypted_bitarray, key)

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
These ids are garunteed to be unique; the chance of collision is about 1 / (2.42721841x10^229).
For reference, the number of atoms in the universe is estimated to be 10^78.


# Documentation:
## PCSS
### `encrypt(data: Union[str, bytes, bitarray], key: Union[str, bytes, bitarray, None]=None, final_key: Union[bitarray, None]=None, rounds=None, salt=None) -> bitarray`
Encrypts data using an advanced method including XOR encrytion and byte and bit reversal.
`salt` will defualt to the key.

### `decrypt(encrypted_data: Union[str, bytes, bitarray], key: Union[str, bytes, bitarray, None]=None, final_key: Union[bitarray, None]=None, rounds=None, salt=None) -> bitarray`
Decrypts data that was encrypted using the PCSS.encrypt function. Parameters that do not match will generate an incorrect output.

### `makeid()`
Generates a long and secure id. 
These ids are garunteed to be unique; the chance of collision is about 1 / (2.42721841x10^229).
For reference, the number of atoms in the universe is estimated to be 10^78.

## PCSS.hash
### `hash(data: str, length: int = 256, block_size: int = 4) -> str`
