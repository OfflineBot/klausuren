# Themen-Masterliste: "Numerical Methods" (Prof. Dr.-Ing. Mark Schutera)

Konsolidierte, verlustfreie Synthese aus `pass_1.md` (Struktur & Konzepte), `pass_2.md` (Formeln/Sätze/Algorithmen), `pass_3.md` (Beispiele/Randnotizen/Details), `pass_4_coverage.md` (Nachextraktion N1/N2) und `review/errata_original_pdf.md` (verbindliche Errata).

Quelle: `Numerical Methods - notes_numerischemethoden.pdf`, 71 Seiten, englischsprachige Vorlesungsnotizen ("Unfinished Lecture Notes"). Seitenangaben `[S. n]` = aufgedruckte PDF-Seitenzahl (identisch mit physischer Seite; die aufgedruckte Paginierung beginnt mit "3" auf der dritten physischen Seite). Gleichungsnummern (1)–(51), Algorithmen 1–4, Tabellen 1–3, Abbildungen (Figures) 1–38 wie im Original.

Konvention: An allen in den Errata verifizierten Fehlerstellen wird die korrekte Version verwendet und mit `[Korrektur ggü. Original, S. n: PDF druckt "..."]` markiert. Originalgetreue Tippfehler werden mit [sic] dokumentiert.

---

## Vorspann (S. 1–8)

### [S. 1] Titelseite
- "PROF. DR.-ING. MARK SCHUTERA — NUMERICAL METHODS — UNFINISHED LECTURE NOTES". Sonst leer, kein mathematischer Inhalt.

### [S. 2] Impressum / Copyright / Lizenz
- Copyright © 2026 Prof. Dr.-Ing. Mark Schutera, "published by unfinished lecture notes".
- Hinweis: "Combobulated with the help of multiple large language model driven tools." (erstellt mit Hilfe mehrerer LLM-getriebener Tools).
- Lizenz: Creative Commons Attribution-NonCommercial 4.0 International ("CC BY-NC-SA 4.0"); Lizenz-URL: https://creativecommons.org/licenses/by-nc-sa/4.0/. Keine kommerzielle Nutzung; Remix/Transformation/Bearbeitungen müssen unter gleicher Lizenz verbreitet werden; Nutzung über die Lizenz hinaus nur mit expliziter Genehmigung des Autors. Material wird "AS IS" ohne Gewährleistung bereitgestellt.
- Mitmach-Hinweis: "These notes are, by their very nature, unfinished, and they improve with every reader." Fehler, Einwände, Quellen, Fragen oder Positionen per Pull Request an: https://github.com/Quillstacks/LectureMaterial/tree/main/lecturenotes/notes_numerischemethoden — "Every contribution is welcome."
- Datums-/Versionszeile (Build-Name): *2026-05-06 · feisty cranberry Hermelin*; grüner QR-Code unten rechts (vermutlich Link zum Repository).

### [S. 3] Zitatseite (Motto)
> "AN INFINITELY ACCURATE APPROXIMATION IS NO LONGER AN APPROXIMATION." — PROBABLY SOMEONE SMART

(Humorvolles Pseudozitat als Motto der Notizen.)

### [S. 4] Leer.

### [S. 5] Inhaltsverzeichnis (Contents)
1. Enter Numerical Methods — S. 9
2. Floating-Point Arithmetic — S. 17
3. Error Analysis — S. 25
4. Newton Methods — S. 35
5. Global Optimization — S. 47
6. Numerical Integration — S. 57
7. Index — S. 71

### [S. 6] Leer.

### [S. 7] Introduction (Einführung)
- "Numerical Methods are essential for solving mathematical problems that cannot be addressed analytically." — Numerische Methoden (numerical methods) sind essenziell zur Lösung mathematischer Probleme, die nicht analytisch behandelt werden können.
- Kursinhalt: fundamentale Konzepte, Fehleranalyse (error analysis), Konditionierung von Problemen (problem conditioning), Stabilität (stability) und verschiedene numerische Techniken — Ziel: zuverlässige und effiziente Algorithmen im wissenschaftlichen Rechnen (scientific computing) und in Ingenieursanwendungen implementieren können.
- Anwendungsversprechen des Kurses: "everything you need to know to become proficient with numerical methods, and how to put them to good use in machine learning, data science, and engineering contexts." (alles Nötige, um mit numerischen Methoden kompetent umzugehen und sie in Machine Learning, Data Science und Engineering einzusetzen).

### [S. 8] Leer.

---

## Thema 1: Enter Numerical Methods (S. 9–16)

### Motivation / The Why — "Tapping into Computational Power" [S. 9]
- Versionszeile des Kapitels: *2026-04-05 · regal coconut Wachtel*.
- **Definition (informell, wörtlich):** "Numerical methods are a subfield of mathematics in which we calculate our solutions not analytically exactly, but approximately." — Numerische Methoden sind ein Teilgebiet der Mathematik, in dem Lösungen nicht analytisch exakt, sondern approximativ berechnet werden. Sie sind essenziell zur Lösung mathematischer Probleme, die nicht analytisch adressiert werden können.
- Begründung ("And we have good reason to do so"):
  - Viele Probleme sind analytisch nicht lösbar oder zu komplex, um praktikabel zu sein.
  - Wir können Rechenleistung (computational power) anzapfen, um approximative Lösungen effizient zu erhalten.
- **Bezug ML/AI [S. 9], vollständiger Wortlaut (inkl. Nachextraktion N1):** In Machine Learning und künstlicher Intelligenz sind numerische Methoden entscheidend für das Training von Modellen, die Optimierung von Parametern und die Simulation komplexer Systeme, wo analytische Lösungen unmöglich (infeasible) sind. "They enable efficient handling of large datasets and complex algorithms, **ensuring that models can learn effectively from data while managing computational resources.**" — Sie ermöglichen effizienten Umgang mit großen Datensätzen und komplexen Algorithmen und stellen dabei sicher, dass Modelle effektiv aus Daten lernen können, während die Rechenressourcen (computational resources) im Rahmen gehalten werden. Besonders im Deep Learning, wo Modelle Millionen Parameter umfassen und umfangreiche Berechnungen erfordern, erleichtern numerische Methoden die Optimierungsprozesse, die dem Modelltraining zugrunde liegen — "making them indispensable for advancing models." (unverzichtbar für den Fortschritt der Modelle).

### Hands On Experience — Grenzen analytischer Skalierung [S. 10–11]
- Ankündigung: Später im Kurs theoretische Grundlagen; zunächst ein Gefühl dafür, warum AI/ML so stark auf numerischen Methoden beruht.
- **Die Grenzen der Skalierung analytischer Lösungen** (the limits of scaling analytical solutions) werden bei großskaligen Problemen offensichtlich. Einfaches Beispiel: Lösen eines linearen 2×2-Gleichungssystems analytisch per Substitution, Gleichung (1):
  $$\begin{bmatrix} 2 & 1 \\ 5 & 1 \end{bmatrix} \begin{bmatrix} w_1 \\ w_2 \end{bmatrix} = \begin{bmatrix} 11 \\ 13 \end{bmatrix} \quad (1)$$
- **Vollständige Substitutionsrechnung [S. 10]:**
  - Aus der ersten Gleichung: $2w_1 + w_2 = 11 \Rightarrow w_2 = 11 - 2w_1$
  - In die zweite Gleichung einsetzen: $5w_1 + 1(11 - 2w_1) = 13$
  - $5w_1 + 11 - 2w_1 = 13$
  - $3w_1 + 11 = 13$
  - $3w_1 = 2$
  - $w_1 = \frac{2}{3}$
  - Dann: $w_2 = 11 - 2\left(\frac{2}{3}\right) = 11 - \frac{4}{3} = \frac{33-4}{3} = \frac{29}{3}$
  - Verifikation 1. Gleichung: $2\left(\frac{2}{3}\right) + \frac{29}{3} = \frac{4}{3} + \frac{29}{3} = \frac{33}{3} = 11$ ✓
  - Verifikation 2. Gleichung: $5\left(\frac{2}{3}\right) + 1\left(\frac{29}{3}\right) = \frac{10}{3} + \frac{29}{3} = \frac{39}{3} = 13$ ✓
- **However [S. 11]:** Für 2 Gleichungen lösbar, aber mit wachsender Systemgröße (z. B. Tausende Gleichungen mit Tausenden Unbekannten) werden analytische Lösungen wegen Rechenkomplexität (computational complexity) und Zeitbeschränkungen unpraktikabel.
- **Grenzen analytischer Lösungen auch bei nichtlinearen Gleichungen** — Beispiel Sigmoid, Gleichung (3):
  $$\sigma(x) = \frac{1}{1 + e^{-x}} \quad (3)$$
- **Kernaussage/Definition (Transzendenz):** Transzendente Funktionen (transcendental functions) können nicht als endliche Kombinationen algebraischer Operationen (Addition, Subtraktion, Multiplikation, Division, Wurzeln) ausgedrückt werden und besitzen daher keine geschlossenen Lösungen (closed-form solutions). Der Exponentialterm macht es unmöglich, $x$ mit elementaren Funktionen (Polynome, rationale, trigonometrische Funktionen) zu isolieren.

### Lernziele (Learning Objectives) Kapitel 1 [S. 11]
1. Erklären, wann numerische Methoden eingesetzt werden und welche Probleme beim analytischen Lösen auftreten.
2. Diskretisierung (discretization): kontinuierliche mathematische Probleme in diskrete, computerlösbare Approximationen transformieren.
3. Grundlegende numerische Techniken auf einfache Probleme von Hand anwenden und größere Probleme am Computer "crunchen".

### Definitionen
- **Diskretisierung (Discretization) [S. 12]:** Zerlegen kontinuierlicher Domänen (Zeit, Raum oder andere Funktionen) in endliche Schritte oder Gitter (grids) und Auswertung dieser Funktionen an diskreten Punkten mit endlicher Präzision:
  - Kontinuierliche Funktion: $f(x), \quad x \in [a, b]$
  - Diskretisierte Funktion: $f(x_i), \quad x_i = a + ih, \quad i = 0, 1, \ldots, N$
  - mit Schrittweite (step size), Gleichung (4):
    $$h = \frac{b - a}{N} \quad (4)$$
    wobei $N$ die Anzahl der Schritte auf dem Intervall ist.
- **Brute Force [S. 13, Randnotiz]:** alle möglichen Optionen ausprobieren und die beste wählen — hier per Gittersuche (grid search).
- **Approximationsfehler (Approximation Error) [S. 13, Randnotiz]:** Differenz zwischen analytischer und numerischer Lösung. Hier konkret: $|-1 - (-0.9093)| = 0.0907$.
- **Extrema auf geschlossenem Intervall (Konzept/Stolperfalle) [S. 13]:** Das Minimum (oder Maximum) einer Funktion auf einem geschlossenen Intervall $[a,b]$ kann an einem kritischen Punkt (Ableitung null oder nicht definiert) im Inneren ODER an den Endpunkten $a$, $b$ auftreten — auch wenn dort die Ableitung nicht null ist. Deshalb müssen bei Extremasuche auf geschlossenen Intervallen stets kritische Punkte UND Endpunkte geprüft werden.

### Formeln/Gleichungen (mit Original-Nummern)
- Gl. (1): 2×2-System $\begin{bmatrix} 2 & 1 \\ 5 & 1 \end{bmatrix}\begin{bmatrix} w_1 \\ w_2 \end{bmatrix} = \begin{bmatrix} 11 \\ 13 \end{bmatrix}$ [S. 10]
- Gl. (2): 3×3-Übungssystem (Randnotiz, s. u.) [S. 10]
- Gl. (3): Sigmoid $\sigma(x) = \frac{1}{1+e^{-x}}$ [S. 11]
- Gl. (4): Schrittweite $h = \frac{b-a}{N}$ [S. 12]
- Gl. (5): identisches System mit Variablen $w, b$ (s. Beispiele) [S. 14]
- Gl. (6): Fehlerdefinition Grid Search (s. Beispiele) [S. 14]
- Gl. (7): $f(x) \approx f(x_i), \quad x_i = a + ih$ [S. 16]

### Durchgerechnete Beispiele
- **Analytische Minimumsuche von $\sin(x)$ auf $[-3, 1]$ [S. 12–13]:** gesucht $\min_{x \in [-3,1]} \sin(x)$. Das Minimum tritt auf, wo die Ableitung verschwindet und die zweite Ableitung positiv ist:
  $$f(x) = \sin(x), \qquad f'(x) = \cos(x) = 0 \implies x^* = \frac{\pi}{2} + k\pi, \; k \in \mathbb{Z}$$
  - Kritische Punkte in $[-3, 1]$:
    $$x_1 = -\frac{\pi}{2} \approx -1.5708$$
    $$x_2 = \frac{\pi}{2} \approx 1.5708 \quad (> 1, \text{ nicht im Intervall — Grenzfall!})$$
  - Prüfung der Endpunkte und von $x_1$:
    $$\sin(-3) \approx -0.1411, \qquad \sin\left(-\frac{\pi}{2}\right) = -1, \qquad \sin(1) \approx 0.8415$$
  - Ergebnis: Minimum ist $-1$ bei $x = -\frac{\pi}{2} \approx -1.5708$.
- **On To the Numerical Solution — Brute-Force-Gittersuche (grid search) [S. 13]:** Funktion an diskreten Punkten über dem Intervall auswerten, Punkt mit minimalem Wert wählen. Diskretisierung von $[-3,1]$ mit Schrittweite $h = 1$:
  | $x_i$ | Wert |
  |---|---|
  | $x_0 = -3$ | $\sin(-3) \approx -0.1411$ |
  | $x_1 = -2$ | $\sin(-2) \approx -0.9093$ |
  | $x_2 = -1$ | $\sin(-1) \approx -0.8415$ |
  | $x_3 = 0$ | $\sin(0) = 0$ |
  | $x_4 = 1$ | $\sin(1) \approx 0.8415$ |
  - Ergebnis: "the minimum among these is $\sin(-2) \approx -0.9093$ at $x = -2$." Approximationsfehler gegenüber analytisch: $|-1 - (-0.9093)| = 0.0907$.
- **Grid Search für das lineare System [S. 14], Gleichung (5):**
  $$\begin{bmatrix} 2 & 1 \\ 5 & 1 \end{bmatrix} \begin{bmatrix} w \\ b \end{bmatrix} = \begin{bmatrix} 11 \\ 13 \end{bmatrix} \quad (5)$$
  Das System kann auch via Brute-Force-Diskretisierung und Approximation gelöst werden: Variablen $w$ und $b$ über ein Gitter möglicher Werte diskretisieren, lösen und die fehlerminimierende Lösung wählen. Grid Search für $w, b$ mit Schrittweite 2.5 über $w, b \in \{0, 2.5, 5, 7.5, 10\}$; für jede Kombination wird der Fehler berechnet.
  **Fehlerdefinition (Error), Gleichung (6)** — Summe der absoluten Differenzen zwischen linker und rechter Seite der Gleichungen:
  $$\text{error}_1 = |2w + b - 11|, \qquad \text{error}_2 = |5w + b - 13| \quad (6)$$
  Alle Kombinationen auswerten, $(w,b)$-Paar mit kleinstem akkumuliertem Fehler wählen.
- **Wert des Handrechnens [S. 14]:** "There is value in doing this by hand" — hilft, die Mechanik numerischer Methoden zu verstehen; gibt Intuition über die Rechenkosten von Brute-Force-Methoden ("This was only 100 operations"; später effizientere Ansätze). Botschaft: so etwas will man an den Computer übergeben und automatisieren — der mit dieser Problemgröße nicht einmal ansatzweise Probleme hat.
- **Enter the machine [S. 14]:** Viele numerische Methoden sind für Computer-Implementierung konzipiert. Im Kurs Wechsel zwischen Handrechnungen (kleine Beispiele) und Computer-Implementierungen (größere Probleme). "You get a jupyter notebook pre-hosted at your fingertips. With it you get a python template for this excercise [sic]. Use the self-reflection questions below to guide your while exploring and experimenting with the implementation." (Jupyter Notebook vorgehosted mit Python-Template; Selbstreflexionsfragen als Leitfaden.)

### Tabellen
- **Tabelle 1 [S. 15]:** "Grid search for $w, b$ in $\{0, 2.5, 5, 7.5, 10\}$: values of $2w + b$ and $5w + b$ with errors to 11 and 13 in parentheses. The last column shows the accumulated error (sum of absolute errors). The minimum error occurs at $w = 0, b = 10$ with an error of 4 (marked with *)." Vollständig (alle 25 Zeilen):

  | $w$ | $b$ | $2w+b$ (error₁) | $5w+b$ (error₂) | Error |
  |---|---|---|---|---|
  | 0 | 0 | 0 (11) | 0 (13) | 24 |
  | 0 | 2.5 | 2.5 (8.5) | 2.5 (10.5) | 19 |
  | 0 | 5 | 5 (6) | 5 (8) | 14 |
  | 0 | 7.5 | 7.5 (3.5) | 7.5 (5.5) | 9 |
  | 0 | 10 | 10 (1) | 10 (3) | **4\*** |
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

  (Anmerkung aus Pass 3: Das Grid-Search-Minimum $w=0, b=10$ weicht stark von der wahren Lösung $w = 2/3, b = 29/3 \approx 9.67$ ab — illustriert die Grenzen grober Gitter; $b=10$ liegt nahe am wahren $b$, $w$ jedoch falsch.)

### Abbildungsbeschreibungen
- **Figure 1 [S. 12]:** "Continuous curve $f(x) = \sin(x)$ and its discretized version (black dots) on $[-3, 1]$ with step size $h = 1$." — Plot der Sinuskurve von $x = -3$ bis $1$ (y-Achse $-1$ bis $1$) mit schwarzen Punkten bei den ganzzahligen Stützstellen.
- **Figure 2 [S. 12]:** "Continuous curve $f(x) = \sin(x)$ (black), its derivative $f'(x) = \cos(x)$ (gray, dashed), and the analytical minimum (black dot) on $[-3,1]$. The dashed gray line marks the critical point where $\cos(x) = 0$ and the minimum of $\sin(x)$." — vertikale gestrichelte graue Linie bei $x = -\frac{\pi}{2}$.
- **Figure 3 [S. 13]:** "Continuous curve $f(x) = \sin(x)$ and its discretized version (black dots) on $[-3,1]$ with step size $h = 1$." (wie Figure 1).

### Randnotizen / Fußnoten / Literatur
- **Further Reading [S. 9]** (Fußnoten 1–4):
  1. T. Arens, F. Hettlich, C. Karpfinger, U. Kockelkorn, K. Lichtenegger, H. Stachel: *Mathematik*, Springer.
  2. W. Dahmen, A. Reusken: *Numerik für Ingenieure und Naturwissenschaftler*, Springer.
  3. M. P. Deisenroth, A. A. Faisal, C. S. Ong: *Mathematics for Machine Learning*, Cambridge University Press.
  4. P. Deuflhard, A. Hohmann: *Numerische Mathematik 1 – Eine algorithmisch orientierte Einführung*, De Gruyter.
- **Approximation (Etymologie) [S. 9]:** vom Lateinischen *approximare*, "to come near to" (sich annähern).
- **Moore's Law [S. 9]:** besagt, dass sich die Rechenleistung ca. alle zwei Jahre verdoppelt. Heutige Consumer-GPUs haben Tausende Kerne und schaffen Billionen Gleitkommaoperationen pro Sekunde. Quelle: G. E. Moore: "Cramming more components onto integrated circuits", *Electronics*, 38(8):114–117, 1965.
- **GPT-2: 1.5B release [S. 9]:** Link: https://openai.com/index/gpt-2-1-5b-release/
- **Analytics [S. 10]:** umfasst Methoden wie Substitution, Elimination, Matrixinversion etc. aus der linearen Algebra.
- **Computational complexity [S. 10]:** wächst mit der Systemgröße. Übungsaufgabe in der Marginalie ("Now take a shot and solve this larger system of three equations with three unknowns"), Gleichung (2):
  $$\begin{bmatrix} 2 & 1 & 3 \\ 1 & 4 & 2 \\ 3 & 2 & 5 \end{bmatrix} \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix} = \begin{bmatrix} 14 \\ 20 \\ 32 \end{bmatrix} \quad (2)$$
- **Sigma [S. 11]:** "$\sigma(x)$ is the sigmoid activation function commonly used in neural networks, and a transcendental function. A closed-form solution for $\sigma(x) = 0$ does not exist. $\sigma(x)$ approaches 0 asymptotically as $x$ approaches negative infinity, but never actually reaches 0 for any finite value of $x$." (Grenzfall/Warnung: Nullstelle existiert nicht!)
- **Remember [S. 12]:** Die Klammern "[" und "]" heißen geschlossenes Intervall (closed interval) und bedeuten, dass die Werte $a$ und $b$ in der Definitionsmenge enthalten sind.
- **Trigonometric Rules [S. 12]:** geben die allgemeine Lösung für $\cos(x) = 0$; falls vergessen, am Einheitskreis herleitbar.
- **The minimum [S. 13]:** "among these is $\sin(-2) \approx -0.9093$ at $x = -2$." Die Wahl der Schrittweite $h$ beeinflusst die Genauigkeit der Approximation; kleinere Schrittweite ⇒ nähere Approximation ans wahre Minimum. "Further the interval selection matters, in a sense that it ." [Anm.: Satz bricht im Original mitten im Satz ab — Inhalt nicht rekonstruierbar; in allen Pässen und im PDF so bestätigt.]
- **Excercises [sic] [S. 14]:** "are for practice and reinforcing concepts. Try to solve them on your own first, try things, play with it, discuss, this is not a time trial. And there is no shame in not ending up at the right answer, in the same sense, that uncovering great questions and tossing them around is usually pretty fruitful on the long run." (Lernhinweis: Übungen dienen Übung und Festigung; kein Zeitrennen; gute Fragen aufzudecken und hin- und herzuwerfen ist langfristig fruchtbar.)
- **Linear regression [S. 14]:** "see how $xw + b$ forms a linear model, which can also be thought of as the most basic form of a single unit neural network $\theta$." (ML-Anwendungsbezug)
- **Code-Hosting [S. 14]:** Code ist als Notebooks gehostet: https://enlitenment.schutera.com/landing [UNSICHER laut Pass 3: URL-Schreibweise, evtl. "enlightenment"].

### Übungsaufgaben & Selbstreflexionsfragen
- Übung (Randnotiz [S. 10]): Das größere 3×3-System (Gl. (2)) selbst lösen.
- Übung [S. 14]: Grid Search für Gl. (5)/(6) im vorgehosteten Jupyter Notebook (Python-Template) explorieren und experimentieren.
- **Self-Reflection [S. 15]:**
  - "Why is the choice of step size $h$ important when discretizing a continuous function, and how does it affect the accuracy and the compute time of the numerical solution?" (Warum ist die Wahl der Schrittweite $h$ beim Diskretisieren wichtig, und wie beeinflusst sie Genauigkeit und Rechenzeit?)
  - "How does the selection of the interval $[a,b]$ influence the results of discretization and the location of extrema found numerically?" (Wie beeinflusst die Intervallwahl $[a,b]$ Diskretisierungsergebnisse und Lage numerisch gefundener Extrema?)
  - "What are the main differences between a continuous function and its discretized version, and what are the implications for solving mathematical problems numerically?" (Hauptunterschiede kontinuierliche vs. diskretisierte Funktion; Implikationen fürs numerische Lösen?)

