# Open File with open
# Function, Pfad, Filename, mode
File1 = open("/testfiletoopen.txt", "r")  #Modes: r(read) , w(write), a(append)

print(File1.name) # Gibt einen String mit dem Dateinamen
print(File1.mode) # Zeigt an, in welchem Modus die Datei ist.
File1.close() # Man sollte die Datei immer mit close() wieder schliessen.

# Mit Close schliessen kann manchmal mühsam sein. Dafür können wir
# with-Statement verwenden. Dies ist die bessere Variante, da das File automatisch geschlossen wird

with open("testfiletoopen.txt", "r") as File1:  # as File1 (File1 ist ein File Object)
    file_stuff = File1.read()
    print(file_stuff)

print(File1.closed)

# Inhalt des Dateiinhalts ausserhalb des open Blocks.
print(file_stuff)

# Wir können jede Zeile einer Datei auch als Liste einlesen und bearbeiten.

with open("testfiletoopen.txt", "r") as File1:  # as File1 (File1 ist ein File Object)
    file_stuff = File1.readlines()
    print(file_stuff)

print(file_stuff[1])  # Auf einzelne Elemente der Liste zugreifen.


# readlines() liest alle Zeilen ein. readline() würde nur eine Zeile einlesen. ruft man readline() 2x mal auf,
# wird zuerst Zeile1, dann Zeile2 ausgegeben.
# Man kann auch loopen.

with open("testfiletoopen.txt", "r") as File1:
    for line in File1:
        print(line)

# Die ersten 2 Zeichen von einer  Zeile
with open("testfiletoopen.txt", "r") as File1:
    file_stuff = File1.readlines(3)
    print(file_stuff)
    file_stuff = File1.readlines(1)
    print(file_stuff)
    file_stuff = File1.readlines(5)
    print(file_stuff)


# Writing Files with open
# Falls eine Datei bereits mit diesem Namen besteht, wird die Datei überschrieben.
File1 = open("testfiletowrite.txt", "w")  #Modes: r(read) , w(write), a(append)
File1.write("Dieser Text wurde eingefügt mit File1.write()\n")
File1.write("Eine 2te Zeile File1.write()\n")


# Writing files with open with loop
Zeilen = ["Dies ist eine Testzeile 1\n", "Dies ist eine Testzeile 2\n", "Dies ist eine Testzeile 3\n"]
with open("testfiletowrite.txt", "w") as File1:
    for zeile in Zeilen:
        File1.write(zeile)

# Writing file with open with append. Mit append "a" wird die Datei nicht überschrieben sondern angehngt.
Zeilen = ["Dies ist eine Testzeile 4\n", "Dies ist eine Testzeile 52\n", "Dies ist eine Testzeile 6\n"]
with open("testfiletowrite.txt", "a") as File1:
    for zeile in Zeilen:
        File1.write(zeile)


# Inhalt einer Datei in eine andere Datei kopieren.
with open ("testfiletoopen.txt", "r") as readfile: # öffnet die Datei zum kopieren
    with open("datacopied.txt", "w") as writefile: # öffnet eine neue Datei zum schreiben
        for line in readfile:  # for Loop, geht jede Zeile durch
            writefile.write(line)  # und schreibt diese in die neue Datei.

# Loading Data with Pandas
