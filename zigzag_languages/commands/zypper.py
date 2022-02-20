from .subprocess import run_subprocess

SEPARATOR = "|"
BASE_ARGS = ("zypper", "--no-refresh")


def run_zypper(*args, process_output=True):
    full_args = BASE_ARGS + args
    raw_response = run_subprocess(full_args)

    return _parse_response(raw_response) if process_output else set()


def _parse_response(raw_response):
    linesplit = _run_linesplit(raw_response, _parse_header)
    if not linesplit:
        return set()

    column_count, column_name_idx = linesplit[0]
    parse_packages = lambda x: _parse_packages(x, column_count, column_name_idx)

    return set(_run_linesplit(raw_response, parse_packages))


def _parse_header(linesplit):
    """Parse table header to get number of columns and name column location"""
    if linesplit[0] != "S":
        return

    return len(linesplit), linesplit.index("Name")


def _parse_packages(linesplit, column_count, column_name_idx):
    """Parse lines that contain packages"""
    if len(linesplit) != column_count or linesplit[0] == "S":
        return

    return linesplit[column_name_idx]


def _run_linesplit(raw_response, func):
    result = []

    for line in raw_response.splitlines():
        linesplit = [segment.strip() for segment in line.split(SEPARATOR)]
        output = func(linesplit)

        if output is not None:
            result.append(output)

    return result
