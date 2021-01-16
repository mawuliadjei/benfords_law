# Benford's Law
A python package for testing if a dataset of numbers passes Benford's law; also known as the law of analogous numbers.

# Installation
```
pip install -U benfords-law
```
## Usages
```
>> import numpy as np
>>
>> from benfords_law import BenfordsLaw
>> 
>> # initialize array with random numbers that will fail Benford's Law
>> data = np.random.randint(low=100, high=1000000, size=1000)
>> benfords = BenfordsLaw(data)
>> benfords.apply_benfords_law()
Chi-squared test failed with statistic: 998.0013682427352 and p-value: 4.032015415461028e-210
>> # Benford's Test Image Below:
```
![Failed Benfords Test with Random Numbers](https://raw.githubusercontent.com/mawuliadjei/benfords_law/main/images/example_benford_failed.png)

### Dependencies
- numpy==1.17.1
- pandas==0.25.1
- scipy==1.6.0
- matplotlib==3.3.3

# Introduction and Description
[Newcomb-Benford's Law](https://en.wikipedia.org/wiki/Benford's_law) (The Law of Analogous Numbers) states that in many naturally occurring sets of numbers, the first significant digit is likely to be small.
This means that in a set of numbers; eg. populations of countries in the world, the first digit of the number is most likely to be 1. And following that, the probability that the first digit is 2, is less that that of one, but greater than all the rest and so on and so forth.

In fact, this expectation from Benford's Law follows a very specific distribution that is shown below:
![](https://raw.githubusercontent.com/mawuliadjei/benfords_law/main/images/benfords_law_distribution.png)
 
As such, using the example of country populations in the world, the distribution of first significant digits against the expected distribution from Benford's Law can be seen as follows:
![2016 National Populations Benfords Test](https://raw.githubusercontent.com/mawuliadjei/benfords_law/main/images/populations_benfords_law.png)

This phenomenon is pervasive in many extensive sets of numbers. Examples are:
- Earthquake Magnitudes
- Dow Jones Industrial Average from 1990– 1993
- 3,141 county populations from the 1990 U.S. Census
- Distance of stars from earth in light years
- Most common iphone passcodes


The explanations for this law are many and debated. However there are some key (non-exhaustive) characteristics of these sets of numbers. These sets generally:
1. Occur 'naturally' without human manipulation
2. Occur in many orders of magnitude.
3. Have some exponentation going on

Why should we care? Glad you asked. If these numbers are naturally occurring, then if a set of naturally occuring set of numbers does not follow Benford's law , then there is cause to believe that there's something unscrupulous going on. For example, in cases where elections have been rigged, you'll find that numbers tallied do not follow Benford's Law. 

As such it's a fair practice to detect inconsistencies in sets of numbers using Benford's Law. Examples of real work applications of Benford's Law in manipulation/fraud/misleading-data detection include:
1. [National COVID-19 Tracking Errors/Inconsitencies](https://www.nature.com/articles/d41586-020-01565-5)
2. [Electoral Fraud](https://towardsdatascience.com/frawd-detection-using-benfords-law-python-code-9db8db474cf8)

## Key Terminology
- **First Leading Digit (fsd)**:The first non-zero digit of a number. eg:
    - 52390234 has fsd=5
    - 0.0004562 has fsd=4
    - 2943.6 has fsd=2

#References

**Wikipedia**
https://en.wikipedia.org/wiki/Benford's_law

**Netflix**
**Connected: Season 1; Episode (Digits)**
https://www.netflix.com/watch/81084953

**Youtube**
*Khan Academy: Benford's Law Explained*
https://youtu.be/SZUDoEdjTzg