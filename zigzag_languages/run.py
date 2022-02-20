import os
import sys
import logging
import shutil
from .commands.rpm import run_rpm
from .backends.zypper import ZypperBackend
from .backends.dnf import DnfBackend

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


def run():
    if os.geteuid() != 0:
        logging.error("Script need to run with super user privileges.")
        sys.exit(1)

    backend = choose_backend()
    logging.info("Backend %s choosen", backend.get_backend_name())
    logging.info("Looking for language packages...")
    installed = run_rpm("-qa")
    to_install = backend.get_language_packages(installed)
    install(backend, to_install)


def choose_backend():
    return ZypperBackend() if shutil.which("zypper") else DnfBackend()


def install(backend, package_list):
    if len(package_list) == 0:
        logging.info("No new language packages to install.")
        sys.exit(0)

    logging.info("Installing %s new language packages.", len(package_list))
    backend.install_new(package_list)
