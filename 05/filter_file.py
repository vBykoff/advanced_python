"""Generator module"""

def filter_file(path_to_file, words_to_find):
    """Lines generator"""
    with open(path_to_file, "r") as file:
        for line in file:
            for word in line.lower().strip().split():
                if word in words_to_find:
                    yield line.strip()
