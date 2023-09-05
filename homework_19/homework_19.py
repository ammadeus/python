# 1. Numpy
#- Create an array with shape (4, 3) of: a. all zeros b. ones c. numbers from 0 to 11
#- Tabulate the following function: F(x)=2x^2+5, x∈[1,100] with step 1.
#- Tabulate the following function: F(x)=e^−x, x∈[−10,10] with step 1.

import numpy as np

array_zeros = np.zeros((4, 3))
array_ones = np.ones((4, 3))
array_numbers = np.arange(12).reshape(4, 3)

print("Array zeros:")
print(array_zeros)

print("\nArray ones:")
print(array_ones)

print("\nArray numbers 0 - 11:")
print(array_numbers)


def F(x):
    return 2 * x**2 + 5

x_values = np.arange(1, 101, 1)
f_values = F(x_values)

for x, f in zip(x_values, f_values):
    print(f"x = {x}, F(x) = {f}")
    
def F(x):
    return np.exp(-x) 

x_values = np.arange(-10, 11, 1)
f_values = F(x_values)

for x, f in zip(x_values, f_values):
    print(f"x = {x}, F(x) = {f}")


#2. Pandas
#- Import the dataset from this address and assign it to df variable.
#- Select only the Team, Yellow Cards and Red Cards columns.
#- How many teams participated in the Euro2012?
#- Filter teams that scored more than 6 goals

import pandas as pd

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"
df = pd.read_csv(url)

df_selected = df[["Team", "Yellow Cards", "Red Cards"]]

numero_squadre_partecipanti = df["Team"].nunique()
print("Numero di squadre partecipanti:", numero_squadre_partecipanti)

squadre_con_piu_di_6_gol = df[df["Goals"] > 6]
print("Squadre con più di 6 gol segnati:")
print(squadre_con_piu_di_6_gol)

#3. DataViz
  #Choose a dataset, you can use Seaborn example datasets. Create a cheat sheet for yourself containing all plot types discussed in the lecture.
  #Provide the following info:  
  #- Plot type 
  #- Use cases (categorical data, distribution, etc.) 
  #- Example on the dataset
  
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Grafic (
        ID INTEGER PRIMARY KEY,
        "Plot type"  TEXT,
        "Use cases" TEXT,
        "Example on the dataset" TEXT,
        "Python code" TEXT
    )
''')

data = [
    ("Scatter Plot", "Esplorazione dei dati", "Visualizzazione delle relazioni tra lunghezza e larghezza dei petali", 'sns.scatterplot(x="colonna_x", y="colonna_y", data=dataset)'),
    ("Bar Plot", "Dati categorici", "Numero di fiori di ciascuna specie nell'insieme di dati", 'sns.barplot(x="colonna_x", y="colonna_y", data=dataset, hue="specie")'),
    ("Histogram", "Distribuzione", "Distribuzione della lunghezza dei petali", 'sns.histplot(x="colonna_x", data=dataset, bins=20, kde=True)'),
    ("Line Plot", "Tendenze nel tempo", "Variazione della lunghezza dei sepali nel tempo", 'sns.lineplot(x="colonna_x", y="colonna_y", data=dataset)'),
    ("Box Plot", "Rilevamento di outlier", "Rappresentazione della distribuzione della larghezza dei sepali", 'sns.boxplot(x="colonna_x", y="colonna_y", data=dataset)'),
    ("Violin Plot", "Distribuzione", "Confronto tra distribuzioni di lunghezza dei petali per diverse specie", 'sns.violinplot(x="colonna_x", y="colonna_y", data=dataset)'),
]

for item in data:
    cursor.execute("INSERT INTO Grafic (\"Plot type\", \"Use cases\", \"Example on the dataset\", \"Python code\") VALUES (?, ?, ?, ?)", item)

conn.commit()
conn.close()