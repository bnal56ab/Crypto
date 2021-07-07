import argparse

from lib import Common, Ciphers


if __name__ == '__main__':
	Common.Logo()
	parser = argparse.ArgumentParser()
	parser.add_argument('--coded', '-c', type=str, choices=["E", "D"], help="(E)ncode (D)ecode")
	parser.add_argument('--Cipher', '-C', type=int, required=True, help="Do -C0 to get number and example of the cipher")
	parser.add_argument('--Text', '-T', type=str, help="Text you want to (en|de)code")
	parser.add_argument('--Key', '-K', type=str, help="Used if the cripto wanted key Hex:key or Ascii:key or Dec:key")
	args = parser.parse_args()

	if args.Cipher == 0:
		for element in Common.Ciphers:
			print(element.name + ":", element.value)
	else:
		if args.coded == None or args.Text == None:
			exit("coded and Text are required")
		if args.coded == "E":
			Ciphers.Encode(args.Cipher, args.Text, args.Key)
		elif args.coded == "D":
			Ciphers.Decode(args.Cipher, args.Text, args.Key)
