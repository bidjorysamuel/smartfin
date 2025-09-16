
from typing import Literal
from utils.validators import (
    check_none_count,
    is_rate
)

class Format:
    def __init__(self, data, fw:Literal["ci", "other"]="ci"):
        self.data = data

        self.for_what = fw

        self.len_data = len(data)

        if not isinstance(data, list):
            raise TypeError("data must be a python list()")

        if self.for_what == "ci":
            if self.len_data != 4:
                raise ValueError("For 'ci', data must have exactly 4 elements: [amount, capital, rate, period]")
            
            check_none_count(self.data)
            self.amount, self.capital, self.rate, self.period = self.data
            is_rate(self.rate)


    def __len__(self):
        return self.len_data
    
    def __str__(self):
        return f"SMARTFIN({self.data})"
    
    def data_for_what(self):
        if self.for_what == "ci":
            return "SMARTFIN( DATA IS FOR COUMPOUND INTEREST )"
        else:
            return "SMARTFIN( DATA IS FOR OTHER TYPE OF CALCULATION )"
    