import pandas as pd
import random
from sqlalchemy import create_engine

#1!
pd.set_option ('display.max_columns', 500)
pd.set_option ('display.width', 1000)
pd.set_option ('display.max_colwidth', 100)

readset = {"name": str, "prep_time": int}
#import danych
df_fileproject = pd.read_excel("kartuzy_1.xls", dtype=readset,
                               index_col=0, header= 0,)
#przedstawienie wartości

print(df_fileproject.head(10))
print(df_fileproject.tail(10))

print("----------------------------3-------------------------------------")#3
print(df_fileproject.shape)
print(df_fileproject.dtypes)
print("----------------------------4-------------------------------------")#4

#usuwanie danych osobowych i innych zbędnych

df_fileproject = df_fileproject.drop('Zmodyfikował(a)', axis=1)
df_fileproject = df_fileproject.drop('Identyfikator', axis=1)
df_fileproject = df_fileproject.drop('Klasoużytki', axis=1)

#dodanie kulomny
df_fileproject['Nazwa_powiatu'] = 'Kartuski'
#zmodyfikowanie nazw kolumn
#można użyć kilku metod lecz globalnie do zmiany można zastosować słownik

nanmescol = {
    "Nr działki" : "nr_dzialki",
    "Jednostka ewidencyjna" : "jednostka_ewidencyjna",
    "Obręb": "obreb",
    "Powierzchnia ewidencyjna": "powierzchnia_ewidencyjna",
    "Adres": "adres",
    "Granica sporna?": "granica_sporna",
    "Teren zamknięty?": "teren_zamkniet",
    "Rejestr zabytków": "rejestr_zabytkow",
    "Nazwa_powiatu": "nazwa_powiatu", }

df_fileproject = df_fileproject.rename(columns=(nanmescol))
#
#zamiana wartosci NAN na Brak_danych
df_fileproject = df_fileproject.fillna(value="Brak_danych")
print("----------------------------5-------------------------------------")#5

print(df_fileproject.head(10))

#Eksport danych do formatu xlsx jako dane do bazy

df_fileproject.to_excel('../venv/Danae_do_załadowania.xlsx',
                                                     sheet_name="Kartuzy",
                                                     index=True)

#Grupowanie danych wg powierzchni od największej działki
print("----------------------------6-------------------------------------")#6

max_pow_dzial = df_fileproject.groupby(['nr_dzialki'], as_index=False)['powierzchnia_ewidencyjna'].max()
powierzchnia = max_pow_dzial['powierzchnia_ewidencyjna'].sum()
max_pow_dzial['Powierzchnia_Calkowita'] = powierzchnia
print(max_pow_dzial)
#Zapis grupowania do pliku
max_pow_dzial.to_excel('../venv/Dzialki_rosnaco.xlsx',
                                                     sheet_name="Kartuzy",
                                                     index=False)


print("----------------------------7-------------------------------------")#7

print(df_fileproject.columns)
print(df_fileproject['powierzchnia_ewidencyjna'].count(), "hektarów")

