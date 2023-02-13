# populäre Library für Datenanalyse
# mit as kann ich der import Bibliothek einen
# anderen Namen geben
import pandas as derpanda


# ermöglicht funktionen und Methoden wie read_csv(), Series(), DataFrame(), values etc.

#csv_path = "file1.csv"
#dataframe = derpanda.read_csv(csv_path)
#dataframe.head()  # zeigt die ersten 5 Zeilen des Frames an.

# Excel
#xlsx_path = "file1.xlsx"
#df = derpanda.read_excel(xlsx_path)
#df.head()

# Ein Dataframe aus einem Dictionary
songs = {"Album": ["Thriller", "Back in Black", "The Dark side of the Moon", "The Bodyguard", "Bat Out of Hell"], "Released": [1982, 1989, 1973, 1992, 1977], "Length": ["00:42:19", "00:42:11", "00:42:49", "00:57:44", "00:46:33"]}
songs_frame = derpanda.DataFrame(songs) # typecast mit panda funktion zu einem Dataframe
print(songs_frame)

# Neues Frame mit einzelnen Spalten

Spalte12 = songs_frame[["Album", "Released"]]
print(Spalte12)

songs_frame["Released"].unique()

# Dataframe Bedingungen
new_songs_frame = songs_frame[songs_frame["Released"] >= 1980]
print(new_songs_frame)

# Speichern in csv

new_songs_frame.to_csv("songs_after_1980.csv")

print(songs_frame.loc[0:2, "Album"])
print(songs_frame.iloc[0:2, 0])  # mit iloc am schluss eine zahl mehr
# von:bis(Zeile),Spalte

A = ["1","2","3"]
for a in A:
    print(2*a)


for i in range(1, 5):
    if (i!=2):
        print(i)


