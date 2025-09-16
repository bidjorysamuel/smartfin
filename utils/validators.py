
def is_positive_number(value):
    if value is not None and not isinstance(value, (int, float)):
        raise TypeError(f"Expected int or float or None, got {type(value)}")
    
    if value is not None and value < 0:
        raise ValueError("Value must be positive")
    
    return True



def is_rate(value):
    # If its None, return True
    if value is None:
        return True
    
    # Check if its a number
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected int or float or None, got {type(value)}")
    
    # Check if its positive
    if value < 0:
        raise ValueError("Rate must be positive")
    
    # Check if its <= 1
    if value > 1:
        raise ValueError("Rate must be <= 1 (as decimal)")
    
    return True



def check_none_count(args):
    """Only one parameter should be None"""
    none_count = sum(x is None for x in args)
    if none_count != 1:
        raise ValueError("Exactly one parameter must be None")
    return True
