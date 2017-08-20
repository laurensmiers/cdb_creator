import unittest
import os
import shutil
from cdb_creator.clang_complete import clang_complete


class test_clang_complete(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("make tmp dir for testing...\n")
        os.mkdir("tmp_test_dir")
        os.mkdir("tmp_test_dir/src")
        os.mkdir("tmp_test_dir/src/inc")
        os.mkdir("tmp_test_dir/include")

    @classmethod
    def tearDownClass(cls):
        print("remove tmp dir...\n")
        shutil.rmtree("tmp_test_dir")

    def test_0(self):
        self.cdb = clang_complete()


if __name__ == '__main__':
    unittest.main()
