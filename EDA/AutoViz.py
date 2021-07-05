import pandas as pd
from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()

def AutoViz(frame):
    dft = AV.AutoViz(frame, sep=sep, depVar=target, dfte=df, header=0, verbose=2, lowess=False,chart_format='svg',max_rows_analyzed=1500,max_cols_analyzed=30)
