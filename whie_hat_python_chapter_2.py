# File Functions

file = open('text.txt','rt')    # text read only
file2 = open('text.txt','rb')    # binary read only

file3 = open('text.txt','wt')   # text write only
file4 = open('text.txt','wb')   # binary write only

file5 = open('text.txt','wt+')  # text file created and read&write
file6 = open('text.txt','wb+')  # binary file created and read&write

file7 = open('text.txt','at')   # text edit at the end of the existing file
file8 = open('text.txt','ab')   # binary edit at the end of the existing file

# Caesar's Cipher

"""
Enc(i) = (i+k) mod 26
"""

# Alberti's Cipher Disk

"""
Enc(i) = (i+k) mod 36
"""

# Caesar's Cipher Source Code

ENC = 0
DEC = 1

def makeDisk(key):
    keytable = map(lambda x: (chr(x+65),x),range(26))

    key2index = {}
    for t in keytable:
        alphabet, index = t[0],t[1]
        key2index[alphabet] = index

    if key in key2index:
        k = key2index[key]
    else:
        return None, None

    enc_disk = {}
    dec_disk = {}

    for i in range(26):
        enc_i = (i+k)%26
        enc_ascii = enc_i + 65
        enc_disk[chr(i+65)] = chr(enc_ascii)
        dec_disk[chr(enc_ascii)] = chr(i+65)

    return enc_disk, dec_disk

def caesar(msg,key,mode):
    ret = ''

    msg = msg.upper()
    enc_disk, dec_disk = makeDisk(key)

    if enc_disk is None:
        return ret

    if mode is ENC:
        disk = enc_disk
    if mode is DEC:
        disk = dec_disk

    for c in msg:
        if c in disk:
            ret += disk[c]
        else:
            ret += c
    return ret

def main():
    plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = 'F'

    print('Original:\t%s' %plaintext.upper())
    ciphertext = caesar(plaintext,key,ENC)
    print('Caesar Cipher:\t%s' %ciphertext)
    deciphertext = caesar(ciphertext,key,DEC)
    print('Deciphered:\t%s' %deciphertext)

if __name__ == '__main__':
    main()

# Caesar's Cipher Source Code Explanation

"""
ENC = 0
DEC = 1

def makeDisk(key):
    # input: an alphabet that represents as a key to the cipher
    # output: two disks (enc & dec) that represent the encoding & decoding cipher disks
    keytable = map(lambda x: (chr(x+65),x),range(26))
    # keytable = [('A',0),('B',1),('C',2),...,('Z',25)]
    # chr(ASCII number) = ASCII text
    # ord(ASCII text) = ASCII number

    key2index = {}
    for t in keytable:
        alphabet, index = t[0],t[1]
        key2index[alphabet] = index
        # key2index = {'A':0,'B':1,'C':2,...,'Z':25}

    if key in key2index:
        k = key2index[key]
    else:
    # when a user inputs something that is not an alphabet
        return None, None

    enc_disk = {}
    dec_disk = {}

    for i in range(26):
        enc_i = (i+k)%26
        enc_ascii = enc_i + 65
        enc_disk[chr(i+65)] = chr(enc_ascii)
        # key = plain alphabet
        # value = encrypted alphabet
        dec_disk[chr(enc_ascii)] = chr(i+65)
        # value = encrypted alphabet
        # key = plain alphabet

    return enc_disk, dec_disk

def caesar(msg,key,mode):
    ret = ''

    msg = msg.upper()
    enc_disk, dec_disk = makeDisk(key)

    if enc_disk is None:
        return ret

    if mode is ENC:
        disk = enc_disk
    if mode is DEC:
        disk = dec_disk

    for c in msg:
        if c in disk:
            ret += disk[c]
        else:
            ret += c
    return ret

def main():
    plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = 'F'

    print('Original:\t%s' %plaintext.upper())
    ciphertext = caesar(plaintext,key,ENC)
    print('Caesar Cipher:\t%s' %ciphertext)
    deciphertext = caesar(ciphertext,key,DEC)
    print('Deciphered:\t%s' %deciphertext)

if __name__ == '__main__':
    main()

"""
'''
lambda
'''

f = lambda x: x*x
f(2)        #4

'''
map()
'''
result = map(lambda x: x*x,[1,2,3])     # [1,4,9]

'''
list()
'''
d = {'a':97,'b':98}
result2 = list(d)       # ['a','b']


'''
Text Formatting Operators
'''

