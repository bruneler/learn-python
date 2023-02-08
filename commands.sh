# this is not a working script

whoami #zeigt usernamen an
uname -a #zeigt den OS Nmaen -a zeigt den Kernel, -s -r zeigt ales an. -v versionsinfos.
id # zeigt die Gruppenzugehörigekten an - u zeigt ur id an, mit -u -n nur den namen
ps # zeigt laufende Prozesse / - u root zeit alle prozesse welche unter root rechte laufen
top # zeigt laufende Prozesse und ihren Ressourcenverbrauch / -n 5 zeigt nur die top 5 an.e
df # Infos über Mounted Systeme / bsp: df -h ~ (-h macht es human readybale)
man #manpage für Shellcomands
cp #copy
rm #löschen
rmdir #löscht ein ganzes verzeichnis
mv #verschieben oder rename
touch #erstelltes leere datei
update file timestamp #
chmod # change/modify file permissions
wc # zählt wörter, zeichen usw
grep #filtert ausgabe nach einem bestimmten wort usw.
find #zum suchen nach Dateien welche ein wort beinhalten im aktuellen verzeihniss
pwd #aktuelles verzeichnis
cd #verzeichnis wechseln
mkdir #erstellt ein verzeichnis

cat #zeigt den Inhalt einer Datei alles auf einmal an
more #zeigt den Inhalt seitenweise an.
head n # zeigt die ersten n Zeilen einer Datei an.
tail n # zeigt die letzten n Zeilen einer Datei an.
echo xyz # zeigt einen Ausgabe an. z.B einen Input oder variable
echo $PATH # zeigt alle Pfade in meiner path variable
tar #zum Archiviern eines Set of Dateien
zip
unzip

hostname #zeigt den PC Namen an
ping
ifconfig
curl #zeigt den INhalt einer Datei über eine URL an
wget # Download eines files über eine URL

sort #sortiert eine Datei und gibt die einträge alphanummerisch zurück
sort -r # sortiert diie liste z-a
uniq # entfent doppeltte, wiederholende gleiche zeilen einer Datei. Aber nur bis zum nächsten neuen Eintrag.

grep # global regular expression print
grep -i # nicht case sensitive




cut -c 2-9 datei.txt # entfernt die zeichen 2 bis 9 jeder zeile
cut -d ' ' -f2 datei.txt # entfernt alles nach dem zeichen im hochkomma
paste datei1 datei1 datei3.txt # merged zeile für zeile dateien zusammen
default ist mit Tab. aber man kann als delimiter irgendwas setzen.
paste -d "," datei1 datei2 datei2

tar -cf meinarchiv.tar /diese/pfad/oder/datei/archiviert
-c #neues archiv
-z #für kompression dadurch geht der inhalt durch GNU programm g-zip
tar -czf meinarchiv.tar.gz /der/inhalt # stellt sicher dass .gz beim dateinamehm windows es verstehen kann z.B.
tar -tf # zeigt den inhalt eines archivs an.
tar -xf meinarchiv.tar #entpacken
tar -xzf mein archiv.tar.gz wenn es dekomprimieren gleichzeitig.
zip # geht auch. unterschied ist in de reihenfolge. zip kompriert zuerst, dann archiv. tar macht zuerst ein archiv und komprimiert dann.

| Pipe
programm1 | programm2 # Output von Programm1 ist Input von programm2

set # zeigt shell-variablen an. kann auch setzen. nur lokal gültig in shell aktueller shel

ls -la | sort
set | more

VARABLENNAME="Das ist der Text" # setzt eine shell-variable
unset #löscht wieder die Variable

env variable # Environment Variable. ausser das sie mit jedem shell-prozess vererbt wird.

export VARIABLENNAME # macht aus der Shell-variable eine Umgebungsvariable/Environment-Varialbe

env # listet alle env-variablen auf

tr #translate, tausch ein String aus einem input
cat pets.txt | tr "[a-z]" "[A-Z]" # tausch alle kleine buchstaben in grosse



curl -s --location --request GET https://api.coinstats.app/public/v1/coins/bitcoin\?currency\=USD | \grep -oE "\"price\":\s*[0-9]*?\.[0-9]*"
# gibt den aktuellen BitCoin Preis von einer öffentlichen API aus. mit GREP auf price.


    -o tells grep to only return the matching portion
    -E tells grep to be able to use extended regex symbols such as ?
    \"price\" matches the string "price"
    \s* matches any number (including 0) of whitespace (\s) characters
    : matches :
    [0-9]* matches any number of digits (from 0 to 9)
    ?\. optionally matches a . (this is in case price were an integer)

befehl1;befehl2 # mit ; kann man mehrere befehle auf einer Zeile schreiben.

crontab -e # öffnet das fenster für cronjobs
min hour day month wochentag command

if [ condition ]
then
	statement
else
	statement2
fi



if [ condition_1 ]
then
    statement_1
elif [ condition_2 ]
then
    statement_2
fi



$ cat elif_example.sh
a=2
b=2
if [ $a -lt $b ]
then
    echo "a is less than b"
elif [ $a == $b ]
then
    echo "a is equal to b"
else # Here a is not <= b, so a > b
    echo "a is greater than b"
fi




cat nested_ifs_example.sh
a=3
b=3
c=3
if [ $a == $b ]
then
    if [ $a == $c ]
    then
        if [ $b == $c ]
        then
            echo "a, b, and c are equal"
        fi
    fi
else
    echo "the three variables are not equal"
fi

#oder kurz

a=3
b=3
c=3
if [ $a == $b ] && [ $a == $c ] && [ $b == $c ]
then
    echo "a, b, and c are equal"
else
    echo "the three variables are not equal"
fi

# anstatt klammern, kann man auch test verwenden