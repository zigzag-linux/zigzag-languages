import os
import sys
import logging
from .commands.zypper import ZypperCommand
from .commands.rpm import RpmCommand

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

def get_packages_to_install():
    recommended = ZypperCommand("packages", "-u", "--recommended").run()
    recommended_langpacks = {
        package for package in recommended if package.endswith("-lang")
    }

    zypper_all_lang = ZypperCommand("search", "-u", "*-lang").run()
    installed = RpmCommand("-qa").run()
    installed_with_lang_appended = {f"{package}-lang" for package in installed}

    langpacks_matching_installed = zypper_all_lang.intersection(
        installed_with_lang_appended
    )
    return langpacks_matching_installed.union(recommended_langpacks)


def install(package_list):
    if len(package_list) == 0:
        logging.info("No new language packages to install.")
        sys.exit(0)

    logging.info("Installing %s new language packages.", len(package_list))
    ZypperCommand("install", "-y", *package_list).run(process_output=False)


def run():
    if os.geteuid() != 0:
        logging.error("Script need to run with super user privileges.")
        sys.exit(1)

    logging.info("Searching for language packages...")
    to_install = get_packages_to_install()
    install(to_install)
