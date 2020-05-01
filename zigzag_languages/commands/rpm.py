from .base import PackageCommand


class RpmCommand(PackageCommand):
    BASE_ARGS = ["rpm", "--qf", "%{NAME}\n"]

    def run(self):
        full_args = self.BASE_ARGS + self._supplied_args
        output = self._run_subprocess(full_args)

        return set(output.splitlines())
