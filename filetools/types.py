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
	@classmethod
	def accepts_path(cls, path: str) -> bool:
		return Path(path).is_file()

	def __init__(self, path, lazy=True):
		super().__init__(path, lazy)
		

class Directory(FileSystemObject):
	"""

	class toolbox.filetools.types.Directory(path)

	Model class representing Directory entities.

	Parameters:
		(Inherited from abc.FileSystemObject)

	Properties:
		(Inherited from abc.FileSystemObject)

	"""
	@classmethod
	def accepts_path(cls, path: str) -> bool:
		return Path(path).is_dir()

	def __init__(self, path, lazy=True):
		super().__init__(path, lazy)

