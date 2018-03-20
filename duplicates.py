from os import walk
from os import stat
import os
import hashlib
import argparse

def calcHash(name, size):
    namesize = str({"name":name, "size":size}).encode("utf-8")
    val = hashlib.md5(namesize).hexdigest()
    return val


def printResults(duplicates):
    files = duplicates.values()
    results = list(filter(lambda file: len(file) > 1, files))
    if len(results) > 0:
        for result in results:
            print("Found coincidence between files:")
            for subresult in result:
                print("%s" % subresult)
    else:
        print('No coincidence found.')


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        dest="path",
        help="custom path to search duplicates",
        default="default"
    )
    return parser.parse_args()


if __name__ == "__main__":
    files = []
    duplicates = {}
    args = get_args()
    for (dirpath, dirnames, filenames) in walk(args.path):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            
            size = os.stat(path).st_size
            file_hash = calcHash(filename, size)
            
            if file_hash in duplicates:
                duplicates[file_hash].append(path)
            else:
                duplicates[file_hash] = [path]
    printResults(duplicates)
    pass
