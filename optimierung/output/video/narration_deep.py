#!/usr/bin/env python3
import subprocess
MODEL="/tmp/piper/hi.onnx"
N=[
 # D01
 "Willkommen zum Komplettkurs Optimierungsverfahren. Anders als der Überblick gehe ich jetzt jedes einzelne "
 "Verfahren durch, mit den passenden Formeln. Wir behandeln die Grundlagen, analytische Optima, "
 "Gradientenabstieg und Newton, die lineare und die ganzzahlige Optimierung, das Transportproblem mit "
 "Konstruktion und Optimierung, die KKT-Bedingungen, gradientenfreie Verfahren, alle Metaheuristiken und "
 "die Mehrzieloptimierung. Pausiere ruhig bei den Formeln.",
 # D02
 "Jedes Optimierungsproblem hat dieselbe Struktur: Wir minimieren eine Zielfunktion f, unter Nebenbedingungen. "
 "Ungleichungen schreibt man als g von x kleiner gleich null, Gleichungen als h von x gleich null. Wichtig ist "
 "die Einteilung: Ist alles linear, oder kommt etwas Nichtlineares vor, wie Wurzeln, Quadrate oder Sinus? Sind "
 "die Variablen reell oder ganzzahlig? Gibt es ein Ziel oder mehrere? Und hat die Funktion nur ein Optimum, "
 "also unimodal, oder mehrere, dann multimodal?",
 # D03
 "Bei einer Variable findest du Optima so: Erste Ableitung gleich null setzen. Im Beispiel f gleich zwei x hoch "
 "drei minus neun x Quadrat plus zwölf x. Die Ableitung, sechs x Quadrat minus achtzehn x plus zwölf gleich null, "
 "liefert x gleich eins und x gleich zwei. Welche Art es ist, sagt die zweite Ableitung: Bei x gleich eins ist sie "
 "negativ, also ein Maximum, bei x gleich zwei positiv, also ein Minimum.",
 # D04
 "Bei mehreren Variablen setzt du den ganzen Gradienten gleich null. Dann bildest du die Hesse-Matrix, also die "
 "Matrix der zweiten Ableitungen, und schaust auf ihre Eigenwerte. Sind alle positiv, ist es ein Minimum, alle "
 "negativ ein Maximum, und bei gemischten Vorzeichen ein Sattelpunkt. Im Beispiel führt der Gradient auf die "
 "Punkte eins null und minus eins null; der erste ist ein Minimum, der zweite ein Sattelpunkt.",
 # D05
 "Wenn man das Optimum nicht direkt ausrechnen kann, tastet man sich heran. Beim Gradientenabstieg gilt: x neu "
 "gleich x minus lambda mal Gradient von f. Der Gradient zeigt immer bergauf, deshalb geht man für eine "
 "Minimierung in die Gegenrichtung. Lambda ist die Schrittweite und steuert, wie weit man pro Schritt geht.",
 # D06
 "Das Newton-Verfahren ist schneller, weil es zusätzlich die Krümmung nutzt. Die Formel: x n plus eins gleich x n "
 "minus f Strich durch f zwei Strich. Beispiel: f gleich ein Drittel x hoch drei minus zwei x, Start bei x null "
 "gleich zwei. Ein Schritt ergibt zwei minus zwei Viertel, also eins Komma fünf. Das Verfahren konvergiert gegen "
 "Wurzel zwei, etwa eins Komma vier eins.",
 # D07
 "Bei der linearen Optimierung bringt man das Problem zuerst in die Standardform: nur Gleichungen und "
 "nicht-negative Variablen. Eine Ungleichung g kleiner gleich b wird mit einer Slack-Variable s zu g plus s gleich "
 "b. Lösen kann man grafisch oder mit dem Simplex-Algorithmus: Er startet im Ursprung und läuft entlang der "
 "Kanten von Ecke zu Ecke, bis es nicht mehr besser wird. Das Optimum liegt immer in einer Ecke.",
 # D08
 "Bei der ganzzahligen Optimierung dürfen die Variablen nur ganze Zahlen sein. Man löst zuerst das kontinuierliche "
 "Problem, das ist der rote Punkt. Liegt er nicht auf ganzen Zahlen, fügt man Schnittebenen hinzu oder verzweigt "
 "mit Branch-and-Bound, bis man beim ganzzahligen Optimum landet, dem gelben Punkt. Wichtig: Der ganzzahlige "
 "Zielwert ist immer kleiner oder gleich dem kontinuierlichen.",
 # D09
 "Das Transportproblem: Produktionsstätten beliefern Läden, und beim klassischen Fall ist die Summe von Angebot "
 "und Nachfrage gleich. Ziel ist, Summe Kosten mal Menge zu minimieren. Für eine erste zulässige Lösung gibt es "
 "drei Methoden: Die Nordwesteckenregel beginnt oben links. Die Matrix-Minimum-Methode belegt immer die günstigste "
 "Zelle zuerst. Und die Vogel-Methode arbeitet mit Strafkosten und ist meistens am besten.",
 # D10
 "Die Startlösung ist aber oft noch nicht optimal. Mit Stepping-Stone oder der MODI-Methode verbessert man sie. "
 "Bei MODI bestimmt man Potentiale u und v, sodass für jede belegte Zelle u i plus v j gleich den Kosten c i j ist. "
 "Dann berechnet man für die leeren Zellen die reduzierten Kosten, c i j minus u i minus v j. Ist eine negativ, "
 "kann man über einen Zyklus Menge umverteilen und Kosten sparen. Sind alle größer gleich null, ist die Lösung optimal.",
 # D11
 "Bei nichtlinearen Problemen mit Nebenbedingungen nutzt man die KKT-Bedingungen. Zuerst die Lagrange-Funktion: "
 "L gleich f plus a mal h plus b mal g. Dann gelten vier Bedingungen: Erstens Stationarität, der Gradient von L ist "
 "null. Zweitens Zulässigkeit, h gleich null und g kleiner gleich null. Drittens Komplementarität, b mal g gleich "
 "null. Und viertens, b größer gleich null. Der Trick ist die Fallunterscheidung: Entweder b ist null, die "
 "Ungleichung inaktiv, oder g ist null, sie ist aktiv.",
 # D12
 "Zwei Begriffe noch im nichtlinearen Bereich. SQO, die sequentielle quadratische Optimierung, nähert die "
 "Zielfunktion quadratisch und die Nebenbedingungen linear an und löst dann eine Folge einfacher Teilprobleme. "
 "Und Konvexität: Eine Funktion ist konvex, wenn die zweite Ableitung größer gleich null ist, beziehungsweise die "
 "Hesse-Matrix positiv semidefinit. Das ist wichtig, denn bei konvexen Problemen ist jedes lokale Optimum "
 "automatisch global.",
 # D13
 "Hat man keinen Gradienten, helfen gradientenfreie Verfahren. Nelder-Mead arbeitet mit einem Simplex aus D plus "
 "eins Punkten. Den schlechtesten Punkt spiegelt man über die Mitte der anderen, das ist reflect. Je nachdem, wie "
 "gut der neue Punkt ist, folgt expand, contract oder shrink. Nelder-Mead sucht lokal, während DIRECT global sucht.",
 # D14
 "DIRECT teilt den Suchraum in Rechtecke und untersucht die potentiell optimalen. Trägt man Größe gegen "
 "Funktionswert auf, sind das die Punkte auf der unteren-rechten Hülle, also große Rechtecke mit niedrigem Wert. "
 "SMBO dagegen baut ein Surrogatmodell, eine billige Näherung der teuren Zielfunktion, wertet dessen Minimum aus "
 "und verbessert damit das Modell Schritt für Schritt.",
 # D15
 "Jetzt die Metaheuristiken. Die ein-plus-eins-Evolutionsstrategie mutiert eine einzige Lösung und behält sie nur, "
 "wenn sie besser ist. Die Schrittweite passt die Ein-Fünftel-Regel an: Ist die Erfolgsrate größer als ein Fünftel, "
 "wird sigma mit a multipliziert, sonst durch a geteilt. Evolutionäre Algorithmen arbeiten mit einer ganzen "
 "Population und nutzen Mutation, wie den Bitflip, Crossover und Selektion.",
 # D16
 "Drei weitere Metaheuristiken solltest du kennen. Simulated Annealing akzeptiert auch schlechtere Lösungen, und "
 "zwar mit der Wahrscheinlichkeit e hoch minus delta f durch T; die Temperatur T sinkt langsam, dadurch wird die "
 "Suche immer gieriger. Die Partikelschwarmoptimierung aktualisiert die Geschwindigkeit aus drei Teilen: Trägheit, "
 "der kognitiven Komponente zum eigenen Besten, und der sozialen zum Besten des Schwarms. Und der "
 "Ameisenalgorithmus nutzt Pheromone, die mit der Zeit verdunsten.",
 # D17
 "Beim letzten Thema gibt es mehrere Ziele. Ein Punkt dominiert einen anderen, wenn er in allem mindestens so gut "
 "und irgendwo echt besser ist. Nicht dominierte Punkte heißen Pareto-optimal und bilden die Pareto-Front. Beim "
 "Non-Dominated-Sorting trägt man diese Schichten nacheinander ab, das gibt die Ränge. Die Crowding Distance "
 "summiert die normierten Abstände der Nachbarn, Randpunkte bekommen unendlich. Das Hypervolumen misst die "
 "abgedeckte Fläche zu einem Referenzpunkt. NSGA zwei nutzt die Crowding Distance, SMS-EMOA den Hypervolumen-Beitrag.",
 # D18
 "Das waren alle Verfahren. Behandle jedes wie ein festes Rezept: erkennen, passende Formel, durchrechnen. Übe "
 "aktiv mit den Übungen und den drei Probeklausuren, erst verdeckt, dann mit der Musterlösung. Schreib dir die "
 "Formeln auf dein Open-Book-Blatt. Viel Erfolg bei der Klausur!",
]
for i,text in enumerate(N,1):
    out=f"d{i:02d}.wav"
    subprocess.run(["/tmp/ttsenv/bin/python","-m","piper","-m",MODEL,
                    "--length-scale","1.05","--sentence-silence","0.35","-f",out],
                   input=text.encode("utf-8"),check=True,
                   stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    print("ok",out,len(text.split()),"W")
print("FERTIG")
