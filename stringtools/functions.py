from typing import Container, Iterator
import collections
import string

DEFAULT_TOKEN_CHARSET = tuple("'", *string.ascii_letters)

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

def tokenize(data: str, remove_whitespace: bool = False, remove_punctuation: bool = False, continuity_charset: Container[str] = DEFAULT_TOKEN_CHARSET) -> Iterator[str]:
	cur_token = ''
	for char in str(data):
		if char in continuity_charset:
			cur_token += char
		else:
			if cur_token:
				yield cur_token
				cur_token = ''
			if remove_whitespace and (char in string.whitespace):
				continue
			if remove_punctuation and (char in string.punctuation):
				continue

			yield char
	if cur_token:
		yield cur_token