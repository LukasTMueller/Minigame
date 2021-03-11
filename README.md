# Minigame
 
Aufgabe:
Erstellen eines Geschicklichkeitsspiels, bei welchem man, durch anklicken, eine bestimmte Anzahl von Zielen treffen soll.


Probleme:
Erstellen eines neuen Ziels, sobald das vorherige getroffen wurde -> Einfaches verschieben führte zu Problemen.

Fehlerhafter Zähler für Treffer und Nichttreffer -> Beim erreichen des Ziels musste das Programm teilweise neugestartet werden.

Implementierung der Möglichkeit die Anzahl der Ziele zu ändern -> Wenn die Anzahl nach dem Spielstart geändert wurde
								und unter die Anzahl der bisher getroffenen Ziele gesetzt wurde,
								beendete das Programm nicht mehr und lief weiter.

Erscheinen weiterer Ziele sobald "Start" gedrückt wurde -> Ließen sich nicht anklicken und Programm musste neugestartet werden.


Fehlerbehebung:
Nutzung von zwei verschiedenen Zielen, welche abwechselnd erstellt und gelöscht werden -> Wird durch einen Zähler gesteuert

Änderungen an den betreffenden Variablen für die Zähler und den Bedingungen für das beenden des Spiels

Deaktivierung des "Settings" Button, sobald "Start" gedrückt wird. Reaktivierung sobald die Runde vorbei ist, oder "Reset" gedrückt wird.

Bei drücken von "Start" wird zusätzlich die "Reset"-Funktion aufgerufen.