import sys

def count_bytes(filename):
    try:
        with open(filename, 'rb') as file:
            data = file.read()
            return len(data)
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return -1


def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return -1

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            words = data.split()
            return len(words)
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return -1

def count_chars(filename):
    try:
        with open(filename, 'rb') as file:
            data = file.read().decode('utf-8', 'ignore')
            return len(data)
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return -1

def count_all(filename):
    lines = count_lines(filename)
    words = count_words(filename)
    bytes_count = count_bytes(filename)
    return lines, words, bytes_count


def main(args):
    if len(args) not in [2, 3] or (len(args) == 3 and args[1] not in ['-c', '-l', '-w', '-m']):
        print("Usage: ccws [-c|-l|-w|-m] <filename>")
        return

    filename = args[-1]

    if len(args) == 2:
        lines, words, bytes_count = count_all(filename)
        if lines != -1 and words != -1 and bytes_count != -1:
            print(f"{lines} {words} {bytes_count} {filename}")
    else:
        match args[1]:
            case "-c":
                byte_count = count_bytes(filename)
                if byte_count != -1:
                    print(f"{byte_count} {filename}")
            case "-l":
                line_count = count_lines(filename)
                if line_count != -1:
                    print(f"{line_count} {filename}")
            case "-w":
                word_count = count_words(filename)
                if word_count != -1:
                    print(f"{word_count} {filename}")
            case "-m":
                char_count = count_chars(filename)
                if char_count != -1:
                    print(f"{char_count} {filename}")

if __name__ == "__main__":
    main(sys.argv)
