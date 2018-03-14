"""Reading in text files."""
import os, glob


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


def test_run():
    # Test read_file()
    print(read_file("data/hieroglyph.txt"))

    # Test read_files()
    texts = read_files("data/*.txt")
    for name in texts:
        print("\n***", name, "***")
        print(texts[name])


if __name__ == '__main__':
    test_run()
