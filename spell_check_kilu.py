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
    j = 1
    for line in final_lines:
        words = line.split(" ")
        i = 1
        for word in words:
            if word not in final_list_words:
                print(
                    f" line {j} column {i} {word} appears to be a typo ")
            i += 1
        j += 1


main()
