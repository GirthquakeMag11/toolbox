from typing import Any, Callable, Hashable


class LazyLoader:

	def __init__(self):
		self._data = {}

	def load(self, key: Hashable) -> LazyLoader:
		if self._data.setdefault(key, {}).setdefault("value", None) is None:
			if self._data[key].setdefault("factory", None) is not None:
				self._data[key]["value"] = self._data[key]["factory"]()
		return self

	def set_factory(self, key: Hashable, factory: Callable) -> LazyLoader:
		if callable(factory):
			self._data[key]["factory"] = factory
			return self
		else:
			raise TypeError(f"'factory' argument must be callable, provided value failed callable check {factory}")