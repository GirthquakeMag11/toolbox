
def fibonacci_value(i: int) -> int:
	if not isinstance(i, int):
		raise TypeError(f"'fibonacci_value' accepts integers as values, provided {type(i).__name__}")
	if v < 0:
		raise ValueError(f"'fibonacci_value' accepts positive integers as values, provided {v}")

	a, b = 0, 1
	for _ in range(int(i)):
		a, b = b, a + b
	return a


def fibonacci_index(v: int) -> int:
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
