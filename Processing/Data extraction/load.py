import pandas as pd
import numpy as np

def load_data_csv(path):
    print('loading;', path)

    data = pd.read_csv(path)

    print('data', data.shape)

    print('nUni', df.nunique())
    print('nNull', df.isnull().sum())

    return data

