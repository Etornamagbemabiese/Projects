import pytest
from dictionary import invert, favorite_color, count, alphabetizer, update_attendance

# invert function tests
def test_invert_expected():
    """Tests the output with a simple dictionary (use case)."""
    input_dict = {"a": "apple", "b": "banana", "c": "cherry"}
    assert invert(input_dict) == {"apple": "a", "banana": "b", "cherry": "c"}

def test_invert_edge():
    """Tests if KeyError is raised with duplicate values (edge case)."""
    input_dict = {"a": "apple", "b": "banana", "c": "apple"}
    with pytest.raises(KeyError):
        invert(input_dict)

def test_invert_empty():
    """Tests the output with an empty dictionary (edge case)."""
    empty_dict = {}
    assert invert(empty_dict) == {}

# favorite_color function tests
def test_favorite_color_expected():
    """Tests the output with a dictionary of favorite colors (use case)."""
    input_dict = {"Alice": "blue", "Bob": "red", "Charlie": "blue", "David": "green"}
    assert favorite_color(input_dict) == "blue"

def test_flipped_input():
    """Tests what the function returns given flipped inputs(edge case)."""
    input = {"orange": "John", "violet": "Marco", "purple": "Corey"}
    assert favorite_color(input) == "None"


def test_favorite_color_edge():
    """Tests the output with an empty dictionary (edge case)."""
    empty_dict = {}
    assert favorite_color(empty_dict) == "None"

# count function tests
def test_count_expected():
    """Tests the output with a list of colors (use case)."""
    input_list = ["red", "blue", "green", "red", "yellow", "blue"]
    assert count(input_list) == {"red": 2, "blue": 2, "green": 1, "yellow": 1}

def test_count_edge():
    """Tests if KeyError is raised with an empty list (edge case)."""
    empty_list = []
    with pytest.raises(KeyError, match="Len of input cannot be equal 0"):
        count(empty_list)

def test_count_numbers():
    """Tests the output with a list of numbers (use case)."""
    input_list = [1, 2, 3, 1, 4, 2, 5]
    assert count(input_list) == {1: 2, 2: 2, 3: 1, 4: 1, 5: 1}

# alphabetizer function tests
def test_alphabetizer_expected():
    """Tests the output with a list of names (use case)."""
    input_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
    assert alphabetizer(input_list) == {"a": ["Alice"], "b": ["Bob"], "c": ["Charlie"], "d": ["David"], "e": ["Eve"]}

def test_alphabetizer_edge():
    """Tests the output with an empty list (edge case)."""
    empty_list = []
    assert alphabetizer(empty_list) is None

def test_alphabetizer_case_insensitive():
    """Tests the output with a list of names with mixed case (use case)."""
    input_list = ["Alice", "bob", "Charlie", "david", "Eve"]
    assert alphabetizer(input_list) == {"a": ["Alice"], "b": ["bob"], "c": ["Charlie"], "d": ["david"], "e": ["Eve"]}

# update_attendance function tests
def test_update_attendance_expected():
    """Tests the output with a dictionary of attendance (use case)."""
    input_dict = {"Monday": ["Alice", "Bob"], "Tuesday": ["Charlie"]}
    assert update_attendance(input_dict, "Monday", "Eve") == {"Monday": ["Alice", "Bob", "Eve"], "Tuesday": ["Charlie"]}

def test_update_attendance_edge():
    """Tests the output with an empty dictionary (edge case)."""
    empty_dict = {}
    assert update_attendance(empty_dict, "Wednesday", "Alice") == {"Wednesday": ["Alice"]}

def test_update_attendance_duplicate():
    """Tests if duplicate attendance is handled correctly (use case)."""
    input_dict = {"Monday": ["Alice", "Bob"], "Tuesday": ["Charlie"]}
    assert update_attendance(input_dict, "Monday", "Alice") == {"Monday": ["Alice", "Bob"], "Tuesday": ["Charlie"]}
