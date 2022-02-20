from ..commands.dnf import run_dnf
from .base import PackageBackend, AvailableBackends


class DnfBackend(PackageBackend):
    def get_backend_name(self):
        return AvailableBackends.DNF

    def get_language_packages(self, installed_packages):
        recommended = run_dnf(
            "--cacheonly",
            "repoquery-n",
            "--qf",
            "%{name}",
            "--latest-limit=1",
            "--whatsupplements",
            ",".join(installed_packages),
            "*-lang",
        )
        return recommended.difference(installed_packages)

    def install_new(self, language_packages):
        run_dnf("install", "-y", *language_packages)
