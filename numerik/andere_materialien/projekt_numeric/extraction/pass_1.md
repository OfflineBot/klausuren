# Pass 1: Struktur & Konzepte — "Numerical Methods" (Prof. Dr.-Ing. Mark Schutera)

Quelle: `Numerical Methods - notes_numerischemethoden.pdf` (71 Seiten, englische Vorlesungsnotizen, "Unfinished Lecture Notes"). Seitenangaben `[S. n]` = aufgedruckte PDF-Seitenzahl (identisch mit physischer Seite).

---

## Vorspann (S. 1–8)

### [S. 1] Titelseite
- Autor: PROF. DR.-ING. MARK SCHUTERA
- Titel: NUMERICAL METHODS
- Reihe/Untertitel: UNFINISHED LECTURE NOTES
- Sonst leer.

### [S. 2] Impressum / Copyright
- Copyright © 2026 Prof. Dr.-Ing. Mark Schutera, "published by unfinished lecture notes".
- Hinweis: "Combobulated with the help of multiple large language model driven tools." Lizenz: Creative Commons Attribution-NonCommercial 4.0 International ("CC BY-NC-SA 4.0"); keine kommerzielle Nutzung; Weitergabe von Bearbeitungen unter gleicher Lizenz; Nutzung über die Lizenz hinaus nur mit expliziter Genehmigung des Autors; Material "as is", ohne Gewährleistung.
- Die Notizen sind "by their very nature, unfinished" und verbessern sich mit jedem Leser; Fehler/Einwände/Ergänzungen per Pull Request an: https://github.com/Quillstacks/LectureMaterial/tree/main/lecturenotes/notes_numerischemethoden — "Every contribution is welcome."
- Datums-/Versionszeile: *2026-05-06 · feisty cranberry Hermelin*; QR-Code (rechts unten).

### [S. 3] Zitatseite
> "AN INFINITELY ACCURATE APPROXIMATION IS NO LONGER AN APPROXIMATION." — PROBABLY SOMEONE SMART

### [S. 4] Leer.

### [S. 5] Inhaltsverzeichnis (Contents)
Kapitelstruktur des gesamten Dokuments:
1. Enter Numerical Methods — S. 9
2. Floating-Point Arithmetic — S. 17
3. Error Analysis — S. 25
4. Newton Methods — S. 35
5. Global Optimization — S. 47
6. Numerical Integration — S. 57
7. Index — S. 71

### [S. 6] Leer.

### [S. 7] Introduction (Einführung)
- Numerische Methoden (Numerical Methods) sind essenziell zur Lösung mathematischer Probleme, die nicht analytisch behandelt werden können. Der Kurs behandelt: fundamentale Konzepte, Fehleranalyse (error analysis), Konditionierung von Problemen (problem conditioning), Stabilität (stability) und verschiedene numerische Techniken — Ziel: zuverlässige und effiziente Algorithmen im wissenschaftlichen Rechnen (scientific computing) und in Ingenieursanwendungen implementieren können.
- Versprechen des Kurses: alles Nötige, um mit numerischen Methoden kompetent umzugehen und sie in Machine Learning, Data Science und Engineering-Kontexten einzusetzen.

### [S. 8] Leer.

---

## Kapitel 1: Enter Numerical Methods (S. 9–16)

### [S. 9] Kapitelbeginn — "Tapping into Computational Power / The Why"
- Versionszeile: *2026-04-05 · regal coconut Wachtel*.
- **Definition (sinngemäß vollständig):** Numerische Methoden sind essenziell zur Lösung mathematischer Probleme, die nicht analytisch adressiert werden können. "Numerical methods are a subfield of mathematics in which we calculate our solutions not analytically exactly, but approximately." (Teilgebiet der Mathematik, in dem Lösungen nicht analytisch exakt, sondern approximativ berechnet werden.)
- Begründung ("And we have good reason to do so"):
  - Viele Probleme sind analytisch nicht lösbar oder zu komplex, um praktikabel zu sein.
  - Wir können Rechenleistung (computational power) anzapfen, um approximative Lösungen effizient zu erhalten.
- **Bezug ML/AI:** In Machine Learning und künstlicher Intelligenz sind numerische Methoden zentral für das Training von Modellen, die Optimierung von Parametern und die Simulation komplexer Systeme, wo analytische Lösungen unmöglich (infeasible) sind. Sie ermöglichen effizienten Umgang mit großen Datensätzen und komplexen Algorithmen; besonders im Deep Learning (Millionen Parameter, umfangreiche Berechnungen) erleichtern numerische Methoden die Optimierungsprozesse des Modelltrainings — unverzichtbar für den Fortschritt der Modelle.
- Randnotizen (Margin notes):
  - **Further Reading** (Literatur): ¹ T. Arens, F. Hettlich, C. Karpfinger, U. Kockelkorn, K. Lichtenegger, H. Stachel: *Mathematik*, Springer. ² W. Dahmen, A. Reusken: *Numerik für Ingenieure und Naturwissenschaftler*, Springer. ³ M. P. Deisenroth, A. A. Faisal, C. S. Ong: *Mathematics for Machine Learning*, Cambridge University Press. ⁴ P. Deuflhard, A. Hohmann: *Numerische Mathematik 1 - Eine algorithmisch orientierte Einführung*, De Gruyter.
  - **Approximation**: vom Lateinischen *approximare*, "to come near to" (sich annähern).
  - **Moore's Law**: besagt, dass sich die Rechenleistung ca. alle zwei Jahre verdoppelt. Heutige Consumer-GPUs haben Tausende Kerne und schaffen Billionen Gleitkommaoperationen pro Sekunde. Quelle: G. E. Moore: "Cramming more components onto integrated circuits", *Electronics*, 38(8):114–117, 1965.
  - **GPT-2: 1.5B release** — Link: https://openai.com/index/gpt-2-1-5b-release/

### [S. 10] Hands On Experience — Grenzen analytischer Skalierung
- Ankündigung: Später im Kurs theoretische Grundlagen; zunächst Gefühl dafür, warum AI/ML so stark auf numerischen Methoden beruht.
- **Die Grenzen der Skalierung analytischer Lösungen** (The limits of scaling analytical solutions) werden bei großskaligen Problemen offensichtlich. Beispiel: Lösen eines linearen 2×2-Gleichungssystems analytisch per Substitution:
  $$\begin{bmatrix} 2 & 1 \\ 5 & 1 \end{bmatrix} \begin{bmatrix} w_1 \\ w_2 \end{bmatrix} = \begin{bmatrix} 11 \\ 13 \end{bmatrix} \quad (1)$$
- Vollständige Rechnung im Dokument:
  - Aus erster Gleichung: $2w_1 + w_2 = 11 \Rightarrow w_2 = 11 - 2w_1$.
  - Einsetzen in zweite: $5w_1 + 1(11 - 2w_1) = 13 \Rightarrow 3w_1 + 11 = 13 \Rightarrow 3w_1 = 2 \Rightarrow w_1 = \frac{2}{3}$.
  - Dann: $w_2 = 11 - 2\cdot\frac{2}{3} = \frac{33-4}{3} = \frac{29}{3}$.
  - Verifikation 1. Gleichung: $2(\frac{2}{3}) + \frac{29}{3} = \frac{4}{3} + \frac{29}{3} = \frac{33}{3} = 11$. ✓
  - Verifikation 2. Gleichung: $5(\frac{2}{3}) + 1(\frac{29}{3}) = \frac{10}{3} + \frac{29}{3} = \frac{39}{3} = 13$. ✓
- Randnotizen:
  - **Analytics** umfasst Methoden wie Substitution, Elimination, Matrixinversion etc. aus der linearen Algebra.
  - **Computational complexity** (Rechenkomplexität) wächst mit der Systemgröße. Übungsaufgabe in der Marginalie: Löse das größere 3×3-System
    $$\begin{bmatrix} 2 & 1 & 3 \\ 1 & 4 & 2 \\ 3 & 2 & 5 \end{bmatrix} \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix} = \begin{bmatrix} 14 \\ 20 \\ 32 \end{bmatrix} \quad (2)$$

### [S. 11] Grenzen analytischer Lösungen; Lernziele Kapitel 1
- **However:** Für 2 Gleichungen lösbar, aber mit wachsender Systemgröße (z. B. Tausende Gleichungen mit Tausenden Unbekannten) werden analytische Lösungen wegen Rechenkomplexität und Zeitbeschränkungen unpraktikabel.
- **Grenzen analytischer Lösungen** sind auch generelles Problem bei nichtlinearen Gleichungen, Beispiel Sigmoid:
  $$\sigma(x) = \frac{1}{1 + e^{-x}} \quad (3)$$
- **Kernaussage/Definition:** Transzendente Funktionen (transcendental functions) können nicht als endliche Kombinationen algebraischer Operationen (Addition, Subtraktion, Multiplikation, Division, Wurzeln) ausgedrückt werden und besitzen daher keine geschlossenen Lösungen (closed-form solutions). Der Exponentialterm macht es unmöglich, $x$ mit elementaren Funktionen (Polynome, rationale, trigonometrische Funktionen) zu isolieren.
- Randnotiz **Sigma**: $\sigma(x)$ ist die Sigmoid-Aktivierungsfunktion, häufig in neuronalen Netzen, und eine transzendente Funktion. Eine geschlossene Lösung für $\sigma(x) = 0$ existiert nicht: $\sigma(x)$ nähert sich 0 asymptotisch für $x \to -\infty$, erreicht 0 aber für keinen endlichen Wert von $x$.
- **Lernziele (Learning Objectives) Kapitel 1:**
  1. Erklären, wann numerische Methoden eingesetzt werden und welche Probleme beim analytischen Lösen auftreten.
  2. Diskretisierung (Discretization): kontinuierliche mathematische Probleme in diskrete, computerlösbare Approximationen transformieren.
  3. Grundlegende numerische Techniken auf einfache Probleme von Hand anwenden und größere Probleme am Computer "crunchen".

### [S. 12] Discretization and Approximation (Diskretisierung und Approximation)
- **Abbildung (Figure 1):** Kontinuierliche Kurve $f(x) = \sin(x)$ und ihre diskretisierte Version (schwarze Punkte) auf $[-3, 1]$ mit Schrittweite $h = 1$. (Plot: Sinuskurve von $x=-3$ bis $1$, Punkte bei den ganzzahligen Stellen.)
- **Definition Diskretisierung (Discretization):** Zerlegen kontinuierlicher Domänen (Zeit, Raum oder andere Funktionen) in endliche Schritte oder Gitter (grids) und Auswertung dieser Funktionen an diskreten Punkten mit endlicher Präzision:
  - Kontinuierliche Funktion: $f(x), \quad x \in [a, b]$
  - Diskretisierte Funktion: $f(x_i), \quad x_i = a + ih, \quad i = 0, 1, \ldots, N$
  - mit Schrittweite (step size)
    $$h = \frac{b - a}{N} \quad (4)$$
    wobei $N$ die Anzahl der Schritte auf dem Intervall ist.
- Randnotiz **Remember**: Die Klammern "[" und "]" heißen geschlossenes Intervall (closed interval) und bedeuten, dass die Werte $a$ und $b$ in der Definitionsmenge enthalten sind.
- **Analytisches Beispiel:** Minimum von $\sin(x)$ auf $[-3, 1]$: gesucht $\min_{x \in [-3,1]} \sin(x)$. Das Minimum tritt auf, wo die Ableitung verschwindet und die zweite Ableitung positiv ist.
  - $f(x) = \sin(x)$, $f'(x) = \cos(x) = 0 \implies x^* = \frac{\pi}{2} + k\pi, \; k \in \mathbb{Z}$
- **Abbildung (Figure 2):** Kurve $f(x)=\sin(x)$ (schwarz), Ableitung $f'(x)=\cos(x)$ (grau, gestrichelt), analytisches Minimum (schwarzer Punkt) auf $[-3,1]$; gestrichelte graue Linie bei $x = -\frac{\pi}{2}$ markiert kritischen Punkt mit $\cos(x)=0$ und das Minimum von $\sin(x)$.
- Randnotiz **Trigonometric Rules**: Diese allgemeine Lösung für $\cos(x) = 0$; falls vergessen, am Einheitskreis herleitbar.

### [S. 13] Fortsetzung: analytisch vs. numerisch (Grid Search)
- Kritische Punkte in $[-3, 1]$:
  - $x_1 = -\frac{\pi}{2} \approx -1.5708$
  - $x_2 = \frac{\pi}{2} \approx 1.5708$ ($> 1$, nicht im Intervall)
- **Konzept (Extrema auf geschlossenem Intervall):** Minimum/Maximum einer Funktion auf $[a,b]$ kann an einem kritischen Punkt (Ableitung null oder nicht definiert) im Inneren ODER an den Endpunkten $a$, $b$ auftreten — auch wenn dort die Ableitung nicht null ist. Deshalb müssen bei Extremasuche auf geschlossenem Intervall sowohl kritische Punkte als auch Endpunkte geprüft werden.
- Prüfung Endpunkte und $x_1$: $\sin(-3) \approx -0.1411$; $\sin(-\frac{\pi}{2}) = -1$; $\sin(1) \approx 0.8415$. ⇒ Minimum ist $-1$ bei $x = -\frac{\pi}{2} \approx -1.5708$.
- **On To the Numerical Solution:** Brute-Force-Gittersuche (grid search): Funktion an diskreten Punkten über dem Intervall auswerten, Punkt mit minimalem Wert wählen. Diskretisierung von $[-3,1]$ mit $h = 1$:
  - $x_0 = -3: \sin(-3) \approx -0.1411$
  - $x_1 = -2: \sin(-2) \approx -0.9093$
  - $x_2 = -1: \sin(-1) \approx -0.8415$
  - $x_3 = 0: \sin(0) = 0$
  - $x_4 = 1: \sin(1) \approx 0.8415$
  - ⇒ Minimum unter diesen: $\sin(-2) \approx -0.9093$ bei $x = -2$.
- **Abbildung (Figure 3):** wie Figure 1 — $\sin(x)$ und Diskretisierung (schwarze Punkte) auf $[-3,1]$, $h=1$.
- Randnotizen:
  - **Brute Force**: alle möglichen Optionen ausprobieren und die beste wählen — hier per Grid Search.
  - **The minimum**: Wahl der Schrittweite $h$ beeinflusst die Genauigkeit der Approximation; kleinere Schrittweite ⇒ nähere Approximation ans wahre Minimum. Auch die Intervallwahl spielt eine Rolle (matters, "in a sense that it ." [UNSICHER: Satz bricht im Original offenbar ab]).
  - **Definition Approximation Error (Approximationsfehler):** Differenz zwischen analytischer und numerischer Lösung. Hier: $|-1 - (-0.9093)| = 0.0907$.

### [S. 14] Examples & Excercises [sic]
- Rückgriff auf System (1), nun als
  $$\begin{bmatrix} 2 & 1 \\ 5 & 1 \end{bmatrix} \begin{bmatrix} w \\ b \end{bmatrix} = \begin{bmatrix} 11 \\ 13 \end{bmatrix} \quad (5)$$
- Lösbar auch über Brute-Force-Diskretisierung und Approximation: Variablen $w$ und $b$ über ein Gitter möglicher Werte diskretisieren, lösen und die fehlerminimierende Lösung wählen.
- Grid Search für $w, b$ mit Schrittweite 2.5 über $w, b \in \{0, 2.5, 5, 7.5, 10\}$; für jede Kombination Fehler berechnen.
- **Fehlerdefinition (Error):** Summe der absoluten Differenzen zwischen linker und rechter Seite der Gleichungen:
  $$\text{error}_1 = |2w + b - 11|, \quad \text{error}_2 = |5w + b - 13| \quad (6)$$
  Alle Kombinationen auswerten, Paar $(w,b)$ mit kleinstem akkumuliertem Fehler wählen.
- **Wert des Handrechnens:** hilft, die Mechanik numerischer Methoden zu verstehen; gibt Intuition über die Rechenkosten von Brute-Force-Methoden (hier nur 100 Operationen); später effizientere Ansätze; Botschaft: so etwas will man an den Computer übergeben und automatisieren — der mit dieser Problemgröße nicht einmal ansatzweise Probleme hat.
- **Enter the machine:** Viele numerische Methoden sind für Computer-Implementierung konzipiert. Im Kurs Wechsel zwischen Handrechnungen (kleine Beispiele) und Computer-Implementierungen (größere Probleme).
- Jupyter Notebook vorgehosted mit Python-Template für diese Übung; Selbstreflexionsfragen als Leitfaden beim Explorieren/Experimentieren.
- Randnotizen:
  - **Excercises** [sic]: dienen Übung und Festigung; selbst versuchen, ausprobieren, diskutieren — kein Zeitrennen; kein Makel, nicht bei der richtigen Antwort zu landen; gute Fragen aufdecken und hin- und herwerfen ist langfristig fruchtbar.
  - **Linear regression**: $xw + b$ bildet ein lineares Modell — auch denkbar als grundlegendste Form eines neuronalen Netzes mit einer Einheit (single unit neural network) $\theta$.
  - **Code-Hosting:** Notebooks unter https://enlitenment.schutera.com/landing.