### Recap of Key Concepts [S. 16]
- Numerische Methoden sind essenziell für komplexe mathematische Probleme ohne analytische Lösung.
- Diskretisierung transformiert kontinuierliche Probleme in diskrete, für rechnerische Methoden geeignete Approximationen.
- Numerische Berechnungen von Hand für kleine Probleme (Verständnis der Mechanik); Computer sind für größere Probleme unverzichtbar.
- **Errors everywhere:** Mathematische Modelle sind Vereinfachungen der Realität, und numerische Methoden führen zusätzliche Fehler durch Approximation ein, Gleichung (7):
  $$f(x) \approx f(x_i), \quad x_i = a + ih \quad (7)$$
- Numerische Berechnung führt einige Fehlertypen ein, die verstanden werden müssen, "in order to be able to fully harness this new methodology." (Überleitung zu Kapitel 2/3.)

### Teaser [S. 16]
- Randnotiz: "Can you think of a simple way to improve the accuracy to compute ratio of our grid search example from above?" (Einfacher Weg, das Verhältnis Genauigkeit/Rechenaufwand der Grid Search zu verbessern? — Denkanstoß für adaptive/verfeinerte Suche.)

---

## Thema 2: Floating-Point Arithmetic (S. 17–24)

### Motivation / The Why — "Getting used to Errors Everywhere" [S. 17]
- Versionszeile des Kapitels: *2026-04-29 · lively date Hase*.
- Rückbezug: Numerische Methoden führen Fehler durch Approximation ein. Sei $f(x)$ eine kontinuierliche Funktion auf $[a,b]$; die diskretisierte Version $f(x_i)$ approximiert $f(x)$ an diskreten Punkten $x_i$ mit einem Fehler, der von der Schrittweite $h$ und der Glattheit (smoothness) von $f$ abhängt.
- Numerische Werte können im Computerspeicher zudem nur approximativ gespeichert werden — in Gleitkommadarstellung (floating-point representation). Das führt zu Rundungsfehlern (rounding errors) bei arithmetischen Operationen, die sich zu den Abschneide-/Trunkierungsfehlern (truncation errors) addieren, die beim Approximieren unendlicher Prozesse durch endliche entstehen (auch Approximationsfehler/approximation error genannt).
- Gute Gründe, diese Fehler und ihr Zusammenspiel mit den Maschinen zu verstehen:
  - Numerische Methoden führen Rundungs- und Abschneidefehler (rounding and truncation errors) ein.
  - Je nach Maschine wirken sich diese Fehler unterschiedlich aus und können sich verstärken (amplify) und akkumulieren (accumulate).
- **Bezug ML/AI:** Numerische Methoden sind fürs Training zentral, Gleitkomma-Arithmetik ist aber genauso relevant in der Modell-Inferenz (model inference) — besonders in rechenarmen Umgebungen "on the edge" oder beim Einsatz quantisierter Modelle (quantized models, Fußnote 5); dann ist Verständnis der Gleitkomma-Arithmetik und der zugrunde liegenden Mechanik nützlich.

### Hands On Experience — Rundungsfehler [S. 18]
- **Beispiel: Division $10 \div 3$** (vollständige Dezimalentwicklung, schriftliche Division):
  - $10 \div 3 = 3$, Rest 1
  - "Bring down a 0": $10 \div 3 = 3$, Rest 1
  - "Bring down a 0": $10 \div 3 = 3$, Rest 1
  - "Bring down a 0": $10 \div 3 = 3$, Rest 1
  - … und so weiter ⇒ $\frac{10}{3} = 3.333\ldots$ — die 3en wiederholen sich unendlich.
- Beim Aufschreiben/Eingeben in Rechner/Computer muss man irgendwo stoppen, Gleichung (8):
  $$\frac{10}{3} \approx 3.333 \quad \text{(gerundet bzw. abgeschnitten/trunkiert nach 3 Ziffern)} \quad (8)$$
- **Definition Rundungsfehler (rounding error):** Differenz zwischen wahrem Wert und dem Wert, den man nach Abschneiden (truncate) der Entwicklung erhält. "No matter how many digits you write, as soon as you stop, you introduce an error", Gleichung (9):
  $$\text{Rounding error} = |3.333333\ldots - 3.333| = 0.000333\ldots \quad (9)$$
- Je mehr Ziffern, desto kleiner der Fehler; er verschwindet aber nie vollständig, außer man schriebe unendlich viele Ziffern — "which well, you know is impossible."
- **This is rounding error:** Computer speichern Zahlen stets mit endlich vielen Ziffern, daher tauchen Rundungsfehler unvermeidlich auf und müssen gemanagt werden. Diese kleinen Fehler können akkumulieren, sich verstärken und zu signifikanten Ungenauigkeiten führen — besonders in iterativen Algorithmen, wie sie in numerischen Methoden und Machine Learning üblich sind.

### Lernziele (Learning Objectives) Kapitel 2 [S. 18]
1. Die verschiedenen Typen numerischer Fehler verstehen: Modellierungs-, Abschneide- und Rundungsfehler (modeling, truncation, rounding errors).
2. Gleitkommadarstellung (floating-point representation), Maschinengenauigkeit (machine epsilon) und Auslöschung (loss of significance) verstehen.
3. Numerische Fehler in praktischen Berechnungen handhaben können.

### Definitionen
- **Modeling Error (Modellierungsfehler) [S. 17, Randnotiz]:** tritt auf, da alle Modelle Vereinfachungen der Realität sind; die Differenz zwischen Modell und realem System führt einen Fehler ein. Wird in diesem Kurs nicht vertieft — "Yet, mind the fine difference between what we term $f(x)$ and what actually is a $f(x)$." (den feinen Unterschied beachten zwischen dem, was wir $f(x)$ nennen, und dem, was tatsächlich ein $f(x)$ ist).
- **Gleitkommazahlen (Floating-point numbers) [S. 19]:** Methode für Computer, reelle Zahlen mit endlicher Bitzahl darzustellen. Der IEEE-754-Standard (Fußnote 6) ist das am weitesten verbreitete Format. Eine Gleitkommazahl wird typischerweise gespeichert als Gleichung (10):
  $$x = (-1)^s \cdot m \cdot 2^e \quad (10)$$
  wobei $s$ das Vorzeichenbit (sign bit), $m$ die Mantisse (mantissa, auch significand) ist, die die Präzision bestimmt, und $e$ der Exponent, der die Skala (Größenordnung/magnitude) der Zahl bestimmt. Erlaubt einen weiten Wertebereich, aber nur eine endliche Menge reeller Zahlen ist exakt darstellbar. IEEE 754 single precision (float): 32 Bit = 1 Vorzeichenbit + 8 Exponentenbits + 23 Mantissenbits.
- **Exponent mit Bias [S. 19]:** Der Exponent wird mit einem Bias gespeichert, um positive und negative Exponenten zu ermöglichen — so können sehr kleine und sehr große Größenordnungen dargestellt werden. Beispiel IEEE 754 single precision: 8 Exponentenbits, Bias 127. Gespeicherter Exponent $E$ und wahrer Exponent $e$: $e = E - 127_{10}$. Grund: Mit 8 Bits speichert das Exponentenfeld Werte von 0 ($2^0 - 1$) bis 255 ($2^8 - 1$); durch Subtraktion des Bias (127) kann der tatsächliche Exponent $e$ positive und negative Werte annehmen, zentriert um null. "This makes encoding and comparison of floating-point numbers easier in hardware." (vereinfacht Kodierung und Vergleich in Hardware).
- **Machine Epsilon ($\varepsilon_{\text{mach}}$, Maschinengenauigkeit) [S. 20]:** die kleinste positive Zahl, sodass $1 + \varepsilon_{\text{mach}} \neq 1$ in der Computerarithmetik. Quantifiziert die obere Schranke des relativen Fehlers durch Rundung in Gleitkomma-Arithmetik, Gleichung (11):
  $$\varepsilon_{\text{mach}} = 2^{-t} \quad (11)$$
  wobei $t$ die Anzahl der Mantissenbits ist. Im 2-Bit-Beispiel: $\varepsilon_{\text{mach}} = 2^{-2} = 0.25$.
- **Relative vs. absolute Präzision [S. 20]:** Die relative Präzision von Gleitkommazahlen ist ca. $2^{-t}$, während die absolute Präzision von der Größenordnung der dargestellten Zahl abhängt, Gleichung (12):
  $$\varepsilon_{\text{mach}} \cdot |x| \quad (12)$$
- **Fixed-point representation (Festkommadarstellung) [S. 21]:** Eine andere Art, reelle Zahlen in Computern zu speichern, besonders wenn vorhersagbare Präzision und Performance gewünscht sind. Bei Fixed-Point wird vorab entschieden, wie viele Bits für den Ganzzahl- und wie viele für den Bruchteil verwendet werden. Dadurch ist die Lücke zwischen darstellbaren Zahlen (die Präzision) immer gleich, egal wie groß oder klein der Wert ist — "Which gives more control."
- **Loss of significance (Auslöschung), auch catastrophic cancellation (katastrophale Auslöschung) [S. 22]:** tritt auf, wenn zwei nahezu gleiche Zahlen subtrahiert werden, wodurch sich führende Ziffern aufheben und nur die weniger signifikanten, rundungsfehleranfälligen Ziffern übrig bleiben. "This can greatly amplify rounding errors." (kann Rundungsfehler stark verstärken).
- **Pseudo-Accuracy [S. 22, Randnotiz]:** allgemein ein ungerechtfertigt hoher Detailgrad, der ein irreführendes, künstliches Genauigkeitsgefühl erzeugt. (Warnung vor Scheingenauigkeit.)
- **Overflow [S. 23, Randnotiz]:** tritt auf, wenn Zahlen großer Magnitude als $+\infty$ oder $-\infty$ approximiert werden.
- **Underflow [S. 23, Randnotiz]:** tritt auf, wenn Zahlen nahe null auf null gerundet werden.
- **Bit [S. 19, Randnotiz]:** kurz für *binary digit*, die grundlegendste Informationseinheit in Computertechnik und digitaler Kommunikation; kann Wert 0 oder 1 haben.

### Formeln/Gleichungen und Beispielrechnungen
- Gl. (8): $\frac{10}{3} \approx 3.333$ [S. 18]
- Gl. (9): Rounding error $= |3.333333\ldots - 3.333| = 0.000333\ldots$ [S. 18]
- Gl. (10): $x = (-1)^s \cdot m \cdot 2^e$ [S. 19]
- Gl. (11): $\varepsilon_{\text{mach}} = 2^{-t}$ [S. 20]
- Gl. (12): absolute Präzision $\varepsilon_{\text{mach}} \cdot |x|$ [S. 20]
- **Constructing scale in Gleitkommadarstellung [S. 20]** (Beispielrechnungen, Skala über Exponent):
  $$10^1 = 10_{10} = 1010_2 = 1.010 \times 2^3, \quad E = 10000010_2$$
  $$10^2 = 100_{10} = 1100100_2 = 1.100100 \times 2^6, \quad E = 10000101_2$$
  $$10^3 = 1000_{10} = 1111101000_2 = 1.111101000 \times 2^9, \quad E = 10001000_2$$
- **Die Mantisse [S. 20]** bestimmt, wie fein Zahlen zwischen Zweierpotenzen dargestellt werden können.
- **2-Bit-Mantissen-Beispiel (unnormalisiert) [S. 20]:** Mantissen-Bitkombinationen 00, 01, 10, 11; unnormalisierter Significand $0.xx_2$:
  $$00:\ 0.00_2 = 0 + 0 \times 2^{-1} + 0 \times 2^{-2} = 0.0$$
  $$01:\ 0.01_2 = 0 + 0 \times 2^{-1} + 1 \times 2^{-2} = 0.25$$
  $$10:\ 0.10_2 = 0 + 1 \times 2^{-1} + 0 \times 2^{-2} = 0.5$$
  $$11:\ 0.11_2 = 0 + 1 \times 2^{-1} + 1 \times 2^{-2} = 0.75$$
  Eine 2-Bit-Mantisse erlaubt vier verschiedene Werte zwischen zwei beliebigen Zweierpotenzen; eine 3-Bit-Mantisse acht Werte usw. **Allgemein:** Mantisse mit $t$ Bits ⇒ $2^t$ verschiedene Werte zwischen zwei Zweierpotenzen, skaliert durch den Exponenten.
- **In other words [S. 21]:** Große Zahlen haben größere absolute Lücken (gaps) zwischen darstellbaren Werten als kleine Zahlen.
- **Fixed-Point-Beispiel (Skalierungsfaktor) [S. 21]:** Zahlen zwischen $-1000$ und $1000$ mit 32-Bit signed Integer speichern. Normal stellt ein 32-Bit-Integer Werte von $-2147483648$ bis $2147483647$ dar — viel mehr als nötig. Für mehr Präzision: Skalierungsfaktor verwenden, z. B. jede reelle Zahl mit $10^6$ multiplizieren und als Integer speichern. So wird $1.234567$ zu $1234567$ im Speicher.

### Durchgerechnete Beispiele (Loss of Significance) [S. 22–23]
- **Beispiel 1 [S. 22]:** Zwei Zahlen $a$, $b$ im Computer mit begrenzter Präzision, je auf 8 signifikante Stellen gerundet (Fixed-Point-Darstellung):
  $$a = 12345678.5, \qquad b = 12345678.0$$
  Mit 8 signifikanten Stellen gespeichert als:
  $$\tilde{a} = 12345679, \qquad \tilde{b} = 12345678$$
  Subtraktion: $\tilde{a} - \tilde{b} = 12345679 - 12345678 = 1$.
  Wahre Differenz: $a - b = 12345678.5 - 12345678.0 = 0.5$.
  Der Fehler im Resultat ist 0.5 — gleich dem Rundungsfehler in $\tilde{a}$ bzw. $\tilde{b}$ einzeln auf Machine-Epsilon-Niveau 0.5.
- **Beispiel 2 (minimale Abweichung der Zahlen — Gegenstück) [S. 22]:**
  $$a = 12345678.4, \qquad b = 12345678.0$$
  Mit 8 signifikanten Stellen gespeichert ($12345678.4$ rundet ab!):
  $$\tilde{a} = 12345678, \qquad \tilde{b} = 12345678$$
  Subtraktion: $\tilde{a} - \tilde{b} = 12345678 - 12345678 = 0$.
  Wahre Differenz: $a - b = 12345678.4 - 12345678.0 = 0.4$.
- **Diskussion der Beispiele [S. 23]:** Die Differenz der wahren Resultate beider Beispiele ist 0.1 (0.5 vs. 0.4); die Maschinenresultate sind aber 0 in einem Fall und 1 im anderen — "which is a huge relative error. This shows how loss of significance can lead to large errors in computations, especially when the numbers being subtracted are very close to each other." (zentrale Warnung).

### Abbildungsbeschreibungen
- **Figure 4 [S. 19]:** "Bit layout of IEEE 754 HALF (16): sign (dark), exponent (medium), mantissa (light)." — Balken mit Markierungen bei Bit 1, 6, 16, d. h. 1 Sign + 5 Exponent + 10 Mantisse.
- **Figure 5 [S. 19]:** "Bit layout of IEEE 754 SINGLE (32): sign (dark), exponent (medium), mantissa (light)." — Markierungen bei Bit 1, 9, 32, d. h. 1 Sign + 8 Exponent + 23 Mantisse.
- **Figure 6 [S. 19]:** "Bit layout of IEEE 754 DOUBLE (64): sign (dark), exponent (medium), mantissa (light)." — Markierungen bei Bit 1, 12, 64, d. h. 1 Sign + 11 Exponent + 52 Mantisse.
- **Figure 7 [S. 21]:** "Absolute error for single (black, labeled SINGLE) and double (gray, dashed, labeled DOUBLE) precision as a function of the represented value $x$. The error grows linearly with $x$ and is proportional to machine epsilon for each format." — doppelt-logarithmischer Plot: x-Achse von $10^{-16}$ bis $10^{16}$, y-Achse (Absolute error) von $10^{-23}$ bis $10^{7}$; zwei parallele Geraden (SINGLE oben, DOUBLE unten gestrichelt).
- **Figure 8 [S. 23]:** "Demonstration of catastrophic loss of significance: $1/(1 + \epsilon - 1)$ vs $\epsilon$ (log-x, linear-y scale). For large $\epsilon$, the result follows $1/\epsilon$. For very small $\epsilon$, rounding error dominates and the result becomes infinite." — Plot: x-Achse $\epsilon$ von $10^{-17}$ bis $10^{-14}$ (log), y-Achse von 0 bis $2 \times 10^{16}$; Kurve fällt von "$\uparrow \infty$" (links, bei kleinen $\epsilon$ nahe $\epsilon \approx 10^{-16.5}$) hyperbelartig ab.

### Randnotizen / Fußnoten / Literatur
- **On the Edge [S. 17]:** Modelle nutzen niedrigpräzise Arithmetik, z. B. 8-Bit-Integer oder sogar binäre Gewichte und Aktivierungen.
- **Binary neural networks (BNNs) [S. 17]:** Gewichte und Aktivierungen auf $\{-1, +1\}$ beschränkt — drastische Reduktion von Speicher- und Rechenbedarf, macht aber Gleitkommadarstellung und Rundungseffekte kritisch. Fußnote 5: M. Courbariaux, Y. Bengio: "Binarynet: Training deep neural networks with weights and activations constrained to +1 or -1", *CoRR*, abs/1602.02830, 2016, http://arxiv.org/abs/1602.02830
- **Typen numerischer Darstellungen in Computern [S. 18]** (Wortlaut gegen das PDF verifiziert, Nachextraktion N2):
  - **Integer (int):** $3$
  - **Floating-point (float):** $3.3333333$ (7 Nachkommastellen)
  - **Double precision (double):** $3.3333333333333333$ (16 Nachkommastellen)
  - **Fixed-point (e.g. 4-digits):** $3.3333$ (4 Nachkommastellen)
- **Impossible? [S. 18]:** "Mathematical annotation helps us with period: $3.\overline{3}$." (Periodenschreibweise.)
- Fußnote 6 [S. 19]: IEEE Computer Society: "IEEE standard for floating-point arithmetic", https://ieeexplore.ieee.org/document/4610935, August 2008. IEEE Std 754-2008 (Revision von IEEE Std 754-1985).
- **Die größte Zahl in single precision [S. 20]:** ist ca. $10^{38}$, gesetzt durch den größten Exponenten $e = +127$; der Dezimalexponent 38 kommt von $\log_{10}(2^{128}) \approx 38.5$.
- **Remember (SI-Präfixe) [S. 20]:** mega ($10^6$), giga ($10^9$), tera ($10^{12}$), peta ($10^{15}$), exa ($10^{18}$), zetta ($10^{21}$), yotta ($10^{24}$), ronna ($10^{27}$), quetta ($10^{30}$); **kein offizielles SI-Präfix** für $10^{33}$.
- **Konkrete Epsilon-Werte [S. 20]:** Für IEEE 754 single precision: $\varepsilon_{\text{mach}} \approx 1.19 \times 10^{-7}$; double precision: $\varepsilon_{\text{mach}} \approx 2.22 \times 10^{-16}$.
- **Absolute precision [S. 20]:** "is just about to become clear, $1 : 2 = 0.5$ but $10 : 2 = 5$. Same number of steps (relative precision), but gaps of 0.5 vs 5." (Veranschaulichung relative vs. absolute Präzision.)
- **Precision [S. 21]:** Mit Skalierungsfaktor $10^{-6}$ ist die kleinste darstellbare Differenz $0.000001$. Der maximale Rundungsfehler ist ein halber Schritt: $0.5 \times 10^{-6} = 0.0000005$.
- **Infinity [S. 22]:** "in mathematics there is an infinity between 0 and 1. The difference between something and nothing." (philosophische Randbemerkung zum Unterschied Ergebnis 0 vs. 1.)
- **Code [S. 23]:** https://github.com/Quillstacks/lecturecode_numericalmethods.git
- **Is double enough? [S. 23]** mit Fußnote 7: D. Blochinger: *Numerische Methoden – Foliensatz*, Zentrum für Angewandte Ökonomik (ZAÖ), DHBW Ravensburg, 2025. URL https://www.economicon.de/repository/index.html. Illustration: Prof. Dr. Daniel Blochinger. Lizenz: CC BY-NC-SA 4.0. Stand: 28. Mai 2025. Weitere Materialien: https://www.economicon.de/repository/index.html
- **What happens for $a > b$? [S. 23]:** "Think along the lines of significant digits." (Denkanstoß/Grenzfall: entlang signifikanter Stellen denken.)

### Übungsaufgaben & Selbstreflexionsfragen
- **Hands on machine epsilon (Übung) [S. 23]:** Vor dem Gang an die Maschine überlegen, wie man das Machine Epsilon eines beliebigen Systems für ein spezifisches Gleitkommaformat per Programm bestimmen würde. Definition von Machine Epsilon wiederholen, Gedanken als Pseudocode notieren. "What would such a program show when run on a fixed-point system vs a floating-point system?" Dann verschiedene Typen am eigenen Rechner in Code ausprobieren, Beobachtungen notieren und reflektieren. Frage (mit Fußnote 7): "When you would build a calculator, which type would you choose and why?" (Wenn man einen Taschenrechner bauen würde, welchen Typ würde man wählen und warum?)
- **Loss of significance example (Übung) [S. 23]:** Überlegen, wie man Auslöschung auf der eigenen Maschine demonstrieren würde; Pseudocode notieren, bevor man weiterliest.
- **Reason about (Denkaufgabe) [S. 23]:** wie das Berechnen von $f(\epsilon) = 1/(a + \epsilon - b)$ für kleines $\epsilon$ und $a = b$ den Zweck erfüllen würde. "What do you expect to see when $\epsilon$ is very small?"
- **Self-Reflection [S. 24]:**
  - "How is floating-point representation structured, and what are its components?" (Wie ist die Gleitkommadarstellung strukturiert, was sind ihre Komponenten?)
  - "What is machine epsilon, and how does it relate to numerical precision?" (Was ist Machine Epsilon und wie hängt es mit numerischer Präzision zusammen?)
  - "How do these concepts impact numerical computations in practice?" (Wie wirken sich diese Konzepte praktisch auf numerische Berechnungen aus?)

### Recap of Key Concepts [S. 24]
- Gleitkommadarstellung erlaubt Computern, einen weiten Bereich reeller Zahlen mit endlich vielen Bits zu speichern, führt aber Rundungsfehler ein.
- Machine Epsilon quantifiziert die kleinste darstellbare Differenz in Gleitkomma-Arithmetik und beeinflusst die Präzision numerischer Berechnungen.
- Auslöschung (loss of significance) tritt beim Subtrahieren nahezu gleicher Zahlen auf, verstärkt Rundungsfehler und führt zu ungenauen Resultaten.
- **Knowing what can go wrong (Überleitung zu Kapitel 3):** Wir sind nah dran zu verstehen, wie wir definieren, was gut ist, und die Qualität unserer Methoden. "We now know that there is a true function $f$ and an approximated function $\hat{f}$, further we have a true input $x$ and a rounded input $\tilde{x}$. These effect and characterize our numerical methods." (Notation: wahre Funktion $f$, approximierte Funktion $\hat{f}$; wahre Eingabe $x$, gerundete Eingabe $\tilde{x}$.)

