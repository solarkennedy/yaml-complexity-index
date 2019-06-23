#!/usr/bin/env python3.7
from dataclasses import dataclass
import yaml
import argparse
import sys
import logging


def get_line_count(fd):
    fd.seek(0)
    return sum(1 for line in fd)


@dataclass
class Report:
    num_files: int = 0
    num_lines: int = 0
    num_semantic_lines: int = 0
    max_nestedness: int = 0

    def calculate_semantic_ratio(self):
        return self.num_semantic_lines / self.num_lines * 100

    def print_report(self):
        print("Complexity Report:")
        print(f"Number of files: {self.num_files}")
        print(f"Number of lines: {self.num_lines}")
        print(f"Number of semantic lines: {self.num_semantic_lines}")
        print(f"Number of lines / semantic lines percent: {self.calculate_semantic_ratio():.2f}%")
        print(f"Max nestedness: {self.max_nestedness}")


def get_semantic_lines(document):
    return yaml.safe_dump(document).count('\n')


def measure_max_nestedness(document):
    depths = []
    if isinstance(document, dict):
        for v in document.values():
            depths.append(measure_max_nestedness(v))
    if len(depths) > 0:
        return 1 + max(depths)
    return 1


def main(argv=None):
    parser = argparse.ArgumentParser(description='YAML Complexity Analyzer')
    parser.add_argument('filenames', nargs='*', help='YAML filenames to check.')
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG)

    r = Report()
    for filename in args.filenames:
        logging.debug(f"Inspecting {filename}")
        r.num_files = r.num_files + 1
        with open(filename) as fd:
            for document in yaml.safe_load_all(fd):
                logging.debug(document)
                r.num_semantic_lines = r.num_semantic_lines + get_semantic_lines(document)
                r.max_nestedness = measure_max_nestedness(document)
            r.num_lines = r.num_lines + get_line_count(fd)

    r.print_report()
    return 0

if __name__ == '__main__':
    sys.exit(main())
