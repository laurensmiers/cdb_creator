import unittest
import os
from cdb_creator.clang_complete import clang_complete

def path_in_cdb_file(cdb_file, path):
    inc_prefix = "-I"
    occurences = 0
    for line in cdb_file:
        # remove trailling whitespace, newlines, ...
        line = line.rstrip()
        # first part of line should be "-I"
        if (line[0:2] == inc_prefix) and (line[2:] == path):
            occurences += 1
    return occurences


class test_clang_complete(unittest.TestCase):
    test_dir = "test_dir"

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        cb_file = os.path.join(cls.test_dir, ".clang_complete")
        # TODO: setup tmp dir with header files
        try:
            os.remove(cb_file)
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        # TODO: see setUpClass TODO, remove temp dir
        cb_file = os.path.join(cls.test_dir, ".clang_complete")
        try:
            os.remove(cb_file)
        except FileNotFoundError:
            pass

    def test_creation(self):
        self.cdb = clang_complete()

    def test_generate(self):
        self.cdb = clang_complete()
        self.cdb.generate_cdb(self.test_dir)
        # root_dir is set correctly
        self.assertTrue(self.cdb.root_dir == self.test_dir)
        # .clang_complete file is generated
        cdb_file_location = os.path.join(self.test_dir, ".clang_complete")
        self.assertTrue(os.path.exists(cdb_file_location))

    def test_cb_file_filled_with_includes(self):
        cdb_file_location = os.path.join(self.test_dir, ".clang_complete")
        inc_paths = ["./src/inc", "./inc"]

        self.cdb = clang_complete()
        self.cdb.generate_cdb(self.test_dir)

        # check if include paths are in cdb file
        # AND they are mentioned only once!
        for inc_path in inc_paths:
            with open(cdb_file_location, 'r') as cdb_file:
                print("\nCheck if ", inc_path, "is in ", cdb_file_location, "...")
                self.assertTrue(path_in_cdb_file(cdb_file, inc_path) == 1)


if __name__ == '__main__':
    unittest.main()
