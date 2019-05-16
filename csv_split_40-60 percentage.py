from numpy.random import RandomState
import pandas as pd
df = pd.read_csv('C:/Users/admin/Desktop/practice_problems/mortgage_new/solution_file.csv')
rng = RandomState()

public1 = df.sample(frac=0.4, random_state=rng)
private1 = df.loc[~df.index.isin(public.index)]
public.to_csv('public_mortage.csv', index=False)
private.to_csv('private_mortage.csv', index=False)

public.info()
private.info()
