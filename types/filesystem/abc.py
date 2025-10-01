from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Set, Type, Union
from pathlib import Path

if TYPE_CHECKING:
	from .file import File
	from .directory import Directory


class FileSystemObject(ABC):

	_registry: Set[Type[FileSystemObject]] = set()

	def __init__(self, path: str, strict=True):
		self._strict = strict
		self._path = Path(path)
		if strict is True and not self._path.exists():
			raise FileNotFoundError(path)
			
	def __init_subclass__(cls):
		super().__init_subclass__()
		if not hasattr(cls, "accepts_path") or not callable(getattr(cls, "accepts_path", None)):
			raise TypeError(f"{cls.__name__} must define classmethod 'accepts_path'")
		FileSystemObject._registry.add(cls)

	@property
	def path(self):
		return str(self._path.resolve(strict=self._strict))