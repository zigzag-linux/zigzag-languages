from .subprocess import run_subprocess

BASE_ARGS = ("dnf", "--quiet")


def run_dnf(*args):
    full_args = BASE_ARGS + args
    output = run_subprocess(full_args)

    return set(output.splitlines())
