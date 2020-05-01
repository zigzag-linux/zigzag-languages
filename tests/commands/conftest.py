import pytest


@pytest.fixture
def zypper_stdout_two_packages():
    return lambda x: """
Loading repository data...
Reading installed packages...

S  | Name                 | Summary                                    | Type   
---+----------------------+--------------------------------------------+--------
i+ | vlc-codecs           | Additional codecs for the VLC media player | package
   | vlc-codecs-debuginfo | Debug information for package vlc-codecs   | package
    """


@pytest.fixture
def zypper_stdout_no_packages():
    return lambda x: """
Loading repository data...
Reading installed packages...
No matching items found.
"""
