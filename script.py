import sys # Used for sys Version function

print('Hello, Python!')

# Check the Python Version
print(sys.version)

# Type of 12 ,2.14 und a string
print(type(12))
print(type(2.14))
test_type_string = type("Das ist ein Test")
print(test_type_string)

# SystemSettings about float z.b
print(sys.float_info)

# Convert integer 2 to a float and check its type
print(type(float(2)))

# Convert the string "1.2" into a float
print(float('1.2'))

# Convert Boolean True to int
print(int(True))
print(int(False))

type(6//2) # int, as the double slashes stand for integer division

# As seen in the quiz above, we can use the double slash for integer division, where the result is rounded down to the nearest integer:
# Integer division operation expression

25 // 6 # gibt 5

total_min = 43 + 42 + 57 # Total length of albums in minutes
# Name the variables meaningfully

total_hours = total_min / 60 # Total length of albums in hours

total_hours = (43 + 42 + 57) / 60  # Total hours in a single expression

name = "Michael Jackson"
print(name)
print(name[0])
print(name[-1]) # Von Hinten anfangen zu zählen
print(name[0:5]) # Zeichen 0-5 des Strings
print(name[::2]) # gibt jeden 2ten String an. Das Erste Zeichen auch.
print(name[0:5:2]) # Jedes 2te Zeichen bis zum 4ten Zeichen.
print(len("Michale Jackeson")) # Zeigt die Länge eines Strings hier 16. Also Array[0:15]

# String mit Variable
statement = name+" Ist der Beste"
print(statement)
print(3*statement)

# Ein Backslash \ steht für eine Escape Sequenz.
# z.B.
# \n für new Line
# \t für new tab
# \\ für eine Backslash zu machen oder mit einem r vor dem String
print(r"Michael \ Jackson")

# Methoden auf Stings

A = " thriller ist das beste album"
B = A.upper()
print(B)
C = A.replace("thriller","mini Eier")
print(C)
print(C.upper())

# Methode find findet substrings.

print(C.find("eier")) # Wenn ausgabe -1, dann ist das Wort falsch oder es gibt keine Übereinstimmjung
print(C.find("Eier")) # Find gibt an, wo das wort gefunden wurde, bei welchem Zeichen, hier bei 6.

wtype = 2/2

#Tuples /
Ratings = (10,4,5,3,8,8,5)
DivRating = ("Schlecht",3,10,1.2,"Gut")
print(type(DivRating)) # Data type tuple
RatingExt = DivRating + ("Sehr Gut", 4,5) # 2 Tupeln addiert
print(RatingExt)

# Slicing

print(RatingExt[0:4]) # dies gibt das erste bis 3te an. BEACHTE: Die letzte Zahl immer 1 höher als den wert den mal will.
RatingsSorted = sorted(Ratings)
print(RatingsSorted) # keine Strings.
# Tuples sind umutables und können nicht nochmal zugewiesen werden. Es muss immer ein neues tupe erstellt werden

# Nesting Tuples

Nesting =(1,2,3,("Rap","Soul"),(4,5),("Disco",(1,2)))
print(Nesting)
print(Nesting[3])
print(Nesting[3][1])
print(Nesting[3][1][2:4]) # kann bis auf einzelne zeichen

# Unterschied tuples und Lists.
# List ist mutuable Einzelne Werte können getauscht werden.
Liste = [1, 2, 3, "Rap", "Soul", 4, 5, ["Disco", 1, 2]]
print(Liste)
Liste.extend(["Test", 100])
print(Liste)
# List mit [] statt () klammern.
Liste.append(["Test",100])
print(Liste)

# Unterschied extend und append. Append fügt dein Eintrag als ganzes
# element hinz. Der Indux wächst um 1.
# Bei extend wird jedes element einzeln hinzugefügt. Der INdex wächst mit der anzahl Element darin.

# Mutuable
L = ["Thun", 1, 2, 3]
print(L)
L[0] = "Bern"
print(L)

# Löschen mit del
del(L[0])
print(L)

# convert a String to a list mit split funktion
T = "Das ist ein Test".split()
print(T)
T2 = "Dies,ist,ein,Test".split(",")
print(T2)
A = ["banane", 2]
B = A
B[0] = "Apfel"
print(B)
print(A)
# um zu umgehen, dass auch die Liste A überschrieben wird
# kann mit die Liste klonen, damit wird eine neue Liste erstellt, unabhänig.
C = B[:]
C[0] = "Banane"
print(B)
print(C)

# dictionaries {}
# Syntax {"key":Value, "key2" :"value2","key3" :[3,3,3], "key4":(4,4,4),('key5"):5}
# Keys sind eindeutig und nicht änderbar.
Dic = {"key": 1, "key2": "value2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'):5}
print(Dic)
print(type(Dic))
# Zugriff wie immer über den Schlüssel wie folgt.
print(Dic["key3"])
# Neuen Wert hinzufügen
Dic["Key100"] = "fuck"
print(Dic)
del(Dic)["key2"]
print(Dic)

# Prüfen ob ein Key in einemDict vorhanden ist
Test = "Key1" in Dic
print(Test)
print("Key100" in Dic)
print(Dic.keys()) # Nur die Keys drucken
print(Dic.values())

# Sets, wie Tupeln und Listen, aber die Position ist nicht fix.
# Sets haben eindeutige Elemente
# Erstellen wie ein Dictionary, nur ohne Doppelpunkt.
Set1 = {"Die", "obergiele", "Sets", "Sets"}
print(Set1) # Doppelte Werte werden aus dem Set entfernt
#Convert a list to a set
#SetbyList = set(List
Set1.add("Porno")
print(Set1)
Set1.remove("Die")
print(Set1)
# Suchen in Sets wie in Dic
print("Porno" in Set1)
Set2 = {"test", "Test4", "Porno"}
print(Set1 & Set2) # Gibt die Überschneidung an in einem neuen Set.
Set3 = Set1 & Set2
# Die Sets verbinden
Set4 = Set1.union(Set2, Set3)
print(Set4)

# Prüfen auf ein Subset. Sind alle elemente eines Sets bereits ein einem andersn Set vorhanden. Also überflüssig eigentich.
print(Set2.issubset(Set4))