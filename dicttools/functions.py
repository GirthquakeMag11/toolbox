from typing import Any, Callable, Dict, Hashable

def getdefault(data: Dict[Hashable | None, Any | None], key: Hashable, default_value: Any = None, default_factory: Callable = None) -> Any:
	"""
	
	def getdefault(data, key, *, default_value=None, default_factory=None)

	Get the value for `key` in `data`, setting it to `default_value` or `default_factory()` if missing.

	Arguments:
		data (dict): Target dictionary. (Required, positional)
		key (Hashable): Key to look up. (Required, positional)
		default_value (Any, optional): Value to insert if key is absent. (Keyword only)
		default_factory (Callable, optional): Callable returning value if key is absent and `default_value` is not set. (Keyword only)

	Returns:
		Any: Value for `key` in `data`, or None if not found and no default provided.

	"""
	if not key in data:
		if not default_value and not default_factory:
			return None
		elif default_value:
			data[key] = default_value
		elif default_factory and callable(default_factory):
			data[key] = default_factory()
	return data[key]
