from packaging.version import parse


def compare_versions(version_A: str, version_B: str) -> int:
    if parse(version_A) < parse(version_B):
        return -1
    elif parse(version_A) > parse(version_B):
        return 1
    return 0
