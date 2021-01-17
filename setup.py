import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="benfords_law",
    version="1.0.0rc1",
    description="Apply and run tests of Newcomb-Benford's Law on provided data",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mawuliadjei/benfords_law",
    author="Mawuli Adjei",
    author_email="mawuliadjei@gmail.com",
    license="MIT",
    keywords='Newcomb Benford Analogous-Numbers Statistics Testing',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    project_urls={
        'Documentation': 'https://benfords-law.readthedocs.io/',
        # 'Funding': 'https://donate.pypi.org',
        # 'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/mawuliadjei/benfords_law/',
        'Tracker': 'https://github.com/mawuliadjei/benfords_law/issues',
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy==1.17.1',
        'pandas==0.25.1',
        'scipy==1.6.0',
        'matplotlib==3.3.3',
    ],
    # entry_points={
    #     "console_scripts": [
    #         "benfords_law=benfords_law:main",
    #     ]
    # },
    python_requires='>=3.6',
)
