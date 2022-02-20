from ..commands.zypper import run_zypper
from .base import PackageBackend, AvailableBackends


class ZypperBackend(PackageBackend):
    def get_backend_name(self):
        return AvailableBackends.ZYPPER

    def get_language_packages(self, installed_packages):
        recommended = run_zypper("packages", "-u", "--recommended")
        recommended_langpacks = {
            package for package in recommended if package.endswith("-lang")
        }

        zypper_all_lang = run_zypper("search", "-u", "*-lang")
        installed_with_lang_appended = {
            f"{package}-lang" for package in installed_packages
        }

        langpacks_matching_installed = zypper_all_lang.intersection(
            installed_with_lang_appended
        )
        return langpacks_matching_installed.union(recommended_langpacks)

    def install_new(self, language_packages):
        run_zypper("install", "-y", *language_packages, process_output=False)
