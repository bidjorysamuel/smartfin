from dtype.dtype import Format


class CI(Format):
    """
    CI = Compound Interest
    
    This class allows you to calculate any one of the four key parameters 
    in the compound interest formula:

        M = C * (1 + i)^t

    Where:
        M      : total amount (montante / future value)
        C      : capital (principal / present value)
        i      : interest rate per period (as a decimal, e.g., 0.05 for 5%)
        t      : period (number of periods)

    Usage:
        You must provide exactly **four elements** in the CI format:
        [amount, capital, rate, period]
        
        - Use `None` for the value you want to calculate.
        - The class will automatically compute the missing value.

    Examples:
        1️⃣ Calculate future value (amount):
            ci = CI([None, 3000, 0.05, 3])
            ci.calculate()  # returns 3477.375

        2️⃣ Calculate capital:
            ci = CI([3477.375, None, 0.05, 3])
            ci.calculate()  # returns 3000

        3️⃣ Calculate rate:
            ci = CI([3477.375, 3000, None, 3])
            ci.calculate()  # returns 0.05

        4️⃣ Calculate period:
            ci = CI([3477.375, 3000, 0.05, None])
            ci.calculate()  # returns 3

    Notes:
        - All rates should be expressed as decimals, not percentages.
        - The calculation for the rate or period uses logarithms to isolate the exponent.
        - Ensure you provide **exactly one None** value, otherwise the calculation may be ambiguous.
    """

    def calculate(self):
        import math

        if self.amount is None:
            # Calculate amount (future value)
            jc = self.capital * (1 + self.rate) ** self.period

    
        elif self.capital is None:
            # Calculate capital (present value)
            jc = self.all / (1 + self.rate) ** self.period

        elif self.rate is None:
            # Calculate rate
            jc = (self.all / self.capital)**(1 / self.period) - 1

        elif self.period is None:
            # Calculate period
            jc = math.log(self.all / self.capital) / math.log((1 + self.rate))


        
        return jc