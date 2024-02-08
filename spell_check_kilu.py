import argparse


parser = argparse.ArgumentParser()
parser.add_argument("input_file")
args = parser.parse_args()


def main():
    file_name = args.input_file
    file1 = open(file_name, "r")
    lines = file1.readlines()
    final_lines = [line.strip() for line in lines]


main()
