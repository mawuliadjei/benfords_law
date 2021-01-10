from typing import Union, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chisquare

temp_actuals = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
}


class BenfordsLaw:
    def __init__(self,
                 data: Union[list, np.array, pd.Series]):
        self.expected_distribution = {
            '1': 0.301,
            '2': 0.176,
            '3': 0.125,
            '4': 0.097,
            '5': 0.079,
            '6': 0.067,
            '7': 0.058,
            '8': 0.051,
            '9': 0.046,
        }

        self.fsd_counts, self.fsd_distribution = dict(), dict()
        try:
            # enforce that all numbers passed can be evaluated into a numeric representation
            # handles the non-essential case where numbers are negative
            self.data = np.array([abs(float(x)) for x in data])
        except ValueError:
            print('All values must be numerical')
            raise
        self.expected_counts = {k: int(v * len(data)) for k, v in self.expected_distribution.items()}

    def _get_fsd(self, number: float):
        # this handles for integers and decimals like in one run
        # the possible cost is increasing the run time for integers without the need to
        # however, the increase in run time for ints should be negligible especially to the end user
        if number > 0:
            fsd = str(float(str(number).replace('.', '')))[0]
            return fsd

    def _extract_fsd(self):
        self.fsd = [self._get_fsd(number) for number in self.data]

    def get_counts(self):
        temp_counts = temp_actuals
        self.fsd_counts = dict((x, self.fsd.count(x)) for x in set(self.fsd))
        temp_counts.update(self.fsd_counts)
        self.fsd_counts = temp_counts

    def get_distribution(self):
        temp_distribution = temp_actuals
        self.fsd_distribution = dict((x, (self.fsd.count(x) / len(self.fsd))) for x in set(self.fsd))
        temp_distribution.update(self.fsd_distribution)
        self.fsd_distribution = temp_distribution

    def prepare_actual_distribution(self,
                                    return_values: bool = False,
                                    get_fsd_counts: bool = False):
        self._extract_fsd()
        self.get_distribution()
        if get_fsd_counts:
            self.get_counts()

    def apply_visual_test(self,
                          figsize: Tuple[int, int] = (15, 7)):
        barWidth = 0.25

        r1 = np.arange(len(self.expected_distribution.values()))
        r2 = [x + barWidth for x in r1]

        # Make the plot
        plt.figure(figsize=figsize)
        plt.bar(r1, self.expected_distribution.values(), color='blue', width=barWidth, edgecolor='white',
                label='expected')
        plt.bar(r2, self.fsd_distribution.values(), color='red', width=barWidth, edgecolor='white', label='actual')

        # Add xticks on the middle of the group bars
        plt.xlabel('First Significant Digit', fontweight='bold')
        plt.ylabel('Distribution', fontweight='bold')
        plt.xticks([r + barWidth for r in range(len(self.expected_distribution.values()))],
                   self.expected_distribution.keys())

        # Create legend & Show graphic
        plt.legend()
        plt.show()

    def apply_chi_sq_test(self,
                          alpha=0.05):
        statistic, p_value = chisquare(f_obs=list(self.fsd_counts.values()), f_exp=list(self.expected_counts.values()))
        if p_value < alpha:
            test_status = 'passed'
        else:
            test_status = 'failed'
        print(f'Chi-squared test {test_status} with statistic: {statistic} and p-value: {p_value}')
        return statistic, p_value

    def apply_benfords_law(self):
        self._extract_fsd()
        self.get_counts()
        self.get_distribution()
        self.apply_visual_test()
        self.apply_chi_sq_test()
