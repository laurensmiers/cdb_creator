from abc import ABCMeta, abstractmethod


class cdb_creator(metaclass=ABCMeta):
    @abstractmethod
    def generate_cdb(self, result_dir):
        pass

    @abstractmethod
    def add_exclude_dir(self, exclude_dir):
        pass

    @abstractmethod
    def add_exclude_define(self, exclude_define):
        pass
