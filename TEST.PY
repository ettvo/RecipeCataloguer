from hashlib import sha1
name = 'non'
email = 'sdjsad'
shaOne = sha1()
shaTwo = sha1()

hsh = sha1((name+email).encode('utf-8'))

hsh2 = sha1((name+email).encode('utf-8'))

print(hsh)