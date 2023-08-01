import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

# Łączenie z bazą PostgresSQL

conection = psycopg2.connect(
            host = "localhost",
            database = "postgres",
            user = "postgres",
            password = "baza4444")

#Cursor - obiekt wykonawczy
curs = conection.cursor()

readset = {"name": str, "prep_time": int}
df_dane = pd.read_excel("Danae_do_załadowania.xlsx", dtype=readset,
                               index_col=0, header= 0,)
print(df_dane)

#Sqlalchemy do wyeksportowania danych do bazy
engine = create_engine("postgresql+psycopg2://postgres:baza4444@localhost:5432/postgres")

try:
    df_dane.to_sql('geodezja', engine, if_exists='fail', index=True)
    print("Wprowadzono do bazy Danych Postgres")
except ValueError:
    print("Czy zastąpić istnięjące dane?")
    user_input = input('yes/no: ')
    yes_choices = ['yes', 'y']
    if user_input.lower() in yes_choices:
        df_dane.to_sql('geodezja', engine, if_exists='replace', index=True)
        print("Usunięto istniejące dane i zastapiono aktualnymi")
    else:
        print("Proces przerwano")
#Cursor - wykonywanie polecen SQL
curs.close()

#zamykanie kursora

curs.close()

#zakończenie sesji z bazą
conection.close()
print("Zakończenie sesji z bazą")
