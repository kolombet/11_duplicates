import os
import argparse
import sys
from collections import defaultdict


def find_duplicates(path):
    duplicates = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            size = os.stat(path).st_size
            duplicates[(filename, size)].append(path)
    return list(filter(lambda paths: len(paths) > 1, duplicates.values()))


def print_duplicates(duplicates):
    if duplicates:
        for paths in duplicates:
            print("Found coincidence between files:")
            print('\n'.join(paths));
    else:
        print("No coincidence found.")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        dest="path",
        help="custom path to search duplicates",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    if not args.path:
        sys.exit("please specify directory to search duplicates")
    duplicates = find_duplicates(args.path)
    print_duplicates(duplicates)
