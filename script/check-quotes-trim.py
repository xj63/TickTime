#!/bin/env python3

import sys

QUOTE_PATH = "./public/quotes.txt"


class Color:
    FG_COLORS = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37,
    }
    BOLD = "\033[1m"
    END = "\033[0m"

    @staticmethod
    def fg_code(color):
        return Color.FG_COLORS[color]

    @staticmethod
    def bg_code(color):
        return 10 + Color.FG_COLORS[color]

    @staticmethod
    def encode(code):
        return f"\033[{code}m"

    @staticmethod
    def fg(color):
        return lambda text: Color.encode(Color.fg_code(color)) + text + Color.END

    @staticmethod
    def bg(color):
        return lambda text: Color.encode(Color.bg_code(color)) + text + Color.END

    @staticmethod
    def bold():
        return lambda text: Color.BOLD + text + Color.END


FRED = Color.fg("red")
FGREEN = Color.fg("green")
FCYAN = Color.fg("cyan")

BRED = Color.bg("red")


def PRED(text):
    return BRED(FRED(text))


def highlight_spaces(line):
    """
    Highlights leading and trailing spaces in a line by wrapping them with PRED.

    Args:
        line (str): The input line to process.

    Returns:
        str: The processed line with leading and trailing spaces highlighted.
    """
    leading_spaces = len(line) - len(line.lstrip())
    trailing_spaces = len(line) - len(line.rstrip())
    return (
        PRED(line[:leading_spaces].replace(" ", "-"))
        + line[leading_spaces : len(line) - trailing_spaces]
        + PRED(line[len(line) - trailing_spaces :].replace(" ", "-"))
    )


def check_quotes_for_extra_spaces(quotes):
    """
    Check if any quotes contain extra spaces.

    Args:
        quotes (list): A list of quotes.

    Returns:
        list: A list of line numbers where quotes contain extra spaces.
    """
    return [i for i, line in enumerate(quotes) if line.strip() != line.strip("\n")]


def check_file_for_extra_spaces(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            quotes = file.readlines()

        print(FCYAN(f"Analyzing {QUOTE_PATH} for whitespace issues..."))
        errlines = check_quotes_for_extra_spaces(quotes)

        if len(errlines) == 0:
            print(FGREEN(f"No whitespace issues found in {QUOTE_PATH}."))
            sys.exit(0)

        print(FRED(f"Found {len(errlines)} whitespace issue(s) in {QUOTE_PATH}:"))
        for line in errlines:
            print(FRED(f"{line + 1}: ") + highlight_spaces(quotes[line].strip("\n")))

    except FileNotFoundError:
        print(FGREEN(f"File {QUOTE_PATH} not found. Skipping check."))
        sys.exit(0)
    except Exception as e:
        print(FRED(f"An unexpected error occurred when opening {QUOTE_PATH}: {e}"))
        sys.exit(1)


if __name__ == "__main__":
    check_file_for_extra_spaces(QUOTE_PATH)
