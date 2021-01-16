Examples
=============

Installation/Usage:
*******************
pip install -U benfords-law

Run simple test of Benford's Law on random numbers
**************************************************
.. code-block:: python

    """This example shows the application of Benford's Law on a dataset of random numbers.
    Since the numbers are exactly random, our expectation is that this dataset will not visually
    conform to Benford's Law and will fail the Chi-Squared Goodness of Fit test.
    """

    import numpy as np
    from benfords_law import BenfordsLaw

    # initialize array with random numbers that will fail Benford's Law
    data = np.random.randint(low=100, high=1000000, size=1000)
    benfords = BenfordsLaw(data)
    benfords.apply_benfords_law()