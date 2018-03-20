import os
import argparse
from collections import defaultdict


def find_duplicates():
    duplicates = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(args.path):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            size = os.stat(path).st_size
            duplicates[(filename, size)].append(path)
    return list(filter(lambda paths: len(paths) > 1, duplicates.values()))


def print_duplicates(duplicates):
    if duplicates:
        for paths in duplicates:
            print("Found coincidence between files:")
            for path in paths:
                print(path)
    else:
        print('No coincidence found.')


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        dest="path",
        help="custom path to search duplicates",
        default="test"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    duplicates = find_duplicates()
    print_duplicates(duplicates)
