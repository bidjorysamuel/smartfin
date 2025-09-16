from dtype.dtype import Format
from typing import Literal
import math

class CI(Format):
    """
    CI = Compound Interest

    Calculate any one of the four key parameters in the compound interest formula:

        M = C * (1 + i)^t   (normal compounding)
        M = C * e^(i * t)   (continuous compounding)

    Where:
        M      : amount / future value
        C      : capital / present value
        i      : interest rate per period (decimal)
        t      : period (number of periods)

    Usage:
        Provide exactly **four elements** in CI format: [amount, capital, rate, period]
        - Set the value you want to calculate as None.
        - Class will automatically compute it.

    Examples:
        ci = CI([None, 3000, 0.05, 3])
        ci.calculate()  # returns amount

        ci = CI([3477.375, None, 0.05, 3])
        ci.calculate()  # returns capital

        ci = CI([3477.375, 3000, None, 3])
        ci.calculate()  # returns rate

        ci = CI([3477.375, 3000, 0.05, None])
        ci.calculate()  # returns period
    """

    def __init__(self, data, to_dict=False, continuous=False):
        super().__init__(data)
        self.to_dict = to_dict
        self.continuous = continuous


    def calculate(self):
        """Call the proper calculation method depending on continuous flag."""
        return self._continuous_compounding() if self.continuous else self._ci_normal()
    

    def _ci_normal(self):

        if self.amount is None:
            # Calculate amount (future value)
            jc = self.capital * (1 + self.rate) ** self.period

            self.data[0] = jc

    
        elif self.capital is None:
            # Calculate capital (present value)
            jc = self.amount / (1 + self.rate) ** self.period

            self.data[1] = jc

        elif self.rate is None:
            # Calculate rate
            jc = (self.amount / self.capital)**(1 / self.period) - 1

            self.data[2] = jc

        elif self.period is None:
            # Calculate period
            jc = math.log(self.amount / self.capital) / math.log((1 + self.rate))

            self.data[3] = jc
            
        else:
            raise ValueError("Exactly one value must be None to compute it.")

        if self.to_dict:
            return {"Amount":self.data[0],
                    "Capital":self.data[1],
                    "Rate":self.data[2],
                    "Period":self.data[3]
                }
        
        return self._return_data()
    
    


    def _continuous_compounding(self):

        if self.amount is None:
            result = self.capital * math.e ** (self.rate * self.period)
            self.data[0] = result

        # Capital (C)
        elif self.capital is None:
            result = self.amount / (math.e ** (self.rate * self.period))
            self.data[1] = result

        # Taxa (i)
        elif self.rate is None:
            result = math.log(self.amount / self.capital) / self.period
            self.data[2] = result

        # Tempo (t)
        elif self.period is None:
            result = math.log(self.amount / self.capital) / self.rate
            self.data[3] = result

        else:
            raise ValueError("Exactly one value must be None to compute it.")
        
        if self.to_dict:
            return {"Amount":self.data[0],
                    "Capital":self.data[1],
                    "Rate":self.data[2],
                    "Period":self.data[3]
                }
        
        return self._return_data()
    
    def _return_data(self):
        """Return result either as a list or as a dictionary with labels."""
        if self.to_dict:
            return {
                "Amount": self.data[0],
                "Capital": self.data[1],
                "Rate": self.data[2],
                "Period": self.data[3],
            }
        return self.data
    

    
    

    
    

