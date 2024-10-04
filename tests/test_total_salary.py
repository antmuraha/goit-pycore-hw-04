import io
import os
import sys
import unittest

from libs.total_salary import total_salary

SOURCE_PATH = "tests/source"
# Get the current working directory
current_directory = os.getcwd()


class TestTotalSalary(unittest.TestCase):

    def run_total_salary(self, path_file):
        # Create a StringIO object to capture the output
        captured_output = io.StringIO()
        # Redirect stdout to the StringIO object
        sys.stdout = captured_output

        result = total_salary(path_file)

        # Reset stdout back to its original state
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        output = output.replace(current_directory, "")

        return result, output

    def test_total_salary(self):
        file = "salary_file.txt"
        path_file = f"{SOURCE_PATH}/{file}"

        result, output = self.run_total_salary(path_file)

        expected_logs = ""\
            f"[INFO] File /tests/source/{file}. Line 3 is empty\n"\
            f"[INFO] File /tests/source/{file}. Line 5 is empty"

        self.assertEqual(expected_logs, output)
        self.assertEqual(result[0], 6000)
        self.assertEqual(result[1], 2000)

    def test_salary_file_bad_1(self):
        file = "salary_file_bad_1.txt"
        path_file = f"{SOURCE_PATH}/{file}"

        cats_info, output = self.run_total_salary(path_file)

        expected_logs = f"[ERROR] File /tests/source/{file}. The Salary in line '2' is incorrect"
        expected_list = None

        self.assertEqual(expected_logs, output)
        self.assertEqual(expected_list, cats_info)

    def test_salary_file_bad_2(self):
        file = "salary_file_bad_2.txt"
        path_file = f"{SOURCE_PATH}/{file}"

        result, output = self.run_total_salary(path_file)

        expected_logs = f"[ERROR] File /tests/source/{file}. The Name in line '3' is incorrect"

        self.assertEqual(expected_logs, output)
        self.assertEqual(result, None)

    def test_salary_file_bad_3(self):
        file = "salary_file_bad_3.txt"
        path_file = f"{SOURCE_PATH}/{file}"

        result, output = self.run_total_salary(path_file)

        expected_logs = f"[ERROR] File /tests/source/{file}. Line '1'. too many values to unpack (expected 2)"

        self.assertEqual(expected_logs, output)
        self.assertEqual(result, None)

    def test_salary_file_bad_4(self):
        file = "salary_file_bad_4.txt"
        path_file = f"{SOURCE_PATH}/{file}"

        result, output = self.run_total_salary(path_file)

        expected_logs = f"[ERROR] File /tests/source/{file}. The Salary in line '1' is incorrect"

        self.assertEqual(expected_logs, output)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
