from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class RawSearchHit:
    title: str
    url: str
    snippet: str


class SearchProvider(ABC):
    @abstractmethod
    async def search(self, query: str, limit: int = 5) -> list[RawSearchHit]: ...
