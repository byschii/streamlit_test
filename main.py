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

risp = streamlit.slider("risparmio su pensione minima", min_value=0, max_value=30, value=None, step=2)

inc = streamlit.slider("operatore incremento rispatio", min_value=1.00, max_value=2.5, value=None, step=0.2)


def calculate_risp(e, r):
    risparmio = []
    risparmio2 = []
    for i, (_qt, _sum, _avg) in enumerate(pensioni_parsed):
        # print(_sum, _sum-(_qt*15*i), _qt*15*i)
        risp = r*i**e
        risp2 = (r+1)*i**e
        risparmio.append(_qt*risp)
        risparmio2.append(_qt*risp2)
    return risparmio



streamlit.write(
    sum(calculate_risp(inc, risp)) // 1_000_000, "kk"
)


