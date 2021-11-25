import scipy.stats as sps
import pandas as pd


data = pd.read_csv('napoje.csv', sep=';', na_values='.')
data_reklama = pd.read_csv('napoje_po_reklamie.csv', sep=';', na_values='.')


def zad1():
    print(" ")
    print(f"###### ZADANIE 1 ######")
    print(" ")
    norm = sps.norm.rvs(2, 30, size=200)
    results = sps.ttest_1samp(norm, 2.5)
    print(results)

def zad2():
    print(" ")
    print(f"###### ZADANIE 2 ######")
    print(" ")

    cola = sps.ttest_1samp(data['cola'], 222000)
    print(f"Cola: {cola}")

    lech = sps.ttest_1samp(data['lech'], 60500)
    print(f"Lech: {lech}")

    regionalne = sps.ttest_1samp(data['regionalne'], 43500)
    print(f"Regionalne: {regionalne}")

def zad3():
    print(" ")
    print(f"###### ZADANIE 3 ######")
    print(" ")
    alpha = 1e-3

    for x in data:
        k2, p = sps.normaltest(data[x])
        print(f"==={x}===")
        print(f"k2: {k2}")
        print(f"p: {p}")
        if p < alpha:
            print(f"Result: can be rejected")
        else:
            print(f"Result: cannot be rejected")

def zad4():
    print(" ")
    print(f"###### ZADANIE 4 ######")
    print(" ")
    okocim_lech = sps.ttest_ind(data['okocim'], data['lech'])
    print("Równość średnich dla OKOCIM-LECH: ", okocim_lech)

    fanta_regionalne = sps.ttest_ind(data['fanta'], data['regionalne'])
    print("Równość średnich dla FANTA-REGIONALNE: ", fanta_regionalne)

    cola_pepsi = sps.ttest_ind(data['cola'], data['pepsi'])
    print("Równość średnich dla COLA-PEPSI: ", cola_pepsi)

def zad5():
    print(" ")
    print(f"###### ZADANIE 5 ######")
    print(" ")
    okocim = data['okocim']
    lech = data['lech']
    fanta = data['fanta']
    regionalne = data['regionalne']
    cola = data['cola']
    pepsi = data['pepsi']
    zywiec = data['żywiec']

    okocim_lech = sps.levene(okocim,lech)
    zywiec_fanta = sps.levene(zywiec, fanta)
    regionalne_cola = sps.levene(regionalne, cola)

    print(f"Równośc wariancji okocim - lech: {okocim_lech.pvalue}")
    print(f"Równośc wariancji zywiec - fanta: {zywiec_fanta.pvalue}")
    print(f"Równośc wariancji regionalne - cola: {regionalne_cola.pvalue}")

def zad6():
    print(" ")
    print(f"###### ZADANIE 6 ######")
    print(" ")
    data_2001 = data['regionalne'].loc[data['rok'] == 2001]
    data_2015 = data['regionalne'].loc[data['rok'] == 2015]

    test_mean = sps.ttest_ind(data_2001, data_2015)
    print(f"Równość średnich pomiędzy latami 2001 i 2015 dla piw regionalnych: {test_mean}")

def zad7():
    print(" ")
    print(f"###### ZADANIE 7 ######")
    print(" ")

    data_2016 = data[['pepsi', 'cola', 'fanta']][data["rok"] == 2016]
    results_pepsi = sps.ttest_rel(data_2016['pepsi'], data_reklama['pepsi'])
    results_fanta = sps.ttest_rel(data_2016['fanta'], data_reklama['fanta'])
    results_cola = sps.ttest_rel(data_2016['cola'], data_reklama['cola'])

    print(f"Równośc średnich (napoje, napoje_po_reklamie) - pepsi: {results_pepsi.pvalue}")
    print(f"Równośc średnich (napoje, napoje_po_reklamie) - fanta: {results_fanta.pvalue}")
    print(f"Równośc średnich (napoje, napoje_po_reklamie) - cola: {results_cola.pvalue}")


zad1()
zad2()
zad3()
zad4()
zad5()
zad6()
zad7()
