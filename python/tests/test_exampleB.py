import pytest

from exampleB import find_quantity, calculate_total

"""
    Empty basket - basket contains no items
    one item "A" - basket contains 1 item "A"
    two items "A" - basket contains 2 items "A"
    two items, "A" and "B" - basket contains 1 item "A"
    Empty basket - total price 0
    "A" costs $10, basket contains one "A" - total $10
    "D" costs $160, basket contains one "D" - total $152 (5% discount)
    "E" costs $250, basket contains one "E" - total $225 (10% discount)
    Basket contains two "D" - total $288 (10% discount)
    Remove the "Ignore" marking on the original test and hopefully it will pass!
"""

def test_empty_basket():
    basket = { }
    assert find_quantity(basket, "A") == 0

def test_contains_one_item():
    basket = {
    "A": {"quantity": 1, "price": 10},
  }
    assert find_quantity(basket, "A") == 1

def test_when_item_quantity_greater_than_one():
    basket = {
        "A": {"quantity": 5, "price": 10},
    }
    assert find_quantity(basket, "A") == 5
@pytest.mark.skip(reason="Not implemented yet")
def test_total_over_100_gives_five_percent_discount():
    basket = {
        "A": {"quantity": 5, "price" : 10},
        "B": {"quantity": 2, "price" : 25},
        "C": {"quantity": 6, "price" : 9.99},
    }
    assert find_quantity(basket, "C") == 6
    assert calculate_total(basket) == pytest.approx(151.94, 0.01)
