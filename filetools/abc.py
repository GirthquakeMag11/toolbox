from typing import Union
from pathlib import Path
from __future__ import annotations


class FileSystemObject:
	"""
	
	class toolbox.filetools.abc.FileSystemObject(path)

	Abstract base class for Directory and File types.

	Parameters:
		path (str, positional, required): Path to target file system entity.

	Properties:
		path (str): Path to target file system entity.

	"""
	_registry = {}

	def __init__(self, path):
		self._path = Path(path).resolve()

	def __init_subclass__(cls):
		FileSystemObject._registry[cls.__name__] = cls

	@staticmethod
	def factory(path: str) -> Union[filetools.types.File, filetools.types.Directory]:
		"""

		staticmethod toolbox.filetools.abc.FileSystemObject.factory(path)

		Manufactures instance of appropriate FileSystemObject subclass based on `path` provided.

		Arguments:
			path (str, positional, required): Path to target file system entity.

		Returns:
			Union[filetools.types.File, filetools.types.Directory]: Manufactured object representing file system entity.

		Raises:
			FileNotFoundError: If `path` can not be resolved because it doesn't exist.

		"""
		try:
			path = Path(path).resolve()
		except FileNotFoundError:
			raise FileNotFoundError(f"'path' argument does not resolve to existing file system entity, provided: {path}")
		for cls in FileSystemObject._registry:
			if getattr(cls, '_factory_check', lambda x: False)(path) is True:
				return cls(path)