import pickle


def write_to_file(filename, data):
    file = open(filename, "wb")
    pickle.dump(data, file)
    file.close()


def read_from_file(filename):
    scores = []
    with (open(filename,"rb")) as openfile:
        while True:
            try:
               scores.append(pickle.load(openfile))
            except EOFError:
                break
    return scores