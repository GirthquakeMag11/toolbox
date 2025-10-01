from typing import Container, Iterator
import string


def alpha_index(data: str) -> int | Tuple[int]:
	if not isinstance(data, str):
		try:
			data = str(data)
		except:
			raise TypeError(f"'data' argument must be a string. Received type: {type(char).__name__}") from None
	if len(data) > 1:
		return tuple(alpha_index(char) for char in data)

	if data in string.ascii_letters:
		return ord(data) - ord('A' if data.isupper() else 'a')
	else:
		return -1

def tokenize(data: str, remove_whitespace: bool = False, remove_punctuation: bool = False, continuity_charset: Container[str] = ("'", *string.ascii_letters)) -> Iterator[str]:
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

