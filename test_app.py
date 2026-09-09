import pytest
from app import get_first

def test_get_first_with_non_empty_list():
    assert get_first([1, 2, 3]) == 1

def test_get_first_with_empty_list():
    assert get_first([]) is None
