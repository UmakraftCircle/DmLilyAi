"""Embedders. The default is a local, deterministic hashing embedder (no API, no cost).

Swap in a neural embedder by implementing `Embedder`.
"""
import hashlib
import math
from abc import ABC, abstractmethod

from LilyAiCore.Helpers.text import tokenize


class Embedder(ABC):
    dim: int

    @abstractmethod
    def embed(self, text: str) -> list[float]: ...

    def embed_many(self, texts: list[str]) -> list[list[float]]:
        return [self.embed(t) for t in texts]


class HashingEmbedder(Embedder):
    def __init__(self, dim: int = 512):
        self.dim = dim

    def _bucket(self, feature: str) -> tuple[int, float]:
        h = int.from_bytes(hashlib.blake2b(feature.encode("utf-8"), digest_size=8).digest(), "big")
        return h % self.dim, 1.0 if (h >> 63) & 1 else -1.0

    def embed(self, text: str) -> list[float]:
        vec = [0.0] * self.dim
        toks = tokenize(text)
        features = toks + [f"{a}_{b}" for a, b in zip(toks, toks[1:])]
        for f in features:
            idx, sign = self._bucket(f)
            vec[idx] += sign * (1.0 if "_" not in f else 0.7)
        norm = math.sqrt(sum(v * v for v in vec)) or 1.0
        return [v / norm for v in vec]
