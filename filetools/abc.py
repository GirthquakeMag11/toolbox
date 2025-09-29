from typing import Union
from pathlib import Path
import hashlib

class FileSystemObject:
	"""
	
	class toolbox.filetools.abc.FileSystemObject(path)

	Abstract base class for all Directory and File types.

	Properties:
		path: str

	"""
	def __init__(self, path):
		self._path = Path(path)

	@staticmethod
	def factory(path: str, strict: bool = True) -> Union[File, Directory, None]:
		"""

		def toolbox.filetools.abc.FileSystemObject.factory(path, *, strict=True)

		Manufactures an instance of a FileSystemObject subclass.

		Arguments:
			path (str, positional, required): File system path.
			strict (bool, keyword, optional): If `True` raises FileNotFoundError if provided `path` does not resolve to existing entity, not if `False`.

		Returns:
			None: If `strict` is `False` and the path does not resolve to an existing entity.
			File: If `path` resolves to existing file entity.
			Directory: If `path` resolves to existing directory entity.

		Raises:
			FileNotFoundError: If `path` argument does not resolve to existing entity and `strict` is `True`.

		"""
		path = Path(path).resolve(strict=strict)
		if path.exists():
			if path.is_file():
				return File(path)
			elif path.is_dir():
				return Directory(path)
		else:
			return None

	@property
	def path(self):
		return str(self._path)

class File(FileSystemObject):

	def __init__(self, path):
		super().__init__(path)

class Directory(FileSystemObject):

	def __init__(self, path):
		super().__init__(path)