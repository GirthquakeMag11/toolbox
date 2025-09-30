from typing import Callable, Type
from .abc import FileSystemObject


class File(FileSystemObject):
	"""
	
	class toolbox.filetools.types.File(path)

	Model class representing File entities.

	Parameters:
		(Inherited from abc.FileSystemObject)

	Properties:
		(Inherited from abc.FileSystemObject)

	"""
	_factory_check = lambda p: bool(p.is_file())

	def __init__(self, path):
		super().__init__(path)



class Directory(FileSystemObject):
	"""

	clsas toolbox.filetools.types.Directory(path)

	Model class representing Directory entities.

	Parameters:
		(Inherited from abc.FileSystemObject)

	Properties:
		(Inherited from abc.FileSystemObject)

	"""
	_factory_check = lambda p: bool(p.is_dir())

	def __init__(self, path):
		super().__init__(path)