### [S. 15] Grid-Search-Tabelle; Self-Reflection and Recap
- **Tabelle 1:** Grid Search für $w, b \in \{0, 2.5, 5, 7.5, 10\}$: Spalten $w$, $b$, $2w+b$ (error₁), $5w+b$ (error₂), Gesamtfehler (Error = Summe absoluter Fehler zu 11 bzw. 13). Alle 25 Zeilen:
  | w | b | 2w+b (error₁) | 5w+b (error₂) | Error |
  |---|---|---|---|---|
  | 0 | 0 | 0 (11) | 0 (13) | 24 |
  | 0 | 2.5 | 2.5 (8.5) | 2.5 (10.5) | 19 |
  | 0 | 5 | 5 (6) | 5 (8) | 14 |
  | 0 | 7.5 | 7.5 (3.5) | 7.5 (5.5) | 9 |
  | 0 | 10 | 10 (1) | 10 (3) | 4* |
  | 2.5 | 0 | 5 (6) | 12.5 (0.5) | 6.5 |
  | 2.5 | 2.5 | 7.5 (3.5) | 15 (2) | 5.5 |
  | 2.5 | 5 | 10 (1) | 17.5 (4.5) | 5.5 |
  | 2.5 | 7.5 | 12.5 (1.5) | 20 (7) | 8.5 |
  | 2.5 | 10 | 15 (4) | 22.5 (9.5) | 13.5 |
  | 5 | 0 | 10 (1) | 25 (12) | 13 |
  | 5 | 2.5 | 12.5 (1.5) | 27.5 (14.5) | 16 |
  | 5 | 5 | 15 (4) | 30 (17) | 21 |
  | 5 | 7.5 | 17.5 (6.5) | 32.5 (19.5) | 26 |
  | 5 | 10 | 20 (9) | 35 (22) | 31 |
  | 7.5 | 0 | 15 (4) | 37.5 (24.5) | 28.5 |
  | 7.5 | 2.5 | 17.5 (6.5) | 40 (27) | 33.5 |
  | 7.5 | 5 | 20 (9) | 42.5 (29.5) | 38.5 |
  | 7.5 | 7.5 | 22.5 (11.5) | 45 (32) | 43.5 |
  | 7.5 | 10 | 25 (14) | 47.5 (34.5) | 48.5 |
  | 10 | 0 | 20 (9) | 50 (37) | 46 |
  | 10 | 2.5 | 22.5 (11.5) | 52.5 (39.5) | 51 |
  | 10 | 5 | 25 (14) | 55 (42) | 56 |
  | 10 | 7.5 | 27.5 (16.5) | 57.5 (44.5) | 61 |
  | 10 | 10 | 30 (19) | 60 (47) | 66 |
  - Bildunterschrift: Minimaler Fehler bei $w = 0, b = 10$ mit Fehler 4 (mit * markiert).
- **Self-Reflection** — Leitfragen während und nach den Übungen:
  - Warum ist die Wahl der Schrittweite $h$ beim Diskretisieren wichtig, und wie beeinflusst sie Genauigkeit und Rechenzeit der numerischen Lösung?
  - Wie beeinflusst die Wahl des Intervalls $[a,b]$ die Diskretisierungsergebnisse und die Lage numerisch gefundener Extrema?
  - Hauptunterschiede zwischen kontinuierlicher Funktion und ihrer diskretisierten Version; Implikationen für das numerische Lösen mathematischer Probleme?

### [S. 16] Recap of Key Concepts (Kapitel 1)
- Numerische Methoden sind essenziell für komplexe mathematische Probleme ohne analytische Lösung.
- Diskretisierung transformiert kontinuierliche Probleme in diskrete, für rechnerische Methoden geeignete Approximationen.
- Numerische Berechnungen von Hand für kleine Probleme (Verständnis der Mechanik); Computer sind für größere Probleme unverzichtbar.
- **Errors everywhere:** Mathematische Modelle sind Vereinfachungen der Realität, und numerische Methoden führen zusätzliche Fehler durch Approximation ein:
  $$f(x) \approx f(x_i), \quad x_i = a + ih \quad (7)$$
- Numerische Berechnung führt einige Fehlertypen ein, die verstanden werden müssen, um die Methodik voll nutzen zu können. (Überleitung zu Kapitel 2/3.)
- Randnotiz **Teaser**: "Can you think of a simple way to improve the accuracy to compute ratio of our grid search example from above?" (Einfacher Weg, das Verhältnis Genauigkeit/Rechenaufwand der Grid Search zu verbessern?)

---

## Kapitel 2: Floating-Point Arithmetic (S. 17–24)

### [S. 17] Kapitelbeginn — "Getting used to Errors Everywhere / The Why"
- Versionszeile: *2026-04-29 · lively date Hase*.
- Rückbezug: Numerische Methoden führen Fehler durch Approximation ein. Sei $f(x)$ eine kontinuierliche Funktion auf $[a,b]$; die diskretisierte Version $f(x_i)$ approximiert $f(x)$ an diskreten Punkten $x_i$ mit einem Fehler, der von Schrittweite $h$ und der Glattheit (smoothness) von $f$ abhängt.
- Numerische Werte können im Computerspeicher zudem nur approximativ gespeichert werden — in Gleitkommadarstellung (floating-point representation). Das führt zu Rundungsfehlern (rounding errors) bei arithmetischen Operationen, die sich zu den Abschneidefehlern (truncation errors) addieren, die wir bereits beim Approximieren unendlicher Prozesse durch endliche erlebt haben (auch Approximationsfehler/approximation error genannt).
- Gute Gründe, diese Fehler und ihr Zusammenspiel mit den Maschinen zu verstehen:
  - Numerische Methoden führen Rundungs- und Abschneidefehler (rounding and truncation errors) ein.
  - Je nach Maschine wirken sich diese Fehler unterschiedlich aus und können sich verstärken (amplify) und akkumulieren.
- **Bezug ML/AI:** Numerische Methoden sind fürs Training zentral, Gleitkomma-Arithmetik aber genauso relevant in der Modell-Inferenz (model inference) — besonders in rechenarmen Umgebungen "on the edge" oder beim Einsatz quantisierter Modelle⁵; dann ist Verständnis der Gleitkomma-Arithmetik und der zugrunde liegenden Mechanik nützlich.
- Randnotizen:
  - **Definition Modeling Error (Modellierungsfehler):** tritt auf, da alle Modelle Vereinfachungen der Realität sind; die Differenz zwischen Modell und realem System führt einen Fehler ein. Wird in diesem Kurs nicht vertieft — aber den feinen Unterschied beachten zwischen dem, was wir $f(x)$ nennen, und dem, was tatsächlich ein $f(x)$ ist.
  - **On the Edge**: Modelle nutzen niedrigpräzise Arithmetik, z. B. 8-Bit-Integer oder sogar binäre Gewichte und Aktivierungen.
  - **Binary neural networks (BNNs)**: Gewichte und Aktivierungen auf $\{-1, +1\}$ beschränkt — drastische Reduktion von Speicher- und Rechenbedarf, macht aber Gleitkommadarstellung und Rundungseffekte kritisch. ⁵ M. Courbariaux, Y. Bengio: "Binarynet: Training deep neural networks with weights and activations constrained to +1 or -1", CoRR, abs/1602.02830, 2016, http://arxiv.org/abs/1602.02830

### [S. 18] Hands On Experience — Rundungsfehler; Lernziele Kapitel 2
- Beispiel: $10 \div 3$. Dezimalentwicklung schriftlich: $10 \div 3 = 3$ Rest 1; "bring down a 0" wiederholt, jeweils Rest 1 … ⇒ $\frac{10}{3} = 3.333\ldots$ — die 3en wiederholen sich unendlich.
- Beim Aufschreiben/Eingeben in Rechner muss man irgendwo stoppen:
  $$\frac{10}{3} \approx 3.333 \quad \text{(gerundet bzw. abgeschnitten nach 3 Ziffern)} \quad (8)$$
- **Definition Rundungsfehler (rounding error):** Differenz zwischen wahrem Wert und dem Wert, den man nach Abschneiden (truncate) der Entwicklung erhält. Egal wie viele Ziffern man schreibt — sobald man stoppt, entsteht ein Fehler:
  $$\text{Rounding error} = |3.333333\ldots - 3.333| = 0.000333\ldots \quad (9)$$
- Je mehr Ziffern, desto kleiner der Fehler; er verschwindet aber nie vollständig, außer man schriebe unendlich viele Ziffern — unmöglich.
- **This is rounding error:** Computer speichern Zahlen stets mit endlich vielen Ziffern, daher tauchen Rundungsfehler unvermeidlich auf und müssen gemanagt werden. Diese kleinen Fehler können akkumulieren und sich verstärken und zu signifikanten Ungenauigkeiten führen — besonders in iterativen Algorithmen, wie sie in numerischen Methoden und Machine Learning üblich sind.
- **Lernziele (Learning Objectives) Kapitel 2:**
  1. Die verschiedenen Typen numerischer Fehler verstehen: Modellierungs-, Abschneide- und Rundungsfehler (modeling, truncation, rounding errors).
  2. Gleitkommadarstellung (floating-point representation), Maschinengenauigkeit (machine epsilon) und Auslöschung (loss of significance) verstehen.
  3. Numerische Fehler in praktischen Berechnungen handhaben können.
- Randnotizen:
  - **Typen numerischer Darstellungen** in Computern: **Integer** (int): 3; **Floating-point** (float): 3.3333333; **Double precision** (double): 3.3333333333333333 [UNSICHER: genaue Ziffernzahl im Original]; **Fixed-point** (z. B. 4 Ziffern): 3.3333.
  - **Impossible?** Mathematische Notation hilft mit Periode: $3.\overline{3}$.

### [S. 19] Floating Point Representation and Precision (Gleitkommadarstellung und Präzision)
- **Definition Gleitkommazahlen (Floating-point numbers):** Methode für Computer, reelle Zahlen mit endlicher Bitzahl darzustellen. Der IEEE-754⁶-Standard ist das am weitesten verbreitete Format. Eine Gleitkommazahl wird typischerweise gespeichert als:
  $$x = (-1)^s \cdot m \cdot 2^e \quad (10)$$
  wobei $s$ das Vorzeichenbit (sign bit), $m$ die Mantisse (mantissa, auch significand) ist, die die Präzision bestimmt, und $e$ der Exponent, der die Skala (Größenordnung/magnitude) der Zahl bestimmt. Erlaubt weiten Wertebereich, aber nur eine endliche Menge reeller Zahlen ist exakt darstellbar.
- IEEE 754 single precision (float): 32 Bit aufgeteilt in 1 Vorzeichenbit, 8 Exponentenbits, 23 Mantissenbits.
- **Abbildungen:**
  - Figure 4: Bit-Layout IEEE 754 **HALF (16)**: Sign (dunkel, Bit 1), Exponent (mittel, bis Bit 6), Mantisse (hell, bis Bit 16).
  - Figure 5: Bit-Layout IEEE 754 **SINGLE (32)**: Sign (Bit 1), Exponent (bis Bit 9), Mantisse (bis Bit 32).
  - Figure 6: Bit-Layout IEEE 754 **DOUBLE (64)**: Sign (Bit 1), Exponent (bis Bit 12), Mantisse (bis Bit 64).
- **Exponent mit Bias:** Der Exponent wird mit einem Bias gespeichert, um positive und negative Exponenten zu ermöglichen — so können sehr kleine und sehr große Größenordnungen dargestellt werden. Beispiel IEEE 754 single precision: 8 Exponentenbits, Bias 127. Gespeicherter Exponent $E$ und wahrer Exponent $e$: $e = E - 127_{10}$. Grund: Mit 8 Bits speichert das Exponentenfeld Werte von 0 ($2^0 - 1$) bis 255 ($2^8 - 1$); durch Subtraktion des Bias (127) kann der tatsächliche Exponent $e$ positive und negative Werte annehmen, zentriert um null. Das vereinfacht Kodierung und Vergleich von Gleitkommazahlen in Hardware.
- Randnotizen:
  - ⁶ IEEE Computer Society: "IEEE standard for floating-point arithmetic", https://ieeexplore.ieee.org/document/4610935, August 2008. IEEE Std 754-2008 (Revision von IEEE Std 754-1985).
  - **Definition Bit:** kurz für *binary digit*, die grundlegendste Informationseinheit in Computertechnik und digitaler Kommunikation; kann Wert 0 oder 1 haben.

### [S. 20] Skala, Mantisse, Machine Epsilon
- **Constructing scale** in Gleitkommadarstellung (Beispiele):
  - $10^1 = 10_{10} = 1010_2 = 1.010 \times 2^3, \quad E = 10000010_2$
  - $10^2 = 100_{10} = 1100100_2 = 1.100100 \times 2^6, \quad E = 10000101_2$
  - $10^3 = 1000_{10} = 1111101000_2 = 1.111101000 \times 2^9, \quad E = 10001000_2$
- **Die Mantisse** bestimmt, wie fein Zahlen zwischen Zweierpotenzen dargestellt werden können.
- **2-Bit-Mantissen-Beispiel (unnormalisiert):** Mantissen-Bitkombinationen 00, 01, 10, 11; unnormalisierter Significand $0.xx_2$:
  - $00: 0.00_2 = 0 + 0\times2^{-1} + 0\times2^{-2} = 0.0$
  - $01: 0.01_2 = 0 + 0\times2^{-1} + 1\times2^{-2} = 0.25$
  - $10: 0.10_2 = 0 + 1\times2^{-1} + 0\times2^{-2} = 0.5$
  - $11: 0.11_2 = 0 + 1\times2^{-1} + 1\times2^{-2} = 0.75$
- **Konzept:** Eine 2-Bit-Mantisse erlaubt vier verschiedene Werte zwischen zwei beliebigen Zweierpotenzen; 3-Bit-Mantisse acht Werte usw. Allgemein: Mantisse mit $t$ Bits ⇒ $2^t$ verschiedene Werte zwischen zwei Zweierpotenzen, skaliert durch den Exponenten.
- **Definition Machine epsilon ($\varepsilon_{\text{mach}}$):** die kleinste positive Zahl, sodass $1 + \varepsilon_{\text{mach}} \neq 1$ in der Computerarithmetik. Quantifiziert die obere Schranke des relativen Fehlers durch Rundung in Gleitkomma-Arithmetik:
  $$\varepsilon_{\text{mach}} = 2^{-t} \quad (11)$$
  wobei $t$ die Anzahl der Mantissenbits ist. Im 2-Bit-Beispiel: $\varepsilon_{\text{mach}} = 2^{-2} = 0.25$.
- **Konzept relative vs. absolute Präzision:** Die relative Präzision von Gleitkommazahlen ist ca. $2^{-t}$, während die absolute Präzision von der Größenordnung der dargestellten Zahl abhängt:
  $$\varepsilon_{\text{mach}} \cdot |x| \quad (12)$$
- Randnotizen:
  - **Die größte Zahl in single precision** ist ca. $10^{38}$, gesetzt durch den größten Exponenten $e = +127$; der Dezimalexponent 38 kommt von $\log_{10}(2^{128}) \approx 38.5$.
  - **Remember (SI-Präfixe):** mega ($10^6$), giga ($10^9$), tera ($10^{12}$), peta ($10^{15}$), exa ($10^{18}$), zetta ($10^{21}$), yotta ($10^{24}$), ronna ($10^{27}$), quetta ($10^{30}$); **kein offizielles SI-Präfix** für $10^{33}$.
  - Für IEEE 754 single precision: $\varepsilon_{\text{mach}} \approx 1.19 \times 10^{-7}$; double precision: $\varepsilon_{\text{mach}} \approx 2.22 \times 10^{-16}$.
  - **Absolute precision** wird gerade klar: $1 : 2 = 0.5$, aber $10 : 2 = 5$. Gleiche Anzahl von Schritten (relative Präzision), aber Lücken (gaps) von 0.5 vs. 5.

### [S. 21] Absolute Lücken; Fixed-Point-Darstellung
- **In other words:** Große Zahlen haben größere absolute Lücken zwischen darstellbaren Werten als kleine Zahlen.
- **Abbildung (Figure 7):** Absoluter Fehler für single (schwarz, "SINGLE") und double (grau, gestrichelt, "DOUBLE") Präzision als Funktion des dargestellten Werts $x$ (doppelt-logarithmisch, $x$ von $10^{-16}$ bis $10^{16}$, Fehler von $10^{-23}$ bis $10^{7}$). Der Fehler wächst linear mit $x$ und ist proportional zur Maschinengenauigkeit (machine epsilon) des jeweiligen Formats.
- **Definition Fixed-point representation (Festkommadarstellung):** Eine andere Art, reelle Zahlen in Computern zu speichern, besonders wenn vorhersagbare Präzision und Performance gewünscht sind. Bei Fixed-Point wird vorab entschieden, wie viele Bits für den Ganzzahl- und wie viele für den Bruchteil verwendet werden. Dadurch ist die Lücke zwischen darstellbaren Zahlen (die Präzision) immer gleich, egal wie groß oder klein der Wert ist — das gibt mehr Kontrolle.
- **Beispiel:** Zahlen zwischen $-1000$ und $1000$ mit 32-Bit signed Integer speichern. Normal stellt ein 32-Bit-Integer Werte von $-2147483648$ bis $2147483647$ dar — viel mehr als nötig. Für mehr Präzision: Skalierungsfaktor verwenden, z. B. jede reelle Zahl mit $10^6$ multiplizieren und als Integer speichern. So wird $1.234567$ zu $1234567$ im Speicher.
- Randnotiz **Precision**: Mit Skalierungsfaktor $10^{-6}$ ist die kleinste darstellbare Differenz $0.000001$. Der maximale Rundungsfehler ist ein halber Schritt: $0.5 \times 10^{-6} = 0.0000005$.

### [S. 22] Examples & Excercises — Loss of Significance (Auslöschung)
- **Definition Loss of significance (Auslöschung), auch catastrophic cancellation:** tritt auf, wenn zwei nahezu gleiche Zahlen subtrahiert werden, wodurch sich führende Ziffern aufheben und nur die weniger signifikanten, rundungsfehleranfälligen Ziffern übrig bleiben. Das kann Rundungsfehler stark verstärken.
- **Beispiel 1:** Zwei Zahlen $a, b$ im Computer mit begrenzter Präzision, je auf 8 signifikante Stellen gerundet (Fixed-Point-Darstellung):
  - $a = 12345678.5$, $b = 12345678.0$; gespeichert: $\tilde{a} = 12345679$, $\tilde{b} = 12345678$.
  - Subtraktion: $\tilde{a} - \tilde{b} = 12345679 - 12345678 = 1$; wahre Differenz: $a - b = 0.5$.
  - Der Fehler im Resultat ist 0.5 — gleich dem Rundungsfehler in $\tilde{a}$ bzw. $\tilde{b}$ einzeln auf Machine-Epsilon-Niveau 0.5.
- **Beispiel 2 (minimale Abweichung der Zahlen):**
  - $a = 12345678.4$, $b = 12345678.0$; gespeichert: $\tilde{a} = 12345678$, $\tilde{b} = 12345678$.
  - Subtraktion: $\tilde{a} - \tilde{b} = 0$; wahre Differenz: $a - b = 0.4$.
- Randnotizen:
  - **Definition Pseudo-Accuracy:** allgemein ein ungerechtfertigt hoher Detailgrad, der ein irreführendes, künstliches Genauigkeitsgefühl erzeugt.
  - **Infinity:** In der Mathematik liegt eine Unendlichkeit zwischen 0 und 1 — der Unterschied zwischen etwas und nichts.

