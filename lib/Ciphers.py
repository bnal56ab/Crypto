from binascii import hexlify, unhexlify
from base64 import standard_b64encode, urlsafe_b64encode, standard_b64decode, urlsafe_b64decode
from Crypto.Util.number import bytes_to_long, long_to_bytes

from lib import Common


def CheckKeyError(Key):
	if type(Key) == type(None):
		exit(Common.Msg.ErrorNoKey.value)
	elif Key == "":
		exit(Common.Msg.ErrorEmptyKey.value)
	elif not (len(Key.split(":")) == 2):
		exit(Common.Msg.ErrorEmptyKeyType.value)
	Type = Key.split(":")[0].lower()
	if not (Type == "Hex".lower() or Type == "Ascii".lower() or Type == "Dec".lower()):
		exit(Common.Msg.ErrorUnknownKeyType.value)


def Xor(Text, FullKey):
	Type, Key = FullKey.split(":")
	Type = Type.lower()
	if Type == "Hex".lower():
		pass
	elif Type == "Ascii".lower():
		pass
	elif Type == "Dec".lower():
		PlainText = "".join(chr(ord(Letter) ^ int(Key)) for Letter in Text)
	return PlainText


def Encode(Cipher, PlainText, Key):
	if Cipher == Common.Ciphers.Ascii.value:
		print(" ".join([str(ord(Letter)) for Letter in PlainText]))

	elif Cipher == Common.Ciphers.Hex.value:
		print(hexlify(PlainText.encode()))

	elif Cipher == Common.Ciphers.StandardBase64.value:
		print(standard_b64encode(PlainText.encode()).decode())

	elif Cipher == Common.Ciphers.UrlSafeBase64.value:
		print(urlsafe_b64encode(PlainText.encode()).decode())
	
	elif Cipher == Common.Ciphers.ByteToLong.value:
		print(bytes_to_long(PlainText.encode()))

	elif Cipher == Common.Ciphers.Xor.value:
		CheckKeyError(Key)
		print(Xor(PlainText, Key))

	elif Cipher == Common.Ciphers.Binary.value:
		print(" ".join(format(ord(Letter), 'b') for Letter in PlainText))

def Decode(Cipher, EncriptedText, Key):
	if Cipher == Common.Ciphers.Ascii.value:
		print("".join([chr(int(SplitedAsciiCode)) for SplitedAsciiCode in EncriptedText.split(" ")]))

	elif Cipher == Common.Ciphers.Hex.value:
		print(unhexlify(EncriptedText))

	elif Cipher == Common.Ciphers.StandardBase64.value:
		print(standard_b64decode(EncriptedText).decode())

	elif Cipher == Common.Ciphers.UrlSafeBase64.value:
		print(urlsafe_b64decode(EncriptedText).decode())

	elif Cipher == Common.Ciphers.ByteToLong.value:
		print(long_to_bytes(EncriptedText).decode())

	elif Cipher == Common.Ciphers.Xor.value:
		if type(Key) == type(None):
			exit(Common.Msg.ErrorNoKey.value)
		elif Key == "":
			exit(Common.Msg.ErrorEmptyKey.value)
		CheckKeyError(Key)
		print(Xor(EncriptedText, Key))
	
	elif Cipher == Common.Ciphers.Binary.value:
		BinaryList = EncriptedText.split(" ")
		PlainText = []
		for BinaryNumber in BinaryList:
			PlainText.append(chr(int(BinaryNumber, 2)))
		print("".join(PlainText))
