#  Project : SDE Placement Questions
#  Filename : first_bad_version.py
#  Author : thameem
#  Created  time : Wed, 29 Dec 2021 at 12:54 AM India Standard Time
#  Last modified time : Wed, 29 Dec 2021 at 12:52 AM India Standard Time
from beartype import beartype


class SetBadVersion:
    def set_bad_version(self: 'SetBadVersion', latest_version: int) -> None:
        pass

    @staticmethod
    def is_bad_version(version: int) -> bool:
        pass


class FirstBadVersion:
    @beartype
    def __init__(self: 'FirstBadVersion', latest_version: int) -> None:
        first_version = 1
        while first_version < latest_version:
            mid_version = first_version + (latest_version - first_version) // 2
            if SetBadVersion.is_bad_version(mid_version):
                latest_version = mid_version
            else:
                first_version = mid_version + 1

        self.first_bad_version = first_version
