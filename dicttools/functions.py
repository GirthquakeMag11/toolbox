from typing import Any, Callable, Dict, Hashable

#def getdefault(data: Dict[Hashable | None, Any | None], key: Hashable, default_value: Any = None, default_factory: Callable = None) -> Any:
#	"""
#
#	Get the value for `key` in `data`, setting it to `default_value` or `default_factory()` if missing.
#
#	Arguments:
#		data (Dict, positional, required): Target dictionary.
#		key (Hashable, positional, required): Key to look up.
#		default_value (Any, keyword, optional): Value to insert if key is absent.
#		default_factory (Callable, keyword, optional): Callable returning value if key is absent and 
#			`default_value` is not set.
#
#	Returns:
#		Any: Value for `key` in `data`, or None if not found and no default provided.
#
#	Raises:
#		ValueError: If `default_factory` is provided and fallen back to but is not callable.
#
#	"""
#	if not key in data:
#		if not default_value and not default_factory:
#			return None
#		elif default_value and not default_factory:
#			data[key] = default_value
#		elif default_factory and callable(default_factory):
#			data[key] = default_factory()
#
#		elif default_factory and not callable(default_factory):
#			raise ValueError(f"'default_factory' argument must be callable, provided:\n {default_factory!r}")
#	
#	return data[key]
