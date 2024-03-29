from .subprocess import run_subprocess

BASE_ARGS = ("rpm", "--qf", "%{name}\n")


def run_rpm(*args):
    full_args = BASE_ARGS + args
    output = run_subprocess(full_args)

    return set(output.splitlines())
