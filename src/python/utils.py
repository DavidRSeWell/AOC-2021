"""
Helper funcs
"""


def text_to_list(text_path):
    """
    Take in text that is assumed to contain one set of characters per row
    """
    with open(text_path) as f:
        return f.readlines()
