import os
import logging
import sys
from subprocess import PIPE, run


def run_subprocess(full_args):
    result = run(
        full_args,
        stdout=PIPE,
        stderr=PIPE,
        universal_newlines=True,
        env=_get_run_env(),
    )

    if result.returncode != 0:
        logging.error(result.stderr)
        logging.error(
            "Command %s failed with status code %s",
            " ".join(full_args),
            result.returncode,
        )
        sys.exit(1)

    return result.stdout


def _get_run_env():
    env = dict(os.environ)
    env["LC_ALL"] = "C"

    return env
