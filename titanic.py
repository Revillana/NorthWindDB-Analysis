import pandas as pd
import numpy as np
import seaborn as sns 

titanic = sns.load_dataset('titanic')

result= titanic.pivot_table('survived', 'class')
suma= titanic.pivot_table('survived','class', aggfunc=np.sum)
sex_alone= titanic.pivot_table('survived',['sex','alone'], 'class')
embark= titanic.pivot_table(index='class', columns= {'name'}, aggfunc= {'survived': np.sum, 'fare':np.mean})
print(embark)
