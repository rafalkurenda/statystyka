import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sc
 

def ex1():
    print("Zadanie 1")
    data = pd.read_csv('data/MDR.csv')
    column = data['year']

    print(f'Max {column.max()}')
    print(f'Min {column.min()}')
    print(f'Mean {column.mean()}')
    print(f"Standard deviation: {column.std()}")
    print(f"Median: {column.median()}")
    print("")

def ex2():
    print("Zadanie 2")
    data_df = pd.read_csv('data/Wzrost.csv')
    data = data_df.columns.values.astype(float)

    print(f'Variation {sc.variation(data, )}')
    print(f'Devation {sc.tstd(data, )}')
    print("")

def ex3():
    print("Zadanie 3")
    data_df = pd.read_csv('data/MDR.csv')
    data = data_df['year']

    print(f'Geometric standard variation {sc.gstd(data, )}')
    print(f'Trimmed mean {sc.tmean(data, )}')
    print("")
 
def ex4():
    print("Zadanie 4")
    data = pd.read_csv('data/brain_size.csv', delimiter=";")
 
    viq = data['VIQ'].mean()
    gender_counts = data['Gender'].value_counts()

    f_viq = data[data['Gender'].str.contains('Female')]['VIQ']
    f_piq = data[data['Gender'].str.contains('Female')]['PIQ']
    f_fsiq = data[data['Gender'].str.contains('Female')]['FSIQ']

    df_hist = data[['VIQ', 'PIQ', 'FSIQ']]
    df_hist['Female VIQ'] = f_viq
    df_hist['Female PIQ'] = f_piq
    df_hist['Female FSIQ'] = f_fsiq

    df_hist.hist()
    plt.show()
    print("")

ex1()
ex2()
ex3()
ex4()