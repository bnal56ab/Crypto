from enum import Enum, unique


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
	print("""
      ______________________________    . \  | / .
     /                            / \     \ \ / /
    |      Bnal5tab - Nero       | ==========  - -
     \____________________________\_/     / / \ \\
  ______________________________      \  | / | \\
 /                            / \     \ \ / /.   .
|       Cryptanalysis        | ==========  - -
 \____________________________\_/     / / \ \    /
      ______________________________   / |\  | /  .
     /                            / \     \ \ / /
    |        Cryptography        | ==========  -  - -
     \____________________________\_/     / / \ \\
                                        .  / | \  .""")