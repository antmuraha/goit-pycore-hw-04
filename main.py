
from libs.get_cats_info import get_cats_info
from libs.total_salary import total_salary


path_file = "tests/source/salary_file.txt"
total, average = total_salary(path_file)
print(f"Total salary: {total}, Average salary: {average}", "\n")

path_file = "tests/source/cats_file.txt"
cats_info = get_cats_info(path_file)
print(cats_info, "\n")
