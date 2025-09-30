from typing import Sequence, Union
import collections
import string

def alpha_index(char: str) -> int:
	if not isinstance(char, str):
		try:
			char = str(char)
		except:
			raise TypeError(f"'alpha_index' accepts 'char' arguments of string type, provided {type(char).__name__}")
	if char in string.ascii_letters:
		return ord(char) - ord('A' if char.isupper() else 'a')
	else:
		return -1