### [S. 23] Diskussion; Hands on machine epsilon; Loss-of-significance-Demo
- **Diskussion der Beispiele:** Wahre Differenz der Resultate ist 0.1; die Maschinenresultate sind aber 0 bzw. 1 — ein riesiger relativer Fehler. Zeigt, wie Auslöschung zu großen Fehlern führen kann, besonders wenn die subtrahierten Zahlen sehr nahe beieinander liegen.
- **Hands on machine epsilon (Übung):** Vor dem Gang an die Maschine überlegen, wie man das Machine Epsilon eines beliebigen Systems für ein spezifisches Gleitkommaformat per Programm bestimmen würde. Definition von Machine Epsilon wiederholen, Gedanken als Pseudocode notieren. Was würde ein solches Programm auf einem Fixed-Point- vs. Floating-Point-System zeigen? Dann verschiedene Typen in Code ausprobieren, Beobachtungen notieren und reflektieren. Frage: Wenn man einen Taschenrechner bauen würde, welchen Typ würde man wählen und warum⁷?
- **Loss of significance example (Übung):** Überlegen, wie man Auslöschung auf der eigenen Maschine demonstrieren würde; Pseudocode notieren, bevor man weiterliest.
- **Abbildung (Figure 8):** Demonstration katastrophaler Auslöschung: $1/(1 + \epsilon - 1)$ vs. $\epsilon$ (log-x, linear-y; $\epsilon$ von $10^{-17}$ bis $10^{-14}$, y bis $2\times10^{16}$, Pfeil "$\uparrow \infty$"). Für große $\epsilon$ folgt das Resultat $1/\epsilon$; für sehr kleine $\epsilon$ dominiert der Rundungsfehler und das Resultat wird unendlich.
- **Reason about:** wie das Berechnen von $f(\epsilon) = 1/(a + \epsilon - b)$ für kleines $\epsilon$ und $a = b$ den Zweck erfüllen würde. Was erwartet man für sehr kleine $\epsilon$?
- Randnotizen:
  - **Code**: https://github.com/Quillstacks/lecturecode_numericalmethods.git
  - **Definition Overflow:** tritt auf, wenn Zahlen großer Magnitude als $+\infty$ oder $-\infty$ approximiert werden.
  - **Definition Underflow:** tritt auf, wenn Zahlen nahe null auf null gerundet werden.
  - **Is double enough?** ⁷ D. Blochinger: *Numerische Methoden – Foliensatz*, Zentrum für Angewandte Ökonomik (ZAÖ), DHBW Ravensburg, 2025. URL https://www.economicon.de/repository/index.html. Illustration: Prof. Dr. Daniel Blochinger. Lizenz: CC BY-NC-SA 4.0. Stand: 28. Mai 2025. Weitere Materialien: https://www.economicon.de/repository/index.html
  - **What happens for $a > b$?** Entlang signifikanter Stellen denken.

### [S. 24] Self-Reflection and Recap (Kapitel 2)
- **Self-Reflection-Fragen:**
  - Wie ist die Gleitkommadarstellung strukturiert und was sind ihre Komponenten?
  - Was ist Machine Epsilon und wie hängt es mit numerischer Präzision zusammen?
  - Wie wirken sich diese Konzepte in der Praxis auf numerische Berechnungen aus?
- **Recap of Key Concepts:**
  - Gleitkommadarstellung erlaubt Computern, einen weiten Bereich reeller Zahlen mit endlich vielen Bits zu speichern, führt aber Rundungsfehler ein.
  - Machine Epsilon quantifiziert die kleinste darstellbare Differenz in Gleitkomma-Arithmetik und beeinflusst die Präzision numerischer Berechnungen.
  - Auslöschung (loss of significance) tritt beim Subtrahieren nahezu gleicher Zahlen auf, verstärkt Rundungsfehler und führt zu ungenauen Resultaten.
- **Knowing what can go wrong (Überleitung zu Kapitel 3):** Wir sind nah dran zu verstehen, wie wir definieren, was gut ist, und die Qualität unserer Methoden. Wir wissen jetzt: Es gibt eine wahre Funktion $f$ und eine approximierte Funktion $\hat{f}$, ferner eine wahre Eingabe $x$ und eine gerundete Eingabe $\tilde{x}$. Diese beeinflussen und charakterisieren unsere numerischen Methoden.
- Randnotiz **Teaser**: "Can you think of metrics for numerical methods, based on the approximations and errors we discussed?" (Metriken für numerische Methoden auf Basis der diskutierten Approximationen/Fehler?)

---

## Kapitel 3: Error Analysis (S. 25–34)

### [S. 25] Kapitelbeginn — "Some call it Error. I call it Character. / The Why"
- Versionszeile: *2026-04-29 · lively date Hase*.
- **Kernsatz:** Konditionierung, Stabilität, Konsistenz und Konvergenz (Conditioning, Stability, Consistency and Convergence) sind fundamentale Konzepte der numerischen Analysis, die helfen, das Verhalten numerischer Algorithmen und ihre Zuverlässigkeit beim Lösen mathematischer Probleme zu verstehen.
- **Understanding Concepts** — um Verhalten und Charakteristika numerischer Methoden zu beschreiben, wollen wir:
  - Die Sensitivität gegenüber kleinen Änderungen in den Eingabedaten einschätzen (assess).
  - Die Sensitivität der numerischen Lösung gegenüber kleinen Änderungen in den Eingabedaten bewerten (evaluate).
  - Sicherstellen, dass numerische Methoden genaue und reproduzierbare Resultate liefern.
  - Garantieren, dass unsere Approximationen zur wahren Lösung konvergieren.
- **Bezug ML/AI:** Besonders beim Training großer Modelle auf riesigen Datensätzen ist Verständnis dieser Konzepte entscheidend. Training neuronaler Netze und anderer Modelle bedeutet großskalige Optimierungsprobleme, oft mit iterativen numerischen Methoden. Im Deep Learning steht Konvergenz im Zentrum (convergence has the center stage); fast als Nachgedanke folgt die Komplexität (Complexity) — Anzahl Operationen und benötigte Zeit. Allgemein lassen sich AI-Modelle $\theta$ später genau mit diesen Konzepten bewerten und beschreiben.
- Randnotizen:
  - **One last word on model error:** Mit $f(\cdot)$ implizieren wir das exakte Modell eines Systems. In der Praxis sind Modelle Vereinfachungen der Realität — für eine Distanz zwischen Punkten A und B verwendet man vielleicht ein vereinfachtes Manhattan- oder euklidisches Modell, das Terrain, Reisemodus oder Hindernisse nicht berücksichtigt. Also: unser $f(\cdot)$ hier ist ein anderes $f(\cdot)$.
  - **Deep Learning by Goodfellow** leistet großartige Starthilfe in numerische Berechnung (Kap. 4) für Machine Learning. I. Goodfellow, Y. Bengio, A. Courville: *Deep Learning*, MIT Press, 2016, http://www.deeplearningbook.org

### [S. 26] Hands On Experience — Conditioning & Stability intuitiv
- Einstieg: intuitives Gefühl für die Konzepte mit einfachen Beispielen; je Konzept zwei schnelle Übungen (von Hand oder im Kopf), um zwei Seiten derselben Medaille zu zeigen — mit Extremen auf dem Spektrum. Rückgriff auf das diskretisierte Sinus-Beispiel aus Kapitel 1.
- **Conditioning (Konditionierung):** beschreibt, wie sensitiv die Lösung auf kleine Änderungen in den Eingabedaten reagiert.
- **Abbildung (Figure 9):** Kurve $\hat{f}(x) = \sin(x)$ auf $[-3,1]$ mit zwei hervorgehobenen transparenten vertikalen Bändern bei $x = -1.5$ und $x = 0$ (Breite 0.5).
- Annahme: approximierte Funktion = wahre Funktion (Sinus), aber $\tilde{x}$ ist eine leicht gestörte Version von $x$ durch Messfehler oder Rundung ($\pm 0.25$). Betrachtung der zwei grauen Bänder: Bei $x = -1.5$ (nahe Minimum) ist die Region **gut konditioniert** (well-conditioned) — kleine Änderungen in $x$ führen zu kleinen Änderungen in $f(x)$. Das Band um $x = 0$ ist **schlecht konditioniert** (ill-conditioned) — kleine Änderungen in $x$ können zu großen relativen Änderungen in $f(x)$ führen.
- **Stability (Stabilität):** bezieht sich auf die Sensitivität der numerischen Lösung gegenüber kleinen Änderungen in den Eingabedaten.
- **Abbildung (Figure 10):** Kurve $f(x)_{.2} = \sin(x)$ auf $[-3,1]$ mit hervorgehobenem Band bei $x=0$ (Breite 0.5) und diskretisierten Punkten mit Schrittweite $h = 0.2$.
- Beobachtung am grauen Band um $x = 0$: Bei Schrittweite $h = 0.2$ folgen die diskretisierten Punkte der Sinuskurve eng — das zeigt eine Instabilität gegenüber Änderungen $\tilde{x} \pm 0.25$, mit Fluktuationen in den berechneten Werten $\hat{f}(\tilde{x})$. Im Kontrast zeigt die Diskretisierung mit $h = 1$ (Fortsetzung S. 27) …
- Randnotiz: **This is about floating-point representation** und nicht über Schrittweite oder optimale Approximation — das verinnerlichen, bevor man weitergeht. [Anm.: bezieht sich auf das Conditioning-Beispiel mit gestörtem $\tilde{x}$.]

### [S. 27] Stability (Forts.), Consistency, Convergence (Beginn)
- **Abbildung (Figure 11):** Kurve $f(x)_{1.} = \sin(x)$ auf $[-3,1]$ mit Band bei $x = 0$ (Breite 0.5) und diskretisierten Punkten mit Schrittweite $h = 1$.
- Fortsetzung Stability: … nur ein einziger diskretisierter Punkt liegt im grauen Band — führt zu einer **stabilen** Approximation der Sinuskurve in dieser Region, unabhängig von den Abweichungen in $\tilde{x}$.
- **Consistency (Konsistenz):** quantifiziert, wie gut unsere numerische Methode mit der exakten Lösung des Originalproblems übereinstimmt. Zur Veranschaulichung: Diskretisierung mit Schrittweite $h = 1$ und mit $h = 0.2$.
- **Abbildungen:** Figure 12: Balkendiagramm (bar plot) der diskretisierten Werte $f(x)_{1.} = \sin(x)$ auf $[-3,1]$ mit $h = 1$. Figure 13: Balkendiagramm der diskretisierten Werte $f(x)_{.2} = \sin(x)$ auf $[-3,1]$ mit $h = 0.2$.
- Beobachtung: Für infinitesimal kleine Schrittweiten $h \to 0$ kommen die diskretisierten Punkte der wahren Sinuskurve immer näher — am Ende perfekte Übereinstimmung zwischen numerischer Methode und exakter Lösung: **optimale Konsistenz**.
- **Convergence (Konvergenz):** entsteht, wenn wir die Ideen von Stabilität und Konsistenz kombinieren. Eine numerische Methode ist konvergent, wenn beim Verfeinern der Approximation $\hat{f}(x)$ (z. B. durch Verkleinern der Schrittweite $h$) … (Forts. S. 28)
- Randnotiz: **Intuitive convergence example with sine, wanted.** Wer eine bessere Idee hat, die Beispiele im Sinus-Kontext zu verankern, möge sich melden.

### [S. 28] Convergence (Abschluss); Lernziele Kapitel 3
- … die berechnete Lösung sich der exakten Lösung des Problems nähert — unabhängig von den Abweichungen in $\tilde{x}$ oder indem diese implizit berücksichtigt werden.
- **Lernziele (Learning Objectives) Kapitel 3:**
  1. Intuition über die Konzepte Konditionierung, Stabilität, Konsistenz und Konvergenz in numerischen Methoden haben.
  2. Einfache numerische Probleme quantitativ bezüglich dieser Konzepte analysieren.
- Rest der Seite leer.

### [S. 29] Quantitative Characterization of Numerical Methods
- **Notation:** $f(\cdot)$ bezeichnet die exakte (analytische) Lösung eines Problems; $\hat{f}(\cdot)$ die numerische Methode (Algorithmus), die eine Approximation liefert. $x$ steht für die exakten Eingabedaten, $\tilde{x}$ für die tatsächlich verwendeten Eingabedaten, die z. B. durch Messfehler oder Rundung gestört sein können.
- **Definition Conditioning (Konditionierung):** beschreibt, wie sensitiv die Lösung eines Problems auf kleine Änderungen der Eingabedaten reagiert. Formal kann die Konditionierung eines Problems bei $x$ durch die Konditionszahl (condition number) $\kappa$ quantifiziert werden:
  $$\kappa = |f(x) - f(\tilde{x})| \quad (13)$$
  $\kappa$ wird oft normalisiert, um es als relatives Maß auszudrücken.
- **Definition Stability (Stabilität):** gegeben, wenn kleine Fehler in der Eingabe oder in Zwischenschritten nicht zu unverhältnismäßig großen Fehlern in der Ausgabe führen. Mathematisch stellt eine stabile Methode sicher, dass der Fehler in der berechneten Lösung $\hat{f}(\tilde{x})$ durch ein konstantes Vielfaches des Fehlers in den Eingabedaten beschränkt bleibt:
  $$\left|\hat{f}(\tilde{x}) - \hat{f}(x)\right| \leq s \cdot |\tilde{x} - x| \quad (14)$$
  wobei $s$ eine Konstante ist. Für $s \approx 1$ entwickelt sich der Fehler der berechneten Lösung linear mit dem Eingabefehler.
- **Definition Consistency (Konsistenz):** wie gut die numerische Lösung die exakte Lösung des Originalproblems approximiert:
  $$\left|\hat{f}(x) - f(x)\right| \leq c \quad (15)$$
  wobei $c$ eine Konstante ist, die den Konsistenzfehler quantifiziert.
- **Definition Convergence (Konvergenz):** bezieht sich allgemein darauf, dass unsere Approximation einen spezifischen stabilen Grenzwert erreicht. Eine Methode ist konvergent, wenn:
  $$\left|\hat{f}(\tilde{x}) - f(x)\right| \to \lim \quad (16)$$
  Das heißt: sowohl die Annäherung an die echte Lösung als auch Abweichungen in den Daten werden durch eine Fehlerschranke (error margin) kontrolliert.
- Randnotizen:
  - **Hat versus tilde:** Der Hut $\hat{\cdot}$ markiert die numerische Methode (Algorithmus), die Tilde $\tilde{\cdot}$ eine gestörte Eingabe. $\hat{f}(\tilde{x})$ liest sich also: numerische Methode ausgewertet auf gestörten Eingabedaten.
  - **Convergence** strebt üblicherweise eine Fehlerschranke von null an, was oft die exakte Lösung $f(x)$ ist. Oft erleben wir aber Konvergenz gegen einen Wert ungleich null (non-zero convergence). Konvergiert die Methode zu einem von $f(x)$ verschiedenen Wert, zeigt das einen systematischen Fehler (Bias) der Methode an.

### [S. 30] Examples & Excercises — quantitative Analyse am Sinus-Beispiel
- Aufgabe: Minimum der Sinusfunktion auf $[-3,1]$ erneut; Diskretisierung mit zwei Schrittweiten $h = 1$ und $h = 0.2$. Annahme: Eingabe $x$ ist gestört durch $\tilde{x} = x \pm 0.25$ (Messfehler), Präzision: zwei Dezimalstellen. Analysiere Konditionierung, Stabilität, Konsistenz und Konvergenz der numerischen Methode in beiden Fällen; quantifiziere mit den Formeln des vorigen Abschnitts.
- **Conditioning:** unabhängig von der verwendeten numerischen Methode — beschreibt die Sensitivität des Problems selbst. Analyse rein über die Wirkung kleiner Änderungen in $x$ auf $\sin(x)$. Um $x = -1$ (nahe Minimum) ist der Sinus relativ flach ⇒ gute Konditionierung; zum Vergleich $x = 0$, wo der Sinus sich schnell ändert ⇒ schlechte Konditionierung. Rechnungen:
  - $\kappa(-1, +0.25) = |\sin(-1) - \sin(-0.75)| \approx |-0.8415 - (-0.6816)| = 0.1599$
  - $\kappa(-1, -0.25) = |\sin(-1) - \sin(-1.25)| \approx |-0.8415 - (-0.9489)| = 0.1074$
  - ⇒ Gute Konditionierung (well-conditioning) mit $0.1074 \leq \kappa \leq 0.1599$.
  - $\kappa(0, +0.25) = |\sin(0) - \sin(0.25)| \approx |0 - 0.2474| = 0.2474$
  - $\kappa(0, -0.25) = |\sin(0) - \sin(-0.25)| \approx |0 - (-0.2474)| = 0.2474$

### [S. 31] Stability- und Consistency-Quantifizierung
- ⇒ Schlechte Konditionierung (ill-conditioning) mit $\kappa \leq 0.247$ [bei $x=0$].
- **Stability:** hängt von der numerischen Methode ab, die zur Approximation des Sinus und zur Minimumsuche verwendet wird. Für Diskretisierung mit $h = 1$: Methode ist stabil — kleine Änderungen in $\tilde{x}$ führen zu kleinen Änderungen in $\hat{f}(\tilde{x})$. Für $h = 0.2$: weniger stabil — kleine Änderungen in $\tilde{x}$ können größere Fluktuationen in $\hat{f}(\tilde{x})$ verursachen. Quantifizierung über Konstante $s$ in der Stabilitäts-Ungleichung:
  $$\left|\hat{f}(\tilde{x}) - \hat{f}(x)\right| \leq s \cdot |\tilde{x} - x| \quad (17)$$
  Wegen Symmetrie nur Fall $\tilde{x} = x + 0.25$ betrachtet.
  - Für $h = 1$ (bei $x = -1$): $s_{h=1,x=-1} \cdot |\tilde{x} - x| = |\hat{f}(\tilde{x}) - \hat{f}(x)| = |\hat{f}_1(-0.75) - \hat{f}_1(-1)| = |\hat{f}_1(-1) - \hat{f}_1(-1)|$ (siehe A) ⇒ $s_{h=1,x=0} \approx 0 \div 0.25 \approx 0$. [UNSICHER: Im Original wechselt der Index zwischen $x=-1$ und $x=0$; vermutlich Tippfehler im Skript.]
  - Für $h = 0.2$ (bei $x = -1$): $s_{h=0.2,x=-1} \cdot |\tilde{x} - x| = |\hat{f}(\tilde{x}) - \hat{f}(x)| = |\hat{f}_{0.2}(-0.75) - \hat{f}_{0.2}(-1)| = |\hat{f}_{0.2}(-0.8) - \hat{f}_{0.2}(-1)| = |-0.71736 - (-0.84147)|$ ⇒ $s_{h=0.2,x=-1} = 0.12411 \div 0.25 \approx 0.4964$.
