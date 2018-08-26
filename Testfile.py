import pandas as pd
import C2P_Core as Dm
import numpy as np
data1=pd.read_json('Test.json')
s=np.array(data1)
aDict=Dm.Get_PQRS(s)
print(aDict)
