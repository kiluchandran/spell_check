import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
args = parser.parse_args()


def main():
    file_name = args.input_file
    file1 = open(file_name, "r")
    lines = file1.readlines()
    final_lines = [line.strip() for line in lines]
    file2 = open("words.txt", "r")
    lists = file2.readlines()
    final_list_words = [list.strip() for list in lists]


main()
