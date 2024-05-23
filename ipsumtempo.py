def read_cleaned(filename):
    """Reads a cleaned file and returns a list of lines.

    Args:
        filename: The name of the file to read.

    Returns:
        A list of lines from the file.
    """

    with open(filename, "r") as f:
        lines = f.readlines()
    return lines

