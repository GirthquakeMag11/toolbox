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
		
	def data(self, start: int = 0, stop: int = -1, chunk_size: int = 1024, max_chunks: int = -1) -> Iterator[bytes]:
		cur_idx = 0
		total_ch = 0
		with open(self.path, "rb") as file:
			while chunk := file.read(chunk_size):
				if (cur_idx < stop or stop == -1) and (total_ch < chunks or chunks == -1):
					cur_idx += (len(chunk) - 1)
					total_ch += 1
					yield chunk

					if stop != -1 and (remaining := stop - cur_idx) < chunk_size:
						chunk_size = remaining

				else:
					break


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

