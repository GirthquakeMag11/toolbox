from typing import Dict, Iterable, Mapping
import collections
import hashlib

class HashMap(collections.abc.Mapping, collections.abc.Hashable):
	__EMPTY = "NONE"

	__slots__ = ("_data","_hash")
	def __init__(self, initial_data: Mapping | Iterable = None, **kwargs):
		self._data = ()

		def _kw():
			if kwargs:
				return ((k, v) for k, v in kwargs.items())
			return ()

		def _map(): 
			return ((k, v) for k, v in {**initial_data}.items())

		def _zip_iter():
			return ((*item) for item in initial_data)

		def _pair_iter():
			a, b = None, None
			for item in initial_data:
				if not a:
					a = item
					continue
				elif not b:
					b = item
				if a and b:
					yield (a, b)
					a, b = None, None
			if a or b:
				yield (a, b)

		if isinstance(initial_data, collections.abc.Mapping):
			self._data = (*_map(), *_kwargs())
		
		elif isinstance(initial_data, collections.abc.Iterable):
			if any(not hasattr(item, "__len__") for item in initial_data):
				self._data = (*_pair_iter(), *_kwargs())

			elif all(len(item) == 2 for item in initial_data):
				self._data = (*_zip_iter(), *_kwargs())

		setattr(self, "_hash", hash(self))


	def __getitem__(self, key):
		for a, b in self._data:
			if key == a: return b
			if key == b: return a
		raise KeyError(key)

	def __iter__(self):
		yield from self._data

	def __len__(self):
		return sum(1 for item in self._data)

	def __contains__(self, key):
		return bool(any(key in item for item in self._data))

	def __eq__(self, other):
		return hash(self) == hash(other)

	def __hash__(self):
		try:
			return self._hash
		except AttributeError:
			s = []
			for item in self._data:
				for value in item:
					try:
						s.append(hash(value))
					except:
						hasher = hashlib.md5()
						hasher.update(str(repr(value)).encode())
						s.append(int.from_bytes(hasher.digest()))
			return int("".join([str(n) for n in s]).strip())