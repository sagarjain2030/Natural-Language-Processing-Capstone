"""Bigram Model."""

import os,glob
import re
import random

def read_file(filename):
    """Read a plain text file and return the contents as a string."""
    # TODO: Open "filename", read text and return it
    return (open(filename, 'r')).read()


def read_files(path):
    """Read all files that match given path and return a dict with their contents."""
    fileDict = {}
    # TODO: Get a list of all files that match path (hint: use glob)
    for file in glob.glob(path):
        fileDict[os.path.basename(file)] = read_file(file)
    # TODO: Read each file using read_file()
    # TODO: Store & return a dict of the form { <filename>: <contents> }
    # Note: <filename> is just the filename (e.g. "hieroglyph.txt") not the full path ("data/hieroglyph.txt")
    return fileDict


def compute_bigram_model(path, files):
    """Compute a bigram model for a given corpus, including unigram probabilities.

    Params
    ======
        path: directory where input files are located
        files: list of files, or a single string specifying regex pattern to match (e.g. r'.*\.txt')

    Returns
    =======
        p_unigrams: dict with frequency of single words (need not be normalized to [0, 1])
        p_bigrams: dict of dicts with frequency of bigrams (need not be normalized to [0, 1])

    """

    # Grab a list of all files in specified corpus
    if isinstance(files, str):
        files = [f for f in os.listdir(path) if re.match(files, f)]  # collect all matching filenames
    files = [os.path.join(path, f) for f in files]  # prepend path to each filename

    # TODO: Read in text from each file and combine into a single string
    file_Data = ""
    for f in files:
        file_Data += open(f, 'r').read()

    # TODO: Clean and tokenize text (note that you may want to retain case and sentence delimiters)
    #file_Data = file_Data.replace(r"[^a-zA-Z0-9]"," ")
    #print(file_Data)
    words = file_Data.split()

    # TODO: Compute unigram probabilities
    p_unigrams = {}
    for w in words:
        if(w in p_unigrams.keys()):
            p_unigrams[w] += 1
        else:
            p_unigrams[w] = 1

    # TODO: Compute bigram probabilities
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
    p_bigrams = {}
    for w in bigrams:
        if(w in p_bigrams.keys()):
            p_bigrams[w] += 1
        else:
            p_bigrams[w] = 1

    return p_unigrams, p_bigrams


def generate_sequence(p_unigrams, p_bigrams, num_words=100, seed_word=None):
    """Generate a random sequence of words, given unigram and bigram probabilities."""

    # If seed_word is not given, pick one randomly based on unigram probabilities
    if seed_word is None:
        seed_word = random.choices(list(p_unigrams.keys()), weights=list(p_unigrams.values()))[0]
    seq = [seed_word]
    for i in range(num_words):
        seq.append(random.choices(list(p_bigrams[seq[-1]].keys()), weights=list(p_bigrams[seq[-1]].values()))[0])
    return seq


def test_run():
    # Compute bigram model
    p_unigrams, p_bigrams = compute_bigram_model(path='.', files=['carroll-alice.txt'])

    # Check most common unigrams (single words)
    print("10 most common unigrams:")
    sorted_unigrams = sorted(p_unigrams.items(), key=lambda item: item[1], reverse=True)  # each item = (i, count)
    for word, count in sorted_unigrams[:10]:
        print("{}\t{}".format(word, count))

    # Check most common bigrams (pairs of words)
    all_bigrams = [(i, j, count) for i in p_bigrams.keys() for j, count in p_bigrams[i].items()]
    sorted_bigrams = sorted(all_bigrams, key=lambda item: item[2], reverse=True)  # each item = (i, j, count)
    print("10 most common bigrams:")
    for i, j, count in sorted_bigrams[:10]:
        print("{}\t{}\t{}".format(i, j, count))

    # Generate a sample sequence of words
    seq = generate_sequence(p_unigrams, p_bigrams, seed_word="Alice")
    print(" ".join(seq))


if __name__ == "__main__":
    test_run()
