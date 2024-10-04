from pathlib import Path
import typing

from colorama import Fore, Style


class ResultItem(typing.TypedDict):
    level: int
    name: str
    is_dir: bool


ResultList = typing.List[ResultItem]

DEFAULT_INDENT = "    "


def listing_files(result: ResultList, path=".", level=0):
    """
    This function takes a directory path and returns a list of all subdirectories and files
    Example:
        # List for results\n
        result = []

        # Current dir\n
        listing_files(result, ".")

        # Relative path to some_dir\n
        listing_files(result, "some_dir")

        # Absolutely path to some_dir\n
        listing_files(result, "/absolutely-to/some_dir")
    """

    directory = Path(path)
    if level == 0 and not directory.exists():
        raise Exception(f"The directory {directory.resolve()} does not exist")

    if level == 0 and directory.is_file():
        raise Exception(f"This {directory.resolve()} is a file")

    if level == 0:
        result.append({
            "level": 0,
            "name": directory.name,
            "is_dir": True
        })
        listing_files(result, directory.resolve(), level + 1)
        return

    for item in directory.iterdir():
        is_dir = item.is_dir()
        result.append({
            "level": level,
            "name": item.name,
            "is_dir": is_dir
        })
        if is_dir:
            listing_files(result, item.resolve(), level + 1)


def format_result(result: ResultList, indent=DEFAULT_INDENT, dir_color=Fore.BLUE, file_color=Fore.GREEN):
    """
    Visualize the structure of that directory, displaying the names of all subdirectories and files.
    """
    for item in result:
        name = item.get("name")
        level = item.get("level")
        is_dir = item.get("is_dir")
        space = indent * level
        color = dir_color if is_dir else file_color
        ended = "/" if is_dir else ""
        print(color + f"{space}{name}" + ended)

    print(Style.RESET_ALL)