- Warnung: Stabilität hat Anomalien in Randregionen der Diskretisierung — besonders ein Problem für stückweise konstante Approximationen (piece-wise constant approximations).
- **Consistency:** bestimmt durch Vergleich der numerischen Lösung $\hat{f}(x)$ mit der exakten Lösung $f(x)$ für das Minimum des Sinus in $[-3,1]$. Quantifizierung der Konstante $c$ in der Konsistenz-Ungleichung:
  $$\left|\hat{f}(x) - f(x)\right| \leq c \quad (18)$$
- Randnotizen:
  - **Stability** equals the conditioning of the system, for $h \to 0$. Show it. (Stabilität entspricht der Konditionierung des Systems für $h \to 0$ — zeigen!)
  - **A)** Schrittweite $h = 1$ führt an beiden Punkten zum gleichen Funktionswert; Referenz Fig. 12.
  - **Remember**: die analytische Lösung von $\min(\sin(x))$ auf $[-3,1]$ — Kapitel 1 wiederholen.

### [S. 32] Consistency-Rechnungen; Convergence-Quantifizierung
- Für $h = 1$:
  $$c_1 \geq |\hat{f}_1(-\tfrac{\pi}{2}) - f(-\tfrac{\pi}{2})| \geq |\hat{f}_1(-1) - f(-\tfrac{\pi}{2})| \geq |-0.84147 - (-1)| \geq 0.15853$$
- Für $h = 0.2$:
  $$c_{0.2} \geq |\hat{f}_{0.2}(-\tfrac{\pi}{2}) - f(-\tfrac{\pi}{2})| \geq |\hat{f}_{0.2}(-1.2) - f(-\tfrac{\pi}{2})| \geq |-0.94898 - (-1)| \geq 0.05102$$
- **Befund:** Konsistenz verbessert sich mit kleineren Schrittweiten — wie erwartet.
- **Convergence:** kombiniert die Ideen von Stabilität und Konsistenz. Quantifizierung über den Gesamtfehler zwischen numerischer Lösung $\hat{f}(\tilde{x})$ und exakter Lösung $f(x)$:
  $$\left|\hat{f}(\tilde{x}) - f(x)\right| \quad (19)$$
  Wegen Symmetrie nur $\tilde{x} = x + 0.25$.
  - Für $h = 1$: $|\hat{f}_1(\tilde{x}) - f(x)| = |\hat{f}_1(-1) - f(-\tfrac{\pi}{2})|$, $|\hat{f}_1(-0.75) - f(-\tfrac{\pi}{2})| = |\hat{f}_1(-1) - f(-\tfrac{\pi}{2})| = |-0.84147 - (-1)| = 0.1599$ [UNSICHER: Im Original stehen die Zwischenzeilen ohne Gleichheitszeichen untereinander; Endwert 0.1599, obwohl $|-0.84147+1| = 0.15853$ — vermutlich Rundung/Inkonsistenz im Skript.]
  - Für $h = 0.2$: $|\hat{f}_{0.2}(\tilde{x}) - f(x)|$: $|\hat{f}_1(-1.2) - f(-\tfrac{\pi}{2})|$, $|\hat{f}_{0.2}(-0.95) - f(-\tfrac{\pi}{2})|$, $|\hat{f}_{0.2}(-1) - f(-\tfrac{\pi}{2})| = |-0.84147 - (-1)| = 0.1599$ [UNSICHER: gleiche Anmerkung wie oben.]

### [S. 33] Konvergenz-Diskussion; Hands on; Self-Reflection and Recap (Kapitel 3)
- **Diskussion:** Wegen der Stabilitätsprobleme im Fall $h = 0.2$ verbessert sich die Konvergenz in diesem Operationspunkt nicht mit kleineren Schrittweiten. Zwei Erkenntnisse: Beide numerischen Lösungen konvergieren zum gleichen Grenzwert; daraus lässt sich auch sagen, dass die Methode des iterativen Verkleinerns der Schrittweite $h$ ebenfalls zum gleichen Grenzwert konvergiert. Beachte: Die Charakteristika werden sowohl für eine numerische Lösung als auch für die numerische Methode verwendet.
- **Hands on compute-driven error analysis:** Brute-Force-Fehleranalyse des Zwei-Gleichungs-Systems aus Kapitel 1: Konditionierung, Stabilität, Konsistenz und Konvergenz der numerischen Lösung bestimmen und durch Optimierung der numerischen Methode verbessern.
- **Self-Reflection-Fragen:**
  - Verglichen mit der numerischen Lösung des Sinus-Minimums: wie gut konditioniert ist das Zwei-Gleichungs-System?
  - Konvergiert die Stabilität mit kleineren Schrittweiten im Zwei-Gleichungs-System? Gegen was?
  - Wie wirken Störungen der Eingabedaten auf die numerische Lösung des Zwei-Gleichungs-Systems? Gibt es ein Zusammenspiel mit der Schrittweite?
  - Vergleiche Konvergenz mit Stabilität und Konsistenz. Was beobachtest du? Lassen sich die Beobachtungen in Begriffen von Bias und Varianz ausdrücken?
  - Beobachtest du für immer kleinere Schrittweiten eine Grenze der Genauigkeit der numerischen Lösung? Wenn ja, warum?
  - Welches weitere Problem beobachtest du beim Verfeinern der Schrittweite?
- **Recap of Key Concepts:**
  - Konditionierung, Stabilität, Konsistenz und Konvergenz sind fundamentale Konzepte der numerischen Analysis zum Verständnis des Verhaltens numerischer Algorithmen.
  - Diese Konzepte können qualitativ und quantitativ ausgedrückt werden, um numerische Lösungen und Methoden zu analysieren.
- Randnotizen:
  - **Code**: https://github.com/Quillstacks/lecturecode_numericalmethods.git
  - **Teaser**: Bisher Brute-Force-Lösungen. Idee, Brute-Force-Methoden zu verfeinern, um bessere Resultate mit weniger Aufwand zu erzielen? Mit dem Code der Vorlesung designen und testen.

### [S. 34] Überleitung zu Kapitel 4
- Jetzt, da wir das Verhalten einzelner numerischer Lösungen verstehen und charakterisieren können, weiter zum Analysieren ganzer numerischer Methoden und Algorithmen. Bisher wurde die Annahme, wo nach einer Lösung zu suchen ist (innerhalb eines spezifischen Intervalls), als gegeben angenommen. Das ist üblicherweise nicht gegeben — in der nächsten Vorlesung bewegen wir uns weg von lokalen Optimierungsmethoden [UNSICHER: gemeint ist die Erweiterung über lokal begrenzte Suchintervalle hinaus; wörtlich: "we will need to move away from local optimization methods in the next lecture"].
- Rest der Seite leer.

---

## Kapitel 4: Newton Methods (S. 35–46)

### [S. 35] Kapitelbeginn — "A Step in the Right direction. / The Why"
- Versionszeile: *2026-04-05 · regal coconut Wachtel*.
- Rückblick: Im vorigen Kapitel wurden numerische Methoden mit Konditionierung, Stabilität, Konsistenz und Konvergenz charakterisiert. Aber die Brute-Force-Gittersuche ist fundamental begrenzt: Sie erkundet den Lösungsraum blind und benötigt $O(N^d)$ Auswertungen für $N$ Gitterpunkte in $d$ Dimensionen.
- **Schlüsselidee (The key insight):** täuschend einfach — statt an jedem Gitterpunkt zu fragen "Was ist hier der Wert?", fragen wir auch "In welche Richtung soll ich als Nächstes gehen?". Die Steigung der Funktion, ihre Ableitung, zeigt die Richtung zur Lösung. Das transformiert die Suche fundamental.
- **Nutzen dieser Methoden:**
  - Lokale Information nutzen, um anspruchsvolle Schritte statt Brute-Force-Suchen zu machen.
  - Schnellere und optimalere Konvergenz erreichen.
- **Bezug ML/Deep Learning:** Newtons Methode, auf erste Ordnung vereinfacht, ist auch als Gradientenabstieg (gradient descent) bekannt. Man könnte argumentieren, das gesamte Feld des Deep Learning baue auf der Idee auf, lokale Gradienteninformation zu nutzen, um in einer hochdimensionalen Loss-Landschaft zu Minima zu navigieren — um Modelle zu trainieren, die auf spezifische Ziele optimiert sind.
- Randnotiz **Backpropagation**: natürlich vital, um Gradienteninformation durch die Schichten eines neuronalen Netzes zu verteilen, aber der Kern-Optimierungsschritt ist weiterhin eine Form gradientenbasierter Navigation.

### [S. 36] Hands On Experience — Grid Search vs. Newton (Nullstellensuche)
- Intuitives Gefühl für die Kraft lokaler Information: Vergleich Grid Search vs. Newtons Methode an derselben Sinusfunktion aus Kapitel 3, nun Nullstellensuche: $\sin(x) = 0$ auf $[2.5, 4]$ (Lösung nahe $\pi \approx 3.14159$).
- **Abbildung (Figure 14):** Kurve $f(x) = \sin(x)$ auf $[2.5, 4]$ und diskretisierte Punkte mit Schrittweite $h = 0.3$.
- **Grid Search** auf $[2.5, 4]$ mit Schritt $h = 0.3$ wertet blind aus:
  - $f(2.5) \approx 0.599$; $f(2.8) \approx 0.335$; $f(3.1) \approx 0.042$ ← am nächsten an null; $f(3.4) \approx -0.256$; $f(3.7) \approx -0.530$; $f(4.0) \approx -0.757$.
  - Ergebnis: $x \approx 3.1$ mit 6 Auswertungen, Fehler $|3.1 - \pi| \approx 0.042$.
- **Newtons Methode** hat einen adaptiven Suchansatz: An jedem Punkt werden Funktion und Ableitung ausgewertet; diese lokale Information wird genutzt, um einen Schritt Richtung Lösung zu machen.
- **Abbildung (Figure 15):** Newton-Iterationen: Start bei $x_0 = 3.5$, schnelle Konvergenz zu $\pi \approx 3.14159$ (Punkte $x_0$ | 1st eval, $x_1$ | 2nd eval, $x_2$ | 3rd eval auf der Kurve).
- **Ableitung als Quelle lokaler Information:** $f'(x) = \cos(x)$ gibt die Steigung der Tangente an einem Punkt. Es gibt mehrere Wege, … (Forts. S. 37)
- Randnotiz: **We pay for this sophistication** mit mehr Hyperparametern, die bestimmt werden müssen, und komplexeren Berechnungen (Ableitungsauswertung und Division), aber wir gewinnen Konvergenzgeschwindigkeit.

### [S. 37] Newton-Iteration am Sinus; Lernziele Kapitel 4
- … diese Information zu nutzen, um Richtung und Größe des nächsten Schritts abzuleiten: Sicher in Richtung fallender Funktion bewegen; dann Schritt fester Größe ODER Schrittgröße proportional zur Ableitung. Hier zunächst: nächste Schätzung dort, wo die Tangente die Null kreuzt — die Lösung der linearen Approximation von $f$ bei $x_n$.
- Rechnung, Start bei $x_0 = 3.5$:
  - $x_1 = x_0 - \frac{\sin(x_0)}{\cos(x_0)} = 3.5 - \frac{-0.351}{-0.936} = 3.5 - 0.375 = 3.125$
  - $x_2 = 3.125 - \frac{\sin(3.125)}{\cos(3.125)} = 3.125 - \frac{0.0008}{-0.9999} \approx 3.14159$
  - $x_3 \approx 3.14159$, und $\sin(3.14159) \approx 0$.
- Nach nur 2 Iterationen (fairerweise: 4 Funktions-/Ableitungsauswertungen) ist $x \approx 3.14159$ mit Fehler $< 10^{-5}$. Die Ableitung sagte uns weit effizienter, wo zu suchen ist, als wir es gewohnt waren.
- **Lernziele (Learning Objectives) Kapitel 4:**
  1. Newton-Raphson-Iteration für Nullstellensuche (root finding) in 1D herleiten und anwenden.
  2. Taylor-Entwicklung (Taylor expansion) und ihre Rolle in Newtons Methode herleiten und verstehen ["understnad" sic].
  3. Konvergenzraten und Fehlermodi (failure modes) von Newtons Methode analysieren.
  4. Sekantenverfahren (Secant method) verstehen und anwenden, wenn Ableitungen nicht verfügbar sind.
- Randnotiz: **"Newton-Rhapson"** [sic] — weil Isaac Newton die generelle Idee hatte, während Joseph Raphson den Ansatz zu einer praktischen iterativen Methode vereinfachte.

