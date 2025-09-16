import csv
import math
from calculation.ci import CI

class CICSVHandler:
    """
    Handles CSVs for compound interest calculations.
    Fills missing values automatically using CI class.
    """

    def __init__(self, path, continuous=False):
        self.path = path
        self.continuous = continuous
        self.rows = []

    def read_csv(self):
        """Read CSV file and store rows as list of lists"""
        with open(self.path, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)  # skip header
            for row in reader:
                # convert empty strings to None and numbers to float
                self.rows.append([float(x) if x.strip() != '' else None for x in row])
        return self.rows

    def fill_all(self):
        """Fill missing values in all rows using CI"""
        filled_data = []
        for row in self.rows:
            ci = CI(row, to_dict=True, continuous=self.continuous)
            filled_data.append(ci.calculate())
        return filled_data

    def to_pandas(self):
        """Return a pandas DataFrame"""
        import pandas as pd
        filled = self.fill_all()
        return pd.DataFrame(filled)
