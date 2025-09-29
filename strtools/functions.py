from typing import Sequence, Union
import string

def alpha_index(data: str) -> Union[int, Sequence[int]]:
	"""

	def toolbox.strtools.functions.alpha_index(data)

	Get the 0-indexed position for one or more characters in the alphabet, or -1 if character not alphabetical.

	Arguments:
		data (str, positional, required): Target string.

	Returns:
		int | Sequence[int]: Index of character or sequence of indexes for sequence of characters. 

	Raises:
		TypeError: If 'data' is not a string and fails to be coerced into string type.

	"""
	if len(data) > 1:
		result = [alpha_index(char) for char in data]
	else:
		if not isinstance(data, str):
			try:
				data = str(data)
			except:
				raise TypeError(f"'data' argument must be string type, provided {type(data).__name__}")
		if c in string.ascii_letters:
			result = ord(c) - ord('A' if c.isupper() else 'a')
		else:
			result = -1

	return result
