import streamlit
import tabella_pensioni as tb

import numpy as np
import pandas as pd

pensioni_parsed = []
for riga in tb.tabella_pensioni.split("\n"):
    r = list(map(lambda x:int(x.strip().replace(".","")), riga.split("|")[1:]))
    pensioni_parsed.append(r)

pensioni_parsed = np.array(pensioni_parsed)
streamlit.write(pd.DataFrame(pensioni_parsed))