### Teaser [S. 24]
- Randnotiz: "Can you think of metrics for numerical methods, based on the approximations and errors we discussed?" (Metriken für numerische Methoden auf Basis der diskutierten Approximationen/Fehler? — Brücke zu Kapitel 3.)

---

## Thema 3: Error Analysis (S. 25–34)

### Motivation / The Why — "Some call it Error. I call it Character." [S. 25]
- Versionszeile des Kapitels: *2026-04-29 · lively date Hase*.
- **Kernsatz:** Konditionierung, Stabilität, Konsistenz und Konvergenz (Conditioning, Stability, Consistency and Convergence) sind fundamentale Konzepte der numerischen Analysis, die helfen, das Verhalten numerischer Algorithmen und ihre Zuverlässigkeit beim Lösen mathematischer Probleme zu verstehen.
- **Understanding Concepts** — um Verhalten und Charakteristika numerischer Methoden zu beschreiben, wollen wir:
  - Die Sensitivität gegenüber kleinen Änderungen in den Eingabedaten einschätzen (assess) — bezogen auf das Problem.
  - Die Sensitivität der numerischen Lösung gegenüber kleinen Änderungen in den Eingabedaten bewerten (evaluate) — bezogen auf die Methode.
  - Sicherstellen, dass numerische Methoden genaue und reproduzierbare Resultate liefern.
  - Garantieren, dass unsere Approximationen zur wahren Lösung konvergieren.
- **Bezug ML/AI:** Besonders beim Training großer Modelle auf riesigen Datensätzen ist Verständnis dieser Konzepte entscheidend. Training neuronaler Netze und anderer Modelle bedeutet großskalige Optimierungsprobleme, oft mit iterativen numerischen Methoden. "In Deep Learning convergence has the center stage, then almost as an afterthought comes Complexity – the number of operations and amount of time it takes to get there." (Im Deep Learning steht Konvergenz im Zentrum; fast als Nachgedanke folgt die Komplexität — Anzahl Operationen und benötigte Zeit.) Allgemein lassen sich AI-Modelle $\theta$ später genau mit diesen Konzepten bewerten und beschreiben. "So the maths aside, this will come in handy."

### Hands On Experience — Conditioning & Stability intuitiv [S. 26–28]
- Einstieg: intuitives Gefühl für die Konzepte mit einfachen Beispielen; je Konzept **zwei** schnelle Übungen (von Hand oder im Kopf) — "as we want to highlight two sides of the same coin for each concept, introducing somewhat extremes on the spectrum." Rückgriff auf das diskretisierte Sinus-Beispiel aus Kapitel 1.
- **Conditioning (Konditionierung), intuitiv:** "is about how sensitive the solution is to small changes in the input data." — Annahme: approximierte Funktion = wahre Funktion (Sinus), aber $\tilde{x}$ ist eine leicht gestörte Version von $x$ durch Messfehler oder Rundung ($\pm 0.25$). Betrachtung der zwei grauen Bänder (Figure 9): Bei $x = -1.5$ (nahe Minimum) ist die Region **gut konditioniert** (well-conditioned) — kleine Änderungen in $x$ führen zu kleinen Änderungen in $f(x)$. Das Band um $x = 0$ ist **schlecht konditioniert** (ill-conditioned) — kleine Änderungen in $x$ können zu großen relativen Änderungen in $f(x)$ führen.
- **Stability (Stabilität), intuitiv:** "refers to the sensitivity of the numerical solution to the small changes in the input data." — Beobachtung am grauen Band um $x = 0$: Bei Schrittweite $h = 0.2$ (Figure 10) folgen die diskretisierten Punkte der Sinuskurve eng — das zeigt eine **Instabilität** gegenüber Änderungen $\tilde{x} \pm 0.25$, mit Fluktuationen in den berechneten Werten $\hat{f}(\tilde{x})$. Im Kontrast zeigt die Diskretisierung mit $h = 1$ (Figure 11, [S. 27]) nur einen einzigen diskretisierten Punkt im grauen Band — führt zu einer **stabilen** Approximation der Sinuskurve in dieser Region, unabhängig von den Abweichungen in $\tilde{x}$. (Pointe: gröbere Diskretisierung = stabiler, aber weniger konsistent!)
- **Consistency (Konsistenz), intuitiv [S. 27]:** "quantifies how well our numerical method matches the exact solution of the original problem." Zur Veranschaulichung: Diskretisierung mit Schrittweite $h = 1$ und mit $h = 0.2$ (Figures 12–13). Beobachtung: Für infinitesimal kleine Schrittweiten $h \to 0$ kommen die diskretisierten Punkte der wahren Sinuskurve immer näher — am Ende perfekte Übereinstimmung zwischen numerischer Methode und exakter Lösung: **optimale Konsistenz**.
- **Convergence (Konvergenz), intuitiv [S. 27–28]:** entsteht, wenn wir die Ideen von Stabilität und Konsistenz kombinieren. "A numerical method is convergent if, as we refine our approximation $\hat{f}(x)$ (for example, by decreasing the step size $h$), the computed solution approaches the exact solution of the problem regardless of the deviations in $\tilde{x}$, or by implicitly accounting for them." (Eine numerische Methode ist konvergent, wenn beim Verfeinern der Approximation die berechnete Lösung sich der exakten Lösung nähert — unabhängig von Abweichungen in $\tilde{x}$ oder indem diese implizit berücksichtigt werden.)

### Lernziele (Learning Objectives) Kapitel 3 [S. 28]
1. Intuition über die Konzepte Konditionierung, Stabilität, Konsistenz und Konvergenz in numerischen Methoden haben.
2. Einfache numerische Probleme quantitativ bezüglich dieser Konzepte analysieren.

(Rest der Seite 28 leer.)

### Definitionen & Notation — Quantitative Characterization of Numerical Methods [S. 29]
- **Notation:** $f(\cdot)$ bezeichnet die exakte (analytische) Lösung eines Problems; $\hat{f}(\cdot)$ die numerische Methode (Algorithmus), die eine Approximation liefert. $x$ steht für die exakten Eingabedaten, $\tilde{x}$ für die tatsächlich verwendeten Eingabedaten, die z. B. durch Messfehler oder Rundung gestört sein können.
- **Definition Conditioning (Konditionierung):** beschreibt, wie sensitiv die Lösung eines Problems auf kleine Änderungen der Eingabedaten reagiert. Formal kann die Konditionierung eines Problems bei $x$ durch die Konditionszahl (condition number) $\kappa$ quantifiziert werden, Gleichung (13):
  $$\kappa = |f(x) - f(\tilde{x})| \quad (13)$$
  "$\kappa$ is often normalized to express it as a relative measure." ($\kappa$ wird oft normalisiert, um es als relatives Maß auszudrücken.)
- **Definition Stability (Stabilität):** gegeben, wenn kleine Fehler in der Eingabe oder in Zwischenschritten nicht zu unverhältnismäßig großen Fehlern in der Ausgabe führen. Mathematisch stellt eine stabile Methode sicher, dass der Fehler in der berechneten Lösung $\hat{f}(\tilde{x})$ durch ein konstantes Vielfaches des Fehlers in den Eingabedaten beschränkt bleibt, Gleichung (14):
  $$\left|\hat{f}(\tilde{x}) - \hat{f}(x)\right| \leq s \cdot |\tilde{x} - x| \quad (14)$$
  wobei $s$ eine Konstante ist. "For $s \approx 1$, the error in the computed solution develops linearly with the error in the input data." (Für $s \approx 1$ entwickelt sich der Fehler der berechneten Lösung linear mit dem Eingabefehler.)
- **Definition Consistency (Konsistenz):** wie gut die numerische Lösung die exakte Lösung des Originalproblems approximiert, Gleichung (15):
  $$\left|\hat{f}(x) - f(x)\right| \leq c \quad (15)$$
  wobei $c$ eine Konstante ist, die den Konsistenzfehler quantifiziert.
- **Definition Convergence (Konvergenz):** bezieht sich allgemein darauf, dass unsere Approximation einen spezifischen stabilen Grenzwert erreicht. Eine Methode ist konvergent, wenn, Gleichung (16):
  $$\left|\hat{f}(\tilde{x}) - f(x)\right| \to \lim \quad (16)$$
  "That is, as both the real solution is approximated and deviations in data are controlled by an error margin." (sowohl die Annäherung an die echte Lösung als auch Abweichungen in den Daten werden durch eine Fehlerschranke kontrolliert.)

### Durchgerechnete Beispiele — quantitative Analyse am Sinus-Beispiel [S. 30–33]
- **Aufgabenstellung [S. 30]:** Minimum der Sinusfunktion auf $[-3,1]$ erneut; Diskretisierung mit zwei Schrittweiten $h = 1$ und $h = 0.2$. Annahme: Eingabe $x$ gestört durch $\tilde{x} = x \pm 0.25$ (Messfehler), Präzision: zwei Dezimalstellen. Analysiere Konditionierung, Stabilität, Konsistenz und Konvergenz der numerischen Methode in beiden Fällen; quantifiziere mit den Formeln des vorigen Abschnitts.
- **Conditioning [S. 30–31]:** unabhängig von der verwendeten numerischen Methode — beschreibt die Sensitivität des Problems selbst. Analyse rein über die Wirkung kleiner Änderungen in $x$ auf $\sin(x)$. Um $x = -1$ (nahe Minimum) ist der Sinus relativ flach ⇒ gute Konditionierung; zum Vergleich $x = 0$, wo der Sinus sich schnell ändert ⇒ schlechte Konditionierung. Rechnungen:
  $$\kappa(-1, +0.25) = |\sin(-1) - \sin(-0.75)| \approx |-0.8415 - (-0.6816)| = 0.1599$$
  $$\kappa(-1, -0.25) = |\sin(-1) - \sin(-1.25)| \approx |-0.8415 - (-0.9489)| = 0.1074$$
  ⇒ Gute Konditionierung (well-conditioning) mit $0.1074 \leq \kappa \leq 0.1599$.
  $$\kappa(0, +0.25) = |\sin(0) - \sin(0.25)| \approx |0 - 0.2474| = 0.2474$$
  $$\kappa(0, -0.25) = |\sin(0) - \sin(-0.25)| \approx |0 - (-0.2474)| = 0.2474$$
  ⇒ [S. 31] Schlechte Konditionierung (ill-conditioning) mit $\kappa \approx 0.2474$. [Anm. zur PDF-Schreibweise, S. 31: Original druckt "ill-conditioning with κ ≤ 0.247" — numerisch unsauber, da der berechnete Maximalwert $0.2474$ beträgt (korrekt: $\kappa \approx 0.2474$ bzw. $\leq 0.25$); zudem belegt eine obere Schranke allein keine schlechte Konditionierung.]
- **Stability [S. 31], Gleichung (17):** hängt von der numerischen Methode ab (Diskretisierung + Minimumsuche). Für $h = 1$: Methode stabil — kleine Änderungen in $\tilde{x}$ führen zu kleinen Änderungen in $\hat{f}(\tilde{x})$. Für $h = 0.2$: weniger stabil — kleine Änderungen in $\tilde{x}$ können größere Fluktuationen in $\hat{f}(\tilde{x})$ verursachen. Quantifizierung über die Konstante $s$ in der Stabilitätsungleichung:
  $$\left|\hat{f}(\tilde{x}) - \hat{f}(x)\right| \leq s \cdot |\tilde{x} - x| \quad (17)$$
  "Due to symmetry we only consider the case $\tilde{x} = x + 0.25$." (Aus Symmetriegründen nur Fall $\tilde{x} = x + 0.25$.)
  - **Für $h = 1$ (bei $x = -1$):**
    $$s_{h=1,\,x=-1} \cdot |\tilde{x} - x| = |\hat{f}(\tilde{x}) - \hat{f}(x)| = |\hat{f}_1(-0.75) - \hat{f}_1(-1)| = |\hat{f}_1(-1) - \hat{f}_1(-1)| \quad \text{(siehe Randnotiz A)}$$
    $$s_{h=1,\,x=-1} \approx 0 \div 0.25 \approx 0$$
    [Korrektur ggü. Original, S. 31: PDF druckt in derselben Rechnung einen Indexwechsel "$s_{h=1,x=-1}$ → $s_{h=1,x=0}$"; gemeint ist durchgängig derselbe Fall ($\tilde{x} = x + 0.25$, $x = -1$). Das Ergebnis $s \approx 0$ ist korrekt.]
  - **Für $h = 0.2$ (bei $x = -1$):**
    $$s_{h=0.2,\,x=-1} \cdot |\tilde{x} - x| = |\hat{f}(\tilde{x}) - \hat{f}(x)| = |\hat{f}_{0.2}(-0.75) - \hat{f}_{0.2}(-1)| = |\hat{f}_{0.2}(-0.8) - \hat{f}_{0.2}(-1)| = |-0.71736 - (-0.84147)|$$
    $$s_{h=0.2,\,x=-1} = 0.12411 \div 0.25 \approx 0.4964$$
  - **Warnung (Stolperfalle):** "Be aware that stability has anomalies in border regions of the discretization. This is especially a problem for piece-wise constant approximations." (Stabilität hat Anomalien in Randregionen der Diskretisierung — besonders ein Problem für stückweise konstante Approximationen.)
- **Consistency [S. 31–32], Gleichung (18):** bestimmt durch Vergleich der numerischen Lösung $\hat{f}(x)$ mit der exakten Lösung $f(x)$ für das Minimum des Sinus in $[-3,1]$. Quantifizierung der Konstante $c$:
  $$\left|\hat{f}(x) - f(x)\right| \leq c \quad (18)$$
  - **Für $h = 1$ [S. 32]:**
    $$c_1 \geq \left|\hat{f}_1\left(-\tfrac{\pi}{2}\right) - f\left(-\tfrac{\pi}{2}\right)\right| \geq \left|\hat{f}_1(-1) - f\left(-\tfrac{\pi}{2}\right)\right| \geq |-0.84147 - (-1)| \geq 0.15853$$
  - **Für $h = 0.2$ [S. 32]:**
    $$c_{0.2} \geq \left|\hat{f}_{0.2}\left(-\tfrac{\pi}{2}\right) - f\left(-\tfrac{\pi}{2}\right)\right| \geq \left|\hat{f}_{0.2}(-1.2) - f\left(-\tfrac{\pi}{2}\right)\right| \geq |-0.93204 - (-1)| \geq 0.06796$$
    [Korrektur ggü. Original, S. 32: PDF druckt $-0.94898$ (= $\sin(-1.25)$) und $0.05102$; aber $-1.25$ ist kein Gitterpunkt des $h=0.2$-Gitters. Korrekt ist $\hat{f}_{0.2}(-1.2) = \sin(-1.2) = -0.93204$, damit $c_{0.2} \geq |-0.93204 - (-1)| = 0.06796$.]
  - **Befund:** "Consistency improves with smaller step sizes, as expected." (Konsistenz verbessert sich mit kleineren Schrittweiten — wie erwartet; $c_1 = 0.15853$ vs. $c_{0.2} = 0.06796$; die qualitative Aussage bleibt auch mit dem korrigierten Wert richtig, da $0.06796 < 0.15853$.)
- **Convergence [S. 32], Gleichung (19):** kombiniert die Ideen von Stabilität und Konsistenz. Quantifizierung über den Gesamtfehler zwischen numerischer Lösung $\hat{f}(\tilde{x})$ und exakter Lösung $f(x)$:
  $$\left|\hat{f}(\tilde{x}) - f(x)\right| \quad (19)$$
  Aus Symmetriegründen nur $\tilde{x} = x + 0.25$.
  - **Für $h = 1$:**
    $$\left|\hat{f}_1(\tilde{x}) - f(x)\right| = \left|\hat{f}_1(-1) - f\left(-\tfrac{\pi}{2}\right)\right| = \left|\hat{f}_1(-0.75) - f\left(-\tfrac{\pi}{2}\right)\right| = \left|\hat{f}_1(-1) - f\left(-\tfrac{\pi}{2}\right)\right| = |-0.84147 - (-1)| = 0.15853$$
  - **Für $h = 0.2$:**
    $$\left|\hat{f}_{0.2}(\tilde{x}) - f(x)\right| = \left|\hat{f}_{0.2}(-1.2) - f\left(-\tfrac{\pi}{2}\right)\right| = \left|\hat{f}_{0.2}(-0.95) - f\left(-\tfrac{\pi}{2}\right)\right| = \left|\hat{f}_{0.2}(-1) - f\left(-\tfrac{\pi}{2}\right)\right| = |-0.84147 - (-1)| = 0.15853$$
    [Korrektur ggü. Original, S. 32: PDF druckt in beiden Fällen den Endwert "= 0.1599"; korrekt ist $|-0.84147 - (-1)| = 0.15853$. Zudem fehlen im PDF in den Umformungsketten die verbindenden Relationszeichen (die Zeilen stehen ohne Gleichheitszeichen gestapelt untereinander), und im $h=0.2$-Block steht einmal fälschlich $\hat{f}_1(-1.2)$ statt $\hat{f}_{0.2}(-1.2)$.]
- **Konvergenz-Diskussion [S. 33]:** Wegen der Stabilitätsprobleme im Fall $h = 0.2$ verbessert sich die Konvergenz in diesem Operationspunkt **nicht** mit kleineren Schrittweiten. Zwei Erkenntnisse: Beide numerischen Lösungen konvergieren zum gleichen Grenzwert; daraus lässt sich auch sagen, dass die Methode des iterativen Verkleinerns der Schrittweite $h$ ebenfalls zum gleichen Grenzwert konvergiert. "Notice that we use the characteristics for both a numerical solution and the numerical method." (Begriffsdifferenzierung: Die Charakteristika werden sowohl für eine numerische Lösung als auch für die numerische Methode verwendet.)

### Abbildungsbeschreibungen
- **Figure 9 [S. 26]:** "Continuous curve $\hat{f}(x) = \sin(x)$ on $[-3,1]$ with two highlighted transparent vertical bands at $x = -1.5$ and $x = 0$ (width 0.5)." — Sinuskurve mit zwei grauen vertikalen Bändern.
- **Figure 10 [S. 26]:** "Continuous curve $f(x)_{.2} = \sin(x)$ on $[-3,1]$ with a highlighted transparent vertical band at $x = 0$ (width 0.5), and discretized points with step size $h = 0.2$." — Sinuskurve mit dichten schwarzen Punkten.
- **Figure 11 [S. 27]:** "Continuous curve $f(x)_{1.} = \sin(x)$ on $[-3,1]$ with a highlighted transparent vertical band at $x = 0$ (width 0.5), and discretized points with step size $h = 1$." — Sinuskurve mit wenigen Punkten.
- **Figure 12 [S. 27]:** "Bar plot of discretized values $f(x)_{1.} = \sin(x)$ on $[-3,1]$ with step size $h = 1$." — Balkendiagramm (stückweise konstante Approximation), grobe Balken.
- **Figure 13 [S. 27]:** "Bar plot of discretized values $f(x)_{.2} = \sin(x)$ on $[-3,1]$ with step size $h = 0.2$." — Balkendiagramm mit feinen Balken.

### Randnotizen / Fußnoten / Literatur
- **One last word on model error [S. 25]:** "With $f(\cdot)$ we imply the exact model of a system. In practice, models are simplifications of reality, for a distance between two points A and B we might use a simplified Manhattan or Euclidean model that does not account for terrain, mode of travel, or obstacles. So keep in mind that our $f(\cdot)$ here, is another $f(\cdot)$." (Warnung Modellfehler; Beispiel Manhattan-/euklidische Distanz ohne Terrain, Reisemodus, Hindernisse.)
- **Deep Learning by Goodfellow [S. 25]:** "does a great job kick-starting you into numerical computation (Ch. 4) for machine learning. Check it out for further reading:" — I. Goodfellow, Y. Bengio, A. Courville: *Deep Learning*, MIT Press, 2016, http://www.deeplearningbook.org (Kapitelhinweis: Kap. 4, numerical computation).
- **This is about floating-point representation [S. 26]:** "and not about step size or optimal approximation. Make sure to wrap your head around that, before moving on." (Wichtige Abgrenzung/Stolperfalle beim Conditioning-Beispiel mit gestörtem $\tilde{x}$.)
- **Intuitive convergence example with sine, wanted [S. 27]:** "If you have a better idea to have the examples stick to the sine context, let me know." (Anmerkung des Autors — Werkstattcharakter.)
- **Hat versus tilde [S. 29]** (Merkhilfe): "The hat $\hat{}$ marks the numerical method (algorithm), while the tilde $\tilde{}$ marks a perturbed input. So $\hat{f}(\tilde{x})$ reads as: numerical method evaluated on perturbed input data."
- **Convergence (non-zero) [S. 29]:** "usually aims for zero error margin, which is often the exact solution $f(x)$. However, often we will experience non-zero convergence. If the method converges to a value different from $f(x)$, this indicates a systematic error (bias) in the method." (Konvergenz gegen einen von $f(x)$ verschiedenen Wert zeigt einen systematischen Fehler/Bias der Methode an.)
- **Stability (Übungsaufgabe) [S. 31]:** "equals the conditioning of the system, for $h \to 0$. Show it." (Stabilität entspricht der Konditionierung des Systems für $h \to 0$ — zeigen! Beweisaufgabe.)
- **A) [S. 31]:** "See how the step size $h = 1$ leads to the same function value at both points. For reference, Fig. 12." (Erklärung des Rechenschritts $\hat{f}_1(-0.75) = \hat{f}_1(-1)$ — stückweise konstant.)
- **Remember [S. 31]:** "the analytical solution of min(sin(x)) on $[-3,1]$ – revisit Chapter 1." (= $-1$ bei $x = -\pi/2$.)
- **Code [S. 33]:** https://github.com/Quillstacks/lecturecode_numericalmethods.git

### Übungsaufgaben & Selbstreflexionsfragen
- **Hands on compute-driven error analysis (Übung) [S. 33]:** Brute-Force-Fehleranalyse des Zwei-Gleichungs-Systems aus Kapitel 1: "You will determine and optimize the conditioning, stability, consistency, and convergence of the numerical solution by optimizing the numerical method." (Konditionierung, Stabilität, Konsistenz, Konvergenz der numerischen Lösung bestimmen und durch Optimierung der numerischen Methode verbessern.)
- **Self-Reflection [S. 33]:**
  - "Compared to the numerical solution to the minimum of the sine function, how well conditioned is the two-equation system?" (Wie gut konditioniert ist das Zwei-Gleichungs-System verglichen mit dem Sinus-Minimum?)
  - "Does stability converge with smaller step sizes in the two-equation system? Against what?" (Konvergiert die Stabilität mit kleineren Schrittweiten? Gegen was?)
  - "How do perturbations in the input data affect the numerical solution of the two-equation system? Is there an interplay with step size?" (Wirkung von Eingabestörungen; Zusammenspiel mit der Schrittweite?)
  - "Compare convergence with stability and consistency. What do you observe? Can you express your observations in terms of bias and variance?" (Vergleich; Beobachtungen in Begriffen von Bias und Varianz ausdrücken — ML-Begriffe!)
  - "For ever smaller step sizes, do you observe a limit to the accuracy of the numerical solution? If so, why?" (Grenze der Genauigkeit bei immer kleineren Schrittweiten? Warum?)
  - "What is another problem you observe while refining the step size?" (Welches weitere Problem beim Verfeinern der Schrittweite?)

