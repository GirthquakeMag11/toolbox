from typing import Any, Callable, Hashable, Iterator, Tuple, Union
from threading import Lock

class LazyLoader:

	def __init__(self, auto_load: bool = True, auto_clear: bool = False):
		self._data = {}
		self._data_lock = Lock()
		self.set_auto_clear(auto_clear)
		self.set_auto_load(auto_load)

	def __setitem__(self, key: Hashable, item: Any):
		with self._data_lock:
			self._data.setdefault(key, {})["value"] = item

	def __getitem__(self, key: Hashable) -> Any:
		self.load_value(key)
		return self._data.get(key).get("value")
		if self._ac:
			self.clear_value(key)

	def _load_event(self, key: Hashable) -> Union[Any, None]:
		if self._ac is True:
			self.load_value(key)
			return self[key]
		else:
			return None

	def keys(self) -> Iterator[Hashable]:
		yield from self._data.keys()

	def values(self) -> Iterator[Union[Any, None]]:
		for key, data in self._data.items():
			yield data.get("value", self._load_event(key))

	def items(self) -> Iterator[Tuple[Hashable, Union[Any, None]]]:
		for key, value in self._data.items():
			yield (key, value.get("value", self._load_event(key)))

	def load_value(self, key: Hashable) -> LazyLoader:
		with self._data_lock:
			if self._data.setdefault(key, {}).setdefault("value", None) is None:
				if self._data[key].setdefault("factory", None) is not None:
					self._data[key]["value"] = self._data[key]["factory"]()
		return self

	def set_factory(self, key: Hashable, factory: Callable) -> LazyLoader:
		with self._data_lock:
			if not callable(factory):
				raise TypeError(f"'factory' argument must be callable, provided value failed callable check {factory}")
			self._data[key]["factory"] = factory
		return self

	def add_factory(self, key: Hashable, factory: Callable) -> LazyLoader:
		if not callable(factory):
			raise TypeError(f"'factory' argument must be callable, provided value failed callable check {factory}")
		with self._data_lock:
			if not existing_factory := self._data.setdefault(key, {}).get("factory", None):
				return self.set_factory(key, factory)
			else:
				raise KeyError(f"'add_factory' method can not add new factory '{factory!r}' under key '{key!r}' until existing factory '{existing_factory!r} is removed")

	def rem_factory(self, key: Hashable) -> LazyLoader:
		if key in self._data:
			with self._data_lock:
				self._data.setdefault(key, {})["factory"] = None
		return self

	def clear_value(self, key: Hashable) -> LazyLoader:
		if key in self._data:
			with self._data_lock:
				self._data.setdefault(key, {})["value"] = None
		return self

	def set_auto_load(self, setting: bool):
		with self._data_lock:
			self._al = bool(setting)

	def set_auto_clear(self, setting: bool):
		with self._data_lock:
			self._ac = bool(setting)