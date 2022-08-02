import streamlit
import tabella_pensioni as tb

import numpy as np
import pandas as pd

pensioni_parsed = []
for riga in tb.tabella_pensioni.split("\n"):
    r = list(map(lambda x:int(x.strip().replace(".","")), riga.split("|")[1:]))
    pensioni_parsed.append(r)

pensioni_parsed = np.array(pensioni_parsed)
streamlit.write(pd.DataFrame(pensioni_parsed, columns=["#num", "€", "media"]))

risp = streamlit.slider("risparmio su pensione minima", min_value=0, max_value=30, value=None, step=2)
inc = streamlit.slider("operatore incremento rispatio", min_value=1.00, max_value=2.5, value=None, step=0.2)

def calculate_risp(e, r):
    risparmio = []
    for i, (_qt, _sum, _avg) in enumerate(pensioni_parsed):
        # print(_sum, _sum-(_qt*15*i), _qt*15*i)
        risp = r*i**e
        risparmio.append(_qt*risp)
    return risparmio

array_dei_risparmi = calculate_risp(inc, risp)
streamlit.write(str(np.around(np.array(array_dei_risparmi))))
streamlit.write(
    "Quantita Risparmiata", sum(array_dei_risparmi) // 1_000_000, "kk"
)


