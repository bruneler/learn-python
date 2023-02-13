import sys  # Used for sys Version function

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

type(6 // 2)  # int, as the double slashes stand for integer division

# As seen in the quiz above, we can use the double slash for integer division,
# where the result is rounded down to the nearest integer:
# Integer division operation expression

Erg = 25 // 6  # gibt 5

total_min = 43 + 42 + 57  # Total length of albums in minutes
# Name the variables meaningfully

total_hours = total_min / 60  # Total length of albums in hours

total_hours_singleExpr = (43 + 42 + 57) / 60  # Total hours in a single expression

name = "Michael Jackson"
print(name)
print(name[0])
print(name[-1])  # Von Hinten anfangen zu zählen
print(name[0:5])  # Zeichen 0-5 des Strings
print(name[::2])  # gibt jeden 2ten String an. Das Erste Zeichen auch.
print(name[0:5:2])  # Jedes 2te Zeichen bis zum 4ten Zeichen.
print(len("Michale Jackeson"))  # Zeigt die Länge eines Strings hier 16. Also Array[0:15]

# String mit Variable
statement = name + " Ist der Beste"
print(statement)
print(3 * statement)

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
C = A.replace("thriller", "mini Eier")
print(C)
print(C.upper())

# Methode find findet substrings.

print(C.find("eier"))  # Wenn ausgabe -1, dann ist das Wort falsch oder es gibt keine Übereinstimmjung
print(C.find("Eier"))  # Find gibt an, wo das wort gefunden wurde, bei welchem Zeichen, hier bei 6.

wtype = 2 / 2

# Tuples /
Ratings = (10, 4, 5, 3, 8, 8, 5)
DivRating = ("Schlecht", 3, 10, 1.2, "Gut")
print(type(DivRating))  # Data type tuple
RatingExt = DivRating + ("Sehr Gut", 4, 5)  # 2 Tupeln addiert
print(RatingExt)

# Slicing

print(
    RatingExt[0:4])  # dies gibt das erste bis 3te an. BEACHTE: Die letzte Zahl immer 1 höher als den wert den mal will.
RatingsSorted = sorted(Ratings)
print(RatingsSorted)  # keine Strings.
# Tuples sind umutables und können nicht nochmal zugewiesen werden. Es muss immer ein neues tupe erstellt werden

# Nesting Tuples

Nesting = (1, 2, 3, ("Rap", "Soul"), (4, 5), ("Disco", (1, 2)))
print(Nesting)
print(Nesting[3])
print(Nesting[3][1])
print(Nesting[3][1][2:4])  # kann bis auf einzelne zeichen

# Unterschied tuples und Lists.
# List ist mutuable Einzelne Werte können getauscht werden.
Liste = [1, 2, 3, "Rap", "Soul", 4, 5, ["Disco", 1, 2]]
print(Liste)
Liste.extend(["Test", 100])
print(Liste)
# List mit [] statt () klammern.
Liste.append(["Test", 100])
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
del (L[0])
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
Dic = {"key": 1, "key2": "value2", "key3": [3, 3, 3], "key4": (4, 4, 4), 'key5': 5}
print(Dic)
print(type(Dic))
# Zugriff wie immer über den Schlüssel wie folgt.
print(Dic["key3"])
# Neuen Wert hinzufügen
Dic["Key100"] = "fuck"
print(Dic)
del Dic["key2"]
print(Dic)

# Prüfen ob ein Key in einemDict vorhanden ist
Test = "Key1" in Dic
print(Test)
print("Key100" in Dic)
print(Dic.keys())  # Nur die Keys drucken
print(Dic.values())

# Sets, wie Tupeln und Listen, aber die Position ist nicht fix.
# Sets haben eindeutige Elemente
# Erstellen wie ein Dictionary, nur ohne Doppelpunkt.
Set1 = {"Die", "obergiele", "Sets", "Sets"}
print(Set1)  # Doppelte Werte werden aus dem Set entfernt
# Convert a list to a set
# SetbyList = set(List
Set1.add("Porno")
print(Set1)
Set1.remove("Die")
print(Set1)
# Suchen in Sets wie in Dic
print("Porno" in Set1)
Set2 = {"test", "Test4", "Porno"}
print(Set1 & Set2)  # Gibt die Überschneidung an in einem neuen Set.
Set3 = Set1 & Set2
# Die Sets verbinden
Set4 = Set1.union(Set2, Set3)
print(Set4)

# Prüfen auf ein Subset. Sind alle elemente eines
# Sets bereits ein einem andersn Set vorhanden. Also überflüssig eigentich.
print(Set2.issubset(Set4))

# Vergleichsoperatoren
# == ist gleich
# > grösser als
# >= grösser oder gleich gross
# < kleiner als
# <= kleiner oder gleich gross
# != ungleich/not same. Gibt True zurück wenn ungleich
# == und != funktioniert auch mit Strings

# Branching / Verzweigungen
# Klammern in if Prüfung nicht zwingend. Wenn if true,
# dann wird das eingerückte ausgeführt. Für false muss dann else verwendet werden
# für eine zweite prüfung, wenn das erste if nicht gegeben
# mit elif
Alter = 18
if Alter > 20:
    print("Sie dürfen ans Hardcore Konzert")
elif Alter > 17:
    print("Sie dürfen ans Soft konzert")
else:
    print("Kind, EINTRITT verboten!")

print(Alter)

# Logic Operators wie 'not' prüft boolean wert

print(not True)  # gibt false.
print(not False)  # gib true

# OR: Wenn eine von beiden Boolean Variablen True ist, ist der neue boolen Wert True
# nur wenn beide false, gibt or ein false.
Bool_A = True
Bool_B = False

Jahrgang = 1987

if (Jahrgang < 1980) or (Jahrgang > 1989):
    print("True: Jahrgang ist vor oder nach den 80igern")
else:
    print("False: Ist ein 80er")

# And: Beide boolean Werte müssen True sein.
if (Jahrgang > 1979) and (Jahrgang < 1990):
    print("True: 80er")
else:
    print("False: ")

# Loops - for loops und while loops
# for Loop hauptsächlich für Listen, vieles geht auch für tupeln
# range - generiert eine geordnete Liste gemäss dem Input
Range = range(10, 20)  # 10-19
print(*Range)
print(*range(100, 130))  # 100 - 129 ohne umweg über variable

# for mit Tupel
print(Liste)
for i in range(0, 5):
    Liste[i] = "Boss"

print(Liste)

ListeNew = ["Adam", "John", "Wick"]
print(ListeNew)

# mit enumerate können wir den index und den wert einer Liste
# und dadurch iterieren können.
for i, x in enumerate(ListeNew):  # i ist der index, x das element des indexes
    print(i, x)

# while Schleife

ListWhile = ["grün", "grün", "Grün", "blau"]
NewListWhile = []
i = 0  # Start bei index
while ListWhile[i] == "grün":
    NewListWhile.append(ListWhile[i])
    i = i + 1
print(ListWhile)
print(NewListWhile)


# Functions
# erste Zeile mit def und : am schluss
# der Codeblock einrücken
# am Schluss return

def add1(input):
    """Add 1 to input"""
    output = input + 1
    return output


def add2(input):
    """Add 2 to input"""
    output = input + 2
    return output


print(add2(5))

# sorted vs sort
# sorted(List) sortiert und speichert die Sortierte Liste in eine neue Liste
# List.sort() sortiert die Liste und speichert sie so ab

help(add1)


# Funktion kann mehrere Parameter als Input haben.
def Multi(zahl1, zahl2):
    """Mulitpliziert zahl1 mit zahl2 und gibt das Ergebnis zurück"""
    ErgMulit = zahl1 * zahl2
    return ErgMulit


print(Multi(345, 3556))


def mj():
    """gibt nur den String Michael Jackson aus"""
    print("Michael Jackson")


mj()


## Leere funktion. Python erlaubt keine leeren Body.
## Dazu gibt es den Ausdruck "pass". im Hintergrund wirdd dann ein return None eingefügt.


def Nothing():
    pass


print(Nothing())

# Loop in functions

Albumbewertungen = [5, 6.6, 10, 8, 4.3, 1, 9, 9.99]


def printAlbumwertungen(Input):
    for i, x in enumerate(Input):
        print("Album", i, "Bewertung ist", x)


printAlbumwertungen(Albumbewertungen)


# Collecting Arguments
def Kunstlername(*namen):
    for i in namen:
        print(i)


Kunstlername("Michael Jackson", "Bruno Banani", "Wu-Tang Clan")


# Variablendeklaration innerhalb Funktionen sind fluchtig
# ausser man deklariert sie darin mit global

def PinkFloyd():
    global ErwUmsatz
    ErwUmsatz = "100 Millionen"
    return ErwUmsatz


PinkFloyd()
print(ErwUmsatz)

# Exception Handling
# try: .... except:....

try:
    getfile = open("myFile", "r")
    getfile.write("File for something")
except IOError:
    print("Kann die Datei nicht zum lesen öffnen")
# except:
#    print("irgend ein anderer Fehler als IOERROR")
else:
    print("Es hat wunschgemäss funktioniert")
# finally:
#   getfile.close()
#    print("Datei wurde geschlossen")


# Objekte
# Jedes Objekt hat ein:
# - type
# - ein interne daten representation ( ein blueprint)
# - ein set von Prozeduren zum interagieren mit dem Objekt (Methoden)
# - ein Objekt ist eine Instanz von einem type

# Methoden
# Eine Klassen oder type Methode ist eine Funktion, welche jede Instanz diese Klasse oder type zur Verfügung stellt.
# damit interagiert man mit den Daten in einem Objekt. z.B. sorting Liste.sort()
# Methoden werden am Ende eines Objekts angefügt. objekt.methode()
# Liste.reverse() grösster wert zuerst

# Eigene Klasse oder Type
# Die Klasse hat Data Attribute und Methoden

class Kreis(object):  # Klasse definieren object ist Klassenparent
    def __init__(self, radius, farbe):  # Daten Atribute die beim initialisieren jeder Instanz verwendet werden.
        #  mit Standardwerten
        #  def __init__(self, radius=5, farbe="schwarz"):
        self.radius = radius
        self.farbe = farbe
    def add_radius(self,r):  # eigene Methode um den Radius zu ändern
        self.radius = self.radius + r
        return self.radius

class Rechteck(object):
    def __int__(self, laenge, breite,
                farbe):  # __init__ ist eine spezial Mehtode oder Konstruktor, welche
        # zum initialisieren von Daten Atributen verwendet wird.
        # 'lange' und 'breite' sind parameter welche benötigt werden zum starten.
        # Der Parameter 'self' referenziert dabei auf die neu erzeugte Instanz der Klasse.
        self.laenge = laenge
        self.breite = breite
        self.farbe = farbe


# Das Objekt erstellen
GreenKreis = Kreis(10, "Grün")
test_radius = GreenKreis.radius
print(test_radius)
test_radius = GreenKreis.add_radius(50)
print(test_radius)
GreenKreis.farbe = "Hellgrün"  # ändert die Farbe
#  GreenKreis.drawCircle()

print(dir(GreenKreis))  # zeigt alle attribute und methoden eines Objektes an.
# die Attribute mt _Atribute sind nur für internen Gebrauch und nicht relevant.

