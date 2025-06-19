import sys
from typing import List

def digit_sum(n: int) -> int:
    """Return the sum of the digits of *n*."""
    return sum(int(d) for d in str(n))
               
if __name__ == "__main__":
    user_text: str = input("Enter an integer: ")
    while not user_text.isdigit():
        user_text = input("Please enter digits only: ")

    number: int = int(user_text)
    print(digit_sum(number))
