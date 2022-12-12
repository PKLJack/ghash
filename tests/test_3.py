from pprint import pprint as pp
from ghash.utils import dict_unnest


""" 
The files comes from a very good place.
"""
data_input = {
    "crc32": {
        "D:\\fake-dir\\README.rst": "FF903451",
        "D:\\fake-dir\\setup.py": "2B908073",
    },
    "md5": {
        "D:\\fake-dir\\README.rst": "1ff407b7687e21f59c0bee1215c46e88",
        "D:\\fake-dir\\setup.py": "e62a11d4bf850ecfc34e67d1c09cc6db",
    },
    "sha1": {
        "D:\\fake-dir\\README.rst": "41055544c276fac0c01fefb7ee9e17774282dce4",
        "D:\\fake-dir\\setup.py": "8de72f11c2d9dedcf7d70745fd1cbf50416f9447",
    },
    "sha224": {
        "D:\\fake-dir\\README.rst": "88bc91c2068662c32f582d378a7edfc9ed4b03c074f40d6a8d30b1f6",
        "D:\\fake-dir\\setup.py": "38301f12f656fa7a58e33ac81ae17cc9bf080637ab96cae571cf2e82",
    },
    "sha256": {
        "D:\\fake-dir\\README.rst": "7f6e38aaf8c60db7247a2a43df0726137275d616448fd37aae4a182eaa3b16a7",
        "D:\\fake-dir\\setup.py": "0cd25227e3b767b54aac4477667688384461ccc49bb28db7eb7980f426c6f308",
    },
    "sha384": {
        "D:\\fake-dir\\README.rst": "91c4fdc1d7675d7736fcf9d3c7a18da9d83a7d89ebde9d3bddf65d98eb879a26c4a2fc1a9bda86abcba04f11a9148f16",
        "D:\\fake-dir\\setup.py": "4f826c4bf571425dbe24d0d7ace0c246032fa57f41d8f7dd4ca42ef18a2282f44bbd55756faa46bf1d67233350dd47ba",
    },
    "sha512": {
        "D:\\fake-dir\\README.rst": "d9ed51a7bc51b1bd659470d090c1ef119322a5ef282c608f5369910216b955bd70ac21b3cce2d48b684c2e6630e8ae3eea05855ec908ac39f24cc15d879b33d5",
        "D:\\fake-dir\\setup.py": "e0a5f514f47f00ff5893e2b6efff59f52aaa9d911f8535dd5422baea85b87b9ed80026dce0756349cf8548cba80fc6845144be5d88b8292f0bffa299e41efea3",
    },
}

data_output = [
    # fmt: off
    ["D:\\fake-dir\\README.rst", "crc32", "FF903451"],
    ["D:\\fake-dir\\setup.py", "crc32", "2B908073"],
    ["D:\\fake-dir\\README.rst", "md5", "1ff407b7687e21f59c0bee1215c46e88"],
    ["D:\\fake-dir\\setup.py", "md5", "e62a11d4bf850ecfc34e67d1c09cc6db"],
    ["D:\\fake-dir\\README.rst", "sha1", "41055544c276fac0c01fefb7ee9e17774282dce4"],
    ["D:\\fake-dir\\setup.py", "sha1", "8de72f11c2d9dedcf7d70745fd1cbf50416f9447"],
    ["D:\\fake-dir\\README.rst", "sha224", "88bc91c2068662c32f582d378a7edfc9ed4b03c074f40d6a8d30b1f6"],
    ["D:\\fake-dir\\setup.py", "sha224", "38301f12f656fa7a58e33ac81ae17cc9bf080637ab96cae571cf2e82"],
    ["D:\\fake-dir\\README.rst", "sha256", "7f6e38aaf8c60db7247a2a43df0726137275d616448fd37aae4a182eaa3b16a7"],
    ["D:\\fake-dir\\setup.py", "sha256", "0cd25227e3b767b54aac4477667688384461ccc49bb28db7eb7980f426c6f308"],
    ["D:\\fake-dir\\README.rst", "sha384", "91c4fdc1d7675d7736fcf9d3c7a18da9d83a7d89ebde9d3bddf65d98eb879a26c4a2fc1a9bda86abcba04f11a9148f16"],
    ["D:\\fake-dir\\setup.py", "sha384", "4f826c4bf571425dbe24d0d7ace0c246032fa57f41d8f7dd4ca42ef18a2282f44bbd55756faa46bf1d67233350dd47ba"],
    ["D:\\fake-dir\\README.rst", "sha512", "d9ed51a7bc51b1bd659470d090c1ef119322a5ef282c608f5369910216b955bd70ac21b3cce2d48b684c2e6630e8ae3eea05855ec908ac39f24cc15d879b33d5"],
    ["D:\\fake-dir\\setup.py", "sha512", "e0a5f514f47f00ff5893e2b6efff59f52aaa9d911f8535dd5422baea85b87b9ed80026dce0756349cf8548cba80fc6845144be5d88b8292f0bffa299e41efea3"],
]


def test_dict_unnest():
    """ """
    assert dict_unnest(data_input, True) == data_output
