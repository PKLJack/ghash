from pathlib import Path


def flatten_dirs(filepaths: list[Path]) -> list[Path]:
    """Keep files and expand directories"""
    retval = []

    for fp in filepaths:
        if not fp.is_dir():
            retval.append(fp)
            continue

        # Explore dirs
        for x in fp.iterdir():
            retval.append(x)

    retval.sort()

    return retval


def dict_unnest(dic: dict[str, dict[str, str]], keep_algo: bool) -> list[list[str]]:
    """
    Returns list of
    [
        [file, algo, hash], or [file, hash]
        [...],
        ...
    ]
    """
    retval = []

    for k1, v1 in dic.items():
        for k2, v2 in v1.items():
            if keep_algo:
                retval.append([k2, k1, v2])
            else:
                retval.append([k2, v2])

    return retval
