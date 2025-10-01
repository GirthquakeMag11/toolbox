import collections


class PropertyDict(collections.abc.MutableMapping):
	EMPTY = "N/A"

	class _KeysView(collections.abc.KeysView):
		def __init__(self, mapping):
			self._mapping = mapping

		def __iter__(self):
			return iter(self._mapping._data)
		
		def __contains__(self, key):
			return key in self._mapping._data

		def __len__(self):
			return len(self._mapping._data)

	class _ValuesView(collections.abc.ValuesView):
		def __init__(self, mapping, factories=True):
			self._mapping = mapping
			self._factories = factories

		def __iter__(self):
			for value in self._mapping._data.values():
				if self._factories:
					yield value()
				else:
					yield value

		def __contains__(self, value):
			if self._factories:
				return any(call() == value for call in self._mapping._data.values())
			else:
				return value in self._mapping._data.values()

		def __len__(self):
			return len(self._mapping._data)

	class _ItemsView(collections.abc.ItemsView):
		def __init__(self, mapping, factories=True):
			self._mapping = mapping
			self._factories = factories

		def __iter__(self):
			for key, value in self._mapping._data.items():
				if self._factories:
					yield (key, value())
				else:
					yield (key, value)

		def __contains__(self, value):
			k, v = value
			if self._factories:
				return any((k, v) == (key, call()) for key, call in self._mapping._data.items())
			else:
				return any((k, v) == (key, val) for key, val in self._mapping._data.items())

		def __len__(self):
			return len(self._mapping._data)


	def __init__(self, *args, **kwargs):
		self._data = dict()
		
		if len(args) > 1:
			raise TypeError(f"{type(self).__name__} expected at most 1 positional argument, got {len(args)}")

		if args:
			arg = args[0]

			if hasattr(args, 'keys'):
				for key in arg:
					self[key] = arg[key]

			else:
				try:
					for idx, item in enumerate(arg):
						try:
							k, v = item
						except ValueError:
							if hasattr(item, '__iter__'):
								length = len(item) if hasattr(item, '__len__') else 'unknown'
								raise ValueError(f"{type(self).__name__} update sequence element #{idx} has length {length}: 2 is required") from None
							else:
								raise TypeError(f"{type(self).__name__} update sequence cannot convert element #{idx} to a sequence") from None

						self[k] = v
				except TypeError:
					raise TypeError(f"{type(arg).__name__} object is not iterable")

	def __getitem__(self, key):
		if key in self._data:
			return self._data[key]()
		else:
			raise KeyError(key)
		

	def __setitem__(self, key, value):
		if not callable(value):
			raise ValueError(f"{type(self).__name__} objects accepts callable values, got {value!r}")
		else:
			self._data[key] = value

	def __delitem__(self, key):
		if key in self._data:
			del self._data[key]
		else:
			raise KeyError(key)

	def __iter__(self):
		yield from self.keys()

	def __len__(self):
		return len(self._data)

	def __str__(self):
		return str(self._data)

	def __repr__(self):
		return str(self)

	def __eq__(self, other):
		result = True
		if not isinstance(other, collections.abc.Mapping):
			raise NotImplementedError
		else:
			try:
				for key in other.keys():
					if not key in self.keys():
						result = False
						break
					else:
						if isinstance(other, PropertyDict):
							if self._data[key] in other.values(factories=False):
								continue
							else:
								result = False
								break
						else:
							if self.__getitem__(key) == other.__getitem__(key):
								continue
								result = False
							else:
								break
			except (TypeError, AttributeError, KeyError, ValueError):
				result = False
			finally:
				return result

	def keys(self) -> PropertyDict._KeysView:
		return self._KeysView(self)

	def values(self, factories: bool = True) -> PropertyDict._ValuesView:
		return self._ValuesView(self, factories)

	def items(self, factories: bool = True) -> PropertyDict._ItemsView:
		return self._ItemsView(self, factories)

	def get(self, key, default=PropertyDict.EMPTY):
		try:
			return self.__getitem__(key)
		except KeyError:
			if default is PropertyDict.EMPTY:
				raise
			else:
				return default

	def pop(self, key, default=PropertyDict.EMPTY):
		try:
			value = self.__getitem__(key)
			self.__delitem__(key)
			return value
		except KeyError:
			if default is PropertyDict.EMPTY:
				raise
			else:
				return default

	def setdefault(self, key, default=PropertyDict.EMPTY):

	def popitem(self):
		pass

	def clear(self):
		self._data = {}

	def update(self, other=()):

	def copy(self):
