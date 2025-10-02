
def chunks(path: str, chunk_size: int = 1024, max_chunks: int = -1) -> Iterator[bytes]:
	tc = 0
	with open(path, "rb") as file:
		while (chunk := file.read(chunk_size)) and (tc < max_chunks or max_chunks < 0):
			yield chunk
			tc += 1
