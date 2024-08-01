
def find_quantity(basket, item_name):
    if item_name in basket:
        return basket[item_name]["quantity"]
    return 0

def calculate_total(basket):
    raise NotImplementedError()