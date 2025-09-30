from typing import Callable, Tuple
from dataclasses import dataclass
from fnmatch import fnmatch
from pathlib import Path
from enum import Enum, EnumMeta
import string
import math

@dataclass(frozen=True)
class TypeSignature:
	ext: Tuple[str]
	patterns: Tuple[str]

	def check_data(self, byte_data: bytes) -> bool:
		normalized = byte_data.hex().strip().casefold().translate(str.maketrans({char:None for char in string.whitespace}))
		return any(fnmatch(normalized, pattern + "*") for pattern in self.patterns)


class FileTypeMeta(EnumMeta):
	def __getattr__(cls, name):
		if not name.startswith("_") and hasattr(cls, f"_{name}"):
			name = f"_{name}"
		return getattr(super(), name)


class FileTypes(Enum, metaclass=FileTypeMeta):
	UNKNOWN = TypeSignature((""), ("*"))
	TXT = TypeSignature(("txt"), ("efbbbf","f[ef]f[fe]","0000feff","2b2f76[32][89bf]","0efeff"))
	RTF = TypeSignature(("rtf"), ("7b5c72746631"))

	ICO = TypeSignature(("ico"), ("00010000"))
	JPEG = TypeSignature(("jpg","jpeg"), ("ffd8ff[dee][b0e1]"))
	PNG = TypeSignature(("png"), ("89504e470d0a1a0a"))
	WEBP = TypeSignature(("webp"), ("52494646????????57454250"))

	FLAC = TypeSignature(("flac"), ("664c6143"))
	MP3 = TypeSignature(("mp3"), ("fff[b32]","494433"))
	MKA = TypeSignature(("mka"), ("1a45dfa3*6d6b61"))

	_3GP = TypeSignature(("3gp"), ("667479703367"))
	AVI = TypeSignature(("avi"), ("52494646????????41564920"))
	MKV = TypeSignature(("mkv"), ("1a45dfa3*6d6174726f736b61"))
	MK3D = TypeSignature(("mk3d"), ("1a45dfa3*6d6b3364"))
	MP4 = TypeSignature(("mp4"), ("66747970[64][9d][75]3[64][fe][65][d6]"))
	WAV = TypeSignature(("wav"), ("52494646????????57415645"))
	WEBM = TypeSignature(("webm"), ("1a45dfa3*7765626d"))
	MPEG = TypeSignature(("mpg","mpeg"), ("000001b3"))
	FLV = TypeSignature(("flv"), ("464c56"))

	_7ZIP = TypeSignature(("7z"), ("377abcaf271c"))
	ISO = TypeSignature(("iso"), ("4344303031"))
	RAR = TypeSignature(("rar"), ("526172211a070"))
	WAD = TypeSignature(("wad"), ("49574144"))
	ZIP = TypeSignature(("zip"), ("504b0[357]0[468]"))

	PDF = TypeSignature(("pdf"), ("255044462d"))

	MKS = TypeSignature(("mks"), ("1a45dfa3*6d6b61"))
