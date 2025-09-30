from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Set, Type, Union
from pathlib import Path

if TYPE_CHECKING:
	from .types import File, Directory

class FileSystemObject(ABC):
	"""
	
	class toolbox.filetools.abc.FileSystemObject(path, *, lazy=True)

	Abstract base class for Directory and File types.

	Parameters:
		path (str, positional, required): Path to target file system entity.
		lazy (bool, keyword, optional): Defers the assignment of attributes requiring 
			potentially expensive operations until they are attempted to be accessed.

	Properties:
		path (str): Path to target file system entity.

	"""
	_registry: Set[Type[FileSystemObject]] = []

	def __init__(self, path: str, lazy: bool = True):
		if not isinstance(lazy, bool):
			raise TypeError(f"'lazy' parameter accepts only boolean values, provided {type(lazy).__name__}")
		self._path = Path(path).resolve()
		self._lazy = lazy
		# !!! CHECKPOINT !!!

	def __init_subclass__(cls):
		super().__init_subclass__()
		if not hasattr(cls, "accepts_path") or not callable(getattr(cls, "accepts_path", None)):
			raise TypeError(f"{cls.__name__} must define classmethod 'accepts_path'")
		FileSystemObject._registry.add(cls)

	@classmethod
	@abstractmethod
	def accepts_path(cls, path: str) -> bool:
		"""
		
		classmethod toolbox.filetools.abc.FileSystemObject.accepts_path(path)

		Return True if this class accepts the given path value.

		Arguments:
			path (str, positional, required): Path to target file system entity.

		Returns:
			bool: Value indicating class accepts responsibility for entity designated
				by 'path'.

		"""
		pass

	@staticmethod
	def factory(path: str) -> Union[File, Directory]:
		"""

		staticmethod toolbox.filetools.abc.FileSystemObject.factory(path)

		Manufactures instance of appropriate FileSystemObject subclass based on `path` provided.

		Arguments:
			path (str, positional, required): Path to target file system entity.

		Returns:
			Union[filetools.types.File, filetools.types.Directory]: Manufactured object representing file system entity.

		Raises:
			FileNotFoundError: If `path` can not be resolved because its corresponding entity doesn't exist or no FileSystemObject subclass recognizes it as a valid entity.

		"""
		try:
			path = Path(path).resolve()
		except FileNotFoundError:
			raise FileNotFoundError(f"'path' argument does not resolve to existing file system entity, provided: {path}")
		for cls in FileSystemObject._registry:
			if cls.accepts_path(path):
				return cls(path)
		raise FileNotFoundError(f"No FileSystemObject subclass accepted provided path value: {path}")