### [S. 38] Newton-Raphson and Taylor Expansion — Herleitung & Algorithmus
- **Abbildung (Figure 16):** Geometrische Intuition von Newtons Methode: Für $f(x) = x^2 - 2$ schneidet die Tangente bei $(x_0, f(x_0))$ die $x$-Achse bei $x_1$, der nächsten Approximation. (Plot: Parabel auf ca. $[1.3, 2.2]$, Tangente gestrichelt, Punkte markiert.)
- Formalisierung: gesucht $x^*$ mit $f(x^*) = 0$.
- **Lineare Approximation:**
  $$f(x) \approx f'(x_n) \cdot (x - x_n) \quad \text{für } x \text{ nahe } x_n + f(x_n) \quad (20)$$
  [UNSICHER: Formel im Original etwas eigenartig gesetzt; gemeint ist $f(x) \approx f(x_n) + f'(x_n)(x - x_n)$ für $x$ nahe $x_n$.]
- **Nächste Schätzung finden:** Wir wollen, wo diese lineare Approximation null kreuzt — die beste Schätzung dafür, wo die tatsächliche Funktion null kreuzt. Approximation null setzen:
  - $0 = f(x_n) + f'(x_n) \cdot (x_{n+1} - x_n)$
  - $f'(x_n) \cdot (x_{n+1} - x_n) = -f(x_n)$
  - $x_{n+1} - x_n = -\frac{f(x_n)}{f'(x_n)}$
- **Newton-Raphson-Iterationsformel:**
  $$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \quad (21)$$
- **Algorithmus 1: Newton-Raphson Method** (Pseudocode):
  - Require: Startwert $x_0$, Funktion $f$, Ableitung $f'$, Toleranz $\varepsilon$
  - 1: $x \leftarrow x_0$
  - 2: **while** $|f(x)| > \varepsilon$ **do**
  - 3: Ableitung berechnen: $d \leftarrow f'(x)$
  - 4: **if** $|d| < \varepsilon_{\text{machine}}$ **then**
  - 5: **error** "Derivative too small"
  - 6: **end if**
  - 7: Update: $x \leftarrow x - f(x)/d$
  - 8: **end while** return $x$
- Randnotiz **Note**: Diese lineare Approximation ist die Taylor-Entwicklung erster Ordnung von $f$ um $x_n$. Auf Taylor-Entwicklungen kommen wir zurück, wenn Genauigkeit und Approximation formal untersucht werden.

### [S. 39] Taylor Expansion (Taylor-Entwicklung) — Aufbau Ordnung für Ordnung
- Bisher wurde der linearen Approximation bei $x_n$ einfach vertraut:
  $$f(x) \approx f'(x_n)(x - x_n) + f(x_n) \quad (22)$$
  um schnell die nächste Schätzung $x_{n+1}$ zu finden und schließlich zur Wurzel zu konvergieren — aber ist dieses Vertrauen gerechtfertigt? Die Antwort liegt in der Taylor-Entwicklung, einem fundamentalen Werkzeug, das sagt, wie gut Polynome glatte Funktionen an einem Punkt approximieren.
- Herleitung von Grundprinzipien (first principles), um zu verstehen, warum die lineare Approximation eine gute Wahl für Newtons Methode ist und wie man sie bei Bedarf systematisch verbessert. Illustration: schrittweise Approximation der Sinusfunktion.
- **Abbildung (Figure 17):** Kurve $f(x) = \sin(x)$ und diskretisierte Version (schwarze Punkte) auf $[-3,1]$ mit $h = 1$. [UNSICHER: Bildunterschrift erwähnt Punkte, abgebildet ist primär die Kurve.]
- **0te Ordnung: Funktionswert matchen.** Gesucht Polynom $P(x)$, das $f(x)$ nahe $x_n$ approximiert. Start: am Punkt selbst matchen:
  $$P(x_n) = f(x_n) \quad (23)$$
  Das kommt dem sehr nahe, was Grid Search tut: nur Funktionswerte an diskreten Punkten betrachten, ohne Information über das Verhalten dazwischen.
- **1te Ordnung: erste Ableitung matchen.** Nahe $x_n$ zählt die Steigung; gewünscht $P'(x_n) = f'(x_n)$. Linearen Term hinzufügen:
  $$P(x) = f(x_n) + f'(x_n)(x - x_n) \quad (24)$$
- Randnotizen:
  - **This error** ["Derivative too small", Bezug Algorithmus 1] tritt auf, wenn die Ableitung $f'(x_k)$ gegen null geht, was Division durch null oder numerische Instabilität in Newtons Methode verursachen würde.
  - **Definition Smooth (glatt):** Eine Funktion ist glatt, wenn sie Ableitungen aller Ordnungen besitzt und somit differenzierbar ist.

### [S. 40] Taylor: 2. Ordnung, n-te Ordnung, allgemeine Formel
- **Abbildung (Figure 18):** $f(x) = \sin(x)$ mit konstanter Approximation $P(x) = f(-1)$ (schwarze gestrichelte horizontale Linie), verankert bei $x = -1$ (schwarzer Punkt).
- **Abbildung (Figure 19):** $f(x) = \sin(x)$ mit linearer Approximation $P(x) = f(-1) + f'(-1)(x+1)$ (schwarze gestrichelte Tangente), verankert bei $x = -1$.
- **2te Ordnung: zweite Ableitung matchen.** Die Krümmung (curvature) erfasst, wie sich die Steigung ändert; gewünscht $P''(x_n) = f''(x_n)$. Quadratischen Term hinzufügen:
  $$P(x) = f(x_n) + f'(x_n)(x - x_n) + \frac{f''(x_n)}{2}(x - x_n)^2 \quad (25)$$
- **Abbildung (Figure 20):** $\sin(x)$ mit quadratischer Approximation $P(x) = f(-1) + f'(-1)(x+1) + \frac{f''(-1)}{2}(x+1)^2$ (schwarze gestrichelte Parabel), verankert bei $x = -1$.
- **n-te Ordnung: allgemeines Muster. Definition Taylor-Entwicklung** einer Funktion $f$ um einen Punkt $x_n$:
  $$f(x) = f(x_n) + f'(x_n)(x - x_n) + \frac{f''(x_n)}{2!}(x - x_n)^2 + \frac{f'''(x_n)}{3!}(x - x_n)^3 + \cdots$$
  kompakter:
  $$f(x) = \sum_{k=0}^{\infty} \frac{f^{(k)}(x_n)}{k!}(x - x_n)^k \quad (26)$$
- Randnotizen:
  - **Why divide by 2?** Beim zweimaligen Differenzieren von $(x - x_n)^2$ erhält man 2; will man $P''(x_n) = f''(x_n)$, muss durch 2 geteilt werden, um den Faktor zu kürzen.
  - **Around a point:** Visuell sieht man, dass die Approximationen an einem spezifischen Punkt $x_n$ verankert sind. Die Taylor-Entwicklung ist eine lokale Approximation.

### [S. 41] Warum linear reicht; Herleitung der Konvergenzrate
- **Why linear is enough for Newton?** Wir wollen $f(x^*) = 0$ lösen, nicht $f(x)$ bestmöglich berechnen. Bessere Approximation kostet: höhere Ableitungen berechnen, komplexere Polynome auswerten. In numerischen Berechnungen muss man immer entscheiden, wo die Taylor-Reihe abgeschnitten wird — bei endlicher Ordnung; der lineare Term ist der erste nicht-konstante Term, der Richtungsinformation liefert.
- **Deriving the convergence rate (Konvergenzrate herleiten):** Erinnerung Kapitel 3: Eine Methode ist konvergent, wenn die Approximation einen spezifischen stabilen Grenzwert erreicht. Für Newtons Methode mit Wurzel $x^*$, $f(x^*) = 0$, wollen wir:
  $$|x_n - x^*| \to 0 \quad \text{für } n \to \infty \quad (27)$$
- Dank Taylor-Entwicklung lässt sich quantifizieren, wie schnell der Fehler abnimmt. Sei $e_n = x_n - x^*$ der Fehler bei Iteration $n$. Taylor 2. Ordnung von $f$ um die wahre Wurzel $x^*$:
  $$f(x_n) = f(x^*) + f'(x^*)(x_n - x^*) + \frac{f''(\xi)}{2}(x_n - x^*)^2 \quad (28)$$
  wobei $\xi$ ein Punkt zwischen $x_n$ und $x^*$ ist. Da $f(x^*) = 0$, vereinfacht sich das zu:
  $$f(x_n) = f'(x^*) \cdot e_n + \frac{f''(\xi)}{2}e_n^2 \quad (29)$$
- **Newton-Formel anwenden:**
  - $e_{n+1} = x_{n+1} - x^* = x_n - \frac{f(x_n)}{f'(x_n)} - x^* = (x_n - x^*) - \frac{f(x_n)}{f'(x_n)} = e_n - \frac{f(x_n)}{f'(x_n)}$
  - Vereinfachte Taylor-Entwicklung für $f(x_n)$ einsetzen:
    $$e_{n+1} = e_n - \frac{f'(x^*)\cdot e_n + \frac{f''(\xi)}{2}e_n^2}{f'(x_n)} \quad (30)$$
- **Für Punkte nahe $x^*$:** Annahme $f'(x_n) \approx f'(x^*)$:
  $$e_{n+1} \approx e_n - \frac{f'(x^*)\cdot e_n + \frac{f''(\xi)}{2}e_n^2}{f'(x^*)} = e_n - e_n - \frac{f''(\xi)}{2f'(x^*)}e_n^2 \quad (31)$$
- Randnotiz **Notice the assumption play out**: $10^{-1} \to 10^{-2} \to 10^{-3} \to 10^{-6} \to 10^{-12}$. Sobald wir nah genug sind und die Annahmen gelten (nach Iteration 2), quadriert sich der Fehler perfekt — quadratische Konvergenz demonstriert.

### [S. 42] Quadratische Konvergenz; $\sqrt{2}$-Beispiel; Failure Modes
- … wodurch sich der Fehlerterm erster Ordnung aufhebt und übrig bleibt:
  $$e_{n+1} \approx -\frac{f''(\xi)}{2f'(x^*)}e_n^2 \quad (32)$$
- **Abstrakter:**
  $$|e_{n+1}| \leq C \cdot |e_n|^2 \quad (33)$$
  Der Fehler der nächsten Iteration ist also ungefähr proportional zum Quadrat des aktuellen Fehlers; $C$ ist eine Konstante, die von Krümmung und Steigung der Funktion an der Wurzel abhängt. **Das ist quadratische Konvergenz (quadratic convergence).**
- **Beispiel:** Berechnung von $\sqrt{2}$ mit Newton, Start $x_0 = 2$ — **Tabelle 2** ("Newton's method for computing $\sqrt{2}$. See how the error approximately squares each iteration."):
  | $n$ | $x_n$ | $|e_n|$ (Fehler) |
  |---|---|---|
  | 0 | 2.000000000 | $5.86 \times 10^{-1}$ |
  | 1 | 1.500000000 | $8.58 \times 10^{-2}$ |
  | 2 | 1.416666667 | $2.45 \times 10^{-3}$ |
  | 3 | 1.414215686 | $2.13 \times 10^{-6}$ |
  | 4 | 1.414213562 | $4.5 \times 10^{-12}$ |
  [Anm.: Wird hier als "introductory example" bezeichnet; ein expliziter früherer $\sqrt{2}$-Bezug taucht im Text vorher nicht auf — Querbezug auf Figure 16 mit $f(x)=x^2-2$.]
- **Newton's method can fail** auf mehrere Arten — wird vorerst ertragen, Lösungen folgen später. Als Denksportaufgabe: Failure Modes in diesem Plot visualisieren.
- **Abbildung (Figure 21):** $f(x) = x^3 - x$ hat mehrere Wurzeln (Plot auf ca. $[-0.5, 1.5]$, Wurzeln bei 0 und 1 markiert). Newtons Methode kann scheitern durch: Nullableitung (wenn $f'(x_n) = 0$, kreuzt die Tangente die Achse nicht), Oszillation (besonders bei symmetrischen Funktionen kann Newton zwischen Punkten zykeln), und mehrdeutige Startpunktwahl ($x_0$ beeinflusst stark, welche Wurzel gefunden wird).
- **Was wir nicht ertragen können:** wenn $f'(x)$ nicht berechnet werden kann.
- Randnotiz **This can happen because**:
  - Die Ableitung ist teuer zu berechnen.
  - Die Funktion ist als Black Box gegeben (z. B. eine Simulation).
  - Die Funktion ist nicht überall differenzierbar.

### [S. 43] Secant Method (Sekantenverfahren)
- Eine clevere Art, die Ableitung nur mit Funktionsauswertungen zu approximieren — eliminiert den Bedarf einer expliziten Ableitung.
- **"A poor man's derivative":** Ableitung mit zwei jüngsten Punkten approximieren:
  $$f'(x_n) \approx \frac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}$$
- Visuell: die Steigung der Sekante durch die Punkte $(x_{n-1}, f(x_{n-1}))$ und $(x_n, f(x_n))$ auf dem Graphen von $f$.
- **Abbildung (Figure 22):** Sekantenverfahren: Die Gerade durch $(x_0, f(x_0))$ und $(x_1, f(x_1))$ liefert die nächste Approximation $x_2$. (Plot ähnlich Fig. 16 mit Sekante gestrichelt.)
- **Hinweis:** Es werden zwei Startwerte $x_0$ und $x_1$ benötigt (statt nur einem bei Newton).
- Einsetzen in Newtons Formel liefert das iterative **Sekantenverfahren**:
  $$x_{n+1} = x_n - f(x_n) \cdot \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})} \quad (34)$$
- **Algorithmus 2: Secant Method** (Pseudocode):
  - Require: Startwerte $x_0, x_1$, Funktion $f$, Toleranz $\varepsilon$
  - 1: **while** $|f(x_1)| > \varepsilon$ **do**
  - 2: Sekantensteigung: $s \leftarrow (f(x_1) - f(x_0))/(x_1 - x_0)$
  - 3: Vorherigen speichern: $x_{\text{old}} \leftarrow x_1$
  - 4: Update: $x_1 \leftarrow x_1 - f(x_1)/s$
  - 5: $x_0 \leftarrow x_{\text{old}}$
  - 6: **end while** return $x_1$

### [S. 44] Examples & Exercises — Newton by hand
- **Abbildung (Figure 23):** $f(x) = x^3 - x$ hat mehrere Wurzeln; angenommen, die Wurzel bei $x = 1$ ist das Ziel. Graue gestrichelte Linie zeigt die Ableitung $f'(x) = 3x^2 - 1$.
- **Newton by hand:** Wurzel von $f(x) = x^3 - x = 0$ — erst geometrisch, dann von Hand. Wurzeln bei $x = -1, 0, 1$. Ziel: Wurzel bei $x = 1$, Start $x_0 = 1.4$. Taylor 1. Ordnung um $x_n$:
  - $f(x) \approx f(x_n) + f'(x_n)(x - x_n)$, $f(x_n) \approx f(x) - f'(x_n)(x - x_n)$
- Mit $f(x) = x^3 - x = 0$, $f'(x) = 3x^2 - 1$; umstellen für die nächste Schätzung ab $x_0 = 1.4$:
  - $x_1 = x_0 - \frac{f(x_0)}{f'(x_0)} = x_0 - \frac{x_0^3 - x_0}{3x_0^2 - 1} = 1.4 - \frac{2.744 - 1.4}{5.88 - 1} = 1.4 - \frac{1.344}{4.88} \approx 1.127$
  - $x_2 = 1.127 - \frac{1.127^3 - 1.127}{3(1.127)^2 - 1} \approx 1.127 - \frac{0.432}{2.808} \approx 0.976$
  - $x_3 = 0.976 - \frac{0.976^3 - 0.976}{3(0.976)^2 - 1} \approx 0.976 - \frac{-0.072}{1.857} \approx 1.014$
  - Die Wurzel bei $x = 1$ wird schnell gefunden.
- **Secant by hand:** Sekantenverfahren auf dasselbe Problem mit $x_0 = 1.2$, $x_1 = 1.4$ anwenden — erst geometrisch, dann von Hand. (Rechnung auf S. 45.)
- Randnotiz **Code**: https://github.com/Quillstacks/lecturecode_numericalmethods.git

### [S. 45] Secant by hand (Rechnung); Geometrical Failure Search; Self-Reflection (Beginn)
- Sekanten-Rechnung:
  - $x_2 = x_1 - f(x_1) \cdot \frac{x_1 - x_0}{f(x_1) - f(x_0)} = 1.4 - (0.744)\cdot\frac{1.4 - 1.2}{0.744 - 0.128} = 1.4 - 0.744 \cdot \frac{0.2}{0.616} \approx 1.4 - 0.241 \approx 1.159$
  - $x_3 = 1.159 - f(1.159)\cdot\frac{1.159 - 1.4}{f(1.159) - f(1.4)} \approx 1.159 - (0.283)\cdot\frac{-0.241}{0.283 - 0.744} \approx 1.159 - 0.283\cdot\frac{-0.241}{-0.461} \approx 1.159 - 0.283 \cdot 0.522 \approx 1.159 - 0.148 \approx 1.011$
- **Geometrical Failure Search (Übung):** Startpunkte $x_0$ für verschiedene Failure Modes finden: einen, wo Newton wegen Nullableitung scheitert; einen, wo es zu einer Nicht-Ziel-Wurzel konvergiert; einen, wo es zwischen Punkten oszilliert.
- **Enter the machine (Übung):** Konvergenz und Konvergenzraten von Grid-Search, Newton und Sekantenverfahren in Python betrachten. Mit verschiedenen Startpunkten experimentieren und Failure Modes in der Praxis beobachten. Startpunkte erst geometrisch, dann analytisch finden, dann im Code verifizieren.
- **Self-Reflection-Fragen (Beginn):**
  - Hauptvorteil von Newtons Methode gegenüber Grid-Search?
  - Warum genügt eine lineare Approximation für Nullstellensuche? Was sagt die Taylor-Entwicklung über diese Wahl?
  - Warum ist quadratische Konvergenz so mächtig? Wie viele Iterationen bräuchte Newton von Fehler $10^{-1}$ zu Fehler $10^{-16}$?

### [S. 46] Self-Reflection (Ende); Recap; Überleitung Kapitel 5
- Weitere Self-Reflection-Frage: In welchen Situationen würde man Secant gegenüber Newton bevorzugen? Warum nicht in anderen?
- **Recap of Key Concepts:**
  - Newton-Raphson gibt (begrenzte) Konvergenzgarantien nahe einfacher Wurzeln (simple roots).
  - Taylor-Entwicklung bietet einen systematischen Weg, Funktionen lokal zu approximieren.
  - Die Taylor-Entwicklung rechtfertigt die lineare Approximation in Newtons Methode, erklärt die quadratische Konvergenz und erlaubt die Fehlerschätzung in jeder Iteration.
  - Wenn die Ableitung schwer zu berechnen ist, approximiert das Sekantenverfahren die Ableitung aus zwei Punkten und konvergiert.
- **Local methods find local solutions (Überleitung):** Newton konvergiert zu welchem Optimum auch immer in der Nähe; neigt auch zu Oszillation zwischen Punkten oder Divergenz bei Ableitung null/nahe null. Im nächsten Kapitel: Reformulierung der Nullstellensuche als Optimierungsproblem; von dort: globale Optimierung, wenn die Landschaft viele Täler hat oder anderweitig pathologisch schwierig ist.
- Randnotiz **Teaser**: Wie können wir sicherstellen, dass wir die globale Lösung finden und nicht nur eine lokale?

---

## Kapitel 5: Global Optimization (S. 47–56)

### [S. 47] Kapitelbeginn — "And then there were many. / The Why"
- Versionszeile: *2026-05-06 · feisty cranberry Hermelin*.
- Rückblick: Im vorigen Kapitel wurden Newtons Methode und Gradientenabstieg für Nullstellensuche entwickelt. Diese Methoden sind **lokale Methoden**: Sie konvergieren zu der Lösung, die in der Nähe ist. Aber was, wenn die nahe Lösung schlecht ist? Oder eine viel bessere Lösung weiter entfernt liegt?
- **"Time to do away with oversimplifications."** In diesem Kapitel:
  - Shekel's Foxholes kennenlernen, eine klassische Testfunktion für globale Optimierung.
  - Kurz zeigen, wie man ein Optimierungsproblem als Nullstellenproblem (root-finding problem) formulieren kann.
  - Strategien zum Finden globaler Minima einführen.
- **Bezug ML/Deep Learning:** Verständnis multidimensionaler und globaler Optimierung ist entscheidend, um große Modelle effektiv zu trainieren, sie zur Konvergenz zu bringen und tatsächlich etwas Nützliches lernen zu lassen. Loss-Landschaften neuronaler Netze⁸ sind hochgradig nicht-konvex (non-convex), haben flache Regionen und enthalten viele lokale Minima — Optimierung wird dadurch herausfordernd.
- Randnotiz: **Visualization of neural network loss landscapes** — Li et al. (2018) zeigt das komplexe Terrain der Neuronale-Netz-Optimierung; verschiedene Initialisierungen führen zu verschiedenen Endlösungen. ⁸ H. Li, Z. Xu, G. Taylor, C. Studer, T. Goldstein: "Visualizing the loss landscape of neural nets", 31:6389–6399, 2018. URL https://proceedings.neurips.cc/paper_files/paper/2018/file/a41b3bb3e6b050b6c9067c67f663b915-Paper.pdf

### [S. 48] Hands On Experience — Shekel's Foxholes
- **Definition Shekel's Foxholes:** klassische Testfunktion für globale Optimierung mit kontrollierter Multimodalität (controlled multimodality). In 1D einfache Form:
  $$f(x) = -\sum_{i=1}^{m} \frac{c_i}{(x - a_i)^2 + r_i} \quad (35)$$
  wobei $a_i$ die "Foxhole"-Positionen sind, $c_i$ die Tiefe jedes Lochs steuert und $r_i$ die Breite. Durch Anpassen dieser Parameter lässt sich eine Landschaft mit mehreren lokalen Minima und einem globalen Minimum erzeugen — ideale Spielwiese zum Testen von Optimierungsalgorithmen.
- Konkretes Beispiel mit drei Foxholes:
  $$f(x) = -\frac{1}{(x-0)^2 + 0.7} - \frac{1.7}{(x-4)^2 + 0.2} - \frac{1.1}{(x-7)^2 + 0.4}$$
- **Abbildung (Figure 24):** 1D-Shekel's-Foxholes-Funktion (schwarz) mit drei lokalen Minima und ihre Ableitung (grau gestrichelt); Täler bei $x = 0, 4, 7$, das tiefste (globale Minimum) bei $x = 4$. Die Ableitung (gestrichelt) kreuzt null an jedem Minimum. (Plot von $-2$ bis $12$.)
- **Das globale Minimum** liegt bei $x = 4$; die anderen beiden Minima bei $x = 0$ und $x = 7$ sind lokale Minima. Diese Information ist beim Lauf eines Optimierungsalgorithmus natürlich nicht verfügbar — wir sehen nur Funktionswerte und Gradienten an ausgewerteten Punkten. Aber das Wissen ist nützlich, um das Verhalten von Optimierungsmethoden zu erkunden.
- **Sensitivität gegenüber Anfangsbedingungen** von $x_0$: bereits erlebt. Startet Newtons Methode nahe $x = 0$ oder $x = 7$, konvergiert sie zu einem lokalen Minimum, nicht zum globalen bei $x = 4$.
- **Anwendung:** Newtons Methode auf die 1D-Shekel-Funktion⁹ von verschiedenen Startpunkten anwenden und beobachten, wohin die Methode konvergiert. Vorführung für einen Startpunkt, weitere selbst ausprobieren, dann Diskussion des generellen Verhaltens.
- Randnotizen:
  - **The derivative**, dargestellt als gestrichelte Linie, ist die Antwort auf die Formulierung von Optimierung als Nullstellensuche: Die Minima von $f(x)$ entsprechen den Wurzeln von $f'(x)$.
  - ⁹ J. Shekel: "Test functions for multimodal search techniques", 1971.

### [S. 49] Newton auf Shekel; Optimierung als Nullstellensuche
- **Von $x_0 = 7.2$:** Newtons Methode konvergiert zum lokalen Minimum bei $x \approx 7$. Um Newton für Optimierung anzuwenden, lösen wir das Nullstellenproblem auf $f'(x) = 0$ — Reformulierung des Optimierungsproblems. Das **Newton-Update** wird:
  $$x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)} \quad (36)$$
- **Abbildung (Figure 25):** Erste Ableitung (schwarz) und zweite Ableitung (grau gestrichelt) der 1D-Shekel-Funktion. Täler bei $x = 0, 4, 7$, das tiefste (globale Minimum) bei $x = 4$. Die erste Ableitung kreuzt null an jedem Minimum, die zweite Ableitung ist an Minima positiv (bestätigt lokale Krümmung).
- Die Ableitungen vereinfachen sich zu:
  $$f'(x) = \frac{2x}{(x^2 + 0.7)^2} + \frac{3.4(x-4)}{((x-4)^2 + 0.2)^2} + \frac{2.2(x-7)}{((x-7)^2 + 0.4)^2}$$
  - $f'(7.2) \approx 0.005 + 0.100 + 2.27 = 2.38$
  $$f''(x) = \frac{2(0.7 - 3x^2)}{(x^2 + 0.7)^3} + \frac{3.4(0.2 - 3(x-4)^2)}{((x-4)^2 + 0.2)^3} + \frac{2.2(0.4 - 3(x-7)^2)}{((x-7)^2 + 0.4)^3}$$
  - $f''(7.2) \approx -0.002 - 0.091 + 7.23 = 7.14$
  - $x_1 = 7.2 - \frac{2.38}{7.14} \approx 6.87$; $x_2 \approx 7.02$; $x_3 \approx 7.00$
- **Kernbeobachtung:** So können Nullstellenverfahren für Optimierung genutzt werden, indem man sie auf die Ableitung der Funktion anwendet. Die Ableitung $f'(x)$ ist an Extrema null — an diesem Punkt finden wir Minima oder Maxima.
- Randnotiz **Local minima notation**: Der Asterisk (*) ist konventionell für globale Optima reserviert. Zur Unterscheidung lokaler von globalen Minima alternative Notation wie $x^\circ$ (x-circle) oder $x_i$ für das $i$-te lokale Minimum erwägen.

### [S. 50] Das fundamentale Problem lokaler Optimierung; Lernziele Kapitel 5
- Hier hatten wir Pech: Die Methode wird vom nahegelegenen Foxhole bei $x^\circ \approx 7$ angezogen.
- **Das fundamentale Problem:** Lokale Optimierung garantiert nur das Finden naher Extrema. Selbst mit Konvergenzgarantien: Von $x_0 = 3$ hätten wir Glück gehabt, aber von $x_0 = -2$ oder $x_0 = 8$ verpassen wir die globalen Minima. Genug Motivation für die globalen Optimierungsstrategien, die als Nächstes diskutiert werden.
- **Lernziele (Learning Objectives) Kapitel 5:**
  1. Erklären, warum lokale Methoden das Finden globaler Minima nicht garantieren können.
  2. Strategien zum Finden globaler Extrema anwenden.
  3. Verstehen, wie Gradientenabstieg (gradient descent) hilft, die Optimierung Richtung Minima zu lenken.
- Rest der Seite leer.

### [S. 51] Global Optimization Strategies — Formalisierung & Random Restarts
- Formalisierung lokaler und globaler Extrema:
- **Definition Lokale Optimierung (Local optimization):** findet ein nahes Minimum:
  $$\mathbf{x}^* = \arg\min_{\mathbf{x} \in \mathcal{N}(\mathbf{x}_0)} f(\mathbf{x}) \quad (37)$$
  wobei $\mathcal{N}(\mathbf{x}_0)$ eine Nachbarschaft (neighborhood) des Startpunkts ist.
- **Definition Globale Optimierung (Global optimization):** findet das beste Minimum:
  $$\mathbf{x}^* = \arg\min_{\mathbf{x} \in \Omega} f(\mathbf{x}) \quad (38)$$
  wobei $\Omega$ die gesamte Suchdomäne ist. Leicht zu sehen, wie die Suchdomäne unendlich groß ["inifinitely" sic] sein kann.
- **Convexity is the dividing line (Konvexität als Trennlinie):** Für konvexe Probleme findet jede lokale Methode das globale Optimum. Die Schwierigkeit entsteht bei nicht-konvexer Optimierung, wo die Landschaft mehrere lokale Minima, Sattelpunkte (saddle points) und Plateaus enthält.
- **Random Restarts:** die einfachste globale Strategie — fühlt sich im Ansatz wieder wie Brute-Forcing an. **Algorithmus 3: Random Restarts** (Pseudocode):
  - Require: Suchdomäne $\Omega$, lokaler Optimierer LocalOptimize, Restarts $K$
  - 1: $\mathbf{x}_{\text{best}} \leftarrow$ None; $f_{\text{best}} \leftarrow +\infty$
  - 2: **for** $k = 1$ to $K$ **do**
  - 3: $\mathbf{x}_0 \leftarrow$ RandomPoint($\Omega$)
  - 4: $\mathbf{x}^* \leftarrow$ LocalOptimize($\mathbf{x}_0$)
  - 5: **if** $f(\mathbf{x}^*) < f_{\text{best}}$ **then**
  - 6: $\mathbf{x}_{\text{best}} \leftarrow \mathbf{x}^*$; $f_{\text{best}} \leftarrow f(\mathbf{x}^*)$
  - 7: **end if**
  - 8: **end for**
  - 9: **return** $\mathbf{x}_{\text{best}}$
- **Erfolgswahrscheinlichkeit:** Hat das Anziehungsgebiet (basin of attraction) des globalen Minimums Wahrscheinlichkeit $p$, dann mit $K$ Restarts:
  $$P(\text{find global}) = 1 - (1 - p)^K \quad (39)$$
  Für $p = 0.1$ und $K = 20$: $P = 1 - 0.9^{20} \approx 0.88$. Üblicherweise ist $p$ vorab nicht bekannt. Heuristik für $K$ ohne Kenntnis von $p$: $K$ erhöhen, bis die beste Lösung sich stabilisiert (keine Verbesserung nach mehreren Restarts). **Patience** ist ein üblicher Hyperparameter dieser Heuristik — kontrolliert, wie viele Restarts ohne Verbesserung abgewartet werden, bevor gestoppt wird.
- Randnotizen:
  - **$\mathcal{N}$ is a set** von Punkten um $\mathbf{x}_0$, z. B. $\mathcal{N}(\mathbf{x}_0) = \{\mathbf{x} : \|\mathbf{x} - \mathbf{x}_0\| < \epsilon\}$ für einen Radius $\epsilon$.
  - **Definition Convex vs. non-convex:** Eine Funktion $f$ ist *konvex*, wenn $f(\lambda x + (1-\lambda)y) \leq \lambda f(x) + (1-\lambda)f(y)$ für alle $\lambda \in [0,1]$. Für konvexe Funktionen ist jedes lokale Minimum das globale Minimum — lokale Methoden genügen. Nicht-konvexe Funktionen (wie Shekel's Foxholes oder Loss-Oberflächen neuronaler Netze) sind der schwere Fall.
  - **Neural network initialization**: Training mehrerer Netze mit verschiedenen Seeds ist implizites Random Restarts — für große Modelle jedoch nicht praktikabel.

### [S. 52] Basin Hopping, Simulated Annealing, Stochastic Methods
- **Definition Basin Hopping:** erkundet die Landschaft durch Abwechseln von lokaler Optimierung und zufälligen Sprüngen. Anders als Random Restarts, das die Suche komplett zurücksetzt: Basin Hopping erlaubt das Entkommen aus lokalen Minima, während lokale Optimierung weiter genutzt wird, um bessere Lösungen zu finden. **Algorithmus 4: Basin Hopping** (Pseudocode):
  - Require: Startpunkt $\mathbf{x}_0$, lokaler Optimierer LocalOptimize, Sprungverteilung (jump distribution) für $\delta$, Iterationen $K$
  - 1: $\mathbf{x}_{\text{best}} \leftarrow \mathbf{x}_0$; $f_{\text{best}} \leftarrow f(\mathbf{x}_0)$
  - 2: $\mathbf{x}_{\text{current}} \leftarrow \mathbf{x}_0$
  - 3: **for** $k = 1$ to $K$ **do**
  - 4: $\mathbf{x}^* \leftarrow$ LocalOptimize($\mathbf{x}_{\text{current}}$)
  - 5: **if** $f(\mathbf{x}^*) < f_{\text{best}}$ **then**
  - 6: $\mathbf{x}_{\text{best}} \leftarrow \mathbf{x}^*$; $f_{\text{best}} \leftarrow f(\mathbf{x}^*)$
  - 7: **end if**
  - 8: Sprung samplen: $\delta \sim \mathcal{D}$
  - 9: $\mathbf{x}_{\text{current}} \leftarrow \mathbf{x}^* + \delta$ ▷ Random jump
  - 10: **end for**
  - 11: **return** $\mathbf{x}_{\text{best}}$
- Die Sprungverteilung wird als $\delta \sim \mathcal{D}$ spezifiziert — z. B. eine bei null zentrierte Gauß-Verteilung oder eine Gleichverteilung über einen bestimmten Bereich.
- **Definition Simulated Annealing:** kombiniert Basin Hopping mit einem probabilistischen Akzeptanzkriterium für Kandidatenpunkte. Anfangs wird ein Sprung in eine schlechtere Lösung mit Wahrscheinlichkeit $\exp^{-\Delta f / T}$ akzeptiert, wobei $T$ (Temperatur) mit der Zeit abnimmt. Später wird der Algorithmus konservativer und akzeptiert nur noch Kandidaten, die das Ziel verbessern — erlaubt Konvergenz zu einem Optimum.
- **Stochastic methods (stochastische Methoden):** fügen Rauschen hinzu, indem die Loss-Landschaft approximiert wird, um lokalen Optima zu entkommen. Beispiel: 1D-Shekel-Funktion als Funktion zweiter Ordnung approximieren, indem drei Punkte auf der Foxhole-Kurve gewählt werden.
- **The take away:** Die Loss-Landschaft ist nicht statisch, sondern kann konstruiert und geformt werden (engineered and formed). Durch Approximation der Loss-Landschaft auf Mini-Batches (verschiedene Punktauswahlen) erhält man eine verrauschte Schätzung der wahren Loss-Landschaft, was helfen kann, lokalen Minima zu entkommen. Die Loss-Landschaft wird dann natürlich stark durch die Wahl … (Forts. S. 53)
- Randnotizen:
  - **Noisy Newton** folgt derselben Hopping-Idee: Gauß-Rauschen zum Newton-Schritt addieren: $\mathbf{x}_{n+1} = \ldots + \boldsymbol{\xi}_n$.
  - **$\Delta f$** ist der Anstieg des Zielfunktionswerts beim Übergang von der aktuellen Lösung zu einer schlechteren Kandidatenlösung.

### [S. 53] Smoothing-Abbildung; Newton's Method for finding Minima
- … der Loss-Funktion selbst beeinflusst. Allerdings: Der Newton-Schritt ist sehr rauschempfindlich; wir werden andere Ansätze sehen, die damit besser umgehen.
- **Abbildung (Figure 26):** Die Original-Shekel-Funktion (grau, dünn) mit einer durch drei Stützpunkte (Punkte) gefitteten Approximation zweiter Ordnung (durchgezogen schwarz). Die Ableitung der Approximation als grau gestrichelte Linie. Die Quadratik erfasst den generellen Trend, glättet aber die einzelnen Foxholes aus.
- **Newton's Method for finding Minima:** Im Hands-on gesehen: Reformulierung von Optimierung als Nullstellensuche erlaubt Newtons Methode zum Finden von Optima:
  $$x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)} \quad (40)$$
