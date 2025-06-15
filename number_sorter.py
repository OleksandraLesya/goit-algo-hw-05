"""
Module: profit_calculator
This module provides utilities to extract and sum valid float numbers from a block of text,
intended to represent income components. The module uses a generator for memory efficiency.
"""

import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Extracts all valid float numbers from the input text and yields them one by one.
    Parameters:
        text (str): The input string containing float numbers separated by spaces.
    Yields:
        float: Each valid float number found in the text.
    """
    # Regular expression pattern for float numbers with space boundaries
    pattern = r'\b\d+\.\d+\b'
    for match in re.findall(pattern, text):
        yield float(match)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Calculates the total sum of float numbers extracted 
    from the given text using a generator function.
    Parameters:
        text (str): The input string that contains the numbers.
        func (Callable): A generator function used to extract float numbers from the text.
    Returns:
        float: The total sum of the extracted float numbers.
    """
    return sum(func(text))


# Example usage
if __name__ == "__main__":
    TEXT = (
        "The total employee income consists of several parts: "
        "1000.01 as base salary, supplemented by 27.45 and 324.00 dollars of additional income."
    )
    total_income = sum_profit(TEXT, generator_numbers)
    print(f"Total income: {total_income}")