### Recap of Key Concepts [S. 33]
- "Conditiioning [sic], Stability, Consistency, and Convergence" — Konditionierung, Stabilität, Konsistenz und Konvergenz sind fundamentale Konzepte der numerischen Analysis zum Verständnis des Verhaltens numerischer Algorithmen.
- Diese Konzepte können qualitativ und quantitativ ausgedrückt werden, um numerische Lösungen und Methoden zu analysieren.

### Teaser / Überleitung [S. 33–34]
- Randnotiz Teaser [S. 33]: "So far we did brute-force numerical solutions. Can you think of a way to refine brute-force methods to get better results with less effort? Use the code of this lecture to design and test your idea." (Brute-Force-Methoden verfeinern für bessere Resultate mit weniger Aufwand; mit dem Vorlesungscode designen und testen.)
- Überleitung [S. 34] (wörtlich): "Now that we understand and can characterize the behavior of individual numerical solutions, we can move on to understanding how to analyze entire numerical methods and algorithms. So far we have taken the assumption of where to look for a solution, inside a specific interval, for granted. This is usually not a given, and we will need to move away from local optimization methods in the next lecture." (Rest der Seite leer.)

---

## Thema 4: Newton Methods (S. 35–46)

### Motivation / The Why — "A Step in the Right direction." [S. 35]
- Versionszeile des Kapitels: *2026-04-05 · regal coconut Wachtel*.
- Rückblick: Im vorigen Kapitel wurden numerische Methoden mit Konditionierung, Stabilität, Konsistenz und Konvergenz charakterisiert. Aber die Brute-Force-Gittersuche ist fundamental begrenzt: "it explores the solution space blindly, requiring $O(N^d)$ evaluations for $N$ grid points in $d$ dimensions." (Sie erkundet den Lösungsraum blind und benötigt $O(N^d)$ Auswertungen für $N$ Gitterpunkte in $d$ Dimensionen — Komplexitätsangabe, Fluch der Dimensionalität!)
- **Schlüsselidee (The key insight)** — "is deceptively simple: instead of asking 'what is the value here?' at every grid point, we also ask 'which way should I go next?'. The function's slope, its derivative, tells us the direction towards the solution. This transforms search fundamentally." (Statt an jedem Gitterpunkt nur "Was ist hier der Wert?" zu fragen, fragen wir auch "In welche Richtung soll ich als Nächstes gehen?". Die Steigung/Ableitung zeigt die Richtung zur Lösung — das transformiert die Suche fundamental.)
- **Nutzen dieser Methoden:**
  - Lokale Information nutzen, um anspruchsvolle Schritte statt Brute-Force-Suchen zu machen.
  - Schnellere und optimalere Konvergenz erreichen.
- **Bezug ML/Deep Learning:** "In Machine Learning and Deep Learning, Newton's method simplified to first order is also known as gradient descent. One could argue that the entire field of deep learning is built on the idea of using local gradient information to navigate toward minima in a high-dimensional loss landscape, to train models that are optimized towards specific objectives." (Newtons Methode, auf erste Ordnung vereinfacht, ist als Gradientenabstieg/gradient descent bekannt; das gesamte Feld Deep Learning baut auf lokaler Gradienteninformation zur Navigation in hochdimensionalen Loss-Landschaften auf.)

### Hands On Experience — Grid Search vs. Newton (Nullstellensuche) [S. 36–37]
- Intuitives Gefühl für die Kraft lokaler Information: Vergleich Grid Search vs. Newtons Methode an derselben Sinusfunktion aus Kapitel 3, nun **Nullstellensuche**: $\sin(x) = 0$ auf $[2.5, 4]$ ("the solution is near $\pi \approx 3.14159$").
- **Grid Search** auf $[2.5, 4]$ mit Schritt $h = 0.3$ "evaluates blindly" (vollständige Werte):
  $$f(2.5) \approx 0.599$$
  $$f(2.8) \approx 0.335$$
  $$f(3.1) \approx 0.042 \quad \leftarrow \text{am nächsten an null (closest to zero)}$$
  $$f(3.4) \approx -0.256$$
  $$f(3.7) \approx -0.530$$
  $$f(4.0) \approx -0.757$$
  Ergebnis: "We found $x \approx 3.1$ with 6 evaluations, with an error $|3.1 - \pi| \approx 0.042$."
- **Newtons Methode** hat einen adaptiven Suchansatz: An jedem Punkt werden Funktion und Ableitung ausgewertet; diese lokale Information wird genutzt, um einen Schritt Richtung Lösung zu machen.
- **Ableitung als Quelle lokaler Information:** $f'(x) = \cos(x)$ gibt die Steigung der Tangente an einem Punkt. [S. 37] Es gibt mehrere Wege, diese Information zu nutzen, um Richtung und Größe des nächsten Schritts abzuleiten: "We for sure want to move in the direction where the function decreases, then we could take a step with fixed size, or we could make the step size proportional to the derivative. Let's just take the next guess where the tangent crosses zero for now – which is the solution to the linear approximation of $f$ at $x_n$." (Sicher in Richtung fallender Funktion bewegen; dann Schritt fester Größe ODER Schrittgröße proportional zur Ableitung; hier zunächst: nächste Schätzung dort, wo die Tangente die Null kreuzt — die Lösung der linearen Approximation von $f$ bei $x_n$.)
- **Newton von Hand am Sinus, Start bei $x_0 = 3.5$ [S. 37]:**
  $$x_1 = x_0 - \frac{\sin(x_0)}{\cos(x_0)} = 3.5 - \frac{-0.351}{-0.936} = 3.5 - 0.375 = 3.125$$
  $$x_2 = 3.125 - \frac{\sin(3.125)}{\cos(3.125)} = 3.125 - \frac{0.01659}{-0.99986} \approx 3.125 + 0.0166 \approx 3.1416$$
  [Korrektur ggü. Original, S. 37: PDF druckt im $x_2$-Schritt "$\frac{0.0008}{-0.9999}$"; tatsächlich ist $\sin(3.125) \approx 0.01659$ und $\cos(3.125) \approx -0.99986$. Das Endergebnis $x_2 \approx 3.14159$ stimmt, der gedruckte Zwischenwert nicht.]
  $$x_3 \approx 3.14159, \quad \text{und } \sin(3.14159) \approx 0$$
- Fazit: "After just 2 iterations, to be fair this means 4 function/derivative evaluations, we have $x \approx 3.14159$ with error $< 10^{-5}$. The derivative told us where to look way more efficiently than we have been used to." (Vergleich: Grid Search 6 Auswertungen, Fehler 0.042 vs. Newton 4 Auswertungen, Fehler $< 10^{-5}$.)

### Lernziele (Learning Objectives) Kapitel 4 [S. 37]
1. Newton-Raphson-Iteration für Nullstellensuche (root finding) in 1D herleiten und anwenden.
2. Taylor-Entwicklung (Taylor expansion) und ihre Rolle in Newtons Methode herleiten und verstehen ["understnad" sic im Original].
3. Konvergenzraten und Fehlermodi (failure modes) von Newtons Methode analysieren.
4. Sekantenverfahren (Secant method) verstehen und anwenden, wenn Ableitungen nicht verfügbar sind.

### Definitionen
- **Smooth (glatt) [S. 39, Randnotiz]:** "A function is smooth if it has derivatives of all orders, and is thus differentiable." (Eine Funktion ist glatt, wenn sie Ableitungen aller Ordnungen besitzt und somit differenzierbar ist.)
- **Taylor-Entwicklung (Taylor expansion) [S. 40]:** einer Funktion $f$ um einen Punkt $x_n$:
  $$f(x) = f(x_n) + f'(x_n)(x - x_n) + \frac{f''(x_n)}{2!}(x - x_n)^2 + \frac{f'''(x_n)}{3!}(x - x_n)^3 + \cdots$$
  kompakter, Gleichung (26):
  $$f(x) = \sum_{k=0}^{\infty} \frac{f^{(k)}(x_n)}{k!}(x - x_n)^k \quad (26)$$
- **Quadratische Konvergenz (quadratic convergence) [S. 42]:** Der Fehler der nächsten Iteration ist ungefähr proportional zum Quadrat des aktuellen Fehlers, $|e_{n+1}| \leq C \cdot |e_n|^2$ (Gl. (33)); $C$ ist eine Konstante, die von Krümmung und Steigung der Funktion an der Wurzel abhängt. Konvergenzordnung 2.
- **Sekantenverfahren (Secant method) / "A poor man's derivative" [S. 43]:** Ableitung nur mit Funktionsauswertungen approximieren — eliminiert den Bedarf einer expliziten Ableitung. Differenzenquotient aus den zwei jüngsten Punkten:
  $$f'(x_n) \approx \frac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}$$
  Visuell: die Steigung der Sekante durch die Punkte $(x_{n-1}, f(x_{n-1}))$ und $(x_n, f(x_n))$ auf dem Graphen von $f$. Hinweis: Es werden **zwei Startwerte** $x_0$ und $x_1$ benötigt (statt nur einem bei Newton).

