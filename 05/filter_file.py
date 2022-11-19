
def filter_file(path_to_file, words_to_find):
    with open(path_to_file, "r") as f:
        for line in f:
            for word in line.lower().strip().split():
                if word in words_to_find:
                    yield line.strip()

