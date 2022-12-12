import hashlib
import zlib
from pathlib import Path
from typing import Callable, Optional, Union


class ShortHasher:  # Not in use
    """For small files only"""

    @staticmethod
    def crc32(bytes_: bytes) -> str:
        return f"{zlib.crc32(bytes_):#X}"[2:]

    @staticmethod
    def md5(bytes_: bytes) -> str:
        return hashlib.md5(bytes_).hexdigest()

    @staticmethod
    def sha1(bytes_: bytes) -> str:
        return hashlib.sha1(bytes_).hexdigest()

    @staticmethod
    def sha224(bytes_: bytes) -> str:
        return hashlib.sha224(bytes_).hexdigest()

    @staticmethod
    def sha256(bytes_: bytes) -> str:
        return hashlib.sha256(bytes_).hexdigest()

    @staticmethod
    def sha384(bytes_: bytes) -> str:
        return hashlib.sha384(bytes_).hexdigest()

    @staticmethod
    def sha512(bytes_: bytes) -> str:
        return hashlib.sha512(bytes_).hexdigest()


class FileHasher:
    """Can handle large files"""

    def __init__(self, file_path: Path, algorithm: str) -> None:
        self.hash_func = self.get_hash_func(algorithm)
        self.fp = file_path.resolve()
        self.algorithm = algorithm.lower()
        self.buffer_size = 2**10 * 8

    def crc32(self, bytes_: bytes) -> str:
        return f"{zlib.crc32(bytes_):#X}"[2:]

    def run(self) -> str:
        """ """
        if self.algorithm == "crc32":
            return self.crc32(self.fp.read_bytes())

        # Not crc32
        hasher: hashlib._Hash = self.hash_func()

        with open(self.fp, "rb") as f:
            chunk = f.read(self.buffer_size)
            while chunk:
                hasher.update(chunk)
                chunk = f.read(self.buffer_size)

        return hasher.hexdigest()

    def get_hash_func(self, algorithm: str) -> Callable:
        """ """
        table = {
            "sha1": hashlib.sha1,
            "sha224": hashlib.sha224,
            "sha256": hashlib.sha256,
            "sha384": hashlib.sha384,
            "sha512": hashlib.sha512,
            "md5": hashlib.md5,
            "crc32": zlib.crc32,
        }

        if algorithm not in table:
            raise KeyError(f"Algorithm Not Found: {algorithm}")

        return table[algorithm]  # type: ignore
