
def is_positive_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected int or float, got {type(value)}")
    
    if value < 0:
        raise ValueError("Value must be positive")
    
    return True


def is_rate(value):
    """The rate value might be between 0 & 1"""
    is_positive_number(value)
    if value > 1:
        raise ValueError("Rate should be in decimal (0 - 1)")
    
    return True


def check_none_count(args):
    """Only one parameter should be None"""
    none_count = sum(x is None for x in args)
    if none_count != 1:
        raise ValueError("Exactly one parameter must be None")
    return True
