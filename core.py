import sys, os
import random
from Crypto.Cipher import AES

def shred_file(filename):

    # read in the file data and then delete it
    f = open(filename)
    data = f.read()
    f.close()
    os.remove(filename)

    # encrypt the file
    junk = shred(data)

    # write the new file
    filename = 'shrdd_data_' + str(random.randrange(1000))
    f = open(filename, 'w')
    f.write(junk)
    f.close()

def shred(data):
    data = pad(data)
    key = "".join([chr(random.randrange(256)) for i in range(16)])
    shredder = AES.new(key, AES.MODE_CBC, 'A'*16)
    return shredder.encrypt(data)

def pad(data):
    return data + (16 - (len(data) % 16))*'A'

if __name__ == '__main__':
    shred_file(sys.argv[1])
