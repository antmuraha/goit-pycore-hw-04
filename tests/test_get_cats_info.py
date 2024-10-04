import io
import os
import sys
import unittest

from libs.get_cats_info import get_cats_info

SOURCE_PATH = "tests/source"
# Get the current working directory
current_directory = os.getcwd()


class TestGetCatsInfo(unittest.TestCase):

    def run_get_cats_info(self, path_file):
        # Create a StringIO object to capture the output
        captured_output = io.StringIO()
        # Redirect stdout to the StringIO object
        sys.stdout = captured_output

        cats_info = get_cats_info(path_file)

        # Reset stdout back to its original state
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        output = output.replace(current_directory, "")

        return cats_info, output

    def test_get_cats_info(self):
        file = "cats_file.txt"
        path_file = f"{SOURCE_PATH}/{file}"

        cats_info, output = self.run_get_cats_info(path_file)

        expected_logs = ""\
            f"[INFO] File /tests/source/{file}. Line 2 is empty\n"\
            f"[INFO] File /tests/source/{file}. Line 6 is empty"
        expected_list = [
            {'id': '60b90c1c13067a15887e1ae1', 'name': 'Tayson', 'age': '3'},
            {'id': '60b90c2413067a15887e1ae2', 'name': 'Vika', 'age': '1'},
            {'id': '60b90c2e13067a15887e1ae3', 'name': 'Barsik', 'age': '2'},
            {'id': '60b90c3b13067a15887e1ae4', 'name': 'Simon', 'age': '12'},
            {'id': '60b90c4613067a15887e1ae5', 'name': 'Tessi', 'age': '5'}]

        self.assertEqual(expected_logs, output)
        self.assertEqual(expected_list, cats_info)

    def test_cats_file_bad_1(self):
        file = "cats_file_bad_1.txt"
        path_file = f"{SOURCE_PATH}/{file}"

        cats_info, output = self.run_get_cats_info(path_file)

        expected_logs = f"[ERROR] File /tests/source/{file}. Line '1'. too many values to unpack (expected 3)"
        expected_list = None

        self.assertEqual(expected_logs, output)
        self.assertEqual(expected_list, cats_info)

    def test_cats_file_bad_2(self):
        file = "cats_file_bad_2.txt"
        path_file = f"{SOURCE_PATH}/{file}"

        cats_info, output = self.run_get_cats_info(path_file)

        expected_logs = f"[ERROR] File /tests/source/{file}. The ID in line '2' is incorrect"
        expected_list = None

        self.assertEqual(expected_logs, output)
        self.assertEqual(expected_list, cats_info)

    def test_cats_file_bad_3(self):
        file = "cats_file_bad_3.txt"
        path_file = f"{SOURCE_PATH}/{file}"

        cats_info, output = self.run_get_cats_info(path_file)

        expected_logs = f"[ERROR] File /tests/source/{file}. The Age in line '2' is incorrect"
        expected_list = None

        self.assertEqual(expected_logs, output)
        self.assertEqual(expected_list, cats_info)

    def test_cats_file_bad_4(self):
        file = "cats_file_bad_4.txt"
        path_file = f"{SOURCE_PATH}/{file}"

        cats_info, output = self.run_get_cats_info(path_file)

        expected_logs = f"[ERROR] File /tests/source/{file}. The ID in line '5' is incorrect"
        expected_list = None

        self.assertEqual(expected_logs, output)
        self.assertEqual(expected_list, cats_info)


if __name__ == '__main__':
    unittest.main()
