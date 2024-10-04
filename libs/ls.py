"""
This script takes a directory path as the first command line argument
and visualizes the structure of that directory, displaying the names
of all subdirectories and files.
"""
import sys
import listing_files as lib

if len(sys.argv) > 1:
    path = sys.argv[1]
    # print(f"Directory: {path}\n")
    result = []
    lib.listing_files(result, path)
    lib.format_result(result)
else:
    print("No arguments were passed.")
