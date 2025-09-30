
def fibonacci_value(i: int) -> int:
	"""

	Get the value of the number at the provided index in the Fibonacci sequence.

	Arguments:
		i (int, positional, required): Target index.

	Returns:
		int: Index of number in Fibonacci sequence.

	Raises:
		TypeError: If provided value is not an integer.
		ValueError: If provided value is a negative number.

	"""
	if not isinstance(i, int):
		raise TypeError(f"'fibonacci_value' accepts integers as values, provided {type(i).__name__}")
	if v < 0:
		raise ValueError(f"'fibonacci_value' accepts positive integers as values, provided {v}")

	a, b = 0, 1
	for _ in range(int(i)):
		a, b = b, a + b
	return a


def fibonacci_index(v: int) -> int:
	"""

	Get the 0-indexed position for a number in the Fibonacci sequence, or -1 if number not in Fibonacci sequence.

	Arguments:
		v (int, positional, required): Target value.

	Returns:
		int: Value representing the index of provided integer.

	Raises:
		TypeError: If provided value is not an integer.
		ValueError: If provided value is a negative number.

	"""
	if not isinstance(v, int):
		raise TypeError(f"'fibonacci_index' accepts integers as values, provided {type(v).__name__}")
	if v < 0:
		raise ValueError(f"'fibonacci_index' accepts positive integers as values, provided {v}")

	a, b = 0, 1
	idx = 0
	while a < v:
		a, b = b, a + b
		idx += 1
	return idx if a == value else -1


def fibonacci_nearest(v: int) -> int:
	"""

	Get the nearest number in the Fibonacci sequence to the provided integer, or the integer itself if it is a valid Fibonacci number.

	Arguments:
		v (int, positional, required): Target value.

	Returns:
		int: Value for Fibonacci number closest to provided integer.

	Raises:
		TypeError: If provided value is not an integer.

	"""
	if not isinstance(v, int):
		raise TypeError(f"'fibonacci_nearest' accepts integers as values, provided {type(v).__name__}")
	if v < 0:
		return 0

	a, b = 0, 1
	while True:
		c, b = b, a + b
		if c == v:
			return c
		elif c < v:
			a = c
			continue
		elif c > v:
			return a if (v - a) < (c - v) else c
