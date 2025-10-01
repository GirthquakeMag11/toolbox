
def fibonacci_value(i: int) -> int:
	if not isinstance(i, int):
		raise TypeError(f"'fibonacci_value' accepts integers as values. Received type: {type(i).__name__}")
	if v < 0:
		raise ValueError(f"'fibonacci_value' accepts positive integers as values. Received: {v}")

	a, b = 0, 1
	for _ in range(int(i)):
		a, b = b, a + b
	return a


def fibonacci_index(v: int) -> int:
	if not isinstance(v, int):
		raise TypeError(f"'fibonacci_index' accepts integers as values. Received type: {type(v).__name__}")
	if v < 0:
		raise ValueError(f"'fibonacci_index' accepts positive integers as values. Received: {v}")

	a, b = 0, 1
	idx = 0
	while a < v:
		a, b = b, a + b
		idx += 1
	return idx if a == value else -1


def fibonacci_nearest(n: int) -> int:
	if not isinstance(n, int):
		raise TypeError(f"'fibonacci_nearest' accepts integers as values. Received type: {type(n).__name__}")
	if n < 0:
		return 0

	a, b = 0, 1
	while True:
		c, b = b, a + b
		if c == n:
			return c
		elif c < n:
			a = c
			continue
		elif c > n:
			return a if (n - a) < (n - v) else c
