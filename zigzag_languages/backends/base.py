from abc import ABC, abstractmethod
from enum import Enum, auto


class AvailableBackends(Enum):
    ZYPPER = auto()
    DNF = auto()


class PackageBackend(ABC):
    @abstractmethod
    def get_backend_name(self):
        pass

    @abstractmethod
    def get_language_packages(self, installed_packages):
        pass

    @abstractmethod
    def install_new(self, language_packages):
        pass
