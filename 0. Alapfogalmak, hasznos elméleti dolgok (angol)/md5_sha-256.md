<h1>MD5</h1>

- (Message-Digest Alogirthm 5) is a widely used cryptographic hash function (A hash function is any function that can be used to map data of arbitrary size to fixed-size values) that produces 128-bit hash value (typically represented as a 32-character hexadecimal num)
- it was desiged to provide a unique identifier for data by generating a fixed-size output for any input
- once popular: verify dataintegrity, storing passwords
- MD5 has been declared sunsuitable for security-sensitive applications -> replcaed by SHA-256

<h1>SHA-family</h1>

- (Secure Hash Algorithm) same as md5 but more modern, more secure
- used for tasks such as verifying data integrity, storing passwords securely, reating digital signatures
- example: when you save a password - it is turned into a fixed length hash code - in the database, you store the hash code itself, not the password, but the hash code does not work as a password as the input is being turned into a code -> not readable and not decryptable 




<h3>Python usage</h3>

```python
def hash():
    from hashlib import sha256

    input_ = input('Enter something: ')
    print(sha256(input_.encode('utf-8')).hexdigest())
```