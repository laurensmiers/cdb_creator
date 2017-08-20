import os
import glob
from cdb_creator.cdb import cdb_creator


class clang_complete(cdb_creator):
    def __get_header_files_iterator(self, root_dir):
        old_pwd = os.getcwd()
        os.chdir(root_dir)
        header_iterator = glob.iglob("**/*.h", recursive=True)
        os.chdir(old_pwd)
        return header_iterator

    def generate_cdb(self, root_dir):
        self.root_dir = root_dir
        cdb_file_name = os.path.join(self.root_dir, ".clang_complete")
        header_files_iterator = self.__get_header_files_iterator(self.root_dir)
        known_inc_dirs = set()

        with open(cdb_file_name, "w+") as cdb_file:
            for inc_file_name in header_files_iterator:
                # make relative path from header file path
                inc_file_transformed = inc_file_name.replace(root_dir, ".")
                inc_dir = os.path.dirname(inc_file_transformed)

                if inc_dir not in known_inc_dirs:
                    known_inc_dirs.add(inc_dir)
                    cdb_file.write("-I" + str(inc_dir) + "\n")

    def add_exclude_dir(self, exclude_dir):
        pass

    def add_exclude_define(self, exclude_define):
        pass


if __name__ == '__main__':
    import argparse
    cbd = clang_complete()

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--root_dir",
                        required=True,
                        help="Directory where you want to run and store .clang_complete cdb file")
    args = parser.parse_args()

    if (os.path.exists(args.root_dir)):
        cbd.generate_cdb(args.root_dir)
    else:
        print("Error: supply a valid directory")
