from typing import Any, Callable
from dataclasses import dataclass, field

@dataclass
def LazyLoader:
	name: str
	factory: Callable

	def __getattr__(self, attr_name: str) -> Any:
		if str(attr_name) == self.name:
			return self.load()

	def load(self) -> Any:
		if not hasattr(self, 'data'):
			self.data = self.factory()
		return self.data
