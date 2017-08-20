from cdb_creator.cdb import cdb_creator


class clang_complete(cdb_creator):
    def generate_cdb(self, root_dir, result_dir):
        self.root_dir = root_dir
        self.result_dir = result_dir
        pass

    def add_exclude_dir(self, exclude_dir):
        pass

    def add_exclude_define(self, define):
        pass
