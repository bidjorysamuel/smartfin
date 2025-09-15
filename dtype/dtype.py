
from typing import Literal


class Format:
    def __init__(self, data, fw:Literal["ci", "other"]="ci"):
        self.data = data

        self.for_what = fw

        self.len_data = len(data)

        if self.for_what == "ci" and self.len_data != 4:
            raise Exception("List might have 4 element")
        
        if self.for_what == "ci" and self.len_data == 4:
            self.amount, self.capital, self.rate, self.period = self.data
        

    def __len__(self):
        return self.len_data
    
    def __str__(self):
        return f"SMARTFIN({self.data})"
    
    def data_for_what(self):
        if self.for_what == "ci":
            return "SMARTFIN( DATA IS FOR COUMPOUND INTEREST )"
        else:
            return "SMARTFIN( DATA IS FOR OTHER TYPE OF CALCULATION )"
    