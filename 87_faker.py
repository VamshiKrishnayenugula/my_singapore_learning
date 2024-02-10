"""You can generate fake data using Python. Python has a library 
called Faker that generates different types of data. Install 
Faker by:
pip install Faker
Let’s say we want to generate a random list of Ten countries,"""

from faker import Faker
fake = Faker()

for i in range(20):
    print(fake.country())


    """You can also generate profile data using this model. Below, 
we generate profile data and pass it to pandas to generate a 
Pandas DataFrame."""


import pandas as pd

profiles = [fake.simple_profile()    for i in range(30)]


df = pd.DataFrame(profiles)

print(df)