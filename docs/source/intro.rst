Introduction
============

``benfords_law`` is a python package for testing if a dataset of numbers passes Benford's law; also known as the law of analogous numbers.

A user can simply pass a dataset into a ``benfords_law.BenfordsLaw`` object and simply call the ``benfords_law.BenfordsLaw.apply_benfords_law()`` function.

The current implementation has been developed in Python 3.

Limitations
***********

Current development only supports visual tests and chi-squared goodness of fit tests.