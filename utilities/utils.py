import pickle
import os.path

def write_to_file(filename, data):
    file = open(filename, "ab")
    pickle.dump(data, file)
    file.close()

def generate_greek7():
    words_dir = os.path.normpath(os.path.dirname(__file__) + "/../res/words")
    greek_path = os.path.normpath(words_dir + "/greek.txt")
    greek7_path = os.path.normpath(words_dir + "/greek7.txt")

    # ignore if greek7 exists already
    if os.path.isfile(greek7_path):
        return

    # load greek.txt and keep words with len <= 7
    words7 = []
    with open(greek_path, encoding="utf8") as rfile:
        for line in rfile:
            word = line.strip()

            # ignore words bigger than 7 characters
            if len(word) > 7:
                continue

            words7.append(word)

    # write words with len <= 7 to greek7.txt
    if len(words7) > 0:
        wfile = open(greek7_path, "w", encoding="utf8")
        wfile.write("\n".join(words7))

def read_from_file(filename):
    scores = []
    with (open(filename, "rb")) as openfile:
        while True:
            try:
               scores.append(pickle.load(openfile))
            except EOFError:
                break
    return scores