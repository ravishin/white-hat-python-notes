# File Functions

file = open('text.txt','rt')    # text read only
file2 = open('text.txt','rb')    # binary read only

file3 = open('text.txt','wt')	# text write only
file4 = open('text.txt','wb')	# binary write only

file5 = open('text.txt','wt+')	# text file created and read&write
file6 = open('text.txt','wb+')	# binary file created and read&write

file7 = open('text.txt','at')	# text edit at the end of the existing file
file8 = open('text.txt','ab')	# binary edit at the end of the existing file

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