- **Minima, Maxima und Sattelpunkte:** Newtons Methode findet Punkte mit $f''(x) = 0$ [UNSICHER: so im Original; gemeint ist wohl $f'(x) = 0$], aber diese können Minima, Maxima oder Sattelpunkte sein. Der **Test der zweiten Ableitung (second derivative test)** unterscheidet:
  - (a) $f''(x^*) > 0$: lokales Minimum (Kurve biegt nach oben)
  - (b) $f''(x^*) < 0$: lokales Maximum (Kurve biegt nach unten)
  - (c) $f''(x^*) = 0$: nicht schlüssig (möglicher Sattelpunkt oder Wendepunkt/inflection point)
- **Newton Richtung Minima lenken** — Update modifizieren:
  $$x_{n+1} = x_n - \frac{f'(x_n)}{|f''(x_n)|} \quad (41)$$
  So wird sichergestellt, dass wir uns immer in Richtung fallender $f(x)$ bewegen — der Schritt geht immer in Richtung des negativen Gradienten ("downhill" sozusagen).
- Randnotizen:
  - **In deep learning** verwenden wir typischerweise lokale Methoden (SGD, Adam), hoffen aber: (1) die meisten lokalen Minima sind ungefähr gleich gut, (2) Überparametrisierung (overparameterization) macht schlechte Minima selten, (3) Mini-Batch-Rauschen hilft, scharfen Minima zu entkommen, (4) adaptive Lernraten helfen, Plateaus zu navigieren.
  - **How would you** das Update modifizieren, um stattdessen Maxima zu finden?

### [S. 54] Abbildungen zu $f''$ vs. $|f''|$; Examples & Exercises (Random-Restart-Rechnung)
- **Abbildung (Figure 27):** Durchgezogen schwarz: erste Ableitung $f'(x)$ der 1D-Shekel-Funktion; grau gestrichelt: zweite Ableitung $f''(x)$. Schwarzer Marker bei $x = 6.1$ als Beispielposition; die durchgezogene graue Linie ist die Tangente an $f'(x)$ dort (Steigung $\approx -2.66$). Vorzeichen und Betrag von $f''(x)$ bestimmen Richtung und Schrittweite des Newton-Updates beim Lösen von $f'(x) = 0$.
- **Abbildung (Figure 28):** Durchgezogen schwarz: $f'(x)$; grau gestrichelt: absolute Krümmung $|f''(x)|$. Marker bei $x = 6.1$ wie oben; die graue Linie illustriert das Ersetzen von $f''(x)$ durch $|f''(x)|$ (Steigung $\approx +2.66$). $|f''(x)|$ im Newton-Nenner entfernt das Krümmungsvorzeichen, erzwingt Abwärtsschritte und reduziert die Chance, Richtung lokalem Maximum zu schreiten.
- **Examples & Exercises — konkrete Zahlen:** Funktion mit 5 lokalen Minima; das Anziehungsgebiet des globalen Minimums deckt 15 % der Suchdomäne ($p = 0.15$). Wahrscheinlichkeit, das globale Minimum mit $K = 10$ Random Restarts zu finden:
  $$P = 1 - (1 - 0.15)^{10} = 1 - 0.85^{10} = 1 - 0.1969 = 0.803$$
  Ca. 80 % Chance — nicht schlecht, aber weit von sicher. Wie viele Restarts für 99 %?
  $$K = \frac{\ln(1 - 0.99)}{\ln(1 - 0.15)} = \frac{\ln(0.01)}{\ln(0.85)} = \frac{-4.605}{-0.1625} \approx 28.3$$
- Randnotizen:
  - **Code**: https://github.com/Quillstacks/lecturecode_numericalmethods.git
  - **Hint**: $P = 1 - (1-p)^K$ verwenden und nach $K$ auflösen: $K = \frac{\ln(1-P)}{\ln(1-p)}$.

### [S. 55] Übungen: Shekel selbst bauen, Basins of Attraction
- Also $K = 29$ Restarts. Aufgabe: $K$ für $p = 0.05$ und $p = 0.01$ bei gleichem 99-%-Ziel berechnen.
- **On your machine (Übung):** Eigene 1D-Shekel-Funktion designen (anfangs einfach, später komplexer). Erst mit den bisher gelernten lokalen Optimierungsmethoden vertraut machen und auf die eigene Funktion anwenden. Zeigen, wo Newtons Methode (wieder) scheitert. Verschiedene $x_0$ erkunden und Konvergenzverhalten beobachten. Wieder über Loss-Landschaft und Basin-Grenzen nachdenken.
- **Directing the search towards minima (Übung):** Der $|f''|$-Trick flippt das Vorzeichen der Krümmung im Nenner und zwingt den Schritt immer bergab. Geometrische Bedeutung für die Tangentenkonstruktion durchdenken, dann im Code ausprobieren.
- **Escaping Local Minima (Übung):** Random Restarts und Basin Hopping auf der eigenen 1D-Shekel-Funktion einsetzen; vergleichen, wie viele Funktionsiterationen jede Methode zum Finden des globalen Minimums braucht. Wie anfällig sind sie für Hängenbleiben in lokalen Minima? Wie beeinflusst die Wahl der Schrittweitenverteilung die Performance von Basin Hopping?
- **Noise and landscape engineering:** Die Loss-Landschaft ist nicht statisch, sondern zu konstruieren und zu formen. Durch Approximation der Loss-Landschaft auf Mini-Batches (verschiedene Punktauswahl), … [UNSICHER: Satz endet im Original abrupt mit Komma.]
- **Code exercise:** Random Restarts und Basin Hopping auf der 1D-Shekel-Funktion implementieren; vergleichen, wie viele Funktionsauswertungen jede Methode braucht, um das globale Minimum bei $x \approx 4$ zu finden.
- **Finally, let's map out the basins of attraction:** 1D-Shekel-Funktion; Annahme: ein lokaler Optimierer konvergiert immer zum nächstgelegenen Foxhole. [Im Original: "foxhole.2" — UNSICHER: vermutlich Fußnoten-/Tippfehler]
  - (a) Basins of Attraction für die drei Foxholes bei $x = 0, 4, 7$ (grob) skizzieren. Wo liegen die Basin-Grenzen?
  - (b) Wenn Basin Hopping einen Sprung $\delta \sim \text{Uniform}(-3, 3)$ vom lokalen Minimum $x^\circ = 7$ nutzt: Wahrscheinlichkeit, dass ein einzelner Sprung im Basin des globalen Minimums landet?
  - (c) Warum könnte Basin Hopping hier das globale Minimum schneller finden als Random Restarts?
- Randnotizen:
  - **Basin of Attraction**: Plots der Shekel-Funktion erneut ansehen, Anziehungsgebiete für jedes lokale Minimum markieren und relative Größen schätzen. Welches ist das globale Minimum? Wie hängt das mit der Wahrscheinlichkeit zusammen, es mit Random Restarts zu finden?
  - **Non-Convex Basins**: Shekel ist im Allgemeinen nicht-konvex, die Basins jedoch schon ["however the basins are"]; eine Funktion notieren, bei der die Basins of Attraction nicht so leicht zu kartieren sind.
  - **Can you think of** einem cleveren Weg, die Schrittweitenverteilung während der Optimierung automatisch anzupassen? Was wäre eine gute Heuristik? Wie könnte man katastrophale Sprünge verhindern? Implementieren.

### [S. 56] Self-Reflection and Recap (Kapitel 5); Überleitung Kapitel 6
- **Self-Reflection-Fragen:**
  - Warum scheitert lokale Optimierung auf nicht-konvexen Landschaften wie Shekel's Foxholes?
  - Wie skaliert der benötigte Aufwand mit der Größe des globalen Basins bei Random Restarts?
  - Wie unterscheidet sich Basin Hopping von Random Restarts? ["How do basin hopping differently from random restarts?" sic]
  - Was sagt uns $f''(x_n)$ über die Loss-Landschaft, was charakterisiert es, und wie können wir es nutzen?
  - Wie hilft das Approximieren der Loss-Landschaft mit verrauschten Schätzungen (Mini-Batches), lokalen Optima zu entkommen?
  - $x_0$ so wählen, dass es im Basin eines lokalen Minimums liegt; nun verschiedene Wege finden, wie die Optimierungsmethode entkommen kann — wie effektiv ist was?
- **Recap of Key Concepts:**
  - Lokale Optimierungsmethoden (wie Newtons Methode) können auf nicht-konvexen Funktionen in lokalen Minima stecken bleiben.
  - Globale Optimierungsstrategien (Random Restarts, Basin Hopping, Simulated Annealing, Stochastizität) sind darauf ausgelegt, den Suchraum breiter zu erkunden, um das globale Optimum zu finden.
  - Modifikation von Optimierungsmethoden zur Nutzung von Krümmungsinformation $f''(x)$ erlaubt, die Abstiegsrichtung genauer zu spezifizieren.
  - Die Loss-Landschaft gehört uns zum Konstruieren (is ours to engineer) — durch Wahl der Loss-Funktion und Rauschen, etwa stochastische Gradienten.
- **Überleitung:** Gradient Descent neigt zum Steckenbleiben. Bisher war die Antwort lediglich besser als Brute-Forcing. Im nächsten Kapitel: Wie man die Loss-Landschaft glättet (smoothen), um die Robustheit des Gradient-Descent-Ansatzes zu erhöhen.
- Randnotiz **Teaser**: Was, wenn wir nun einer Hochfrequenz-Version von Shekels Foxholes gegenüberstehen? Welches Problem entsteht?

---

## Kapitel 6: Numerical Integration (S. 57–70)

### [S. 57] Kapitelbeginn — "Smooth Operator. / The Why"
- Versionszeile: *2026-05-04 · sneaky olive Falke*.
- Rückblick: Im vorigen Kapitel globale Optimierungsstrategien zum Entkommen lokaler Minima. Vorstellung: Optimierung einer Funktion mit Tausenden winziger, scharfer lokaler Minima — wie eine Hochfrequenz-Version von Shekel's Foxholes. Ein Gradient-Descent-Algorithmus bliebe sofort im ersten mikroskopischen Schlagloch (pothole) stecken.
- **Die Lösung** fühlt sich vertraut an, blieb aber bisher wohl unbemerkt: Numerische Integration.
  $$I = \int_a^b f(x)\,dx \quad (42)$$
- **Gute Gründe**, numerische Integration zu verstehen:
  - Sie erlaubt, die Loss-Landschaft zu glätten und Optimierungsmethoden robuster zu machen.
  - Sie findet tendenziell robustere Optima durch den Mittelungseffekt (averaging effect)¹⁰ einer Region.
- **Bezug Deep Learning:** Stochastic Gradient Descent (SGD) ist der Arbeitspferd-Optimierungsalgorithmus. Es ist eine Monte-Carlo¹¹,¹²-Methode, die den Gradienten der Loss-Funktion schätzt, indem über den Gradienten eines zufälligen Mini-Batches von Datenpunkten gemittelt wird. Glück, dass es numerische Integration gibt — Modelle auf großskaligen Datensätzen zu trainieren wäre sonst prohibitiv teuer.
- Randnotizen:
  - **Melts all your memories** "and change into gold" [Songzitat-Anspielung auf "Smooth Operator"].
  - ¹⁰ N. Keskar, D. Mudigere, J. Nocedal, M. Smelyanskiy, P. Tang: "On large-batch training for deep learning: Generalization gap and sharp minima", 09 2016, DOI: 10.48550/arXiv.1609.04836
  - **Definition Monte Carlo:** eine Strategie, die Probleme im Wesentlichen durch zufälliges Sampling löst. "Embrace the beauty."
  - ¹¹ J. Bergstra, Y. Bengio: "Random search for hyper-parameter optimization", *Journal of Machine Learning Research*, 13:281–305, 2012.
  - ¹² Y. Gal, Z. Ghahramani: "Dropout as a bayesian approximation: Representing model uncertainty in deep learning", 2016. URL https://arxiv.org/abs/1506.02142

### [S. 58] Hands On Experience — Hochfrequente Landschaften
- Wir wissen bereits, wie man eine kontinuierliche Funktion diskretisiert und mit endlicher Präzision und Systemen mit spärlicher Information an diskreten Punkten umgeht.
- **Abbildung (Figure 29):** Kurve $f(x) = \sin(x)$ und diskretisierte Version (schwarze Punkte) auf $[-3,1]$ mit Schrittweite $h = 0.2$.
- Die Shekel-Funktion als Hochfrequenzfunktion war eine Herausforderung für globale Optimierung, machte unsere generellen Ansätze aber nicht obsolet. Wir diskretisieren und behandeln diese Funktionen weiterhin wie gewohnt.
- **Abbildung (Figure 30):** Kurve $f(x) = \sin(x) + \sin(2\pi x)$ und diskretisierte Version (schwarze Punkte) auf $[-3,1]$ mit $h = 0.2$. (Hochfrequent oszillierende Kurve.)
- Genauerer Blick auf irgendein lokales Minimum zeigt, wie die hochfrequente Loss-Landschaft den Optimierungsalgorithmus ins nächstgelegene lokale Minimum stupst (nudge). Beispiel bei $x = 0.6$ oder $x = -0.4$.
- **Abbildung (Figure 31):** $f(x) = \sin(x) + \sin(2\pi x)$ und diskretisierte Version auf $[-3,1]$ mit $h = 0.2$ — hier als Balkendiagramm (graue Balken). [UNSICHER: Bildunterschrift identisch zu Fig. 30 formuliert, Darstellung aber als Balken.]

### [S. 59] Glättung durch Integration
- **Approximation durch numerische Integration:** Betrachtung bei $x = -0.4$; statt direkt zu lösen:
  $$f(-0.4) = -0.97720 \quad (43)$$
  approximieren wir den Wert durch Integration mit Breite $h = 0.2$:
  - $h \cdot f(-0.4) \approx \int_{-0.5}^{-0.3} f(x)\,dx \approx \frac{h}{2}[f(-0.5) + f(-0.3)] \approx 0.2 \cdot \frac{-1.14973 - 0.97720}{2} = -0.11285$
  - $f(-0.4) \approx \frac{-1.14973 - 0.97720}{2} = -1.06347$
- **Dies ist eine viel bessere Approximation** im Hinblick auf globale Optima als die direkte Auswertung bei $x = -0.4$ ($-0.97720$). Die numerische Integration lieferte eine Korrektur der lokalen Loss-Landschaft hin zu höheren Losses an diesem lokalen Minimum. [UNSICHER: Vorzeichenlogik im Original; gemeint: der geglättete Wert spiegelt die Umgebung besser wider.]
- **Abbildung (Figure 32):** $f(x) = \sin(x) + \sin(2\pi x)$ und diskretisierte Version (schwarze Punkte) auf $[-3,1]$ mit $h = 0.2$, geglättet durch numerische Integration mit Intervalllänge $h$ — zeigt den Glättungseffekt auf der ganzen Kurve.
- **Die Glättung** wird noch deutlicher beim Integrieren über größere Intervalle allgemein, oder im konstruierten Beispiel bei Wahl von $h$, sodass die Frequenz des verrauschten Signals herausgemittelt wird.
- Die bisherige Intervall-Approximation ist allerdings ziemlich grob — sie stützt sich auf nur zwei Punkte.
- Randnotiz **What if**: Was, wenn wir über ein Intervall integrieren würden, das destruktive Interferenz ["inference" sic] der zugrunde liegenden höherfrequenten Sinuskurve ergibt? An Wellenlängen denken.

### [S. 60] Glättungs-Abbildung; Lernziele Kapitel 6
- **Abbildung (Figure 33):** $f(x) = \sin(x) + \sin(2\pi x)$ und diskretisierte Version (schwarze Punkte) auf $[-3,1]$ mit $h = 0.2$, geglättet durch Nachbar-Mittelung (neighbour averaging) mit $h = 0.48$ (sodass $h/2 = 0.24$ nahe daran ist, die $\sin(2\pi x)$-Komponente auszulöschen). (Resultat: glatte, sinusähnliche Kurve.)
- **Lernziele (Learning Objectives) Kapitel 6:**
  1. Mittelpunktsmethode (midpoint method), Trapezregel (trapezoid rule) und Simpson-Regel (Simpson's rule) für numerische Integration herleiten und anwenden.
  2. Zusammengesetzte Regeln (composite rules) für verbesserte Genauigkeit verstehen.
  3. Lagrange-Interpolation kennen und wissen, wie sie mit Quadraturregeln (quadrature rules) zusammenhängt.
  4. Verstehen, wie der Fluch der Dimensionalität (curse of dimensionality) Monte Carlo motiviert.
  5. Monte-Carlo-Integration für hochdimensionale Probleme herleiten und anwenden.
  6. Monte-Carlo-Integration anwenden und erkennen, dass Batch-Mittelung in ML numerische Integration ist.
- Rest der Seite leer.

### [S. 61] Methods of Numerical Intgration [sic] — Mittelpunkts-/Riemann-Summen
- **Trivialste Approximation von Integralen:** ein einzelner diskretisierter Wert:
  $$I = \int_a^b f(x)\,dx, \qquad I = \frac{b-a}{n} \cdot f\left(\frac{a+b}{2}\right), \qquad I = h \cdot f(m)$$
  Die Höhe des Rechtecks ist der Wert am Mittelpunkt (midpoint), die Breite ist $h$.
- **Verfeinerung / Definition Riemann-Summen-Approximation:** $[a,b]$ in $n$ Teilintervalle gleicher Breite $h$ teilen und Beiträge jedes Intervalls summieren:
  $$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n-1} \int_{x_i}^{x_{i+1}} f(x)\,dx \approx \sum_{i=0}^{n-1} h \cdot f(m_i)$$
  wobei $x_i = a + ih$ für $i = 0, 1, \ldots, n$.
- **Definition Midpoint Rule (Mittelpunktsregel):** nutzt in diesen zusammengesetzten Intervallen den Mittelpunkt — den Durchschnitt der Endpunkte — jedes Intervalls; liefert oft bessere Resultate als Links-/Rechts-Endpunkt-Methoden. Intuitiv, weil der Mittelpunkt die Krümmung der Funktion auf dem Intervall besser approximiert.
- **Abbildung (Figure 34):** $f(x) = \sin(x)$ und Mittelpunktsregel-Integrale (graue Balken) für $a = -2$, $b = -1$, $h = 0.5$. Schwarze Punkte: Mittelpunkte; Kreise: Endpunkte. Die Balken berühren sich — illustriert die Mittelpunktsregel ohne Lücke.
- **Mehr Teilintervalle reduzieren den Fehler.**
- Randnotizen:
  - **On the interval $[a,b]$**: Der Mittelpunktswert ist $f(m)$; mit linkem Endpunkt ist die Höhe $f(a)$, mit rechtem $f(b)$.
  - **Doubling the sub intervals** reduzierte den Fehler um $\sim 4\times$ — suggeriert $O(h^2)$-Konvergenz.

### [S. 62] Trapezregel & Composite Trapezoid Rule
- Mehr Teilintervalle kosten mehr Funktionsauswertungen, also mehr Rechenkosten. Geht es besser als Mittelpunkte zu approximieren?
- **Definition Trapezregel (Trapezoids):** Trapeze sind geometrisch ausdrucksstärker als Rechtecke und können lineare Änderungen der Funktion zwischen den Endpunkten erfassen:
  $$\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(a) + f(b)\right] \quad (44)$$
  mit $h = b - a$.
- **Abbildung (Figure 35):** $f(x) = \sin(x)$ und Trapezregel-Flächen (graue Trapeze) für $a = -2$, $b = -1$, $h = 0.5$. Schwarze Punkte: Endpunkte. Die Fläche unter den Verbindungsgeraden der Endpunkte illustriert die Trapez-Approximation.
- **Composite Trapezoid Rule (zusammengesetzte Trapezregel):** Trapezregel auf jedes Teilintervall anwenden und Resultate summieren:
  $$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n-1}\int_{x_i}^{x_{i+1}} f(x)\,dx \approx \sum_{i=0}^{n-1} \frac{h}{2}[f(x_i) + f(x_{i+1})]$$
  $$= \frac{h}{2}(f(x_0)+f(x_1)) + \frac{h}{2}(f(x_1)+f(x_2)) + \cdots + \frac{h}{2}(f(x_{n-1})+f(x_n))$$
  $$= \frac{h}{2}[f(x_0) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{n-1}) + f(x_n)] = \frac{h}{2}\left[f(a) + 2\sum_{i=1}^{n-1} f(x_i) + f(b)\right]$$
  mit $x_i = a + ih$, $i = 0, 1, \ldots, n$.