def textFormat():
    lang1 = 'Python'
    lang2 = 'Perl'
    text = 'I love %s' %lang1
    print(text) # 'I love Python'

    text = '%s is better than %s' %(lang1,lang2)
    print(text) # 'Python is better than Perl'

    a,b = 1,5
    text = '%d + %d = %d' %*(a,b,a+b) 
    print(text) # '1 + 5 = 6'

'''
Escape text
'''
def escape():
    text = 'I love Python\nPython is better than Perl'
    print(text) # 'I love Python'
                # 'Python is better than Perl'

    text = 'Python\tPerl\tJavascript'
    print(text) # 'Python Perl Javascript'

    text = 'Alot of things occur \
    each day, every day'
    print(text) # 'A lot of things occur each day, every day'

    text = '\\t means a tab'
    print(text) # '\t means a tab'

    text = '\'Python\' is a kind of snake' # \' used
    print(text) # ''Python' is a kind of snake'

'''
Affine Cipher: an advanced Caesar's cipher with more ciphering numbers
'''

'''
Rail Fence Cipher: Given a string, you write each letter on a line and move
                   to a new line and repeat that process

Route Cipher: 
    - List each letter of a plaintext vertically in a certain number of columns
    - cipher(read) it in a counterclockwise-spiral way

Columnar Transposition Cipher:
    - List each letter of a plaintext horizontally in a certain number of columns
    - randomize the position of the column
    - cipher(read) each column from left to right

'''

'''
Columnar Transposition Cipher Source Code
'''

ENC = 0
DEC = 1

def parseKey(key):
    tmp = []
    key = key.upper()

    for i,k in enumerate(key):
        tmp.append((i,k))

    tmp = sorted(tmp, key=lambda x:x[1])    # tmp를 정렬함

    enc_table = {}
    dec_table = {}
    for i,r in enumerate(tmp):      # create enc_table, dec_table
        enc_table[r[0]] = i
        dec_table[i] = r[0]

    return enc_table, dec_table

def transposition(msg, key, mode):
    msgsize = len(msg)
    keysize = len(key)
    ret = ''

    filler = ''
    if msgsize%keysize != 0:
        filler = '0'*(keysize-msgsize%keysize)      # '0' for adding to msg
    msg = msg.upper()
    msg += filler

    enc_table, dec_table = parseKey(key)

    if mode == ENC:
        table = enc_table
    else:
        table = dec_table

    if mode == ENC:
        but = ['']*keysize 
        for i,c in enumerate(msg):
            col = i%keysizeindex = table[col]
            buf[index] += c

        for text in buf:
            ret += text
    else:
        blocksize = int(msgsize/keysize)
        buf = ['']*keysize
        pos = 0
        for i in range(keysize):
            text = msg[pos:pos+blocksize]
            index = table[i]
            buf[index] += text
            pos += blocksize

        for i in range(blocksize):
            for j in range(keysize):
                if buf[j][i] != 0:
                    ret += buf[j][i]
    return ret

'''
Syntax Notes
'''

# enumerate()

key = 'ABC'
for i,k in enumerate(key):
    print (i,k)

# 0 A
# 1 B
# 2 C

'''
sorted()
'''
## sort by 2nd elem of tuple (list of tuples)

tmp = [(0,'B'),(1,'R'),(2,'A'),(3,'I'),(4,'N')]
sorted(tmp,key=lambda x:x[1])
# [(2,'A'),(0,'B'),(3,'I'),(4,'N'),(1,'R')]

## sort by keys (dictionary, returns a list of keys)

tmp = {'Mary':1998, 'Anna':2001, 'Suji':788, 'Kelly':4009}
sorted(tmp)
# ['Anna','Kelly','Mary','Suji']

## sort by keys (dictoinary, returns a list of tuples)

tmp = {'Mary':1998, 'Anna':2001, 'Suji':788, 'Kelly':4009}
sorted(tmp.itmes(), key=lambda x:x[0])

# [('Anna',2001),('Kelly',4009),('Mary':1998),('Suji',788)]

## sort by values (dictionary, returns a list of tuples)

tmp = {'Mary':1998, 'Anna':2001, 'Suji':788, 'Kelly':4009}
sorted(tmp.items(), key=lambda x:x[1])

# [('Suji',788),('Mary':1998),('Anna',2001),('Kelly',4009)]

## reverse

sorted(tmp.items(), key=lambda x:x[1], reverse=True)

# [('Kelly',4009),('Anna',2001),('Mary':1998),('Suji',788)]


