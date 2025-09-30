from typing import Any, Callable, Hashable


class LazyLoader:

	def __init__(self):
		self._data = {}

	def load_value(self, key: Hashable) -> LazyLoader:
		if self._data.setdefault(key, {}).setdefault("value", None) is None:
			if self._data[key].setdefault("factory", None) is not None:
				self._data[key]["value"] = self._data[key]["factory"]()
		return self

	def set_factory(self, key: Hashable, factory: Callable) -> LazyLoader:
		if not callable(factory):
			raise TypeError(f"'factory' argument must be callable, provided value failed callable check {factory}")
		self._data[key]["factory"] = factory
		return self

	def add_factory(self, key: Hashable, factory: Callable) -> LazyLoader:
		if not callable(factory):
			raise TypeError(f"'factory' argument must be callable, provided value failed callable check {factory}")
		if not existing_factory := self._data.setdefault(key, {}).get("factory", None):
			return self.set_factory(key, factory)
		else:
			raise KeyError(f"'add_factory' method can not add new factory '{factory!r}' under key '{key!r}' until existing factory '{existing_factory!r} is removed")

	def rem_factory(self, key: Hashable) -> LazyLoader:
		if key in self._data:
			self._data.setdefault(key, {})["factory"] = None
		return self

	def clear_value(self, key: Hashable) -> LazyLoader:
		if key in self._data:
			self._data.setdefault(key, {})["value"] = None
		return self