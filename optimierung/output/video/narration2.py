#!/usr/bin/env python3
# Erzeugt Piper-Audio pro Szene -> n01.wav .. n10.wav
import subprocess, os
MODEL = "/tmp/piper/de.onnx"
N = [
 # S01
 "Hi! In den nächsten gut zehn Minuten erkläre ich dir das ganze Fach Optimierungsverfahren, "
 "mit Animationen und ganz ohne Vorwissen. Wir schauen uns sieben Themen an: Grundlagen, lineare "
 "Optimierung, Transport, nichtlineare Optimierung mit KKT, gradientenfreie Verfahren, Metaheuristiken "
 "und Mehrziel. Lass uns starten.",
 # S02
 "Optimierung heißt: wir suchen den besten Wert einer Zielfunktion f. Die x-Achse ist unsere Variable, "
 "an der wir drehen, die y-Achse der Funktionswert. Wir wollen hier das Minimum, also den tiefsten Punkt. "
 "Diese Funktion hat mehrere Täler, das nennt man lokale Minima. Das tiefste davon ist das globale Minimum, "
 "unser eigentliches Ziel. Eine Funktion mit mehreren Tälern heißt multimodal, mit nur einem unimodal. "
 "Dazu kommen oft Nebenbedingungen, die die erlaubten Werte einschränken.",
 # S03
 "Wie findet man so ein Minimum rechnerisch? Ganz einfach: am tiefsten Punkt ist die Steigung null. "
 "Schau auf die gelbe Tangente: während wir nach rechts wandern, wird sie immer flacher, und genau im "
 "Minimum ist sie waagerecht. Mathematisch setzen wir die erste Ableitung gleich null. Hier: f Strich gleich "
 "zwei x minus zwei gleich null, also x gleich eins. Und weil die zweite Ableitung positiv ist, ist es "
 "wirklich ein Minimum und kein Maximum.",
 # S04
 "Bei der linearen Optimierung mit zwei Variablen geht es grafisch. Wir wollen zwei x eins plus drei x zwei "
 "maximieren. Jede rote Linie ist eine Nebenbedingung; die grüne Fläche dazwischen ist der zulässige Bereich, "
 "also alles was erlaubt ist. Die gelbe gestrichelte Linie ist eine Isolinie der Zielfunktion. Wir schieben "
 "sie nach außen, so weit es geht. Sie verlässt den Bereich zuletzt in einer Ecke, und genau die ist optimal: "
 "der Punkt zwei, fünf. Merk dir: bei linearen Problemen liegt das Optimum immer in einer Ecke.",
 # S05
 "Beim Transportproblem liefern Produktionsstätten links, mit einem Angebot, an Läden rechts mit einer "
 "Nachfrage. Wir wollen die Transportkosten minimieren. Beim klassischen Problem muss Angebot gleich Nachfrage "
 "sein. Um eine erste Lösung zu finden, füllt man die Mengen nach einer Regel auf. Hier siehst du die "
 "Nordwesteckenregel: man beginnt oben links und arbeitet sich durch. Andere Methoden sind Matrix-Minimum "
 "und Vogel; Vogel liefert meistens die günstigste Startlösung.",
 # S06
 "Jetzt nichtlinear mit Nebenbedingung. Die blauen Kreise sind Höhenlinien der Zielfunktion, das Ziel liegt "
 "in der Mitte. Der grüne Kreis ist die Nebenbedingung: wir dürfen nur innerhalb bleiben. Der beste erlaubte "
 "Punkt liegt da, wo eine Höhenlinie den Kreis gerade berührt. Diesen Punkt findet man mit den KKT-Bedingungen: "
 "Man stellt die Lagrange-Funktion auf und prüft vier Dinge: Stationarität, Zulässigkeit, Komplementarität "
 "und das Vorzeichen von b. Der Trick: b mal g gleich null liefert eine Fallunterscheidung.",
 # S07
 "Was, wenn man keine Ableitung hat? Dann nimmt man gradientenfreie Verfahren wie Nelder-Mead. Man arbeitet "
 "mit einem Dreieck aus drei Punkten. Den schlechtesten Punkt spiegelt man über die Mitte der anderen beiden, "
 "das nennt man reflect. Ist der neue Punkt sehr gut, geht man noch weiter, das ist expand; ist er schlecht, "
 "zieht man zusammen, contract, oder man schrumpft das ganze Dreieck. So kriecht das Dreieck Schritt für "
 "Schritt zum Minimum.",
 # S08
 "Metaheuristiken nutzen Zufall clever. Bei der ein-plus-eins-Evolutionsstrategie haben wir eine Lösung, "
 "den gelben Punkt. Wir mutieren sie zufällig, das sind die grauen Kandidaten, und behalten nur, wenn es "
 "besser wird, also näher am Stern. Wichtig ist die Schrittweite sigma: Nach der Ein-Fünftel-Regel vergrößert "
 "man sie, wenn man oft erfolgreich ist, sonst verkleinert man sie. Verwandte Verfahren sind Simulated "
 "Annealing, die Partikelschwarmoptimierung und der Ameisenalgorithmus.",
 # S09
 "Beim letzten Thema haben wir mehrere Ziele gleichzeitig, hier f eins und f zwei, beide sollen klein sein. "
 "Jetzt gibt es nicht den einen besten Punkt. Ein Punkt dominiert einen anderen, wenn er in allem mindestens "
 "so gut und irgendwo echt besser ist. Die grauen Punkte werden dominiert, die sind raus. Die grünen werden "
 "von niemandem dominiert: das sind die Pareto-optimalen Punkte, die besten Kompromisse. Zusammen bilden sie "
 "die Pareto-Front. Welche man auswählt, entscheidet man über Crowding Distance oder Hypervolumen.",
 # S10
 "Das war es! So bestehst du die Klausur: Rechne aktiv mit Stift, die Übungen und die drei Probeklausuren. "
 "Lerne zu jedem Aufgabentyp ein festes Rezept. Löse erst verdeckt und vergleiche dann mit der Musterlösung. "
 "Und zeichne bei Grafik-Aufgaben den zulässigen Bereich sauber. Viel Erfolg, und jetzt ran an die PDFs!",
]
for i, text in enumerate(N, start=1):
    out = f"n{i:02d}.wav"
    subprocess.run(["/tmp/ttsenv/bin/python","-m","piper","-m",MODEL,"-f",out],
                   input=text.encode("utf-8"), check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("ok", out, len(text.split()), "Woerter")
print("FERTIG")