- **Gewichtungs-Intuition:** Funktionswerte an den Endpunkten $a$, $b$ haben Gewicht 1, alle inneren Punkte Gewicht 2 — jeder innere Punkt trägt zu zwei benachbarten Trapezen bei, die Endpunkte nur zu je einem. (Gedanklich durch die eingekreisten Endpunkte der Abbildung gehen: innere Punkte werden zweimal gezählt — einmal als rechter, einmal als linker Endpunkt.)
- Randnotiz: **Dividing the integral by $h$** ergibt einen gewichteten Durchschnitt der Funktionswerte — eine bessere Approximation des Integrals als nur Mittelpunkt oder Endpunkte; reflektiert implizit lokale Krümmung und Information über das Funktionsverhalten über das Intervall.

### [S. 63] Simpson's Rule; Lagrange-Interpolation und Quadratur
- **Definition Simpson's Rule (Simpson-Regel):** kann Krümmung erfassen und liefert daher oft eine viel bessere Approximation als die Trapezregel. Der Idee des linearen Fittens folgend wird ein quadratisches Polynom durch 3 Punkte gefittet statt einer Geraden durch 2. Simpson's Regel ist exakt für quadratische Polynome.
- **Abbildung (Figure 36):** $f(x) = \sin(x)$ und Simpson-Regel-Flächen (grau, unter den Parabeln) für $a = -2, b = -1.5, h = 0.5$ und $a = -1.5, b = -1, h = 0.5$. Schwarze Punkte: Endpunkte; schwarze Punkte: Mittelpunkte bei $x = -1.75$ und $x = -1.25$. Durchgezogene Linie bei $x = -1.5$ trennt die zwei Intervalle. Jede Parabel illustriert den quadratischen Interpolanten der Simpson-Regel auf ihrem Teilintervall.
- **Definition Lagrange interpolation and quadrature:** Lagrange-Interpolation konstruiert das eindeutige Polynom vom Grad $\leq n$, das durch gegebene Stützstellen (nodes) $\{(x_j, y_j)\}_{j=0}^{n}$ verläuft, mit der Basis:
  $$L_j(x) = \prod_{\substack{m=0 \\ m\neq j}}^{n} \frac{x - x_m}{x_j - x_m} \quad (45)$$
- Allgemeine Form eines quadratischen Polynoms (durch Punkte bei $a$, $m$, $b$):
  $$f(x) = f(a)\cdot\frac{(x-m)(x-b)}{(a-m)(a-b)} + f(m)\cdot\frac{(x-a)(x-b)}{(m-a)(m-b)} + f(b)\cdot\frac{(x-a)(x-m)}{(b-a)(b-m)}$$
- **Herleitung der Simpson-Gewichte:** Für ein symmetrisches Intervall wird die Fläche unter $f(x)$ am besten approximiert, indem die Endpunkte Gewicht $h/6$ und der Mittelpunkt Gewicht $2h/3$ erhalten: $A = C = h/6$, $B = 2h/3$ — verifizierbar durch Integration der Lagrange-Basispolynome über $[a,b]$ (detaillierte Rechnung ausgelassen). In einem symmetrischen Intervall sind die Stützstellen äquidistant: $x_0 = a$, $x_1 = m = \frac{a+b}{2}$, $x_2 = b$, sodass der Mittelpunkt $m - a = b - m = h$ erfüllt. Somit:
  $$\int_a^b f(x)\,dx \approx \frac{h}{6}f(a) + \frac{2h}{3}f(m) + \frac{h}{6}f(b) = \frac{h}{6}[f(a) + 4f(m) + f(b)]$$
- **Composite Simpson's Rule:** Simpson-Regel auf jedes Paar von Teilintervallen anwenden und summieren (Annahme: $n$ gerade, $x_i = a + ih$). Beginnend vom Integral: … (Forts. S. 64)
- Randnotiz **Try with some points**: Mit $x = 0$ starten und sehen, wie die Linearfaktoren wirken.

### [S. 64] Composite Simpson (Formel); Genauigkeitstabelle; Monte Carlo & Curse of Dimensionality (Beginn)
- **Composite Simpson's Rule (Formel):**
  $$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n-1}\int_{x_i}^{x_{i+1}} f(x)\,dx \approx \sum_{k=0}^{n/2-1} \frac{h}{6}\left[f(x_{2k}) + 4f(x_{2k+1}) + f(x_{2k+2})\right]$$
  $$= \frac{h}{6}\left[f(x_0) + 4\sum_{k=0}^{n/2-1} f(x_{2k+1}) + 2\sum_{k=1}^{n/2-1} f(x_{2k}) + f(x_n)\right]$$
  $$= \frac{h}{3}\left[f(x_0) + 4\sum_{\substack{i=1 \\ i\text{ odd}}}^{n-1} f(x_i) + 2\sum_{\substack{i=2 \\ i\text{ even}}}^{n-2} f(x_i) + f(x_n)\right]$$
  [UNSICHER: Faktorwechsel $h/6$ → $h/3$ wie im Original gedruckt.]
