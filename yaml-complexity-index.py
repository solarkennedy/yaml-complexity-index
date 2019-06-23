#!/usr/bin/env python3
import yaml
import argparse
import sys
import logging


def get_line_count(fd):
    fd.seek(0)
    return sum(1 for line in fd)


def get_semantic_lines(document):
    return yaml.safe_dump(document).count('\n')


def main(argv=None):
    parser = argparse.ArgumentParser(description='YAML Complexity Analyzer')
    parser.add_argument('filenames', nargs='*', help='YAML filenames to check.')
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)

    num_files = 0
    num_lines = 0
    num_semantic_lines = 0

    for filename in args.filenames:
        logging.debug(f"Inspecting {filename}")
        num_files = num_files + 1
        with open(filename) as fd:
            for document in yaml.safe_load_all(fd):
                logging.debug(document)
                num_semantic_lines = num_semantic_lines + get_semantic_lines(document)
            num_lines = num_lines + get_line_count(fd)


    print("Complexity Report:")
    print(f"Number of files: {num_files}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of semantic lines: {num_semantic_lines}")
    print(f"Number of lines / semantic lines percent: {100 * num_semantic_lines / num_lines:.2f}%")
    return 0

if __name__ == '__main__':
    sys.exit(main())