### Formeln/Gleichungen & Herleitungen (mit Original-Nummern)
- **Herleitung Newton-Raphson [S. 38]:** Ziel formalisieren: finde $x^*$ mit $f(x^*) = 0$.
  - **Lineare Approximation, Gleichung (20):**
    $$f(x) \approx f(x_n) + f'(x_n) \cdot (x - x_n) \quad \text{für } x \text{ nahe } x_n \quad (20)$$
    [Korrektur ggü. Original, S. 38: PDF druckt durch einen Layoutfehler "$f(x) \approx f'(x_n) \cdot (x - x_n)$ for $x$ close to $x_n$ $+ f(x_n)$" — der Term "$+ f(x_n)$" ist hinter die Nebenbedingung gerutscht. Die korrekte Form wird durch die Folgezeile $0 = f(x_n) + f'(x_n)(x_{n+1} - x_n)$ bestätigt.]
  - **Nächste Schätzung finden:** Wir wollen, wo diese lineare Approximation null kreuzt — "because this is our best guess for where the actual function crosses zero." Approximation null setzen:
    $$0 = f(x_n) + f'(x_n) \cdot (x_{n+1} - x_n)$$
    $$f'(x_n) \cdot (x_{n+1} - x_n) = -f(x_n)$$
    $$x_{n+1} - x_n = -\frac{f(x_n)}{f'(x_n)}$$
  - **Newton-Raphson-Iterationsformel, Gleichung (21):**
    $$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \quad (21)$$
- **Taylor-Aufbau Ordnung für Ordnung [S. 39–40]:** Bisher wurde der linearen Approximation bei $x_n$ einfach vertraut, Gleichung (22):
  $$f(x) \approx f'(x_n)(x - x_n) + f(x_n) \quad (22)$$
  um schnell die nächste Schätzung $x_{n+1}$ zu finden — "but is that trust well placed?" Die Antwort liegt in der Taylor-Entwicklung, "a fundamental tool that tells us how well polynomials approximate smooth functions at a given point." Herleitung von Grundprinzipien (first principles); Illustration: schrittweise Approximation der Sinusfunktion.
  - **0. Ordnung — Funktionswert matchen, Gleichung (23):** Gesucht Polynom $P(x)$, das $f(x)$ nahe $x_n$ approximiert; Start: am Punkt selbst übereinstimmen:
    $$P(x_n) = f(x_n) \quad (23)$$
    "This comes very close to what grid search does: it only looks at the function value at discrete points, without any information about how the function behaves between those points." (Analogie Grid Search ↔ 0. Ordnung.)
  - **1. Ordnung — erste Ableitung matchen, Gleichung (24):** Nahe $x_n$ zählt die Steigung; gewünscht $P'(x_n) = f'(x_n)$:
    $$P(x) = f(x_n) + f'(x_n)(x - x_n) \quad (24)$$
  - **2. Ordnung — zweite Ableitung matchen, Gleichung (25) [S. 40]:** "The curvature captures how the slope changes." (Die Krümmung erfasst, wie sich die Steigung ändert); gewünscht $P''(x_n) = f''(x_n)$:
    $$P(x) = f(x_n) + f'(x_n)(x - x_n) + \frac{f''(x_n)}{2}(x - x_n)^2 \quad (25)$$
  - **n-te Ordnung:** allgemeines Muster ⇒ Taylor-Entwicklung, Gl. (26) (s. Definitionen).
- **Why linear is enough for Newton? [S. 41]:** "We want to solve $f(x^*) = 0$, not compute $f(x)$ as best as we can. Improving an approximation of course comes with a cost: We need to compute higher derivatives and evaluate more complex polynomials. In numerical computations we always need to decide where to cut off the Taylor series. We do so at some finite order, and the linear term is the first non-constant term that gives us directional information." (Bessere Approximation kostet; die Taylor-Reihe muss bei endlicher Ordnung abgeschnitten werden; der lineare Term ist der erste nicht-konstante Term mit Richtungsinformation.)
- **Herleitung der Konvergenzrate [S. 41–42]:** Erinnerung Kapitel 3: Eine Methode ist konvergent, wenn die Approximation einen spezifischen stabilen Grenzwert erreicht. Für Newtons Methode mit Wurzel $x^*$, $f(x^*) = 0$, wollen wir, Gleichung (27):
  $$|x_n - x^*| \to 0 \quad \text{für } n \to \infty \quad (27)$$
  Dank Taylor-Entwicklung lässt sich quantifizieren, **wie schnell** der Fehler abnimmt. Sei $e_n = x_n - x^*$ der Fehler bei Iteration $n$. Taylor 2. Ordnung von $f$ um die wahre Wurzel $x^*$, Gleichung (28):
  $$f(x_n) = f(x^*) + f'(x^*)(x_n - x^*) + \frac{f''(\xi)}{2}(x_n - x^*)^2 \quad (28)$$
  wobei $\xi$ ein Punkt zwischen $x_n$ und $x^*$ ist (Lagrange-Restglied-Form). Da $f(x^*) = 0$, vereinfacht sich das zu, Gleichung (29):
  $$f(x_n) = f'(x^*) \cdot e_n + \frac{f''(\xi)}{2}e_n^2 \quad (29)$$
  **Newton-Formel anwenden:**
  $$e_{n+1} = x_{n+1} - x^* = x_n - \frac{f(x_n)}{f'(x_n)} - x^* = (x_n - x^*) - \frac{f(x_n)}{f'(x_n)} = e_n - \frac{f(x_n)}{f'(x_n)}$$
  Vereinfachte Taylor-Entwicklung für $f(x_n)$ einsetzen, Gleichung (30):
  $$e_{n+1} = e_n - \frac{f'(x^*) \cdot e_n + \frac{f''(\xi)}{2}e_n^2}{f'(x_n)} \quad (30)$$
  **Für Punkte nahe $x^*$:** Annahme $f'(x_n) \approx f'(x^*)$, Gleichung (31):
  $$e_{n+1} \approx e_n - \frac{f'(x^*) \cdot e_n + \frac{f''(\xi)}{2}e_n^2}{f'(x^*)} = e_n - e_n - \frac{f''(\xi)}{2f'(x^*)}e_n^2 \quad (31)$$
  [S. 42] … wodurch sich der Fehlerterm erster Ordnung aufhebt und übrig bleibt, Gleichung (32):
  $$e_{n+1} \approx -\frac{f''(\xi)}{2f'(x^*)}e_n^2 \quad (32)$$
  **Abstrakter, Gleichung (33):**
  $$|e_{n+1}| \leq C \cdot |e_n|^2 \quad (33)$$
  "This is quadratic convergence." (Das ist quadratische Konvergenz.)
- **Sekantenverfahren, Gleichung (34) [S. 43]:** Einsetzen des Differenzenquotienten in Newtons Formel liefert die iterative Sekantenmethode:
  $$x_{n+1} = x_n - f(x_n) \cdot \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})} \quad (34)$$

### Algorithmen (wortgetreu)
- **Algorithmus 1: Newton-Raphson Method [S. 38]:**
  ```
  Require: Initial guess x0, function f, derivative f′, tolerance ε
  1: x ← x0
  2: while |f(x)| > ε do
  3:     Compute derivative: d ← f′(x)
  4:     if |d| < ε_machine then
  5:         error "Derivative too small"
  6:     end if
  7:     Update: x ← x − f(x)/d
  8: end while
  return x
  ```
  (Im PDF steht Zeile 8 als "end whilereturn x" — Layoutartefakt für "end while; return x".)
- **Algorithmus 2: Secant Method [S. 43]:**
  ```
  Require: Initial guesses x0, x1, function f, tolerance ε
  1: while |f(x1)| > ε do
  2:     Compute secant slope: s ← (f(x1) − f(x0))/(x1 − x0)
  3:     Store previous: x_old ← x1
  4:     Update: x1 ← x1 − f(x1)/s
  5:     x0 ← x_old
  6: end while
  return x1
  ```
  (Im PDF Zeile 6 als "end whilereturn x1" — Layoutartefakt.)

### Failure Modes (Fehlermodi) von Newtons Methode [S. 42]
- "Newton's method can fail in several ways, which we will endure for now, and for which we will find solutions later on. As a brain teaser, it is a nice exercise to visualize the failure modes in this plot." (Denksportaufgabe: Failure Modes im Plot von Figure 21 visualisieren.) Drei Fehlermodi:
  1. **Nullableitung (zero derivative):** wenn $f'(x_n) = 0$, ist die Tangente horizontal und kreuzt die Achse nicht.
  2. **Oszillation:** besonders bei symmetrischen Funktionen kann Newton zwischen Punkten zykeln.
  3. **Mehrdeutige Startpunktwahl:** $x_0$ beeinflusst stark, welche Wurzel gefunden wird.
- "Now something we can not endure, is if we can't compute $f'(x)$." (Was wir nicht ertragen können: wenn $f'(x)$ nicht berechnet werden kann — Überleitung zum Sekantenverfahren.)

### Durchgerechnete Beispiele
- **$\sqrt{2}$-Beispiel (Tabelle 2) [S. 42]:** Berechnung von $\sqrt{2}$ mit Newton, Start $x_0 = 2$ ("our introductory example"; Querbezug auf Figure 16 mit $f(x) = x^2 - 2$ — ein expliziter früherer $\sqrt{2}$-Bezug taucht im Text vorher nicht auf). Tabellenunterschrift: "Newton's method for computing $\sqrt{2}$. See how the error approximately squares each iteration."

  | $n$ | $x_n$ | $\|e_n\|$ (Fehler) |
  |---|---|---|
  | 0 | 2.000000000 | $5.86 \times 10^{-1}$ |
  | 1 | 1.500000000 | $8.58 \times 10^{-2}$ |
  | 2 | 1.416666667 | $2.45 \times 10^{-3}$ |
  | 3 | 1.414215686 | $2.12 \times 10^{-6}$ |
  | 4 | 1.414213562 | $\approx 1.6 \times 10^{-12}$ |

  [Korrektur ggü. Original, S. 42: PDF druckt in Zeile $n=4$ $|e_4| = 4.5 \times 10^{-12}$ — das ist das Residuum $|x_4^2 - 2|$, nicht der Fehler $|x_4 - \sqrt{2}| \approx 1.6 \times 10^{-12}$ (Spaltendefinition!). Zudem Zeile $n=3$: korrekt $|e_3| = 2.12 \times 10^{-6}$ (PDF: $2.13 \times 10^{-6}$). Übrige Zeilen korrekt.]

- **Newton by hand [S. 44]:** Wurzel von $f(x) = x^3 - x = 0$ — erst geometrisch, dann von Hand. "The roots are at $x = -1, 0, 1$. Let's find the root at $x = 1$ starting from $x_0 = 1.4$." Taylor 1. Ordnung um $x_n$:
  $$f(x) \approx f(x_n) + f'(x_n)(x - x_n), \qquad f(x_n) \approx f(x) - f'(x_n)(x - x_n)$$
  Mit $f(x) = x^3 - x = 0$, $f'(x) = 3x^2 - 1$; umstellen für die nächste Schätzung ab $x_0 = 1.4$ (vollständige korrekte Rechnung):
  $$x_1 = x_0 - \frac{f(x_0)}{f'(x_0)} = x_0 - \frac{x_0^3 - x_0}{3x_0^2 - 1} = 1.4 - \frac{2.744 - 1.4}{5.88 - 1} = 1.4 - \frac{1.344}{4.88} \approx 1.1246$$
  $$x_2 = 1.1246 - \frac{1.1246^3 - 1.1246}{3(1.1246)^2 - 1} \approx 1.1246 - \frac{0.2977}{2.7942} \approx 1.0181$$
  $$x_3 = 1.0181 - \frac{1.0181^3 - 1.0181}{3(1.0181)^2 - 1} \approx 1.0181 - \frac{0.0372}{2.1096} \approx 1.0005$$
  "The root at $x = 1$ is found quickly." — Die korrekte Newton-Folge $1.4 \to 1.1246 \to 1.0181 \to 1.0005$ konvergiert monoton von oben gegen die Wurzel $x = 1$.
  [Korrektur ggü. Original, S. 44: PDF druckt die Kette $1.127 \to 0.976 \to 1.014$ mit u. a. falschem Zähler $0.432$ statt $\approx 0.305$ (selbst mit dem PDF-Wert $x_1 = 1.127$ wäre $f(1.127) \approx 0.3044$); die gedruckte Folge springt dadurch fälschlich unter die Wurzel und scheint um 1 zu oszillieren, tatsächlich konvergiert Newton hier monoton von oben. Methodik (Gl. (21)) korrekt.]
- **Secant by hand [S. 44–45]:** Sekantenverfahren auf dasselbe Problem ($f(x) = x^3 - x$) mit $x_0 = 1.2$, $x_1 = 1.4$ anwenden — "Again first geometrically, then by hand."
  Korrekte Funktionswerte: $f(1.2) = 1.2^3 - 1.2 = 0.528$ und $f(1.4) = 1.4^3 - 1.4 = 1.344$. Damit, Gl. (34):
  $$x_2 = x_1 - f(x_1) \cdot \frac{x_1 - x_0}{f(x_1) - f(x_0)} = 1.4 - 1.344 \cdot \frac{1.4 - 1.2}{1.344 - 0.528} = 1.4 - 1.344 \cdot \frac{0.2}{0.816} \approx 1.0706$$
  Weitere Schritte sind entsprechend mit den korrekten Werten neu zu rechnen.
  [Korrektur ggü. Original, S. 45: PDF druckt mehrere falsche Zahlenwerte — $f(1.2) = 0.128$ (korrekt: 0.528) und $f(1.4) = 0.744$ (korrekt: 1.344) — und darauf aufbauend die Iterationskette $x_2 = 1.4 - (0.744) \cdot \frac{0.2}{0.616} \approx 1.4 - 0.241 \approx 1.159$ sowie $x_3 = 1.159 - (0.283) \cdot \frac{-0.241}{0.283 - 0.744} \approx 1.159 - 0.283 \cdot 0.522 \approx 1.159 - 0.148 \approx 1.011$. Die gedruckte Kette (1.159, 1.011) beruht vollständig auf den falschen Werten; die Methodik (Gl. (34)) ist korrekt.]

### Abbildungsbeschreibungen
- **Figure 14 [S. 36]:** "Continuous curve $f(x) = \sin(x)$ on $[2.5, 4]$, and discretized points with step size $h = 0.3$." — fallende Sinuskurve mit Punkten.
- **Figure 15 [S. 36]:** "Newton's method iterations: starting from $x_0 = 3.5$, converging rapidly to $\pi \approx 3.14159$." — Kurve mit markierten Punkten: $x_0$ | 1st eval (bei 3.5, unterhalb der Achse), $x_1$ | 2nd eval und $x_2$ | 3rd eval (nahe 3.1–3.2/$\pi$).
- **Figure 16 [S. 38]:** "Newton's method geometric intuition: For $f(x) = x^2 - 2$, the tangent line at $(x_0, f(x_0))$ intersects the $x$-axis at $x_1$, our next approximation." — Parabel auf ca. $[1.3, 2.2]$ (y ca. $-2$ bis $2$), Tangente gestrichelt bei $(x_0, f(x_0))$ mit $x_0 = 2$, $f(x_0) = 2$; Schnittpunkt mit der Achse bei ca. 1.5.
- **Figure 17 [S. 39]:** "Continuous curve $f(x) = \sin(x)$ and its discretized version (black dots) on $[-3,1]$ with step size $h = 1$." [Anm.: Bildunterschrift erwähnt Punkte; abgebildet ist primär die durchgezogene Sinuskurve.]
- **Figure 18 [S. 40]:** "Continuous curve $f(x) = \sin(x)$ with constant approximation $P(x) = f(-1)$ (black dashed line) anchored at $x = -1$ (black dot)." — horizontale gestrichelte Linie bei $\approx -0.84$.
- **Figure 19 [S. 40]:** "Continuous curve $f(x) = \sin(x)$ with linear approximation $P(x) = f(-1) + f'(-1)(x+1)$ (black dashed tangent line) anchored at $x = -1$ (black dot)." — Tangente.
- **Figure 20 [S. 40]:** "Continuous curve $f(x) = \sin(x)$ with quadratic approximation $P(x) = f(-1) + f'(-1)(x+1) + \frac{f''(-1)}{2}(x+1)^2$ (black dashed parabola) anchored at $x = -1$ (black dot)." — Parabel schmiegt sich an.
- **Figure 21 [S. 42]:** "$f(x) = x^3 - x$ has multiple roots. Newton's method can fail in several ways: zero derivative (if $f'(x_n) = 0$, the tangent is horizontal and doesn't cross the axis), oscillation (especially for symmetrical functions Newton can cycle between points), and ambiguous starting point selection ($x_0$, heavily influences which root is found)." — Kubik auf ca. $[-0.4, 1.4]$, Nullstellen-Punkte bei 0 und 1 markiert.
- **Figure 22 [S. 43]:** "Secant method: the line through $(x_0, f(x_0))$ and $(x_1, f(x_1))$ gives the next approximation $x_2$." — Kurve ($x^2 - 2$-artig) mit Sekante (gestrichelt) durch $(x_0, f(x_0))$ bei $x_0 \approx 1$ und $(x_1, f(x_1))$ bei $x_1 = 2$; offener Kreis beim Achsenschnitt ($x_2 \approx 1.33$/1.35).
- **Figure 23 [S. 44]:** "$f(x) = x^3 - x$ has multiple roots. We assume the root at $x = 1$ is the target. The gray dashed line shows the derivative $f'(x) = 3x^2 - 1$." — Kubik (schwarz) und Ableitung (grau gestrichelt, Parabel) auf $[-0.4, 1.4]$; Punkt bei $x = 1$; offener Kreis bei $x_0 = 1.4$.

### Randnotizen / Fußnoten / Literatur
- **Backpropagation [S. 35]:** "is of course as vital to distribute gradient information through the layers of a neural network, but the core optimization step is still a form of gradient-based navigation." (vital zur Verteilung der Gradienteninformation durch die Schichten; der Kern-Optimierungsschritt bleibt gradientenbasierte Navigation.)
- **We pay for this sophistication [S. 36]:** "with more hyperparameters that we need to determine and more complex computations (derivative evaluation and division), but we gain in convergence speed." (Trade-off: mehr Hyperparameter und komplexere Berechnungen, aber Gewinn an Konvergenzgeschwindigkeit.)
- **"Newton-Rhapson" [sic] [S. 37]:** "because Isaac Newton came up with the general idea, while Joseph Raphson simplified the approach into a practical iterative method." (historische Anmerkung; korrekte Schreibweise "Raphson".)
- **Note [S. 38]:** Diese lineare Approximation ist die Taylor-Entwicklung erster Ordnung von $f$ um $x_n$. Auf Taylor-Entwicklungen kommen wir zurück, wenn Genauigkeit und Approximation formal untersucht werden.
- **This error [S. 39]:** "occurs when the derivative $f'(x_k)$ approaches zero, which would cause division by zero or numerical instability in Newton's method." (bezieht sich auf den Fehlerfall "Derivative too small" in Algorithmus 1.)
- **Why divide by 2? [S. 40]:** "When we differentiate $(x - x_n)^2$ twice, we get 2. So if we want $P''(x_n) = f''(x_n)$, we need to divide by 2 to cancel this factor." (Begründung der Fakultätsfaktoren.)
- **Around a point [S. 40]:** "Visually we can see that the approximations are anchored on a specific point $x_n$. The Taylor expansion is a local approximation." (Die Taylor-Entwicklung ist eine lokale Approximation.)
- **Notice the assumption play out [S. 41]:** "$10^{-1} \to 10^{-2} \to 10^{-3} \to 10^{-6} \to 10^{-12}$. Once we're close enough and our assumptions hold (after iteration 2), the error squares perfectly, demonstrating quadratic convergence." (Beispielfolge der Fehlerentwicklung — anfangs nicht quadratisch, erst wenn nah genug!)
- **This can happen because [S. 42]** (Gründe, warum $f'$ nicht verfügbar sein kann):
  - "The derivative is expensive to compute." (Ableitung teuer zu berechnen.)
  - "The function is given as a black box (e.g., a simulation)." (Funktion als Black Box, z. B. Simulation.)
  - "The function isn't differentiable everywhere." (Funktion nicht überall differenzierbar.)
- **Code [S. 44]:** https://github.com/Quillstacks/lecturecode_numericalmethods.git

### Übungsaufgaben & Selbstreflexionsfragen
- **Geometrical Failure Search (Übung) [S. 45]:** "Find starting points $x_0$ for different failure modes: One where Newton's method fails due to zero derivative, one where it converges to a non-target root, and one where it oscillates between points." (Startpunkte für drei Fehlermodi finden.)
- **Enter the machine (Übung) [S. 45]:** Konvergenz und Konvergenzraten von Grid-Search, Newton und Sekantenverfahren in Python betrachten. Mit verschiedenen Startpunkten experimentieren ["differentstarting points" sic] und Failure Modes in der Praxis beobachten. "Try to first find the starting points geometrically, then try finding them analytically, before finally moving over to verifying in code."
- **Self-Reflection [S. 45–46]:**
  - "What is the main advantage of using Newton's method over Grid-Search?" (Hauptvorteil Newton vs. Grid Search?)
  - "Why is a linear approximation sufficient for finding roots? What does the Taylor expansion tell us about this choice?" (Warum genügt lineare Approximation? Was sagt Taylor dazu?)
  - "Why is quadratic convergence so powerful? How many iterations would Newton need to go from error $10^{-1}$ to error $10^{-16}$?" (Anm. Pass 3: Antwort implizit ca. 4 Iterationen wegen Quadrierung.)
  - [S. 46] "In what situations would you prefer Secant over Newton? Why not in others?" (Wann Secant statt Newton bevorzugen?)

### Recap of Key Concepts [S. 46]
- "Newton-Raphson gives (limited) convergence guarantees near simple roots." (Newton-Raphson gibt begrenzte Konvergenzgarantien nahe einfacher Wurzeln/simple roots.)
- "Taylor expansion provides a systematic way to approximate functions locally." (Taylor-Entwicklung: systematischer Weg, Funktionen lokal zu approximieren.)
- "You saw how Taylor expansion justifies the linear approximation in Newton's method and explains its quadratic convergence and allows to estimate the error in each iteration." (Taylor rechtfertigt die lineare Approximation, erklärt die quadratische Konvergenz und erlaubt Fehlerschätzung je Iteration.)
- "In situations where the derivative is difficult to compute, the Secant method approximates the derivative from two points and converges." (Sekantenverfahren approximiert die Ableitung aus zwei Punkten und konvergiert.)

### Teaser / Überleitung [S. 46]
- **Local methods find local solutions:** "Newton converges to whatever optimum is nearby, it is also prone to oscillate between points, or diverge if the derivative is zero or near zero. In the next chapter, we will reformulate the root finding into an optimization problem. And from there we'll explore how to go on and handle global optimization when the landscape has many valleys or is otherwise pathologically difficult." (Newton konvergiert zum nächstgelegenen Optimum; nächstes Kapitel: Nullstellensuche als Optimierungsproblem, dann globale Optimierung.)
- Randnotiz Teaser: "How can we make sure that we find the global solution, and not just a local one?" (Wie sicherstellen, dass die globale und nicht nur eine lokale Lösung gefunden wird?)

---

## Thema 5: Global Optimization (S. 47–56)

### Motivation / The Why — "And then there were many." [S. 47]
- Versionszeile des Kapitels: *2026-05-06 · feisty cranberry Hermelin*.
- Rückblick: Im vorigen Kapitel wurden Newtons Methode und Gradientenabstieg für Nullstellensuche entwickelt. "The methods we learned about are local methods: They converge to whatever solution is nearby. But what if the nearby solution is bad? Or if another solution is much better but farther away?" (Lokale Methoden konvergieren zur nächstgelegenen Lösung — was, wenn diese schlecht ist oder eine viel bessere weiter entfernt liegt?)
- **"Time to do away with oversimplifications."** In diesem Kapitel:
  - Shekel's Foxholes kennenlernen, eine klassische Testfunktion für globale Optimierung.
  - Kurz zeigen, wie man ein Optimierungsproblem als Nullstellenproblem (root-finding problem) formulieren kann.
  - Strategien zum Finden globaler Minima einführen.
- **Bezug ML/Deep Learning:** "In machine learning and especially deep learning, understanding multi-dimensional and global optimization is crucial for training large models effectively, and to make them converge, and actually learn something useful. Neural network loss landscapes [Fußnote 8] are highly non-convex, do have flat regions, and contain many local minima, making optimization challenging." (Loss-Landschaften neuronaler Netze sind hochgradig nicht-konvex, haben flache Regionen und viele lokale Minima.)

### Hands On Experience — Shekel's Foxholes [S. 48–50]
- **Definition Shekel's Foxholes [S. 48]:** klassische Testfunktion für globale Optimierung mit kontrollierter Multimodalität (controlled multimodality). In 1D einfache Form, Gleichung (35):
  $$f(x) = -\sum_{i=1}^{m} \frac{c_i}{(x - a_i)^2 + r_i} \quad (35)$$
  wobei $a_i$ die "Foxhole"-Positionen sind, $c_i$ die Tiefe jedes Lochs steuert und $r_i$ die Breite. Durch Anpassen dieser Parameter lässt sich eine Landschaft mit mehreren lokalen Minima und einem globalen Minimum erzeugen — "an ideal playground for testing optimization algorithms."
- **Konkretes Beispiel mit drei Foxholes [S. 48]:**
  $$f(x) = -\frac{1}{(x-0)^2 + 0.7} - \frac{1.7}{(x-4)^2 + 0.2} - \frac{1.1}{(x-7)^2 + 0.4}$$
- **Das globale Minimum** liegt bei $x = 4$; die anderen beiden Minima bei $x = 0$ und $x = 7$ sind lokale Minima. "This information is of course not available to us when we run an optimization algorithm. We only see the function values and gradients at the points we evaluate. But the knowledge comes in handy for exploring the behavior of optimization methods."
- **Sensitivität gegenüber Anfangsbedingungen** von $x_0$: "If we start Newton's method near $x = 0$ or $x = 7$, we'll converge to a local minimum, not the global one at $x = 4$."
- **Anwendung:** Newtons Methode auf die 1D-Shekel-Funktion (Fußnote 9) von verschiedenen Startpunkten anwenden und beobachten, wohin die Methode konvergiert. "Let's show it for one starting point, try another one yourself, and then we will discuss the general behavior." (Übungsaufforderung.)
- **Newton auf Shekel von $x_0 = 7.2$ [S. 49] (vollständige Rechnung):** Newtons Methode konvergiert zum lokalen Minimum bei $x \approx 7$. Um Newton für Optimierung anzuwenden, lösen wir das Nullstellenproblem auf $f'(x) = 0$ — Reformulierung des Optimierungsproblems. Das **Newton-Update** wird, Gleichung (36):
  $$x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)} \quad (36)$$
  Die Ableitungen vereinfachen sich zu (vollständige Formeln):
  $$f'(x) = \frac{2x}{(x^2 + 0.7)^2} + \frac{3.4(x-4)}{((x-4)^2 + 0.2)^2} + \frac{2.2(x-7)}{((x-7)^2 + 0.4)^2}$$
  $$f'(7.2) \approx 0.005 + 0.100 + 2.27 = 2.38$$
  (Anm. gemäß Errata: Die Summanden ergeben arithmetisch 2.375; das PDF rundet zulässig auf 2.38 — keine Korrektur erforderlich.)
  $$f''(x) = \frac{2(0.7 - 3x^2)}{(x^2 + 0.7)^3} + \frac{3.4(0.2 - 3(x-4)^2)}{((x-4)^2 + 0.2)^3} + \frac{2.2(0.4 - 3(x-7)^2)}{((x-7)^2 + 0.4)^3}$$
  $$f''(7.2) \approx -0.002 - 0.091 + 7.23 = 7.14$$
  Newton-Schritte:
  $$x_1 = 7.2 - \frac{2.38}{7.14} \approx 6.87, \qquad x_2 \approx 7.02, \qquad x_3 \approx 7.00$$
- **Kernbeobachtung [S. 49]:** "See how root finding methods can be used for optimization by applying them to the derivative of the function. The derivative $f'(x)$ is zero at extrema, so at this point we find minima or maxima." (Nullstellenverfahren für Optimierung durch Anwendung auf die Ableitung; an Extrema ist $f'(x)$ null — gefunden werden Minima ODER Maxima!)
- **Das fundamentale Problem [S. 50]:** "Here, we were unlucky, and the method is attracted to the nearby foxhole at $x^\circ \approx 7$." — "The fundamental problem however is that local optimization only guarantees finding a nearby extrema. Even with convergence guarantees, we would have got lucky starting from $x_0 = 3$, but from $x_0 = -2$ or $x_0 = 8$, we miss the global minima. Enough motivation for the global optimization strategies we'll discuss next." (Lokale Optimierung garantiert nur das Finden naher Extrema; von $x_0 = 3$ Glück, von $x_0 = -2$ oder $x_0 = 8$ wird das globale Minimum verfehlt.)

### Lernziele (Learning Objectives) Kapitel 5 [S. 50]
1. Erklären, warum lokale Methoden das Finden globaler Minima nicht garantieren können.
2. Strategien zum Finden globaler Extrema anwenden.
3. Verstehen, wie Gradientenabstieg (gradient descent) hilft, die Optimierung Richtung Minima zu lenken.

(Rest der Seite 50 leer.)

### Definitionen — Global Optimization Strategies [S. 51–53]
- **Lokale Optimierung (Local optimization) [S. 51], Gleichung (37):** findet ein nahes Minimum:
  $$\mathbf{x}^* = \arg\min_{\mathbf{x} \in \mathcal{N}(\mathbf{x}_0)} f(\mathbf{x}) \quad (37)$$
  wobei $\mathcal{N}(\mathbf{x}_0)$ eine Nachbarschaft (neighborhood) des Startpunkts ist.
- **Globale Optimierung (Global optimization) [S. 51], Gleichung (38):** findet das beste Minimum:
  $$\mathbf{x}^* = \arg\min_{\mathbf{x} \in \Omega} f(\mathbf{x}) \quad (38)$$
  wobei $\Omega$ die gesamte Suchdomäne ist. "It is easy to see how the search domain can be inifinitely [sic] large." (Die Suchdomäne kann unendlich groß sein.)
- **Convexity is the dividing line (Konvexität als Trennlinie) [S. 51]:** "For convex problems, any local method will find the global optimum. The difficulty arises in non-convex optimization, where the landscape contains multiple local minima, saddle points, and plateaus." (Für konvexe Probleme findet jede lokale Methode das globale Optimum; schwierig ist nicht-konvexe Optimierung mit mehreren lokalen Minima, Sattelpunkten/saddle points und Plateaus.)
- **Random Restarts [S. 51]:** die einfachste globale Strategie — "in its notion it feels like brute-forcing again." (fühlt sich im Ansatz wieder wie Brute-Forcing an; Algorithmus 3, s. u.)
- **Basin Hopping [S. 52]:** erkundet die Landschaft durch Abwechseln von lokaler Optimierung und zufälligen Sprüngen. "This is different from random restarts, which completely resets the search. Basin hopping allows us to escape local minima while still leveraging local optimization to find better solutions." (Anders als Random Restarts, das die Suche komplett zurücksetzt; erlaubt Entkommen aus lokalen Minima bei weiterer Nutzung lokaler Optimierung; Algorithmus 4, s. u.) Die Sprungverteilung (jump distribution) wird als $\delta \sim \mathcal{D}$ spezifiziert — z. B. eine bei null zentrierte Gauß-Verteilung oder eine Gleichverteilung über einen bestimmten Bereich.
- **Simulated Annealing [S. 52]:** kombiniert Basin Hopping mit einem probabilistischen Akzeptanzkriterium für Kandidatenpunkte. "In the beginning, when hopping into a worse solution, it is accepted with probability $\exp^{-\Delta f / T}$, where $T$ (temperature) decreases over time. Later on, the algorithm becomes more conservative and only accepts candidate points that improve the objective, allowing it to converge to an optimum." (Anfangs wird ein Sprung in eine schlechtere Lösung mit Wahrscheinlichkeit $\exp^{-\Delta f / T}$ akzeptiert; $T$ (Temperatur) nimmt über die Zeit ab; später nur noch verbessernde Kandidaten ⇒ Konvergenz zu einem Optimum.)
- **Stochastic methods (stochastische Methoden) [S. 52]:** fügen Rauschen hinzu, indem die Loss-Landschaft approximiert wird, um lokalen Optima zu entkommen. Beispielaufgabe: "Let's approximate the 1D shekels function as a second order function by picking three points on the foxhole curve." (1D-Shekel-Funktion als Funktion zweiter Ordnung approximieren durch Wahl dreier Punkte auf der Foxhole-Kurve.)
- **The take away [S. 52–53]:** "the loss landscape is not static, but is to be engineered and formed. By approximating the loss landscape on mini-batches (different selection of points), we get a noisy estimate of the true loss landscape, which can help us escape local minima. The loss landscape is then of course heavily influenced by the choice of the loss function itself. That being said, the Newton step is very sensitive to noise, we will see other approaches that deal better with this." (Die Loss-Landschaft ist nicht statisch, sondern kann konstruiert und geformt werden; Mini-Batch-Approximation liefert eine verrauschte Schätzung der wahren Loss-Landschaft und hilft, lokalen Minima zu entkommen; der Newton-Schritt ist allerdings sehr rauschempfindlich.)
- **Patience [S. 51]:** üblicher Hyperparameter der $K$-Heuristik — kontrolliert, wie viele Restarts ohne Verbesserung abgewartet werden, bevor gestoppt wird.

### Newton's Method for finding Minima [S. 53]
- Im Hands-on gesehen: Reformulierung von Optimierung als Nullstellensuche erlaubt Newtons Methode zum Finden von Optima, Gleichung (40):
  $$x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)} \quad (40)$$
- **Minima, Maxima und Sattelpunkte:** Newtons Methode (auf $f'$ angewandt) findet Punkte mit $f'(x) = 0$ [Korrektur ggü. Original, S. 53: PDF druckt "Newton's method finds points where $f''(x) = 0$"; sachlich findet Newton auf $f'$ Punkte mit $f'(x) = 0$ (Extremstellen); der anschließende Second-Derivative-Test klassifiziert sie über $f''$], aber diese können Minima, Maxima oder Sattelpunkte sein. Der **Test der zweiten Ableitung (second derivative test)** unterscheidet:
  - (a) $f''(x^*) > 0$: lokales Minimum ("curve bends upward" — Kurve biegt nach oben)
  - (b) $f''(x^*) < 0$: lokales Maximum ("curve bends downward" — Kurve biegt nach unten)
  - (c) $f''(x^*) = 0$: nicht schlüssig ("inconclusive — possible saddle point or inflection point" — möglicher Sattelpunkt oder Wendepunkt)
- **Newton Richtung Minima lenken** — modifiziertes Update, Gleichung (41):
  $$x_{n+1} = x_n - \frac{f'(x_n)}{|f''(x_n)|} \quad (41)$$
  "In this way we ensure that we always move in the direction of decreasing $f(x)$. This forces the step to always move in the direction of the negative gradient (downhill so to speak)." (So bewegt sich der Schritt immer in Richtung abnehmenden $f(x)$ — stets in Richtung des negativen Gradienten, "downhill".)

### Algorithmen (wortgetreu)
- **Algorithmus 3: Random Restarts [S. 51]:**
  ```
  Require: Search domain Ω, local optimizer LocalOptimize, restarts K
  1: x_best ← None; f_best ← +∞
  2: for k = 1 to K do
  3:     x0 ← RandomPoint(Ω)
  4:     x* ← LocalOptimize(x0)
  5:     if f(x*) < f_best then
  6:         x_best ← x*; f_best ← f(x*)
  7:     end if
  8: end for
  9: return x_best
  ```
- **Algorithmus 4: Basin Hopping [S. 52]:**
  ```
  Require: Initial point x0, local optimizer LocalOptimize, jump distribution for δ, iterations K
  1: x_best ← x0; f_best ← f(x0)
  2: x_current ← x0
  3: for k = 1 to K do
  4:     x* ← LocalOptimize(x_current)
  5:     if f(x*) < f_best then
  6:         x_best ← x*; f_best ← f(x*)
  7:     end if
  8:     Sample jump: δ ∼ D
  9:     x_current ← x* + δ        ▷ Random jump
  10: end for
  11: return x_best
  ```

### Formeln/Gleichungen (mit Original-Nummern)
- Gl. (35): Shekel's Foxholes (1D) [S. 48]
- Gl. (36): Newton-Update für Optimierung $x_{n+1} = x_n - f'(x_n)/f''(x_n)$ [S. 49]
- Gl. (37): lokale Optimierung $\mathbf{x}^* = \arg\min_{\mathbf{x} \in \mathcal{N}(\mathbf{x}_0)} f(\mathbf{x})$ [S. 51]
- Gl. (38): globale Optimierung $\mathbf{x}^* = \arg\min_{\mathbf{x} \in \Omega} f(\mathbf{x})$ [S. 51]
- Gl. (39): Erfolgswahrscheinlichkeit Random Restarts (s. u.) [S. 51]
- Gl. (40): Newton-Update für Minima-Suche [S. 53]
- Gl. (41): modifiziertes Update mit $|f''(x_n)|$ [S. 53]
- **Erfolgswahrscheinlichkeit Random Restarts [S. 51], Gleichung (39):** Hat das Anziehungsgebiet (basin of attraction) des globalen Minimums Wahrscheinlichkeit $p$, dann gilt mit $K$ Restarts:
  $$P(\text{find global}) = 1 - (1 - p)^K \quad (39)$$
  Zahlenbeispiel: "For $p = 0.1$ and $K = 20$: $P = 1 - 0.9^{20} \approx 0.88$." Üblicherweise ist $p$ vorab nicht bekannt. Heuristik für $K$ ohne Kenntnis von $p$: $K$ erhöhen, bis die beste Lösung sich stabilisiert (keine Verbesserung nach mehreren Restarts) — Hyperparameter **Patience**.

### Durchgerechnete Beispiele — "Let's put the strategies to work on concrete numbers" [S. 54–55]
- **Random-Restarts-Rechnung [S. 54]:** Funktion mit 5 lokalen Minima; das Anziehungsgebiet des globalen Minimums deckt 15 % der Suchdomäne ($p = 0.15$). "What is the probability of finding the global minimum with $K = 10$ random restarts?" Vollständige Rechnung:
  $$P = 1 - (1 - 0.15)^{10} = 1 - 0.85^{10} = 1 - 0.1969 = 0.803$$
  "About 80% chance, not too bad, but far from certain. How many restarts do we need for 99%?"
  $$K = \frac{\ln(1 - 0.99)}{\ln(1 - 0.15)} = \frac{\ln(0.01)}{\ln(0.85)} = \frac{-4.605}{-0.1625} \approx 28.3$$
  [S. 55] "So $K = 29$ restarts." (Also $K = 29$ Restarts.)

### Abbildungsbeschreibungen
- **Figure 24 [S. 48]:** "A 1D Shekel's foxholes function (black) with three local minima and its derivative (gray dashed). The function has valleys at $x = 0, 4, 7$, with the deepest (global minimum) at $x = 4$. The derivative (dashed line) crosses zero at each minimum." — Plotbereich $x$ von $-2$ bis $12$; tiefste Talsohle bei $x = 4$ (Funktionswert dort ca. $-8.5$; Plot-Skala bis $-5$ sichtbar).
- **Figure 25 [S. 49]:** "A 1D Shekel's foxholes function's first derivative (black), and second derivative (gray dashed). The function has valleys at $x = 0, 4, 7$, with the deepest (global minimum) at $x = 4$. The first derivative crosses zero at each minimum, and the second derivative is positive at minima (confirming local curvature)." — Plotbereich $x$ von $-2$ bis $12$.
- **Figure 26 [S. 53]:** "The original Shekel function (gray thin) with a second-order approximation (solid black) fitted through three sample points (dots). The derivative of the approximation is shown as a gray dashed line. The quadratic captures the general trend but smooths out the individual foxholes." — Parabel durch 3 Stützpunkte (ca. bei $x \approx 4, 6.5, 8.5$) über die Foxholes hinweg.
- **Figure 27 [S. 54]:** "Solid black: the first derivative $f'(x)$ of the 1D Shekel function; gray dashed: the second derivative $f''(x)$. The black marker at $x = 6.1$ is a sample location; the solid gray line is the tangent to $f'(x)$ at that point (slope $\approx -2.66$). The sign and magnitude of $f''(x)$ determine the Newton update direction and step size when solving $f'(x) = 0$."
- **Figure 28 [S. 54]:** "Solid black: the first derivative $f'(x)$; gray dashed: the absolute curvature $|f''(x)|$. Marker at $x = 6.1$ shows the same sample point as above; the solid gray line illustrates replacing $f''(x)$ by $|f''(x)|$ (slope $\approx +2.66$). Using $|f''(x)|$ in the Newton denominator removes the curvature sign, enforcing downhill steps and reducing the chance of stepping toward a local maximum."

### Randnotizen / Fußnoten / Literatur
- **Visualization of neural network loss landscapes [S. 47]:** "Li et al. (2018) shows the complex terrain of neural network optimization. Different initializations lead to different final solutions." Fußnote 8: H. Li, Z. Xu, G. Taylor, C. Studer, T. Goldstein: "Visualizing the loss landscape of neural nets", 31:6389–6399, 2018. URL https://proceedings.neurips.cc/paper_files/paper/2018/file/a41b3bb3e6b050b6c9067c67f663b915-Paper.pdf
- **The derivative [S. 48]:** "illustrated as the dashed line is the answer to formulating optimization as root finding. The minima of $f(x)$ correspond to the roots of $f'(x)$." (Schlüsselidee: Minima von $f$ entsprechen Wurzeln von $f'$.)
- Fußnote 9 [S. 48]: J. Shekel: "Test functions for multimodal search techniques", 1971.
- **Local minima notation [S. 49]:** "The asterisk (*) is conventionally reserved for global optima. To distinguish local from global minima, consider alternative notation like $x^\circ$ (x-circle) or $x_i$ for the $i$-th local minimum." (Notationskonvention.)
- **$\mathcal{N}$ is a set [S. 51]:** "of points around $\mathbf{x}_0$. For example, $\mathcal{N}(\mathbf{x}_0) = \{\mathbf{x} : \|\mathbf{x} - \mathbf{x}_0\| < \epsilon\}$ for some radius $\epsilon$."
- **Convex vs. non-convex (Definition) [S. 51]:** "A function $f$ is *convex* if $f(\lambda x + (1-\lambda)y) \leq \lambda f(x) + (1-\lambda) f(y)$ for all $\lambda \in [0,1]$. For convex functions, every local minimum is the global minimum—local methods suffice. Non-convex functions (like Shekel's foxholes or neural network loss surfaces) are the hard case."
- **Neural network initialization [S. 51]:** "and training multiple networks with different seeds is implicit random restarts. However, this is not practical for large models." (Training mehrerer Netze mit verschiedenen Seeds = implizites Random Restarts; für große Modelle nicht praktikabel.)
- **Noisy Newton [S. 52]:** "follows the same idea around hopping, by adding Gaussian noise to the Newton step: $\mathbf{x}_{n+1} = \ldots + \boldsymbol{\xi}_n$." (Gauß-Rauschen zum Newton-Schritt addieren.)
- **$\Delta f$ [S. 52]:** "is the increase in the objective function value when moving from the current solution to a worse candidate solution." (Anstieg des Zielfunktionswerts beim Übergang zu einer schlechteren Kandidatenlösung.)
- **In deep learning [S. 53]:** "we typically use local methods (SGD, Adam) but hope that: (1) most local minima are roughly equally good, (2) overparameterization makes bad minima rare, (3) mini-batch noise helps escape sharp minima, (4) adaptive learning rates help navigate plateaus." (Vier DL-Hoffnungen.)
- **How would you [S. 53]** (Übungsfrage): "modify the update to find maxima instead?" (Wie müsste das Update modifiziert werden, um stattdessen Maxima zu finden?)
- **Code [S. 54]:** https://github.com/Quillstacks/lecturecode_numericalmethods.git
- **Hint [S. 54]:** "Use $P = 1 - (1-p)^K$ and solve for $K$: $K = \frac{\ln(1-P)}{\ln(1-p)}$."
- **Basin of Attraction (Übung) [S. 55]:** "Revisit the plots of the Shekel function, mark the basins of attraction for each local minimum, and estimate their relative sizes. Which one is the global minimum? How does this relate to the probability of finding it with random restarts?"
- **Non-Convex Basins (Übung) [S. 55]:** "Shekel in general is non-convex, however the basins are, note down a function, where the basins of attraction are not so easy to map out." (Shekel ist im Allgemeinen nicht-konvex, die Basins jedoch schon; eine Funktion notieren, bei der die Basins of Attraction nicht so leicht zu kartieren sind — Gegenbeispiel konstruieren.)
- **Can you think of (Übung) [S. 55]:** "a smart way to automatically adjust the step size distribution during optimization? What would be a good heuristic to follow? How could you prevent disastrous jumps? Implement it." (Schrittweitenverteilung automatisch anpassen; Heuristik; katastrophale Sprünge verhindern; implementieren.)

### Übungsaufgaben & Selbstreflexionsfragen
- **Folgeaufgabe [S. 55]:** "Now compute $K$ for $p = 0.05$ and $p = 0.01$ at the same 99% target." ($K$ für $p = 0.05$ und $p = 0.01$ bei gleichem 99-%-Ziel berechnen.)
- **On your machine (Übung) [S. 55]:** Eigene 1D-Shekel-Funktion designen ("Keep it simple in the beginning, but come back later to make it more complex"). Erst mit den bisher gelernten lokalen Optimierungsmethoden vertraut machen und auf die eigene Funktion anwenden. "Show where Newton's method fails (again)." Verschiedene $x_0$ erkunden und Konvergenzverhalten beobachten. Wieder über Loss-Landschaft und Basin-Grenzen nachdenken.
- **Directing the search towards minima (Übung) [S. 55]:** "Remember the $|f''|$ trick, flips the sign of the curvature in the denominator, forcing the step to always go downhill. Think about what that means geometrically for the tangent line construction. Then try it in code." (Geometrische Bedeutung des $|f''|$-Tricks für die Tangentenkonstruktion durchdenken, dann im Code ausprobieren.)
- **Escaping Local Minima (Übung) [S. 55]:** Random Restarts und Basin Hopping auf der eigenen 1D-Shekel-Funktion einsetzen; vergleichen, wie viele Funktionsiterationen jede Methode zum Finden des globalen Minimums braucht. "How prone are they to getting stuck in local minima? How does the choice of the step size distribution affect basin hopping's performance?"
- **Noise and landscape engineering (Übung) [S. 55]:** "The loss landscape is not static, but is to be engineered and formed. By approximating the loss landscape on mini-batches (different selection of points)," [Anm.: Satz endet im Original abrupt mit Komma — unvollständig im PDF; Inhalt nur teilweise rekonstruierbar.]
- **Code exercise [S. 55]:** "implement random restarts and basin hopping on the 1D Shekel function. Compare how many function evaluations each method needs to find the global minimum at $x \approx 4$."
- **Finally, let's map out the basins of attraction [S. 55]:** "Consider the 1D Shekel function and assume a local optimizer always converges to the nearest foxhole.2" [Anm.: ".2" vermutlich Tippfehler/Fußnotenrest im Original — so im PDF.]
  - (a) "Sketch (roughly) the basins of attraction for the three foxholes at $x = 0, 4, 7$. Where are the basin boundaries?" (Basins of Attraction grob skizzieren; wo liegen die Basin-Grenzen?)
  - (b) "If basin hopping uses a jump of $\delta \sim \text{Uniform}(-3, 3)$ starting from the local minimum $x^\circ = 7$, what is the probability that a single jump lands in the basin of the global minimum?" (Wahrscheinlichkeit, dass ein einzelner Sprung im Basin des globalen Minimums landet?)
  - (c) "Why might basin hopping find the global minimum faster than random restarts here?" (Warum könnte Basin Hopping hier schneller sein als Random Restarts?)
- **Self-Reflection [S. 56]:**
  - "Why does local optimization fail on non-convex landscapes like Shekel's foxholes?" (Warum scheitert lokale Optimierung auf nicht-konvexen Landschaften?)
  - "How does the required effort scale withthe [sic] size of the global basin when doing random restarts?" (Skalierung des Aufwands mit der Größe des globalen Basins?)
  - "How do basin hopping differently from random restarts?" [sic — Grammatik im Original] (Wie unterscheidet sich Basin Hopping von Random Restarts?)
  - "What does $f''(x_n)$ tell us about the loss landscape, what does it characterize, and how can we put it to use?" (Was sagt $f''(x_n)$ über die Loss-Landschaft?)
  - "How does approximating the loss landscape with noisy estimates (mini-batches) help escape local optima?" (Wie hilft die Mini-Batch-Approximation beim Entkommen?)
  - "Choosing $x_0$ such that it lies in the basin of a local minimum, now find different ways such that your optimization method can escape it, how effective is what?" ($x_0$ im Basin eines lokalen Minimums; verschiedene Fluchtwege finden — wie effektiv ist was?)

### Recap of Key Concepts [S. 56]
- "Local optimization methods (like Newton's method) can get stuck in local minima on non-convex functions." (Lokale Methoden können auf nicht-konvexen Funktionen in lokalen Minima stecken bleiben.)
- "Global optimization strategies (random restarts, basin hopping, simulated annealing, stochasticity) are designed to explore the search space more broadly to find the global optimum." (Globale Strategien erkunden den Suchraum breiter.)
- "Modifying optimization methods to use curvature information $f''(x)$ allows to specify the direction of descent more accurately." (Krümmungsinformation $f''(x)$ erlaubt genauere Spezifikation der Abstiegsrichtung.)
- "The loss landscape is ours to engineer through the choice of loss function and noise, such as stochastic gradients." (Die Loss-Landschaft gehört uns zum Konstruieren — Wahl der Loss-Funktion und Rauschen, etwa stochastische Gradienten; Loss Landscape Engineering.)

### Teaser / Überleitung [S. 56]
- **Gradient descent is prone to getting stuck:** "And so far our answer was merely better than brute-forcing out way out, yet again. In the next chapter, we will learn how to smoothen loss landscape to increase the robustness of our gradient descent approach." (Bisher war die Antwort lediglich besser als Brute-Forcing; nächstes Kapitel: Glättung der Loss-Landschaft zur Erhöhung der Robustheit des Gradientenabstiegs.)
- Randnotiz Teaser: "What if we now face a high-frequency version of Shekels foxholes. What is the problem that arises?" (Hochfrequenz-Version von Shekel's Foxholes — welches Problem entsteht?)

## Thema 6: Numerical Integration (S. 57–70)

### Motivation / The Why — "Smooth Operator." [S. 57]
- Versionszeile des Kapitels: *2026-05-04 · sneaky olive Falke*.
- Rückblick: Im vorigen Kapitel globale Optimierungsstrategien zum Entkommen lokaler Minima. "Imagine you are optimizing a function with thousands of tiny, sharp local minima like a high-frequency version of Shekel's Foxholes. A gradient descent algorithm will get stuck instantly in the first microscopic pothole it finds." (Funktion mit Tausenden winziger, scharfer lokaler Minima — wie eine Hochfrequenz-Version von Shekel's Foxholes; ein Gradient-Descent-Algorithmus bliebe sofort im ersten mikroskopischen Schlagloch/pothole stecken.)
- **Die Lösung:** "one that will feel familiar, but probably did go unnoticed until now: Numerical integration." (fühlt sich vertraut an, blieb aber bisher wohl unbemerkt: numerische Integration), Gleichung (42):
  $$I = \int_a^b f(x)\,dx \quad (42)$$
- **Gute Gründe**, numerische Integration zu verstehen:
  - "as it allows us to smoothen the loss landscape and make optimization methods more robust." (Glättung der Loss-Landschaft ⇒ robustere Optimierungsmethoden.)
  - "as it tends to find more robust optima due to the averaging effect [Fußnote 10] of a region." (Findet tendenziell robustere Optima durch den Mittelungseffekt/averaging effect einer Region.)
- **Bezug Deep Learning:** "In deep learning stochastic gradient descent (SGD) is the workhorse optimization algorithm. It is a Monte Carlo [Fußnoten 11, 12] method that estimates the gradient of the loss function by averaging over the gradient of a random mini-batch of data points. We are lucky to have numerical integration around, as it would be prohibitive expensive to train models on large-scale datasets." (SGD ist der Arbeitspferd-Optimierungsalgorithmus — eine Monte-Carlo-Methode, die den Gradienten der Loss-Funktion durch Mittelung über den Gradienten eines zufälligen Mini-Batches schätzt; Training auf großskaligen Datensätzen wäre sonst prohibitiv teuer.)

### Hands On Experience — Hochfrequente Landschaften & Glättung durch Integration [S. 58–60]
- **Ausgangslage [S. 58]:** "We already know how to discretize a continuous function, and how to handle finite precision and systems with sparse information at discrete points." (Diskretisierung, endliche Präzision und Systeme mit spärlicher Information an diskreten Punkten sind bereits bekannt.)
- Die Shekel-Funktion als hochfrequente Funktion war eine Herausforderung für globale Optimierung, "yet did not render our general approaches obsolete. We still discretize and treat these functions as we are used to." (machte die generellen Ansätze aber nicht obsolet — wir diskretisieren und behandeln diese Funktionen wie gewohnt.)
- Beispielfunktion: $f(x) = \sin(x) + \sin(2\pi x)$ auf $[-3, 1]$ mit Schrittweite $h = 0.2$ (Figures 29–31).
- "Taking a closer look at any local minima shows how the high-frequency loss landscape will nudge our optimization algorithm into the nearest local minimum. For example at $x = 0.6$ or $x = -0.4$." (Die hochfrequente Loss-Landschaft stupst/nudged den Optimierungsalgorithmus ins nächstgelegene lokale Minimum — konkrete Beispielstellen $x = 0.6$ und $x = -0.4$.)
- **Glättung durch Integration — vollständiges Rechenbeispiel bei $x = -0.4$ [S. 59]:** Statt direkt zu lösen, Gleichung (43):
  $$f(-0.4) = -0.97720 \quad (43)$$
  approximieren wir den Wert durch Integration mit Breite $h = 0.2$ (Trapez über $[-0.5, -0.3]$, vollständige Rechnung). Mit $f(-0.5) = \sin(-0.5) + \sin(-\pi) = -0.47943$ und $f(-0.3) = \sin(-0.3) + \sin(-0.6\pi) = -1.24658$:
  $$h \cdot f(-0.4) \approx \int_{-0.5}^{-0.3} f(x)\,dx \approx \frac{h}{2}[f(-0.5) + f(-0.3)] \approx 0.2 \cdot \frac{-0.47943 - 1.24658}{2} \approx -0.17260$$
  $$f(-0.4) \approx \frac{-0.47943 - 1.24658}{2} \approx -0.86300$$
  [Korrektur ggü. Original, S. 59: PDF setzt $f(-0.5) = -1.14973$ und $f(-0.3) = -0.97720$ ein — das sind tatsächlich $f(-0.2)$ bzw. $f(-0.4)$ — und erhält damit $h \cdot f(-0.4) \approx -0.11285$ sowie $f(-0.4) \approx -1.06347$. Korrekt (maßgeblich): $f(-0.5) = -0.47943$, $f(-0.3) = -1.24658$, geglättet $f(-0.4) \approx -0.86300$, $h \cdot f(-0.4) \approx -0.17260$. Gl. (43) selbst ($f(-0.4) = -0.97720$) ist korrekt.]
- **Bewertung:** "This is a much better approximation having global optima in mind, than the direct evaluation at $x = -0.4$ which gave us $-0.97720$. The numerical integration gave us a correction of the local loss landscape towards higher losses at this local minima. The next figure shows the effect of this smoothing on the whole curve." (Mit Blick auf globale Optima eine viel bessere Approximation als die direkte Auswertung; die Integration korrigiert die lokale Loss-Landschaft Richtung höherer Losses an diesem lokalen Minimum.) [Anm.: Erst mit den korrigierten Werten ist die Skript-Aussage "correction … towards higher losses" konsistent ($-0.86300 > -0.97720$); mit den PDF-Werten ($-1.06347 < -0.97720$) widerspräche das Ergebnis ihr.]
- **The smoothing** "becomes even more apparent when integrating over larger intervals in general, or in our engineered example when choosing $h$ such that the frequency of the noisy signal gets averaged out." (Glättung noch deutlicher bei größeren Intervallen oder bei Wahl von $h$, sodass die Frequenz des Rauschsignals herausgemittelt wird — siehe Figure 33 mit $h = 0.48$.)
- **Überleitung zu besseren Quadraturregeln [S. 59]:** "the approximation of the interval so far is a pretty coarse approximation, relying on two points only." (Die bisherige Intervall-Approximation ist ziemlich grob — sie stützt sich auf nur zwei Punkte.)

### Lernziele (Learning Objectives) Kapitel 6 [S. 60]
1. Mittelpunktsmethode (midpoint method), Trapezregel (trapezoid rule) und Simpson-Regel (Simpson's rule) für numerische Integration herleiten und anwenden.
2. Zusammengesetzte Regeln (composite rules) für verbesserte Genauigkeit verstehen.
3. Lagrange-Interpolation kennen und wissen, wie sie mit Quadraturregeln (quadrature rules) zusammenhängt.
4. Verstehen, wie der Fluch der Dimensionalität (curse of dimensionality) Monte Carlo motiviert.
5. Monte-Carlo-Integration für hochdimensionale Probleme herleiten und anwenden.
6. Monte-Carlo-Integration anwenden und erkennen, dass Batch-Mittelung (batch averaging) in ML numerische Integration ist.

(Rest der Seite 60 leer.)

### Definitionen
- **Riemann-Summen-Approximation (Riemann sum) [S. 61]:** $[a,b]$ in $n$ Teilintervalle gleicher Breite $h$ teilen und die Beiträge jedes Intervalls summieren:
  $$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n-1} \int_{x_i}^{x_{i+1}} f(x)\,dx \approx \sum_{i=0}^{n-1} h \cdot f(m_i)$$
  wobei $x_i = a + ih$ für $i = 0, 1, \ldots, n$.
- **Mittelpunktsregel (midpoint rule) [S. 61]:** nutzt in diesen zusammengesetzten Intervallen den Mittelpunkt — den Durchschnitt der Endpunkte — jedes Intervalls; "which often gives better results than left or right endpoint methods. Intuitively, this is because the midpoint approximates the curvature of the function better on the interval." (Oft besser als Links-/Rechts-Endpunkt-Methoden, weil der Mittelpunkt die Krümmung auf dem Intervall besser approximiert.)
- **Trapezregel (trapezoid rule) [S. 62]:** Trapeze "are more expressive geometrically than rectangles, and can capture linear changes in the function between the endpoints." (Geometrisch ausdrucksstärker als Rechtecke; erfassen lineare Änderungen der Funktion zwischen den Endpunkten; Gl. (44), s. u.)
- **Simpson-Regel (Simpson's rule) [S. 63]:** "can capture curvature and thus often provides a much better approximation than the trapezoid rule. Following the idea of fitting a linear function, we fit a quadratic polynomial through 3 points instead of a line through 2. You will see Simpson's rule is exact for quadratic polynomials." (Erfasst Krümmung; quadratisches Polynom durch 3 Punkte statt Gerade durch 2; exakt für quadratische Polynome.)
- **Lagrange-Interpolation (Lagrange interpolation and quadrature) [S. 63]:** konstruiert das eindeutige Polynom vom Grad $\leq n$, das durch gegebene Stützstellen (nodes) $\{(x_j, y_j)\}_{j=0}^{n}$ verläuft, mit der Basis Gl. (45) (s. u.).
- **Runge-Phänomen (Runge's phenomenon) [S. 64, Randnotiz]:** "High-degree polynomial interpolation oscillates due to overfitting, leading to large errors at the edges of the interval." (Polynominterpolation hohen Grades oszilliert durch Overfitting — große Fehler an den Intervallrändern.)
- **Monte Carlo [S. 57, Randnotiz]:** "is a strategy which basically solves problems by random sampling. Embrace the beauty:" (Strategie, die Probleme im Wesentlichen durch zufälliges Sampling löst.)
- **i.i.d. (independent and identically distributed) [S. 65, Randnotiz]:** alle $\mathbf{X}_i$ sind unkorreliert und stammen aus derselben zugrunde liegenden Verteilung.
- **$\Omega$ / $|\Omega|$ [S. 64, Randnotiz]:** $\Omega$ ist die Integrationsdomäne, $|\Omega|$ ihre Länge. Für ein 1D-Integral über $[a,b]$: $|\Omega| = b - a$. In höheren Dimensionen: Produkt der Längen jeder Dimension.

### Formeln/Gleichungen & Herleitungen (mit Original-Nummern, Gl. 42–51)
- **Gl. (42) [S. 57]:** das bestimmte Integral $I = \int_a^b f(x)\,dx$ (s. Motivation).
- **Gl. (43) [S. 59]:** direkte Auswertung $f(-0.4) = -0.97720$ (Ausgangspunkt der Glättungsrechnung, s. Hands On).
- **Trivialste Integral-Approximation (Mittelpunkt, ein Intervall) [S. 61]:**
  $$I = \int_a^b f(x)\,dx, \qquad I = \frac{b-a}{n} \cdot f\left(\frac{a+b}{2}\right), \qquad I = h \cdot f(m)$$
  "It is easy to see that the height of the rectangle is the value at the midpoint, and the width is $h$." (Höhe des Rechtecks = Wert am Mittelpunkt $m$, Breite = $h$.)
- **Trapezregel, Gleichung (44) [S. 62]:**
  $$\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(a) + f(b)\right] \quad (44)$$
  mit $h = b - a$.
- **Composite Trapezoid Rule (zusammengesetzte Trapezregel) [S. 62] — vollständige Herleitung:** Trapezregel auf jedes Teilintervall anwenden und summieren:
  $$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n-1}\int_{x_i}^{x_{i+1}} f(x)\,dx \approx \sum_{i=0}^{n-1} \frac{h}{2}\left[f(x_i) + f(x_{i+1})\right]$$
  $$= \frac{h}{2}\left(f(x_0)+f(x_1)\right) + \frac{h}{2}\left(f(x_1)+f(x_2)\right) + \cdots + \frac{h}{2}\left(f(x_{n-1})+f(x_n)\right)$$
  $$= \frac{h}{2}\left[f(x_0) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{n-1}) + f(x_n)\right] = \frac{h}{2}\left[f(a) + 2\sum_{i=1}^{n-1} f(x_i) + f(b)\right]$$
  mit $x_i = a + ih$, $i = 0, 1, \ldots, n$.
  **Gewichtungs-Intuition:** "The function values at the endpoints $a$ and $b$ are each weighted by 1 in the formula, while all interior points are weighted by 2. Intuitively, this is because each interior point contributes to two adjacent trapezoids, while the endpoints only contribute to one trapezoid each. In your mind step through the circled enpoints [sic] in the figure above, and see how the interior points get counted twice, once as a right endpoint and once as a left endpoint, while the endpoints only get counted once." (Endpunkte Gewicht 1, innere Punkte Gewicht 2 — jeder innere Punkt trägt zu zwei benachbarten Trapezen bei.)
- **Lagrange-Basis, Gleichung (45) [S. 63]:**
  $$L_j(x) = \prod_{\substack{m=0 \\ m\neq j}}^{n} \frac{x - x_m}{x_j - x_m} \quad (45)$$
- **Allgemeine Form eines quadratischen Polynoms (durch Punkte bei $a$, $m$, $b$) [S. 63]:**
  $$f(x) = f(a)\cdot\frac{(x-m)(x-b)}{(a-m)(a-b)} + f(m)\cdot\frac{(x-a)(x-b)}{(m-a)(m-b)} + f(b)\cdot\frac{(x-a)(x-m)}{(b-a)(b-m)}$$
- **Herleitung der Simpson-Gewichte [S. 63]:** Für ein symmetrisches Intervall wird die Fläche unter $f(x)$ am besten approximiert, indem die Endpunkte Gewicht $h/6$ und der Mittelpunkt Gewicht $2h/3$ erhalten: "$A = C = h/6$, $B = 2h/3$ – we can verify this by integrating the Lagrange basis polynomials over $[a,b]$ and confirming that they yield these weights, but we omit the detailed calculation here." (Verifizierbar durch Integration der Lagrange-Basispolynome über $[a,b]$; detaillierte Rechnung im Original ausgelassen.) Im symmetrischen Intervall sind die Stützstellen äquidistant: $x_0 = a$, $x_1 = m = \frac{a+b}{2}$, $x_2 = b$, sodass der Mittelpunkt $m - a = b - m = h$ erfüllt. Somit (Simpson-Regel, einfaches Intervall):
  $$\int_a^b f(x)\,dx \approx \frac{h}{6}f(a) + \frac{2h}{3}f(m) + \frac{h}{6}f(b) = \frac{h}{6}\left[f(a) + 4f(m) + f(b)\right]$$
- **Composite Simpson's Rule (zusammengesetzte Simpson-Regel) [S. 63–64] — vollständige Herleitung:** Simpson-Regel auf jedes Paar von Teilintervallen anwenden und summieren ("assume $n$ is even and $x_i = a + ih$"). Beginnend vom Integral, mit Gitterweite $h$ und Paarbreite $2h$ (Faktor pro Paar: $2h/6 = h/3$):
  $$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n-1}\int_{x_i}^{x_{i+1}} f(x)\,dx \approx \sum_{k=0}^{n/2-1} \frac{h}{3}\left[f(x_{2k}) + 4f(x_{2k+1}) + f(x_{2k+2})\right]$$
  $$= \frac{h}{3}\left[f(x_0) + 4\sum_{k=0}^{n/2-1} f(x_{2k+1}) + 2\sum_{k=1}^{n/2-1} f(x_{2k}) + f(x_n)\right]$$
  $$= \frac{h}{3}\left[f(x_0) + 4\sum_{\substack{i=1 \\ i\text{ odd}}}^{n-1} f(x_i) + 2\sum_{\substack{i=2 \\ i\text{ even}}}^{n-2} f(x_i) + f(x_n)\right]$$
  [Korrektur ggü. Original, S. 64: PDF druckt in den Zwischenzeilen der Herleitung pro Teilintervall-Paar den Faktor "$\frac{h}{6}$"; korrekt ist bei Gitterweite $h$ und Paarbreite $2h$ der Faktor $\frac{2h}{6} = \frac{h}{3}$ pro Paar. Die im PDF gedruckte Endformel $\frac{h}{3}\left[f(x_0) + 4\sum_{i\text{ odd}} f(x_i) + 2\sum_{i\text{ even}} f(x_i) + f(x_n)\right]$ ist korrekt; nur die Zwischenzeilen sind inkonsistent (Faktorwechsel $h/6 \to h/3$ ohne Begründung).]
- **Practical advice: Stop at Simpson. [S. 64]:** "For higher accuracy, use composite rules with more subintervals. High-degrees ($n \geq 8$) develop negative weights and become unstable." (Für höhere Genauigkeit zusammengesetzte Regeln mit mehr Teilintervallen verwenden; hohe Grade $n \geq 8$ entwickeln negative Gewichte und werden instabil.)
- **Monte Carlo & the Curse of Dimensionality [S. 64]:** "For $d$-dimensional integrals, deterministic quadrature with $N$ points per dimension needs $N^d$ total points. There is no way to do this, let alone iterate on it during iterative optimization." (Deterministische Quadratur braucht $N^d$ Punkte — unmöglich, erst recht nicht iterierbar während iterativer Optimierung.) **Random Sampling** erlaubt, das Integral ohne volles Gitter zu schätzen. Integral als Erwartungswert, Gleichung (46):
  $$I = \int_\Omega f(\mathbf{x})\,d\mathbf{x} = |\Omega| \cdot \mathbb{E}_{\mathbf{X}\sim\text{Uniform}(\Omega)}[f(\mathbf{X})] \quad (46)$$
  "This identity means the definite integral equals the domain volume times the average value of $f$ under a uniform draw from $\Omega$. Practically this motivates a sampling estimator: draw points uniformly in $\Omega$, compute $f$ at those points, average the results, and multiply by $|\Omega|$ to estimate the integral." (Das bestimmte Integral = Domänenvolumen × Durchschnittswert von $f$ unter gleichverteiltem Ziehen aus $\Omega$.)
- **Monte-Carlo-Schätzer (uniform sampling auf $[-2,-1]$), Gleichung (47) [S. 65]:** Sei $X \sim \text{Uniform}(-2,-1)$. Dann:
  $$I = \frac{|\Omega|}{N}\sum_{i=1}^{N} f(\mathbf{X}_i), \qquad \mathbf{X}_i \overset{\text{i.i.d.}}{\sim} \text{Uniform}(\Omega) \quad (47)$$
- **Bias, Gleichung (48) [S. 65]:** "Because expectation is linear, this estimator is unbiased, meaning its expected value equals the true integral, for the number of $N \to \infty$:" (Da der Erwartungswert linear ist, ist der Schätzer erwartungstreu/unbiased):
  $$\mathbb{E}[\hat{I}_N] = I \quad (48)$$
  [Anm. zur Original-Formulierung, S. 65: "for the number of $N \to \infty$" ist begrifflich unsauber — die Erwartungstreue $\mathbb{E}[\hat{I}_N] = I$ gilt für jedes endliche $N$; $N \to \infty$ betrifft Konsistenz/Konvergenz des Schätzers, nicht seine Erwartungstreue.]
- **Varianz, Gleichung (49) [S. 65]:** "The variance, a measure of the spread of the estimator around its mean, or how how [sic] large the error of the estimator can be, follows from independence of the samples:" (Maß für die Streuung des Schätzers um seinen Mittelwert; folgt aus der Unabhängigkeit der Samples):
  $$\text{Var}(\hat{I}_N) = \frac{|\Omega|^2}{N}\text{Var}(f(\mathbf{X})) = \frac{|\Omega|^2 \sigma_f^2}{N} \quad (49)$$
  mit $\sigma_f^2 = \text{Var}(f(\mathbf{X}))$.
- **Standardfehler (standard error), Gleichung (50) [S. 65]:**
  $$\text{SE}(\hat{I}_N) = \frac{|\Omega|\,\sigma_f}{\sqrt{N}} \quad (50)$$
- **Dimension independent (dimensionsunabhängig) [S. 65]:** "It is trivial to see, that for large $N$ the sampling error converges with, $O(1/\sqrt{N})$ for Monte Carlo, which makes it attractive in high dimensions. Quadrature rules outperform in terms of their convergence rates, but the convergence effort explodes with the dimension, as we need $N^d$ points to maintain the same accuracy." (Schlüssel-Trade-off: Quadraturregeln sind in den Konvergenzraten überlegen, aber der Aufwand explodiert mit der Dimension; Monte Carlo konvergiert dimensionsunabhängig mit $O(1/\sqrt{N})$.)
- **Convergence in SGD [S. 65]:** "Mini-batch gradients used in SGD are Monte Carlo estimates of the true gradient, based on a samples drawn into a batch. Increasing the batch size reduces variance roughly by $1/b$, directly analogous to the $1/N$ variance scaling above. This connection explains why batch size controls the noise–variance trade-off in training." (Mini-Batch-Gradienten in SGD sind Monte-Carlo-Schätzungen des wahren Gradienten; Batch-Größe $b$ reduziert die Varianz grob um $1/b$ — direkt analog zur $1/N$-Skalierung; erklärt den Noise-Varianz-Trade-off im Training.)
- **Erwartungstreuer Stichprobenvarianz-Schätzer (unbiased sample variance estimator), Gleichung (51) [S. 68]:**
  $$Var(f(\mathbf{X})) = \frac{1}{N-1}\sum_{i=1}^{N}(f(X_i) - \bar{f})^2 \quad (51)$$

### Algorithmen / Verfahrensrezepte
- Kapitel 6 enthält **keine nummerierten Algorithmus-Boxen** (Alg. 1–4 stehen in den Kapiteln 4 und 5). Die Verfahren werden als Formeln/Rezepte gegeben:
  - **Mittelpunktsregel** (einfach und zusammengesetzt) [S. 61]: $I = h \cdot f(m)$ bzw. Riemann-Summe über Mittelpunkte $m_i$.
  - **Trapezregel** (einfach Gl. (44), Composite mit Gewichten 1–2–…–2–1) [S. 62].
  - **Simpson-Regel** (einfach $\frac{h}{6}[f(a) + 4f(m) + f(b)]$, Composite mit Gewichten 1–4–2–4–…–4–1) [S. 63–64].
  - **Monte-Carlo-Sampling-Rezept** [S. 64]: Punkte gleichverteilt in $\Omega$ ziehen, $f$ dort auswerten, Resultate mitteln, mit $|\Omega|$ multiplizieren (Gl. (46)/(47)).

### Durchgerechnete Beispiele — "Examples & Exercises" [S. 66–68]
Aufgabe: Integral von $\sin(x)$ von $-2$ bis $-1$ mit verschiedenen Methoden berechnen. Für die Fehlerquantifizierung zuerst der **exakte Wert** (vollständige Rechnung):
$$\tilde{I} = \int_{-2}^{-1} \sin(x)\,dx = [-\cos(x)]_{-2}^{-1} = -\cos(-1) + \cos(-2) \approx -0.9564491424$$

- **Midpoint rule by hand [S. 66]:** $\int_{-2}^{-1}\sin(x)\,dx$ mit Mittelpunktsregel, $n = 1$ Intervall. Mittelpunkt $m = (-2 + (-1))/2 = -1.5$:
  $$\hat{I} \approx (b - a)\cdot f(m) = 1 \cdot \sin(-1.5) \approx -0.99749$$
  Fehler $|\tilde{I} - \hat{I}| \approx 0.04104$ — "which is the small difference between the midpoint estimate and the true value." (kleine Differenz zwischen Mittelpunkt-Schätzung und wahrem Wert.)
- **Midpoint rule mit mehr Intervallen [S. 66]:** $n = 2$ Intervalle ⇒ zwei Mittelpunkte bei $-1.75$ und $-1.25$, $h = 0.5$:
  $$\hat{I} \approx h\cdot[f(-1.75) + f(-1.25)] = 0.5\cdot[\sin(-1.75) + \sin(-1.25)] = 0.5 \cdot (-1.932971) \approx -0.966485$$
  Fehler $|\tilde{I} - \hat{I}| \approx 0.010036$ — kleiner als mit $n = 1$ ($0.04104$); illustriert, "how composites, or increasing the number of intervals improves the approximation." (wie Composites bzw. mehr Intervalle die Approximation verbessern.)
  [Korrektur ggü. Original, S. 66: PDF druckt "$\hat{I} \approx -0.927228$" und Fehler "$\approx 0.02922$"; korrekt ist $\hat{I} = 0.5\cdot[\sin(-1.75) + \sin(-1.25)] = 0.5\cdot(-1.932971) \approx -0.966485$ mit Fehler $|\tilde{I} - \hat{I}| \approx 0.010036$. Die qualitative Aussage "Fehler sinkt mit $n$" bleibt richtig.]
- **Trapezoid by hand [S. 66–67]:** Trapezregel für $\int_{-2}^{-1}\sin(x)\,dx$ mit $n = 2$ Intervallen. Endpunkte $-2$, $-1.5$, $-1$, $h = 0.5$:
  $$T_2 = \frac{h}{2}[f(-2) + 2f(-1.5) + f(-1)] = 0.25\cdot[-0.90930 + 2(-0.99749) + (-0.84147)] = 0.25\cdot(-3.74575) \approx -0.93644$$
  Fehler: $|\tilde{I} - T_2| \approx 0.02001$.
  [Korrektur ggü. Original, S. 67: PDF druckt $T_2 \approx -0.927228$ — zufällig genau der gedruckte Midpoint-$n{=}2$-/Monte-Carlo-Wert (offenbar Kopierfehler); die im PDF selbst gedruckte Formel ergibt $\approx -0.93644$ mit Fehler $\approx 0.02001$. Der Original-Kommentar "The error is the same as the midpoint rule with $n = 2$ intervals, which is not necessarily a coincidence, as both methods are second-order accurate …" ist damit hinfällig — er beruht auf zwei fehlerhaften Werten (falscher Trapez-Wert und falscher Midpoint-Wert, korrekt $-0.966485$/Fehler $0.010036$, s. o.); tatsächlich $0.02001 \neq 0.010036$. Die generelle Aussage, dass beide Methoden zweiter Ordnung genau sind (second-order accurate), bleibt korrekt.]
- **Simpson's rule by hand [S. 67]:** $\int_{-2}^{-1}\sin(x)\,dx$ mit $n = 2$ Intervallen, Endpunkte $-2$, $-1.5$, $-1$, $h = 0.5$:
  $$S_2 = \frac{h}{3}[f(-2) + 4f(-1.5) + f(-1)] = \frac{0.5}{3}\cdot[-0.90930 + 4(-0.99749) + (-0.84147)] = \tfrac{1}{6}\cdot(-5.74073) \approx -0.956788$$
  Fehler: $|\tilde{I} - S_2| \approx 3.4\cdot 10^{-4}$ — sehr klein, aber nicht null; um etwa zwei Größenordnungen besser als Midpoint/Trapez.
  [Korrektur ggü. Original, S. 67: PDF druckt $S_2 \approx -0.9564491424$ (= exakter Integralwert $\tilde{I}$) mit Fehler $\approx 0.0000000000$ und kommentiert "which is essentially zero, illustrating that Simpson's rule is exact for this particular integral, as $\sin(x)$ can be well approximated by a quadratic polynomial over the interval $[-2,-1]$." Die im PDF selbst gedruckte Formel ergibt jedoch $\tfrac{1}{6}\cdot(-5.74073) \approx -0.956788$ mit Fehler $\approx 3.4\cdot 10^{-4}$. Simpson ist exakt für Polynome bis Grad 3; $\sin(x)$ ist kein solches Polynom, daher kleiner, aber nicht verschwindender Fehler. Die qualitative Kernaussage — Simpson deutlich genauer als Midpoint/Trapez — bleibt richtig.]
- **Monte Carlo by hand [S. 67]:** Monte-Carlo-Schätzung für $\int_{-2}^{-1}\sin(x)\,dx$ mit $N = 4$ Zufallssamples, "which is similar to the compute efforts of the trapezoid method." (ähnlicher Rechenaufwand wie die Trapezmethode). Angenommene Zufallssamples (vollständig):
  - $X_1 = -1.95$, $f(X_1) = \sin(-1.95) \approx -0.92895$
  - $X_2 = -1.55$, $f(X_2) = \sin(-1.55) \approx -0.99978$
  - $X_3 = -1.15$, $f(X_3) = \sin(-1.15) \approx -0.91276$
  - $X_4 = -1.05$, $f(X_4) = \sin(-1.05) \approx -0.86742$
  Monte-Carlo-Schätzung:
  $$\hat{I} = (b-a)\cdot\frac{1}{N}\sum_{i=1}^N f(X_i) = 1\cdot\frac{1}{4}(-0.92895 - 0.99978 - 0.91276 - 0.86742) \approx -0.927228$$
  [S. 68] Fehler: "$|\tilde{I} - \hat{I}| \approx 0.02922$, which is the same as the midpoint method." [Anm. — Folgeänderung zu Erratum S. 67/68: Der Gleichheits-Vergleich beruht auf dem im PDF gedruckten, laut Errata fehlerhaften Midpoint-$n{=}2$-Wert $-0.927228$/Fehler $0.02922$; mit dem korrigierten Midpoint-Wert ($-0.966485$, Fehler $0.010036$) gilt er nicht mehr. Der MC-Wert $-0.927228$ und sein Fehler $0.02922$ selbst sind für diese Samples arithmetisch korrekt.]
- **Alternative Fehlerschätzung für Monte Carlo [S. 68] (vollständige Rechnung):** Für das konkrete Beispiel mit $N = 4$ und Stichprobenmittel $\bar{f} \approx -0.927228$. Mit dem erwartungstreuen Stichprobenvarianz-Schätzer (Gl. (51)) — Abweichungsquadrate $(f(X_i) - \bar{f})^2$: $(-0.00172)^2 \approx 2.97 \cdot 10^{-6}$, $(-0.07255)^2 \approx 5.264 \cdot 10^{-3}$, $(0.01447)^2 \approx 2.09 \cdot 10^{-4}$, $(0.05981)^2 \approx 3.577 \cdot 10^{-3}$; Summe $\approx 9.053 \cdot 10^{-3}$, geteilt durch $N - 1 = 3$:
  - $\sigma_f^2 = Var(f(\mathbf{X})) \approx 0.003018$
  - $\sigma_f \approx 0.05493$
  - $\text{SE}(\hat{I}_N) \approx \frac{|\Omega|\,\sigma_f}{\sqrt{N}} = \frac{1 \cdot 0.05493}{2} \approx 0.02747$

  [Korrektur ggü. Original, S. 68: PDF druckt $\sigma_f^2 \approx 0.003036$, $\sigma_f \approx 0.05512$, $\text{SE} \approx 0.02756$ — aus gerundeten Zwischenwerten entstanden, ca. 0.6 % daneben. Aus den vier Samples folgt korrekt $\sigma_f^2 \approx 0.003018$, $\sigma_f \approx 0.05493$, $\text{SE} \approx 0.02747$.]
  **Folgefrage:** "What happens if we increase $N$ to 16? The error should decrease by a factor of 2, since the standard error scales as $1/\sqrt{N}$." (Bei $N = 16$ sollte der Fehler um Faktor 2 sinken, da der Standardfehler mit $1/\sqrt{N}$ skaliert.)

### Tabellen
- **Tabelle 3 [S. 64] — Vergleich der Quadraturmethoden-Genauigkeiten** ("Comparison of quadrature method accuracies. Higher-order methods achieve given accuracy with fewer function evaluations. $h$ is the step size, and $n$ is the number of evaluation points for Gaussian quadrature." — höherwertige Methoden erreichen gegebene Genauigkeit mit weniger Funktionsauswertungen; $h$ Schrittweite, $n$ Anzahl Auswertungspunkte bei Gauß-Quadratur), vollständig:

  | Methode (Method) | Fehler Einzelintervall (Single Interval Error) | Akkumulierter Fehler (Accumulated Error) |
  |---|---|---|
  | Left/Right | $O(h^2)$ | $O(h)$ |
  | Midpoint | $O(h^3)$ | $O(h^2)$ |
  | Trapezoid | $O(h^3)$ | $O(h^2)$ |
  | Simpson's 1/3 | $O(h^5)$ | $O(h^4)$ |
  | In General (Gaussian Quadrature) | $O(h^{2n})$ | $O(h^{2n-1})$ |

### Abbildungsbeschreibungen
- **Figure 29 [S. 58]:** "Continuous curve $f(x) = \sin(x)$ and its discretized version (black dots) on $[-3,1]$ with step size $h = 0.2$." — glatte Sinuskurve mit Diskretisierungspunkten.
- **Figure 30 [S. 58]:** "Continuous curve $f(x) = \sin(x) + \sin(2\pi x)$ and its discretized version (black dots) on $[-3,1]$ with step size $h = 0.2$." — stark/hochfrequent oszillierende Kurve mit vielen lokalen Minima.
- **Figure 31 [S. 58]:** Bildunterschrift identisch zu Fig. 30 formuliert; Darstellung jedoch als Balkendiagramm (graue Balken, diskretisiert, $h = 0.2$). [Anm.: Caption-Recycling im Original.]
- **Figure 32 [S. 59]:** "Continuous curve $f(x) = \sin(x) + \sin(2\pi x)$ and its discretized version (black dots) on $[-3,1]$ with step size $h = 0.2$, and smoothed by numerical integration with interval length $h$." — geglättete Kurve, Oszillationen reduziert; zeigt den Glättungseffekt auf der ganzen Kurve.
- **Figure 33 [S. 60]:** "Continuous curve $f(x) = \sin(x) + \sin(2\pi x)$ and its discretized version (black dots) on $[-3,1]$ with step size $h = 0.2$, smoothed by neighbour averaging with $h = 0.48$ (so $h/2 = 0.24$ gets close to cancel the $\sin(2\pi x)$ component)." — fast glatte, sinusähnliche Kurve: hochfrequenter Anteil durch Wellenlängen-angepasste Intervallwahl nahezu eliminiert.
- **Figure 34 [S. 61]:** "Continuous curve $f(x) = \sin(x)$ and midpoint rule integrals (gray bars) for $a = -2$, $b = -1$, $h = 0.5$. Black dots: midpoints. Circles: endpoints. The bars now touch, illustrating the midpoint rule without a gap." — zwei graue Rechtecke unter der Kurve auf $[-2,-1]$, die sich berühren.
- **Figure 35 [S. 62]:** "Continuous curve $f(x) = \sin(x)$ and trapezoid rule areas (gray trapezoids) for $a = -2$, $b = -1$, $h = 0.5$. Black dots: endpoints. The area under the straight lines connecting endpoints illustrates the trapezoid rule approximation."
- **Figure 36 [S. 63]:** "Continuous curve $f(x) = \sin(x)$ and Simpson's rule areas (gray, under the parabolas) for $a = -2$, $b = -1.5$, $h = 0.5$ and $a = -1.5$, $b = -1$, $h = 0.5$. Black dots: endpoints. Black dots: midpoints at $x = -1.75$ and $x = -1.25$. Solid line at $x = -1.5$ separates the two intervals. Each parabola illustrates the quadratic interpolant used by Simpson's rule on its subinterval."
- **Figure 37 [S. 65]:** Bildunterschrift wie Fig. 34 formuliert ("midpoint rule integrals … The bars now touch, illustrating the midpoint rule without a gap"); der Plot zeigt jedoch ein graues Band auf $[-2,-1]$ mit zufälligen Punkten (offene Kreise und gefüllter Punkt) — Monte-Carlo-Samples. [Anm.: recycelte Mittelpunktsregel-Caption im Original.]
- **Figure 38 [S. 65, Randnotiz]:** "Effect of batch size on gradient noise: smaller batches produce larger variance (showing up in the width of the training loss band) in the gradient estimate (Source: Stanford CS231n Note)." — verrauschte, abfallende Trainings-Loss-Kurve. Zusatznotiz: "As a beneficial side effect, computational cost is $n/b$ times cheaper per update step. For $n = 10^6$, and $b = 100$: SGD does 10,000 iterations with the compute GD needs for 1." (Rechenkosten pro Update-Schritt $n/b$-mal billiger; konkretes Zahlenbeispiel SGD vs. GD.)

### Randnotizen / Fußnoten / Literatur
- **Melts all your memories [S. 57]:** "and change into gold" — Songzitat-Anspielung auf "Smooth Operator" (Sade), passend zum Kapitelmotto.
- **Fußnote 10 [S. 57]:** N. Keskar, D. Mudigere, J. Nocedal, M. Smelyanskiy, P. Tang: "On large-batch training for deep learning: Generalization gap and sharp minima", 09 2016, DOI: 10.48550/arXiv.1609.04836.
- **Fußnote 11 [S. 57]:** J. Bergstra, Y. Bengio: "Random search for hyper-parameter optimization", *Journal of Machine Learning Research*, 13:281–305, 2012.
- **Fußnote 12 [S. 57]:** Y. Gal, Z. Ghahramani: "Dropout as a bayesian approximation: Representing model uncertainty in deep learning", 2016. URL https://arxiv.org/abs/1506.02142
- **What if [S. 59] (Denkfrage/Grenzfall):** "we would be integrating over an interval which results in destructive inference [sic, gemeint: interference] of the underlying higher frequency sine curve? Think wavelengths." (Was, wenn über ein Intervall integriert würde, das destruktive Interferenz der zugrunde liegenden höherfrequenten Sinuskurve ergibt? An Wellenlängen denken.)
- **On the interval $[a,b]$ [S. 61]:** "the midpoint value is $f(m)$. With left endpoint, the height is $f(a)$; with right endpoint, the height is $f(b)$." (Mittelpunktswert $f(m)$; mit linkem Endpunkt Höhe $f(a)$, mit rechtem $f(b)$.)
- **Doubling the sub intervals [S. 61]:** "reduced error by $\sim 4\times$. This suggests $O(h^2)$ convergence." (Verdopplung der Teilintervalle reduzierte den Fehler um ca. das Vierfache — empirischer Hinweis auf $O(h^2)$-Konvergenz.)
- **Dividing the integral by $h$ [S. 62]:** "gives us a weighted average of the function values, which is a better approximation to the integral than just using the midpoint or endpoints. Implicitly reflecting local curvature and information about the function's behavior across the interval." (Division durch $h$ ergibt einen gewichteten Durchschnitt der Funktionswerte; reflektiert implizit lokale Krümmung.)
- **Try with some points [S. 63]:** "Start with $x = 0$ and see how the linear factors play out." (Übungshinweis zur Lagrange-Basis.)
- **What happens, when you approximate a linear function with a quadratic? [S. 64]** (Denkfrage/Grenzfall.)
- **A neural network with $d = 10^6$ [S. 64]:** "or 1 million parameters would need $(N)^{10^6}$ grid points. Even $N = 2$ gives $2^{10^6}$, a number with 300,000 digits." (Drastisches Curse-of-Dimensionality-Beispiel: schon $N = 2$ ergibt eine Zahl mit 300.000 Stellen.)
- **Midpoint rule [S. 65]:** "is a special case of Monte Carlo with $N = 1$ sample at the midpoint." (Mittelpunktsregel = Monte-Carlo-Spezialfall mit $N = 1$ Sample am Mittelpunkt.)
- **Further things worth trying [S. 66]:** "are to calculate the approximation on the endpoints of the interval, comparing the error." (Approximation an den Intervall-Endpunkten berechnen und Fehler vergleichen.)
- **Try with more intervals [S. 67]:** "see how the error decreases and check whether you know your way around composites in Simpson's and Trapezoid rules." (Mit mehr Intervallen probieren; Composite-Varianten von Simpson- und Trapezregel beherrschen.)
- **Code [S. 68]:** https://github.com/Quillstacks/lecturecode_numericalmethods.git

### Übungsaufgaben & Selbstreflexionsfragen
- **Folgefrage zur MC-Fehlerschätzung [S. 68]:** $N$ auf 16 erhöhen — Fehler sollte um Faktor 2 sinken ($1/\sqrt{N}$-Skalierung). "Briefly elaborate on how the error of the Monte Carlo estimator is dimension independant [sic]." (Kurz erläutern, wie der Fehler des Monte-Carlo-Schätzers dimensionsunabhängig ist.)
- **Enter higher dimensions on your machine (Übung) [S. 68]:** "Implement Monte Carlo integration for a $d$-dimensional integral, such as integrating a multivariate Gaussian function over a hypercube. While slowly increasing $d$, observe how the error behaves for different methods. Even more, observe how grid-based quadrature methods become infeasible in terms of computational cost as $d$ grows. Optionally, see how similar effects arise in optimization by implementing gradient descent and mini-batch stochastic gradient descent on a high-dimensional function. Only watch compute times." (Monte-Carlo-Integration $d$-dimensional implementieren, z. B. multivariate Gauß-Funktion über einen Hyperwürfel; Fehlerverhalten bei wachsendem $d$ beobachten; gitterbasierte Quadratur wird infeasible; optional GD vs. Mini-Batch-SGD — nur Rechenzeiten beobachten.)
- Weitere Übungsimpulse aus den Randnotizen (s. o.): Endpunkt-Approximation vergleichen [S. 66], mehr Intervalle/Composites [S. 67], Lagrange-Linearfaktoren bei $x = 0$ durchspielen [S. 63], "What if"-Interferenzfrage [S. 59], Linear-mit-Quadratik-Frage [S. 64].
- **Self-Reflection [S. 69]** (alle 9 Fragen):
  - "How does the error of the midpoint, trapezoid, Simpson's rule and Monte Carlo compare?" (Wie vergleichen sich die Fehler der vier Methoden?)
  - "Why has the midpoint rule better accuracy than the left or right endpoint rules?" (Warum ist die Mittelpunktsregel genauer als Links-/Rechts-Endpunkt-Regeln?)
  - "How does composite methods improve accuracy, and what is the trade-off?" [sic — Grammatik im Original] (Wie verbessern Composite-Methoden die Genauigkeit, was ist der Trade-off?)
  - "Why do deterministic quadrature methods fail in high dimensions?" (Warum scheitern deterministische Quadraturmethoden in hohen Dimensionen?)
  - "In which way, is the midpoint rule a special case of Monte Carlo estimation?" (Inwiefern ist die Mittelpunktsregel ein Monte-Carlo-Spezialfall?)
  - "What is the intuition behind Monte Carlo not exploding in high dimensions?" (Intuition, warum Monte Carlo in hohen Dimensionen nicht explodiert?)
  - "When would you use Simpson's rule vs. Monte Carlo?" (Wann Simpson vs. Monte Carlo?)
  - "How is the mini-batch mean in SGD related to Monte Carlo estimation?" (Wie hängt das Mini-Batch-Mittel in SGD mit Monte-Carlo-Schätzung zusammen?)
  - "How does the gradient estimation in SGD help escape local minima?" (Wie hilft die Gradientenschätzung in SGD beim Entkommen aus lokalen Minima?)

### Recap of Key Concepts [S. 69]
- "Deterministic quadrature methods (midpoint, trapezoid, Simpson's) approximate integrals using weighted sums of function values at specific points. They are accurate and converge fast for smooth, low-dimensional problems." (Deterministische Quadraturmethoden approximieren Integrale über gewichtete Summen von Funktionswerten an spezifischen Punkten — genau und schnell konvergierend für glatte, niedrigdimensionale Probleme.)
- "Monte Carlo integration estimates integrals by averaging function values at random samples. It is unbiased and has a convergence rate of $O(1/\sqrt{N})$, making it independent of the dimensionality of the problem." (Monte-Carlo-Integration: erwartungstreu, Konvergenzrate $O(1/\sqrt{N})$ — unabhängig von der Dimensionalität.)
- "In SGD, mini-batch gradients are Monte Carlo estimates of the true gradient." (In SGD sind Mini-Batch-Gradienten Monte-Carlo-Schätzungen des wahren Gradienten.)

### Teaser / Überleitung [S. 69–70]
- **Überleitung [S. 69]:** "So far stability referred to the sensitivity of the numerical solution to small changes in the input data. But we can also talk about stability in terms of the numerical method itself, and how it behaves …" — [S. 70] "… when approximating different types of functions. In the next chapter, we will see other types of stability issues that arise in numerical methods, and how to mitigate them by sophisticated method selection and configuration." (Bisher: Stabilität = Sensitivität der numerischen Lösung gegenüber kleinen Eingabeänderungen; man kann auch über Stabilität der numerischen Methode selbst sprechen. Nächstes Kapitel: weitere Stabilitätsprobleme und ihre Milderung durch geschickte Methodenwahl und -konfiguration.) [Anm.: Ein solches Folgekapitel ist in diesem PDF nicht enthalten — "unfinished lecture notes"; die Materialien decken daher nur Kap. 1–6 ab.]
- Randnotiz **Teaser [S. 69]:** "Why do high-order quadrature methods become unstable when approximating low-degree polynomials?" (Warum werden Hochordnungs-Quadraturmethoden instabil, wenn sie Polynome niedrigen Grades approximieren? — Denkfrage, Bezug Runge-Phänomen/negative Gewichte.)
- Rest der Seite 70 leer.

---

## Index (S. 71)

Vollständiges Stichwortverzeichnis des Originals (Begriff, Seitenzahl(en)), alphabetisch:

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

## Angewandte Korrekturen

Liste aller im Dokument angewandten `[Korrektur ggü. Original]`-Stellen (verbindliche Referenz: `review/errata_original_pdf.md`). An jeder Stelle wurde die fachlich korrekte Version verwendet und die Abweichung markiert; eigene neue Korrekturen wurden nicht erfunden.

1. **[S. 31] (Thema 3, Stabilitätsrechnung $h=1$):** PDF wechselt in derselben Rechnung den Index "$s_{h=1,x=-1}$ → $s_{h=1,x=0}$"; gemeint ist durchgängig derselbe Fall ($\tilde{x} = x + 0.25$, $x = -1$). Ergebnis $s \approx 0$ ist korrekt.
2. **[S. 32] (Thema 3, Konvergenzrechnung, beide Fälle):** PDF druckt Endwert "= 0.1599"; korrekt ist $|-0.84147 - (-1)| = 0.15853$ (beide Fälle $h=1$ und $h=0.2$). Zudem fehlen die verbindenden Relationszeichen (Layout), und im $h=0.2$-Block steht einmal fälschlich $\hat{f}_1(-1.2)$ statt $\hat{f}_{0.2}(-1.2)$.
3. **[S. 37] (Thema 4, Newton an $\sin(x)$, $x_2$-Schritt):** PDF druckt "$\frac{0.0008}{-0.9999}$"; tatsächlich $\sin(3.125) \approx 0.01659$, $\cos(3.125) \approx -0.99986$. Endergebnis $x_2 \approx 3.1416$ stimmt, der gedruckte Zwischenwert nicht.
4. **[S. 38] (Thema 4, Gl. (20)):** Layoutfehler — "$+ f(x_n)$" ist hinter die Nebenbedingung gerutscht. Korrekt: $f(x) \approx f(x_n) + f'(x_n)\cdot(x - x_n)$ für $x$ nahe $x_n$ (bestätigt durch die Folgezeile $0 = f(x_n) + f'(x_n)(x_{n+1} - x_n)$).
5. **[S. 44] (Thema 4, Newton-Handrechnung an $f(x) = x^3 - x$, $x_0 = 1.4$):** PDF druckt die Iterationskette $1.127 \to 0.976 \to 1.014$ mit mehreren falschen Zwischenwerten, u. a. Zähler $0.432$ statt $\approx 0.305$ ($f(1.127) \approx 0.3044$). Korrekt: $x_1 = 1.4 - 1.344/4.88 \approx 1.1246$, $x_2 \approx 1.1246 - 0.2977/2.7942 \approx 1.0181$, $x_3 \approx 1.0181 - 0.0372/2.1096 \approx 1.0005$ — monotone Konvergenz von oben gegen $x = 1$ (die gedruckte Kette springt fälschlich unter die Wurzel). Methodik (Gl. (21)) ist korrekt.
6. **[S. 45] (Thema 4, Sekanten-Handrechnung an $f(x) = x^3 - x$):** PDF druckt $f(1.2) = 0.128$ (korrekt: $0.528$) und $f(1.4) = 0.744$ (korrekt: $1.344$); die darauf aufbauende Iterationskette ($x_2 \approx 1.159$, $x_3 \approx 1.011$) beruht vollständig auf den falschen Werten. Korrekt: $x_2 = 1.4 - 1.344 \cdot \frac{0.2}{0.816} \approx 1.0706$; weitere Schritte entsprechend neu zu rechnen. Methodik (Gl. (34)) ist korrekt.
7. **[S. 53] (Thema 5, Newton für Minima):** PDF druckt "Newton's method finds points where $f''(x) = 0$"; sachlich findet Newton auf $f'$ angewandt Punkte mit $f'(x) = 0$ (Extremstellen); der Second-Derivative-Test klassifiziert sie anschließend über $f''$.
8. **[S. 64] (Thema 6, Composite Simpson):** PDF druckt in den Zwischenzeilen der Herleitung pro Teilintervall-Paar den Faktor $h/6$; korrekt ist bei Gitterweite $h$ und Paarbreite $2h$ der Faktor $2h/6 = h/3$ pro Paar. Die gedruckte Endformel $\frac{h}{3}[f(x_0) + 4\sum_{i\text{ ungerade}} f(x_i) + 2\sum_{i\text{ gerade}} f(x_i) + f(x_n)]$ ist korrekt; nur die Zwischenzeilen sind inkonsistent.
9. **[S. 66] (Thema 6, Mittelpunktsregel $n=2$):** PDF druckt $\hat{I} \approx -0.927228$ und Fehler $\approx 0.02922$; korrekt ist $\hat{I} = 0.5\cdot[\sin(-1.75) + \sin(-1.25)] = 0.5\cdot(-1.932971) \approx -0.966485$ mit Fehler $|\tilde{I} - \hat{I}| \approx 0.010036$. Die qualitative Aussage "Fehler sinkt mit $n$" bleibt richtig. (Folgehinweise an den PDF-Vergleichsstellen [S. 67]/[S. 68] — "same as the midpoint method" — sind als Anmerkungen markiert, da sie sich auf den gedruckten Wert beziehen.)
10. **[S. 67] (Thema 6, Trapezregel $T_2$):** PDF druckt $T_2 \approx -0.927228$ — identisch mit dem gedruckten Midpoint-$n{=}2$-/Monte-Carlo-Wert (offenbar Kopierfehler). Die im PDF selbst gedruckte Formel ergibt $0.25\cdot[-0.90930 + 2(-0.99749) + (-0.84147)] = 0.25\cdot(-3.74575) \approx -0.93644$ mit Fehler $|\tilde{I} - T_2| \approx 0.02001$. Damit ist auch die Original-Aussage "The error is the same as the midpoint rule with $n = 2$" hinfällig (sie beruht auf zwei falschen Werten).
11. **[S. 67] (Thema 6, Simpson $S_2$):** PDF druckt $S_2 \approx -0.9564491424$ (= exakter Integralwert) mit Fehler $\approx 0$ ("Simpson's rule is exact for this particular integral"). Die im PDF selbst gedruckte Formel ergibt $\tfrac{1}{6}\cdot[-0.90930 + 4(-0.99749) + (-0.84147)] = \tfrac{1}{6}\cdot(-5.74073) \approx -0.956788$ mit Fehler $\approx 3.4\cdot 10^{-4}$ — sehr klein, aber nicht null. Simpson ist exakt für Polynome bis Grad 3, nicht für $\sin(x)$; die qualitative Aussage (deutlich genauer als Midpoint/Trapez) bleibt richtig. (Folgeänderung [S. 68]: "which is the same as the midpoint method" beruht auf dem falschen Midpoint-Wert aus Korrektur 9; der MC-Wert $-0.927228$ und Fehler $0.02922$ selbst sind korrekt — als Anmerkung markiert.)
12. **[S. 32] (Thema 3, Konsistenzrechnung $h=0.2$):** PDF nutzt $\hat{f}_{0.2}(-1.2) = -0.94898$; das ist $\sin(-1.25)$, aber $-1.25$ ist kein Gitterpunkt des $h=0.2$-Gitters. Korrekt: $\hat{f}_{0.2}(-1.2) = \sin(-1.2) = -0.93204$, damit $c_{0.2} \geq |-0.93204 - (-1)| = 0.06796$ (PDF: $0.05102$). Die qualitative Aussage "Consistency improves with smaller step sizes" bleibt richtig ($0.06796 < 0.15853$).
13. **[S. 59] (Thema 6, Glättungsbeispiel an $f(x) = \sin(x) + \sin(2\pi x)$, $x = -0.4$):** PDF setzt $f(-0.5) = -1.14973$ und $f(-0.3) = -0.97720$ ein — das sind tatsächlich $f(-0.2)$ bzw. $f(-0.4)$. Korrekt: $f(-0.5) = \sin(-0.5) + \sin(-\pi) = -0.47943$, $f(-0.3) = \sin(-0.3) + \sin(-0.6\pi) = -1.24658$; damit geglättet $f(-0.4) \approx -0.86300$ (PDF: $-1.06347$) und $h \cdot f(-0.4) \approx -0.17260$ (PDF: $-0.11285$). Erst mit den korrekten Werten wird die Skript-Aussage "correction towards higher losses" konsistent ($-0.86300 > -0.97720$); mit den PDF-Werten widerspräche das Ergebnis ihr. Gl. (43) selbst ($f(-0.4) = -0.97720$) ist korrekt.
14. **[S. 42] (Thema 4, Tabelle 2, Newton für $\sqrt{2}$, $x_0 = 2$):** Zeile $n=4$: PDF druckt $|e_4| = 4.5 \times 10^{-12}$ — das ist das Residuum $|x_4^2 - 2|$, nicht der Fehler $|x_4 - \sqrt{2}| \approx 1.6 \times 10^{-12}$ (Spaltendefinition!). Zudem Zeile $n=3$: korrekt $|e_3| = 2.12 \times 10^{-6}$ (PDF: $2.13 \times 10^{-6}$). Übrige Zeilen korrekt.
15. **[S. 68] (Thema 6, Monte-Carlo-Stichprobenvarianz):** Aus den vier Samples folgt $\sigma_f^2 \approx 0.003018$, $\sigma_f \approx 0.05493$, $\text{SE} \approx 0.02747$ (PDF: $0.003036$/$0.05512$/$0.02756$ — aus gerundeten Zwischenwerten entstanden, ca. 0.6 % daneben). Korrekte Werte verwendet, Abweichungsquadrate gezeigt.

**Keine Korrektur erforderlich (per Errata nur Fußnoten-/[sic]-Niveau):** [S. 49] $f'(7.2)$: Summanden ergeben 2.375, PDF rundet zulässig auf 2.38 (als Anmerkung in Thema 5 dokumentiert); [S. 59] "destructive inference" → gemeint "interference" (als [sic] markiert); [S. 31] "ill-conditioning with κ ≤ 0.247": berechneter Maximalwert ist $0.2474$ — in Thema 3 als $\kappa \approx 0.2474$ mit Anmerkung zur PDF-Schreibweise dokumentiert; [S. 65, Gl. (48)] "unbiased … for the number of $N \to \infty$": Erwartungstreue gilt für jedes endliche $N$, $N \to \infty$ betrifft Konsistenz/Konvergenz — als klarstellende Anmerkung in Thema 6 dokumentiert; diverse Tippfehler ("Excercises", "Newton-Rhapson", "understnad", "Conditiioning", "Intgration", "inifinitely", "independant", "end whilereturn") sind originalgetreu mit [sic] bzw. Anmerkung dokumentiert.
