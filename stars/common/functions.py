from types import FunctionType


def map_over_input(
    function: FunctionType, input_file_url: str, sanitize: FunctionType = None
):
    """
    Maps a function over every line in the given input file.
    """
    output = []
    with open(input_file_url, "r") as input_file:
        for input_line in input_file:
            if sanitize is not None:
                input_line = sanitize(input_line)
            output.append(function(input_line))
    return output
