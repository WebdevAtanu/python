# This demonstrates the use of type annotations in Python.
from typing import List, Dict, Tuple

name : str = "John"
age : int = 30
height : float = 5.9
is_student : bool = False
scores : List[int] = [85, 90, 78]
grades : Dict[str, str] = {"A": "Excellent", "B": "Good", "C": "Average"}
coordinates : Tuple[int, int] = (10, 20)

def Sum(a: int, b: int) -> int:
    return a + b

def Greet(name: str) -> str:
    return f"Hello, {name}!"

print(Sum(5, 10))  # Output: 15
print(Greet("Alice"))  # Output: Hello, Alice!
