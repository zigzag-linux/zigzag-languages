from zigzag_languages.commands.zypper import ZypperCommand


def test_should_parse_zypper_output_two_packages(monkeypatch, zypper_stdout_two_packages):
    # given
    command = ZypperCommand("arg1", "arg2")
    monkeypatch.setattr(command, "_run_subprocess", zypper_stdout_two_packages)

    # when
    result = command.run()

    # then
    assert result == {"vlc-codecs", "vlc-codecs-debuginfo"}


def test_should_parse_zypper_output_no_packages(monkeypatch, zypper_stdout_no_packages):
    # given
    command = ZypperCommand("arg1", "arg2")
    monkeypatch.setattr(command, "_run_subprocess", zypper_stdout_no_packages)

    # when
    result = command.run()

    # then
    assert result == set()

