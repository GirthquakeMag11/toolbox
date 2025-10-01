from typing import Dict, Iterable, Mapping
import collections
import hashlib

class HashMap(collections.abc.Mapping, collections.abc.Hashable):
	__EMPTY = "NONE"
	def __init__(self, initial_data: Mapping | Iterable = None, **kwargs):
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
			data = (*_map(), *_kwargs())
		
		elif isinstance(initial_data, collections.abc.Iterable):
			if any(not hasattr(item, "__len__") for item in initial_data):
				data = (*_pair_iter(), *_kwargs())

			elif all(len(item) == 2 for item in initial_data):
				data = (*_zip_iter(), *_kwargs())

				





	def __getitem__(self, key: Hashable) -> Hashable:

	def __iter__(self):

	def __len__(self):

	def __contains__(self):

	def __eq__(self):

	def __hash__(self):

	def keys(self):

	def values(self):

	def items(self):

	def get(self, key: Hashable, default=HashMap.__EMPTY):