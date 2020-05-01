import os
import logging
import sys
from subprocess import PIPE, run


class PackageCommand:
    _supplied_args = None

    def __init__(self, *args):
        self._supplied_args = list(args)

    def _run_subprocess(self, full_args):
        result = run(
            full_args,
            stdout=PIPE,
            stderr=PIPE,
            universal_newlines=True,
            env=self._get_run_env(),
        )

        if result.returncode != 0:
            logging.error(result.stderr)
            logging.error("Command %s failed with status code %s", " ".join(full_args), result.returncode)
            sys.exit(1)

        return result.stdout

    def _get_run_env(self):
        env = dict(os.environ)
        env["LC_ALL"] = "C"

        return env
