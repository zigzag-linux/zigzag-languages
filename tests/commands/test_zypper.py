from zigzag_languages.commands.zypper import run_zypper
from unittest.mock import patch


def test_should_parse_zypper_output_two_packages(zypper_stdout_two_packages):
    with patch(
        "zigzag_languages.commands.zypper.run_subprocess",
        return_value=zypper_stdout_two_packages,
    ):
        # when
        result = run_zypper("arg1", "arg2")

        # then
        assert result == {"vlc-codecs", "vlc-codecs-debuginfo"}


def test_should_parse_zypper_output_no_packages(monkeypatch, zypper_stdout_no_packages):
    with patch(
        "zigzag_languages.commands.zypper.run_subprocess",
        return_value=zypper_stdout_no_packages,
    ):
        # when
        result = run_zypper("arg1", "arg2")

        # then
        assert result == set()