- **Practical advice: Stop at Simpson.** Für höhere Genauigkeit zusammengesetzte Regeln mit mehr Teilintervallen verwenden. Hohe Grade ($n \geq 8$) entwickeln negative Gewichte und werden instabil.
- **Tabelle 3 — Vergleich der Quadraturmethoden-Genauigkeiten** (höherwertige Methoden erreichen gegebene Genauigkeit mit weniger Funktionsauswertungen; $h$ Schrittweite, $n$ Anzahl Auswertungspunkte bei Gauß-Quadratur):
  | Methode | Fehler Einzelintervall (Single Interval Error) | Akkumulierter Fehler (Accumulated Error) |
  |---|---|---|
  | Left/Right | $O(h^2)$ | $O(h)$ |
  | Midpoint | $O(h^3)$ | $O(h^2)$ |
  | Trapezoid | $O(h^3)$ | $O(h^2)$ |
  | Simpson's 1/3 | $O(h^5)$ | $O(h^4)$ |
  | In General (Gaussian Quadrature) | $O(h^{2n})$ | $O(h^{2n-1})$ |
- **Monte Carlo & the Curse of Dimensionality:**
  - Für $d$-dimensionale Integrale braucht deterministische Quadratur mit $N$ Punkten pro Dimension $N^d$ Punkte insgesamt. Unmöglich — erst recht nicht iterierbar während iterativer Optimierung.
  - **Random Sampling** erlaubt, das Integral zu schätzen, ohne es auf vollem Gitter auszuwerten. Das Integral als Erwartungswert umgeschrieben:
    $$I = \int_\Omega f(\mathbf{x})\,d\mathbf{x} = |\Omega| \cdot \mathbb{E}_{\mathbf{X}\sim\text{Uniform}(\Omega)}[f(\mathbf{X})] \quad (46)$$
    Diese Identität bedeutet: Das bestimmte Integral ist das Domänenvolumen mal dem Durchschnittswert von $f$ unter gleichverteiltem Ziehen aus $\Omega$. Praktisch motiviert das einen Sampling-Schätzer: Punkte gleichverteilt in $\Omega$ ziehen, $f$ dort auswerten, Resultate mitteln, mit $|\Omega|$ multiplizieren.
- Randnotizen:
  - **What happens, when you approximate a linear function with a quadratic?**
  - **Definition Runge's phenomenon (Runge-Phänomen):** Polynominterpolation hohen Grades oszilliert durch Overfitting — führt zu großen Fehlern an den Intervallrändern.
  - **A neural network with $d = 10^6$** (1 Million Parameter) bräuchte $(N)^{10^6}$ Gitterpunkte. Selbst $N = 2$ ergibt $2^{10^6}$ — eine Zahl mit 300.000 Stellen.
  - **$\Omega$** ist die Integrationsdomäne, $|\Omega|$ ihre Länge. Für ein 1D-Integral über $[a,b]$: $|\Omega| = b - a$. In höheren Dimensionen: Produkt der Längen jeder Dimension.

### [S. 65] Monte-Carlo-Schätzer: Bias, Varianz, Dimensionsunabhängigkeit, SGD
- **Monte Carlo uniform sampling auf $[-2,-1]$:** Sei $X \sim \text{Uniform}(-2,-1)$. Dann:
  $$I = \frac{|\Omega|}{N}\sum_{i=1}^{N} f(\mathbf{X}_i), \qquad \mathbf{X}_i \overset{\text{i.i.d.}}{\sim} \text{Uniform}(\Omega) \quad (47)$$
- **Abbildung (Figure 37):** $f(x) = \sin(x)$ und Mittelpunktsregel-Integrale (graue Balken) für $a = -2, b = -1, h = 0.5$; Kreise: Endpunkte; Balken berühren sich. [UNSICHER: Bildunterschrift recycelt die Mittelpunktsregel-Beschreibung; im Plot sind Sample-Punkte markiert.]
- **Bias:** Da der Erwartungswert linear ist, ist dieser Schätzer erwartungstreu (unbiased): sein Erwartungswert ist gleich dem wahren Integral, für $N \to \infty$:
  $$\mathbb{E}[\hat{I}_N] = I \quad (48)$$
- **Varianz:** Maß für die Streuung des Schätzers um seinen Mittelwert bzw. wie groß der Fehler des Schätzers sein kann; folgt aus der Unabhängigkeit der Samples:
  $$\text{Var}(\hat{I}_N) = \frac{|\Omega|^2}{N}\text{Var}(f(\mathbf{X})) = \frac{|\Omega|^2 \sigma_f^2}{N} \quad (49)$$
  mit $\sigma_f^2 = \text{Var}(f(\mathbf{X}))$. Daher Standardfehler (standard error):
  $$\text{SE}(\hat{I}_N) = \frac{|\Omega|\,\sigma_f}{\sqrt{N}} \quad (50)$$
- **Dimension independent (dimensionsunabhängig):** Für große $N$ konvergiert der Sampling-Fehler mit $O(1/\sqrt{N})$ für Monte Carlo — attraktiv in hohen Dimensionen. Quadraturregeln sind bei den Konvergenzraten überlegen, aber der Konvergenzaufwand explodiert mit der Dimension ($N^d$ Punkte für gleiche Genauigkeit).
- **Convergence in SGD:** Mini-Batch-Gradienten in SGD sind Monte-Carlo-Schätzungen des wahren Gradienten, basierend auf in einen Batch gezogenen Samples. Vergrößern der Batch-Größe reduziert die Varianz ungefähr um $1/b$ — direkt analog zur $1/N$-Varianzskalierung oben. Diese Verbindung erklärt, warum die Batch-Größe den Noise-Varianz-Trade-off im Training kontrolliert.
- Randnotizen:
  - **Midpoint rule** ist ein Spezialfall von Monte Carlo mit $N = 1$ Sample am Mittelpunkt.
  - **Definition i.i.d.** (independent and identically distributed): alle $\mathbf{X}_i$ sind unkorreliert und stammen aus derselben zugrunde liegenden Verteilung.
  - **Abbildung (Figure 38):** Effekt der Batch-Größe auf Gradientenrauschen: kleinere Batches erzeugen größere Varianz (sichtbar in der Breite des Trainings-Loss-Bands) in der Gradientenschätzung (Quelle: Stanford CS231n Note). (Plot: verrauschter, abfallender Loss-Verlauf.) Als nützlicher Nebeneffekt: Rechenkosten pro Update-Schritt sind $n/b$-mal billiger. Für $n = 10^6$ und $b = 100$: SGD macht 10.000 Iterationen mit dem Compute, das GD für 1 braucht.

### [S. 66] Examples & Exercises — Integral von $\sin(x)$ von $-2$ bis $-1$
- Beispiel aus den Methodenabschnitten: Integral von $\sin(x)$ von $-2$ bis $-1$ mit verschiedenen Methoden berechnen. Für Fehlerquantifizierung exakter Wert:
  $$\tilde{I} = \int_{-2}^{-1} \sin(x)\,dx = [-\cos(x)]_{-2}^{-1} = -\cos(-1) + \cos(-2) \approx -0.9564491424$$
- **Midpoint rule by hand:** $\int_{-2}^{-1}\sin(x)\,dx$ mit Mittelpunktsregel, $n = 1$ Intervall. Mittelpunkt $m = (-2 + (-1))/2 = -1.5$:
  $$\hat{I} \approx (b - a)\cdot f(m) = 1 \cdot \sin(-1.5) \approx -0.99749$$
  Fehler $|\tilde{I} - \hat{I}| \approx 0.04104$ — kleine Differenz zwischen Mittelpunkt-Schätzung und wahrem Wert.
- **Midpoint rule mit mehr Intervallen:** $n = 2$ Intervalle ⇒ zwei Mittelpunkte bei $-1.75$ und $-1.25$:
  $$h = 0.5, \quad \hat{I} \approx h\cdot[f(-1.75) + f(-1.25)] = 0.5\cdot[\sin(-1.75) + \sin(-1.25)] \approx -0.927228$$
  Fehler $|\tilde{I} - \hat{I}| \approx 0.02922$ — kleiner als mit $n = 1$; illustriert, wie Composites bzw. mehr Intervalle die Approximation verbessern.
- **Trapezoid by hand (Beginn):** Trapezregel für $\int_{-2}^{-1}\sin(x)\,dx$ mit $n = 2$ Intervallen. Endpunkte $-2, -1.5, -1$. … (Forts. S. 67)
- Randnotiz **Further things worth trying**: die Approximation an den Intervall-Endpunkten berechnen und den Fehler vergleichen.

### [S. 67] Trapez-, Simpson-, Monte-Carlo-Rechnung von Hand
- **Trapezregel (Fortsetzung):**
  $$h = 0.5, \quad T_2 = \frac{h}{2}[f(-2) + 2f(-1.5) + f(-1)] = 0.25\cdot[-0.90930 + 2(-0.99749) + (-0.84147)] \approx -0.927228$$
  Der Fehler ist derselbe wie bei der Mittelpunktsregel mit $n = 2$ Intervallen — nicht zwingend Zufall, da beide Methoden zweiter Ordnung genau sind und für bestimmte Funktionen und Intervallwahlen ähnliche Resultate liefern können.
- **Simpson's rule by hand:** $\int_{-2}^{-1}\sin(x)\,dx$ mit $n = 2$ Intervallen, Endpunkte $-2, -1.5, -1$:
  $$h = 0.5, \quad S_2 = \frac{h}{3}[f(-2) + 4f(-1.5) + f(-1)] = \frac{0.5}{3}\cdot[-0.90930 + 4(-0.99749) + (-0.84147)] \approx -0.9564491424$$
  Fehler $|\tilde{I} - S_2| \approx 0.0000000000$ — im Wesentlichen null; illustriert, dass Simpson's Regel für dieses spezielle Integral exakt ist, da $\sin(x)$ über $[-2,-1]$ gut durch ein quadratisches Polynom approximiert werden kann.
- **Monte Carlo by hand:** Monte-Carlo-Schätzung für $\int_{-2}^{-1}\sin(x)\,dx$ mit $N = 4$ Zufallssamples (ähnlicher Rechenaufwand wie die Trapezmethode). Angenommene Zufallssamples:
  - $X_1 = -1.95$, $f(X_1) = \sin(-1.95) \approx -0.92895$
  - $X_2 = -1.55$, $f(X_2) = \sin(-1.55) \approx -0.99978$
  - $X_3 = -1.15$, $f(X_3) = \sin(-1.15) \approx -0.91276$
  - $X_4 = -1.05$, $f(X_4) = \sin(-1.05) \approx -0.86742$
  Monte-Carlo-Schätzung:
  $$\hat{I} = (b-a)\cdot\frac{1}{N}\sum_{i=1}^N f(X_i) = 1\cdot\frac{1}{4}(-0.92895 - 0.99978 - 0.91276 - 0.86742) \approx -0.927228$$
- Randnotiz **Try with more intervals**: sehen, wie der Fehler abnimmt, und prüfen, ob man sich bei Composites in Simpson- und Trapezregel zurechtfindet.

### [S. 68] Monte-Carlo-Fehlerschätzung; Higher Dimensions (Übung)
- Der Fehler ist $|\tilde{I} - \hat{I}| \approx 0.02922$ — derselbe wie bei der Mittelpunktsmethode.
- **Alternative Fehlerschätzung für Monte Carlo:** Für das konkrete Beispiel mit $N = 4$ und Stichprobenmittel $\bar{f} \approx -0.927228$. Mit dem erwartungstreuen Stichprobenvarianz-Schätzer (unbiased sample variance estimator):
  $$Var(f(\mathbf{X})) = \frac{1}{N-1}\sum_{i=1}^{N}(f(X_i) - \bar{f})^2 \quad (51)$$
  Stichprobenvarianz und Standardfehler des Monte-Carlo-Schätzers:
  - $\sigma_f^2 = Var(f(\mathbf{X})) \approx 0.003036$
  - $\sigma_f \approx 0.05512$
  - $\text{SE}(\hat{I}_N) \approx \frac{|\Omega|\,\sigma_f}{\sqrt{N}} = \frac{1 \cdot 0.05512}{2} \approx 0.02756$
- Frage: Was passiert bei Erhöhung von $N$ auf 16? Der Fehler sollte um Faktor 2 abnehmen, da der Standardfehler mit $1/\sqrt{N}$ skaliert. Kurz erläutern, wie der Fehler des Monte-Carlo-Schätzers dimensionsunabhängig ist ["independant" sic].
- **Enter higher dimensions on your machine (Übung):** Monte-Carlo-Integration für ein $d$-dimensionales Integral implementieren, z. B. multivariate Gauß-Funktion über einen Hyperwürfel integrieren. Bei langsam wachsendem $d$ beobachten, wie sich der Fehler für verschiedene Methoden verhält. Mehr noch: beobachten, wie gitterbasierte Quadraturmethoden mit wachsendem $d$ rechnerisch infeasible werden. Optional: ähnliche Effekte in der Optimierung durch Implementierung von Gradient Descent und Mini-Batch-SGD auf einer hochdimensionalen Funktion sehen — nur die Rechenzeiten beobachten.
- Randnotiz **Code**: https://github.com/Quillstacks/lecturecode_numericalmethods.git

### [S. 69] Self-Reflection and Recap (Kapitel 6)
- **Self-Reflection-Fragen:**
  - Wie vergleichen sich die Fehler von Mittelpunkts-, Trapez-, Simpson-Regel und Monte Carlo?
  - Warum hat die Mittelpunktsregel bessere Genauigkeit als die Links-/Rechts-Endpunkt-Regeln?
  - Wie verbessern zusammengesetzte Methoden (composite methods) die Genauigkeit, und was ist der Trade-off?
  - Warum scheitern deterministische Quadraturmethoden in hohen Dimensionen?
  - Inwiefern ist die Mittelpunktsregel ein Spezialfall der Monte-Carlo-Schätzung?
  - Was ist die Intuition dahinter, dass Monte Carlo in hohen Dimensionen nicht explodiert?
  - Wann würde man Simpson's Regel vs. Monte Carlo verwenden?
  - Wie hängt das Mini-Batch-Mittel in SGD mit Monte-Carlo-Schätzung zusammen?
  - Wie hilft die Gradientenschätzung in SGD, lokalen Minima zu entkommen?
- **Recap of Key Concepts:**
  - Deterministische Quadraturmethoden (Midpoint, Trapezoid, Simpson's) approximieren Integrale über gewichtete Summen von Funktionswerten an spezifischen Punkten. Genau und schnell konvergierend für glatte, niedrigdimensionale Probleme.
  - Monte-Carlo-Integration schätzt Integrale durch Mittelung von Funktionswerten an Zufallssamples. Erwartungstreu, Konvergenzrate $O(1/\sqrt{N})$ — unabhängig von der Dimensionalität des Problems.
  - In SGD sind Mini-Batch-Gradienten Monte-Carlo-Schätzungen des wahren Gradienten.
- **Überleitung (Beginn):** Bisher bezog sich Stabilität auf die Sensitivität der numerischen Lösung gegenüber kleinen Änderungen der Eingabedaten. Man kann aber auch über Stabilität der numerischen Methode selbst sprechen, und wie sie sich verhält … (Forts. S. 70)
- Randnotiz **Teaser**: Warum werden Hochordnungs-Quadraturmethoden instabil, wenn sie Polynome niedrigen Grades approximieren?

### [S. 70] Überleitung (Abschluss)
- … beim Approximieren verschiedener Funktionstypen. Im nächsten Kapitel: andere Arten von Stabilitätsproblemen in numerischen Methoden und wie man sie durch geschickte Methodenwahl und -konfiguration abmildert. [Anm.: Ein solches Folgekapitel ist in diesem PDF nicht enthalten — "unfinished lecture notes".]
- Rest der Seite leer.

### [S. 71] Index (Stichwortverzeichnis)
Vollständige Einträge mit Seitenzahlen:
- absolute error, 21 · analytical, 10 · approximation, 12, 58
- basin hopping, 51 · brute-force method, 33
- catastrophic cancellation, 22–24 · complexity, 10 · complexity analysis, 46 · computation, 9 · conditioning, 25 · consistency, 25 · convergence, 25 · curse of dimensionality, 64
- derivative, 35 · discretization, 12, 58
- error, 14, 15 · error analysis, 24 · examples, 14 · exercises, 14, 54, 66
- fixed-point representation, 18, 21–23 · floating-point arithmetic, 17, 24 · floating-point representation, 17–19, 23, 24, 26
- global optimization, 46, 47, 51 · gradient descent, 35 · grid search, 14, 24
- hands-on, 48
- interval, 12, 58 · introduction, 9
- key concepts, 33
- license, 2 · linear approximation, 38 · linear systems, 10 · local information, 35 · local minima, 47 · local optimization, 51 · loss of significance, 18, 22–24
- machine epsilon, 18, 20, 23, 24 · model error, 25 · modeling error, 17, 18, 24 · Monte Carlo, 64 · Moore's Law, 9 · motivation, 9 · multimodal, 48
- Newton optimization, 53 · Newton failure modes, 42 · Newton method, 34 · Newton-Raphson, 38 · numerical algorithms, 33 · numerical integration, 56 (hands-on, 58; motivation, 57) · numerical method, 33 · numerical solution, 33 · numerical stability, 17, 18, 23, 24
- pseudo-accuracy, 22, 24
- quadratic convergence, 41
- random restarts, 51 · recap, 15, 56, 69 · reflection, 15 · rounding error, 17, 18, 22–24
- Secant method, 42 · self-reflection, 33 · significant digits, 22, 24 · Simpson's rule, 62 · simulated annealing, 51 · stability, 25 · stepsize, 12, 58 · stochastic gradient descent, 56
- Taylor expansion, 39 · truncation error, 17, 18

---

## Abdeckungsübersicht (alle 71 Seiten)

| Seiten | Inhalt |
|---|---|
| 1 | Titelseite |
| 2 | Copyright/Lizenz/Repo |
| 3 | Zitat |
| 4 | leer |
| 5 | Inhaltsverzeichnis |
| 6 | leer |
| 7 | Introduction |
| 8 | leer |
| 9–16 | Kap. 1: Enter Numerical Methods |
| 17–24 | Kap. 2: Floating-Point Arithmetic |
| 25–34 | Kap. 3: Error Analysis |
| 35–46 | Kap. 4: Newton Methods |
| 47–56 | Kap. 5: Global Optimization |
| 57–70 | Kap. 6: Numerical Integration |
| 71 | Index |
