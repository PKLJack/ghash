import hashlib
import zlib
from pathlib import Path
import pytest

""" 
Available algorithms:
{
    "md5",
    "sha1", "sha224", "sha256", "sha384", "sha512",
    "blake2b", "blake2s",
    "shake_128", "shake_256",
    "sha3_224", "sha3_256", "sha3_384", "sha3_512",
}
"""
from ghash.hasher import FileHasher

file1 = Path(__file__).resolve().parent / "test_files" / "hello1.txt"


file1_sums = {
    "crc32": "F866A9E6",
    "md5": "9053253e972cf40443a4083f452f24d4",
    "sha1": "495b10744ee2c4d5423d7e25e7632d31db08fc00",
    "sha224": "dd35c187eaed6ec99b7fa91adf95baec1764aa857a72c91723f2fa85",
    "sha256": "15b4d8e3c2d7987b16be2cfba411d5fbd980340d3736ad61913aba0ffaf3608c",
    "sha384": "a7429db6d4c05619a7eb8917a8cb8513ad7f535091bc01b4667f884634e3a3f6dfb96d2acafd2fa445274b59f9481569",
    "sha512": "5a3d898311876b67bffacdd911908301a6ceb0f1256ddc1bbdbf130beed31f3db726c9cc7eac9dc7f70911df319c30a4509db302a271e72bf8d64c0d73718c7e",
}


assert file1.exists(), f"Cannot locate {file1}"


class TestSimpleCall:
    def test_crc32(self):
        b1 = file1.read_bytes()
        assert f"{zlib.crc32(b1):#X}"[2:] == file1_sums["crc32"]

    def test_md5(self):
        b1 = file1.read_bytes()
        assert hashlib.md5(b1).hexdigest() == file1_sums["md5"]

    def test_sha1(self):
        b1 = file1.read_bytes()
        assert hashlib.sha1(b1).hexdigest() == file1_sums["sha1"]

    def test_sha224(self):
        b1 = file1.read_bytes()
        assert hashlib.sha224(b1).hexdigest() == file1_sums["sha224"]

    def test_sha256(self):
        b1 = file1.read_bytes()
        assert hashlib.sha256(b1).hexdigest() == file1_sums["sha256"]

    def test_sha384(self):
        b1 = file1.read_bytes()
        assert hashlib.sha384(b1).hexdigest() == file1_sums["sha384"]

    def test_sha512(self):
        b1 = file1.read_bytes()
        assert hashlib.sha512(b1).hexdigest() == file1_sums["sha512"]


class TestHashFile:
    def test_crc32(self):
        """ """
        hasher = FileHasher(file1, "crc32")
        assert hasher.run() == file1_sums["crc32"]

    def test_md5(self):
        """ """
        hasher = FileHasher(file1, "md5")
        assert hasher.run() == file1_sums["md5"]

    def test_sha1(self):
        """ """
        hasher = FileHasher(file1, "sha1")
        assert hasher.run() == file1_sums["sha1"]

    def test_sha224(self):
        """ """
        hasher = FileHasher(file1, "sha224")
        assert hasher.run() == file1_sums["sha224"]

    def test_sha256(self):
        """ """
        hasher = FileHasher(file1, "sha256")
        assert hasher.run() == file1_sums["sha256"]

    def test_sha384(self):
        """ """
        hasher = FileHasher(file1, "sha384")
        assert hasher.run() == file1_sums["sha384"]

    def test_sha512(self):
        """ """
        hasher = FileHasher(file1, "sha512")
        assert hasher.run() == file1_sums["sha512"]
