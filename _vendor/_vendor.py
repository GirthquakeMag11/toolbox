from typing import Optional, MutableMapping
import types
from dataclasses import dataclass, field
from pathlib import Path
from enum import Enum
import subprocess
import importlib
import sys

@dataclass
class Vendor:
	name: str
	path: str = field(init=False)

	def import_module(self, namespace: Optional[MutableMapping] = None) -> types.ModuleType:
		if not Path(self.path).exists():
			self.pip_install()
		if not self.path in sys.path:
			sys.path.append(self.path)
		mod = importlib.import_module(self.name)
		if hasattr(namespace, "__setitem__"):
			namespace[self.name] = mod
		return mod

	def pip_install(self, target_dir: str = None):
		if not target_dir:
			target_dir = str(Path(__file__).parent / "_vend")
		return subprocess.check_output(["pip","install",self.name,"--target",str(target_dir)], stderr=subprocess.STDOUT)

	def __post_init__(self):
		set_attr = lambda name, value: object.__setattr__(self, name, value)
		set_attr("name", str(self.name).strip().casefold())
		set_attr("path", str((Path(__file__).parent / "_vend" / self.name).resolve(strict=False)))

	def __str__(self):
		return self.name

	def __repr__(self):
		return f"# VENDOR MODULE: {self}\n# VENDOR PATH: {self.path}"

class VendorModules(Enum):
	DILL = Vendor("dill")

def import_vendor_module(module: str, namespace: Optional[MutableMapping] = None) -> types.ModuleType:
	"""
	Import a module from vendor directory "toolbox/_vend/" and optionally inject it into 'namespace'
	"""
	try:
		return getattr(VendorModules, str(module).strip().upper()).value.import_module(namespace)
	except AttributeError as e:
		raise ImportError(f"No vendor module found: {module!r}") from e

#if __name__ == "__main__":
#	import_vendor_module("dill", globals())
#	print(dill.loads(dill.dumps("hello world")))