from .base import PackageCommand


class ZypperCommand(PackageCommand):
    SEPARATOR = "|"
    BASE_ARGS = ["zypper", "--no-refresh"]

    column_count = None
    column_name_idx = None

    def run(self, process_output=True):
        full_args = self.BASE_ARGS + self._supplied_args
        raw_response = self._run_subprocess(full_args)

        return self._parse_response(raw_response) if process_output else set()

    def _parse_response(self, raw_response):
        header = self._run_linesplit(raw_response, self._parse_header)[0]
        self.column_count = header[0]
        self.column_name_idx = header[1]

        return set(self._run_linesplit(raw_response, self._parse_packages))

    def _parse_header(self, linesplit):
        """Parse table header to get number of columns and name column location"""
        if linesplit[0] != "S":
            return

        return len(linesplit), linesplit.index("Name")

    def _parse_packages(self, linesplit):
        """Parse lines that contain packages"""
        if len(linesplit) != self.column_count or linesplit[0] == "S":
            return

        return linesplit[self.column_name_idx]

    def _run_linesplit(self, raw_response, func):
        result = []

        for line in raw_response.splitlines():
            linesplit = [segment.strip() for segment in line.split(self.SEPARATOR)]
            output = func(linesplit)

            if output is not None:
                result.append(output)

        return result
