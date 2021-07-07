from enum import Enum, unique, auto


@unique
class Ciphers(Enum):
	Ascii = 1
	Hex = 2
	StandardBase64 = 3
	UrlSafeBase64 = 4
	ByteToLong = 5
	Xor = 6
	Binary = 7


class Msg(Enum):
	ErrorNoKey = "This cipher needs a key"
	ErrorEmptyKey = "Key is empty"
	ErrorEmptyKeyType = "Not found type in key"
	ErrorUnknownKeyType = "Unkown type in key"


def Logo():
	print("          _nnnn_                      ")
	print("         dGGGGMMb     ,\"\"\"\"\"\"\"\"\"\"\"\"\"\"\".")
	print("        @p~qp~~qMb    | cryptanalysis |")
	print("        M|@||@) M|   _;...............'")
	print("        @,----.JM| -'")
	print("       JS^\__/  qKL")
	print("      dZP        qKRb")
	print("     dZP          qKKb")
	print("    fZP            SMMb")
	print("    HZM   Beroni   MMMM")
	print("    FqM            MMMM")
	print("  __| \".        |\dS\"qML")
	print("  |    `.       | `' \Zq")
	print(" _)      \.___.,|     .'")
	print(" \____   )MMMMMM|   .'")
	print("      `-'       `--' ")