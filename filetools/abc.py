from typing import Union
from pathlib import Path


class FileSystemObject:
	"""
	
	class toolbox.filetools.abc.FileSystemObject(path)

	Abstract base class for Directory and File types.

	Properties:
		path: str

	"""
	_registry = set()

	def __init__(self, path):
		self._path = Path(path).resolve()

	def __init_subclass__(cls):
		FileSystemObject._registry.add(cls)

	@staticmethod
	def factory(path):
		path = Path(path).resolve()
		for cls in FileSystemObject._registry:
			if getattr(cls, '_factory_check', lambda x: False)(path) is True:
				return cls(path)