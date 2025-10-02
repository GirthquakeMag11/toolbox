from typing import Any, Iterable
import collections

__NONE = "NONE"

def find(data: Iterable, default: Any = __NONE, **attrs) -> Any:
	for item in data:

		if isinstance(item, collections.abc.Mapping) or hasattr(item, "__getitem__") or hasattr(item, "keys"):
			if all(k in item.keys() for k in attrs.keys()):
				if all(item[k] == attrs[k] for k in attrs.keys()):
					return item

		elif all(hasattr(item, k) for k in attrs.keys()):
			if all(getattr(item, k) == attrs[k] for k in attrs.keys()):
				return item

	if default is not __NONE:
		return default
	raise ValueError(f"Iterable 'data' {data} contained no object with defined attributes {attrs}")

def get(data: Iterable, default: Any = __NONE, check: Callable) -> Any:
	for item in data:
		if check(item):
			return item
	
	if default is not __NONE:
		return default
	raise ValueError(f"Iterable 'data' {data} contained no object that passed check {check!r}")