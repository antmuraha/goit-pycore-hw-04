
import typing
from pathlib import Path

SEPARATOR_SYMBOL = ","
ID_LENGTH = 24


# Define the type for a single cat
class Cat(typing.TypedDict):
    id: str
    name: str
    age: int


# Define the type for a list of such dictionaries
CatsList = typing.List[Cat]


def get_cats_info(path: str) -> tuple[int, int]:
    cats: CatsList = []
    file = Path(path)

    if not file.exists():
        print(f"[ERROR] File {file.absolute()} not exist")
        return None

    with open(file.absolute(), encoding="utf-8") as content:
        for index, line in enumerate(content.readlines()):
            if line.strip():
                try:
                    id, name, age = prepare_line_data(index + 1, line)
                    cats.append({
                        "id": id,
                        "name": name,
                        "age": str(age)
                    })
                except ExceptionId as e:
                    print(f"[ERROR] File {file.absolute()}. {str(e)}")
                    return None
                except ExceptionName as e:
                    print(f"[ERROR] File {file.absolute()}. {str(e)}")
                    return None
                except ExceptionAge as e:
                    print(f"[ERROR] File {file.absolute()}. {str(e)}")
                    return None
                except Exception as e:
                    print(
                        f"[ERROR] File {file.absolute()}. Line '{index + 1}'. {str(e)}")
                    return None
            else:
                print(f"[INFO] File {file.absolute()}. Line {index + 1} is empty")

    return cats


def prepare_line_data(index: int, line: str) -> str:
    id, name, age = line.split(SEPARATOR_SYMBOL)
    return (prepare_id(index, id), prepare_name(index, name), prepare_age(index, age))


def prepare_id(index: int, id: str) -> str:
    pre_id = id.strip()
    if not pre_id or len(pre_id) != ID_LENGTH:
        raise ExceptionId(index)
    return pre_id


def prepare_name(index: int, name: str) -> str:
    pre_name = name.strip()
    if not pre_name:
        raise ExceptionName(index)
    return pre_name


def prepare_age(index: int, age: str) -> int:
    try:
        pre_age = int(age.strip())
        if not isinstance(pre_age, int) or not pre_age:
            raise ExceptionAge(index)
        return pre_age
    except:
        raise ExceptionAge(index)


class ExceptionId(Exception):
    def __init__(self, line: int) -> None:
        super().__init__(f"The ID in line '{line}' is incorrect")


class ExceptionName(Exception):
    def __init__(self, line: int) -> None:
        super().__init__(f"The Name in line '{line}' is incorrect")


class ExceptionAge(Exception):
    def __init__(self, line: int) -> None:
        super().__init__(f"The Age in line '{line}' is incorrect")
