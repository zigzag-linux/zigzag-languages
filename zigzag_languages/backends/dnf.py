from ..commands.dnf import run_dnf
from .base import PackageBackend, AvailableBackends

COMMON_ARGS = (
    "--cacheonly",
    "repoquery-n",
    "--qf",
    "%{name}",
)


class DnfBackend(PackageBackend):
    def get_backend_name(self):
        return AvailableBackends.DNF

    def get_language_packages(self, installed_packages):
        provided = self._get_provided_packages()
        recommended = run_dnf(
            *COMMON_ARGS,
            "--latest-limit=1",
            "--whatsupplements",
            ",".join(provided),
            "*-lang",
        )
        return recommended.difference(installed_packages)

    def install_new(self, language_packages):
        run_dnf("install", "-y", *language_packages)

    def _get_provided_packages(self):
        """get all provided package-like capabilities"""
        all_capabilities = run_dnf(*COMMON_ARGS, "--provides", "--installed")

        return {
            line.split(" ")[0]
            for line in all_capabilities
            if "=" in line and "(" not in line
        }
