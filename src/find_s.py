import pandas as pd

def find_s(df):
    h = None

    for _, row in df.iterrows():
        x = row[:-1].tolist()
        y = row['Result']

        if y == 'Yes':
            if h is None:
                h = x
            else:
                for i in range(len(h)):
                    if h[i] != x[i]:
                        h[i] = '?'

    return h