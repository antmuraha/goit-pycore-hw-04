
from pathlib import Path

SEPARATOR_SYMBOL = ","


def total_salary(path: str) -> tuple[int, int]:
    total = 0
    file = Path(path)

    if not file.exists():
        print(f"[ERROR] File {file.absolute()} not exist")
        return None

    count = 0
    with open(file.absolute(), encoding="utf-8") as content:
        for index, line in enumerate(content.readlines()):
            if line.strip():
                try:
                    name, salary = prepare_line_data(index + 1, line)
                    total += salary
                    count += 1
                except ExceptionName as e:
                    print(f"[ERROR] File {file.absolute()}. {str(e)}")
                    return None
                except ExceptionSalary as e:
                    print(f"[ERROR] File {file.absolute()}. {str(e)}")
                    return None
                except Exception as e:
                    print(
                        f"[ERROR] File {file.absolute()}. Line '{index + 1}'. {str(e)}")
                    return None
            else:
                print(
                    f"[INFO] File {file.absolute()}. Line {index + 1} is empty")

    return (total, int(total / count))


def prepare_line_data(index: int, line: str) -> str:
    name, salary = line.split(SEPARATOR_SYMBOL)
    return (prepare_name(index, name), prepare_salary(index, salary))


def prepare_name(index: int, name: str) -> str:
    pre_name = name.strip()
    if not pre_name:
        raise ExceptionName(index)
    return pre_name


def prepare_salary(index: int, salary: str) -> int:
    try:
        pre_salary = int(salary.strip())
        if not isinstance(pre_salary, int) or not pre_salary:
            raise ExceptionSalary(index)
        return pre_salary
    except:
        raise ExceptionSalary(index)


class ExceptionName(Exception):
    def __init__(self, line: int) -> None:
        super().__init__(f"The Name in line '{line}' is incorrect")


class ExceptionSalary(Exception):
    def __init__(self, line: int) -> None:
        super().__init__(f"The Salary in line '{line}' is incorrect")
