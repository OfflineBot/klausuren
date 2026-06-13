# Pass 3: Anwendung & Details — Vollständige Extraktion
## "Numerical Methods" — Prof. Dr.-Ing. Mark Schutera (Unfinished Lecture Notes, 71 Seiten)

---

## Frontmatter (S. 1–7)

### [S. 1] Titelseite
- "PROF. DR.-ING. MARK SCHUTERA"
- Titel: "NUMERICAL METHODS"
- Untertitel/Verlag: "UNFINISHED LECTURE NOTES"

### [S. 2] Copyright-/Impressumsseite
- Copyright © 2026 Prof. Dr.-Ing. Mark Schutera
- "published by unfinished lecture notes"
- Hinweis: "Combobulated with the help of multiple large language model driven tools." (Anmerkung: erstellt mit Hilfe mehrerer LLM-Tools)
- Lizenz: Creative Commons Attribution-NonCommercial 4.0 International License ("CC BY-NC-SA 4.0"). Keine kommerzielle Nutzung; Remix/Transformation muss unter gleicher Lizenz verbreitet werden; explizite Erlaubnis des Autors für Nutzungen über die Lizenz hinaus nötig. Lizenz-URL: https://creativecommons.org/licenses/by-nc-sa/4.0/
- Material wird "AS IS" ohne Garantien bereitgestellt.
- Mitmach-Hinweis: "These notes are, by their very nature, unfinished, and they improve with every reader." Fehler, Einwände, Quellen, Fragen oder Positionen können per Pull Request eingereicht werden: https://github.com/Quillstacks/LectureMaterial/tree/main/lecturenotes/notes_numerischemethoden — "Every contribution is welcome."
- Versions-/Datumsstempel: "2026-05-06 · feisty cranberry Hermelin" (Build-Name)
- QR-Code (grün) unten rechts [Abbildung: QR-Code, vermutlich Link zum Repository]

### [S. 3] Zitatseite (Motto)
> "AN INFINITELY ACCURATE APPROXIMATION IS NO LONGER AN APPROXIMATION." — PROBABLY SOMEONE SMART
(Humorvolles Pseudozitat als Motto der Notizen.)

### [S. 4] Leer.

### [S. 5] Inhaltsverzeichnis (Contents)
- Enter Numerical Methods — 9
- Floating-Point Arithmetic — 17
- Error Analysis — 25
- Newton Methods — 35
- Global Optimization — 47
- Numerical Integration — 57
- Index — 71

### [S. 6] Leer.

### [S. 7] Introduction
- "Numerical Methods are essential for solving mathematical problems that cannot be addressed analytically."
- Kursinhalt: fundamentale Konzepte, Fehleranalyse (error analysis), Konditionierung von Problemen (problem conditioning), Stabilität (stability) und diverse numerische Techniken — Ziel: zuverlässige und effiziente Algorithmen in wissenschaftlichem Rechnen und Ingenieursanwendungen implementieren.
- Anwendungsversprechen: "everything you need to know to become proficient with numerical methods, and how to put them to good use in machine learning, data science, and engineering contexts." (Anwendungsbezug: ML, Data Science, Engineering)

### [S. 8] Leer.

---

# Kapitel 1: Enter Numerical Methods (S. 9–16)

### [S. 9] Kapitelbeginn
- Datums-/Build-Stempel: "2026-04-05 · regal coconut Wachtel"
- Abschnitt: **Tapping into Computational Power / The Why**
- Numerische Methoden sind essenziell zur Lösung mathematischer Probleme, die nicht analytisch behandelt werden können. "Numerical methods are a subfield of mathematics in which we calculate our solutions not analytically exactly, but approximately."
- Gründe ("And we have good reason to do so"):
  - Viele Probleme sind analytisch unlösbar oder zu komplex, um praktikabel zu sein.
  - Wir können Rechenleistung anzapfen (tap into computational power), um effizient approximative Lösungen zu erhalten.
- ML/AI-Bezug: Numerische Methoden sind entscheidend für Modelltraining, Parameteroptimierung und Simulation komplexer Systeme, wo analytische Lösungen unmöglich (infeasible) sind. Sie ermöglichen effiziente Verarbeitung großer Datensätze und komplexer Algorithmen. Besonders im Deep Learning (Modelle mit Millionen Parametern, umfangreiche Berechnungen) erleichtern numerische Methoden die Optimierungsprozesse des Modelltrainings — "making them indispensable for advancing models."

**Randnotizen [S. 9]:**
- *Further Reading* (Literaturverweise, Fußnoten 1–4):
  1. T. Arens, F. Hettlich, C. Karpfinger, U. Kockelkorn, K. Lichtenegger, H. Stachel. *Mathematik*. Springer
  2. W. Dahmen, A. Reusken. *Numerik für Ingenieure und Naturwissenschaftler*. Springer
  3. M. P. Deisenroth, A. A. Faisal, C. S. Ong. *Mathematics for Machine Learning*. Cambridge University Press
  4. P. Deuflhard, A. Hohmann. *Numerische Mathematik 1 – Eine algorithmisch orientierte Einführung*. De Gruyter
- *Etymologie*: "Approximation comes from Latin *approximare*, meaning 'to come near to'."
- *Moore's Law*: "states that computing power doubles approximately every two years. As of today consumer GPUs have thousands of cores and can perform trillions of floating point operations per second." Literaturverweis: G. E. Moore. Cramming more components onto integrated circuits. *Electronics*, 38(8):114–117, 1965
- *GPT-2: 1.5B release*: Link https://openai.com/index/gpt-2-1-5b-release/

### [S. 10] Hands On Experience
- Ankündigung: Später theoretische Grundlagen; jetzt Gefühl dafür bekommen, warum AI/ML so stark auf numerischen Methoden lehnen.
- **Die Grenzen der Skalierung analytischer Lösungen** (limits of scaling analytical solutions) werden bei großskaligen Problemen sichtbar. Einfaches Beispiel: Lösen eines linearen 2×2-Gleichungssystems analytisch per Substitution.

**Beispiel (vollständig durchgerechnet), Gleichung (1):**
$$\begin{bmatrix} 2 & 1 \\ 5 & 1 \end{bmatrix} \begin{bmatrix} w_1 \\ w_2 \end{bmatrix} = \begin{bmatrix} 11 \\ 13 \end{bmatrix} \quad (1)$$

Aus der ersten Gleichung:
$$2w_1 + w_2 = 11 \Rightarrow w_2 = 11 - 2w_1$$
In die zweite Gleichung eingesetzt:
$$5w_1 + 1(11 - 2w_1) = 13$$
$$5w_1 + 11 - 2w_1 = 13$$
$$3w_1 + 11 = 13$$
$$3w_1 = 2$$
$$w_1 = \frac{2}{3}$$
Dann:
$$w_2 = 11 - 2\left(\frac{2}{3}\right) = 11 - \frac{4}{3} = \frac{33-4}{3} = \frac{29}{3}$$
Verifikation 1. Gleichung:
$$2\left(\frac{2}{3}\right) + \left(\frac{29}{3}\right) = \frac{4}{3} + \frac{29}{3} = \frac{33}{3} = 11 \checkmark$$
Verifikation 2. Gleichung:
$$5\left(\frac{2}{3}\right) + 1\left(\frac{29}{3}\right) = \frac{10}{3} + \frac{29}{3} = \frac{39}{3} = 13 \checkmark$$

**Randnotizen [S. 10]:**
- *Analytics*: "includes methods like substitution, elimination, matrix inversion, etc. you would learn in linear algebra."
- *Computational complexity* (Übungsaufgabe in Randnotiz!): "increases with the size of the system. Now take a shot and solve this larger system of three equations with three unknowns:"
$$\begin{bmatrix} 2 & 1 & 3 \\ 1 & 4 & 2 \\ 3 & 2 & 5 \end{bmatrix} \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix} = \begin{bmatrix} 14 \\ 20 \\ 32 \end{bmatrix} \quad (2)$$

### [S. 11] Grenzen analytischer Lösungen
- **However**: Für 2 Gleichungen lösbar, aber mit wachsender Systemgröße (z. B. Tausende Gleichungen mit Tausenden Unbekannten) werden analytische Lösungen unpraktikabel wegen Rechenkomplexität und Zeitbeschränkungen.
- **Grenzen analytischer Lösungen auch bei nichtlinearen Gleichungen**, Gleichung (3):
$$\sigma(x) = \frac{1}{1 + e^{-x}} \quad (3)$$
- Transzendente Funktionen (transcendental functions) können nicht als endliche Kombinationen algebraischer Operationen (Addition, Subtraktion, Multiplikation, Division, Wurzeln) ausgedrückt werden und haben daher keine geschlossene Lösung (closed-form solution). Der Exponentialterm macht es unmöglich, $x$ mit elementaren Funktionen (Polynome, rationale, trigonometrische Funktionen) zu isolieren.

**Randnotiz [S. 11]:** *Sigma*: "$\sigma(x)$ is the sigmoid activation function commonly used in neural networks, and a transcendental function. A closed-form solution for $\sigma(x) = 0$ does not exist. $\sigma(x)$ approaches 0 asymptotically as $x$ approaches negative infinity, but never actually reaches 0 for any finite value of $x$." (Grenzfall/Warnung: Nullstelle existiert nicht!)

- **Lernziele (Learning Objectives) des Kapitels:**
  - Erklären, wann wir numerische Methoden einsetzen und welche Probleme beim analytischen Lösen entstehen.
  - Diskretisierung: kontinuierliche mathematische Probleme in diskrete, computerlösbare Approximationen transformieren.
  - Grundlegende numerische Techniken auf einfache Probleme von Hand anwenden, und größere Probleme auf dem Computer "crunchen".

### [S. 12] Discretization and Approximation
- **Abbildung (Figure 1):** "Continuous curve $f(x) = \sin(x)$ and its discretized version (black dots) on $[-3, 1]$ with step size $h = 1$." — Plot von $\sin(x)$ auf $[-3,1]$ mit schwarzen Punkten bei den diskreten Stellen; y-Achse $f(x)$ von $-1$ bis $1$, x-Achse von $-3$ bis $1$.
- **Diskretisierung** (Discretization): kontinuierliche Domänen (Zeit, Raum, Funktionen) in endliche Schritte/Gitter zerlegen und Funktionen an diskreten Punkten mit endlicher Präzision auswerten:
  - Kontinuierliche Funktion: $f(x), \quad x \in [a,b]$
  - Diskretisierte Funktion: $f(x_i), \quad x_i = a + ih, \quad i = 0, 1, \ldots, N$
  - mit Schrittweite (step size), Gleichung (4):
$$h = \frac{b-a}{N} \quad (4)$$
  - $N$ = Anzahl der Schritte auf dem Intervall.
- **Analytische Minimumsuche** von $\sin(x)$ auf $[-3,1]$: gesucht $\min_{x \in [-3,1]} \sin(x)$. Minimum tritt auf, wo die Ableitung verschwindet und die zweite Ableitung positiv ist.
$$f(x) = \sin(x)$$
$$f'(x) = \cos(x) = 0 \implies x^* = \frac{\pi}{2} + k\pi, \; k \in \mathbb{Z}$$
- **Abbildung (Figure 2):** "Continuous curve $f(x) = \sin(x)$ (black), its derivative $f'(x) = \cos(x)$ (gray, dashed), and the analytical minimum (black dot) on $[-3,1]$. The dashed gray line marks the critical point where $\cos(x) = 0$ and the minimum of $\sin(x)$." — vertikale gestrichelte Linie bei $x = -\frac{\pi}{2}$.

**Randnotizen [S. 12]:**
- *Remember*: "the brackets '[' and ']' are called a closed interval and mean that they include the values $a$ and $b$ in the definition set."
- *Trigonometric Rules*: "give us this general solution for $\cos(x) = 0$. If you forget you can always derive it from the unit circle." (Tipp/Merkhilfe)

### [S. 13] Fortsetzung: Analytisch vs. Numerisch
- Kritische Punkte in $[-3,1]$:
$$x_1 = -\frac{\pi}{2} \approx -1.5708$$
$$x_2 = \frac{\pi}{2} \approx 1.5708 \;(> 1, \text{ nicht im Intervall — Grenzfall!})$$
- **Wichtiger Hinweis (Stolperfalle):** Das Minimum (oder Maximum) einer Funktion auf einem geschlossenen Intervall $[a,b]$ kann an einem kritischen Punkt (Ableitung null oder undefiniert) im Inneren ODER an den Endpunkten $a$ oder $b$ auftreten, selbst wenn die Ableitung dort nicht null ist. Deshalb muss man bei Extremasuche auf geschlossenen Intervallen sowohl kritische Punkte als auch Endpunkte prüfen.
- Prüfe Endpunkte und $x_1$:
$$\sin(-3) \approx -0.1411$$
$$\sin\left(-\frac{\pi}{2}\right) = -1$$
$$\sin(1) \approx 0.8415$$
- Ergebnis: Minimum ist $-1$ bei $x = -\frac{\pi}{2} \approx -1.5708$.
- **On To the Numerical Solution**: Brute-Force-Gittersuche (grid search). Bei einer Gittersuche werten wir die Funktion an diskreten Punkten über dem Intervall aus und wählen den Punkt mit dem Minimalwert. Diskretisierung von $[-3,1]$ mit Schrittweite $h = 1$.
- **Abbildung (Figure 3):** "Continuous curve $f(x) = \sin(x)$ and its discretized version (black dots) on $[-3,1]$ with step size $h = 1$."
- **Durchgerechnete Werte:**
$$x_0 = -3, \quad \sin(-3) \approx -0.1411$$
$$x_1 = -2, \quad \sin(-2) \approx -0.9093$$
$$x_2 = -1, \quad \sin(-1) \approx -0.8415$$
$$x_3 = 0, \quad \sin(0) = 0$$
$$x_4 = 1, \quad \sin(1) \approx 0.8415$$
- Ergebnis: "the minimum among these is $\sin(-2) \approx -0.9093$ at $x = -2$."

**Randnotizen [S. 13]:**
- *Brute Force*: "means we try out all possible options and select the best one. Here with a grid search."
- *The minimum*: "among these is $\sin(-2) \approx -0.9093$ at $x = -2$. It is easy to see that the choice of step size $h$ affects the accuracy of the approximation. A smaller step size would yield a closer approximation to the true minimum. Further the interval selection matters, in a sense that it ." [UNSICHER: Satz bricht im Original ab — "in a sense that it ." unvollständig]
- *Approximation Error*: "is the difference between the analytical and numerical solutions. Here: $|-1 - (-0.9093)| = 0.0907$." (Konkreter Zahlenwert des Approximationsfehlers!)

### [S. 14] Examples & Excercises [sic — Schreibweise im Original]
- **Remember**: das Beispiel von oben, Gleichung (5):
$$\begin{bmatrix} 2 & 1 \\ 5 & 1 \end{bmatrix} \begin{bmatrix} w \\ b \end{bmatrix} = \begin{bmatrix} 11 \\ 13 \end{bmatrix} \quad (5)$$
- Dieses System kann auch via Brute-Force-Diskretisierung und Approximation gelöst werden: Variablen $w$ und $b$ über ein Gitter möglicher Werte diskretisieren, gemäß diesen Werten lösen und die Lösung wählen, die den Fehler minimiert.
- **Grid Search**: für $w$ und $b$ mit Schrittweite 2.5 über den Bereich $w, b \in \{0, 2.5, 5, 7.5, 10\}$. Für jede Kombination wird der Fehler berechnet.
- **Fehlerdefinition** (Gleichung (6)): Fehler = Summe absoluter Differenzen zwischen linker und rechter Seite der Gleichungen:
$$\text{error}_1 = |2w + b - 11|,$$
$$\text{error}_2 = |5w + b - 13| \quad (6)$$
- Alle Kombinationen auswerten und $(w,b)$-Paar mit kleinstem akkumulierten Fehler wählen.
- **Didaktischer Hinweis**: "There is value in doing this by hand" — hilft, die Mechanik numerischer Methoden zu verstehen; gibt Intuition für Rechenkosten von Brute-Force-Methoden ("later on we will find more efficient approaches"). "This was only 100 operations" — Botschaft: Das will man an einen Computer übergeben und automatisieren; der Computer hat mit dieser Problemgröße keinerlei Mühe.
- **Enter the machine**: Viele numerische Methoden sind für Computer-Implementierung designt. Im Kurs wird oft zwischen Handrechnung (kleine Beispiele) und Computer-Implementierung (größere Probleme) gewechselt.
- **Jupyter Notebook**: "You get a jupyter notebook pre-hosted at your fingertips. With it you get a python template for this excercise. Use the self-reflection questions below to guide your while exploring and experimenting with the implementation."

**Randnotizen [S. 14]:**
- *Excercises* [sic]: "are for practice and reinforcing concepts. Try to solve them on your own first, try things, play with it, discuss, this is not a time trial. And there is no shame in not ending up at the right answer, in the same sense, that uncovering great questions and tossing them around is usually pretty fruitful on the long run." (Lernhinweis)
- *Linear regression*: "see how $xw + b$ forms a linear model, which can also be thought of as the most basic form of a single unit neural network $\theta$." (ML-Anwendungsbezug!)
- *Code is hosted as notebooks*: "and is to be followed up here https://enlitenment.schutera.com/landing." [UNSICHER: URL-Schreibweise, evtl. "enlightenment"]

### [S. 15] Tabelle 1: Vollständige Grid-Search-Tabelle
**Tabelle (Table 1):** "Grid search for $w, b$ in $\{0, 2.5, 5, 7.5, 10\}$: values of $2w + b$ and $5w + b$ with errors to 11 and 13 in parentheses. The last column shows the accumulated error (sum of absolute errors). The minimum error occurs at $w = 0, b = 10$ with an error of 4 (marked with *)."

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

(Beachte: Das Grid-Search-Minimum $w=0, b=10$ weicht stark von der wahren Lösung $w = 2/3, b = 29/3 \approx 9.67$ ab — illustriert Grenzen grober Gitter. Anmerkung: $w=0,b=10$ liegt nahe $b$-wahr, aber $w$ falsch.)

- **Self-Reflection and Recap** — Selbstreflexionsfragen (prüfungsrelevant als Verständnisfragen):
  - "Why is the choice of step size $h$ important when discretizing a continuous function, and how does it affect the accuracy and the compute time of the numerical solution?"
  - "How does the selection of the interval $[a,b]$ influence the results of discretization and the location of extrema found numerically?"
  - "What are the main differences between a continuous function and its discretized version, and what are the implications for solving mathematical problems numerically?"

### [S. 16] Recap of Key Concepts
- Numerische Methoden sind essenziell für komplexe mathematische Probleme ohne analytische Lösung.
- Diskretisierung transformiert kontinuierliche Probleme in diskrete Approximationen für rechnergestützte Methoden.
- Handrechnung für kleine Probleme (Mechanik verstehen), Computer für größere Probleme essenziell.
- **Errors everywhere**: Mathematische Modelle sind Vereinfachungen der Realität, und numerische Methoden führen zusätzliche Fehler durch Approximation ein. Gleichung (7):
$$f(x) \approx f(x_i), \quad x_i = a + ih \quad (7)$$
- Numerische Berechnung führt einige Fehlertypen ein, die verstanden werden müssen, "in order to be able to fully harness this new methodology."

**Randnotiz [S. 16]:** *Teaser* (Übungsfrage): "Can you think of a simple way to improve the accuracy to compute ratio of our grid search example from above?" (Denkanstoß für adaptive/verfeinerte Suche)

---

# Kapitel 2: Floating-Point Arithmetic (S. 17–24)

### [S. 17] Kapitelbeginn
- Datums-/Build-Stempel: "2026-04-29 · lively date Hase"
- Abschnitt: **Getting used to Errors Everywhere / The Why**
- Rückblick: Numerische Methoden führen Fehler durch Approximation ein. Sei $f(x)$ stetig auf $[a,b]$; die diskretisierte Version $f(x_i)$ approximiert $f(x)$ an diskreten Punkten $x_i$ mit einem Fehler, der von Schrittweite $h$ und Glattheit (smoothness) von $f$ abhängt.
- Numerische Werte können zudem nur approximativ im Computerspeicher abgelegt werden: **Gleitkommadarstellung (floating-point representation)**. Dies führt zu **Rundungsfehlern (rounding errors)** bei arithmetischen Operationen, zusätzlich zu den **Trunkierungsfehlern (truncation errors)**, die beim Approximieren unendlicher Prozesse durch endliche entstehen (auch **Approximationsfehler/approximation error** genannt).
- Gründe, diese Fehler zu verstehen:
  - Numerische Methoden führen Rundungs- und Trunkierungsfehler ein.
  - Je nach Maschine wirken sich diese Fehler unterschiedlich aus und können sich verstärken (amplify) und akkumulieren (accumulate).
- ML/AI-Bezug: Floating-Point-Arithmetik ist auch in der Modell-Inferenz relevant, besonders in rechenarmen Umgebungen "on the edge" oder beim Deployment quantisierter Modelle (quantized models, Fußnote 5).

**Randnotizen [S. 17]:**
- *Modeling Error*: "occurs as all models are simplifications of reality, and the difference between the model and the real-world system introduces an error. We will not dive deeper into this type of error in this course. Yet, mind the fine difference between what we term $f(x)$ and what actually is a $f(x)$." [UNSICHER: letzter Satz wörtlich so kryptisch im Original]
- *On the Edge*: "models use lower-precision arithmetic, such as 8-bit integers or even binary weights and activations."
- *Binary neural networks (BNNs)*: "use weights and activations constrained to $\{-1, +1\}$, drastically reducing memory and computation requirements, but making floating-point representation and rounding effects critical."
- Fußnote 5: M. Courbariaux, Y. Bengio. "Binarynet: Training deep neural networks with weights and activations constrained to +1 or -1." *CoRR*, abs/1602.02830, 2016. URL http://arxiv.org/abs/1602.02830

### [S. 18] Hands On Experience: Rundungsfehler
- **Beispiel: Division 10 durch 3** (vollständige Dezimalentwicklung, schriftliche Division):
  - $10 \div 3 = 3$, Rest 1
  - "Bring down a 0": $10 \div 3 = 3$, Rest 1
  - "Bring down a 0": $10 \div 3 = 3$, Rest 1
  - "Bring down a 0": $10 \div 3 = 3$, Rest 1
  - ... und so weiter
  - $\Rightarrow \frac{10}{3} = 3.333\ldots$
- **Die 3en wiederholen sich für immer.** Beim Aufschreiben/Eingeben in Rechner/Computer muss man irgendwo stoppen (Gleichung (8)):
$$\frac{10}{3} \approx 3.333 \quad \text{(gerundet oder trunkiert nach 3 Stellen)} \quad (8)$$
- **Rundungsfehler** = Differenz zwischen wahrem Wert und dem Wert nach Abschneiden (truncate) der Entwicklung. "No matter how many digits you write, as soon as you stop, you introduce an error" (Gleichung (9)):
$$\text{Rounding error} = |3.333333\ldots - 3.333| = 0.000333\ldots \quad (9)$$
- Je mehr Stellen, desto kleiner der Fehler — aber er verschwindet nie ganz, außer man schreibt unendlich viele Stellen, "which well, you know is impossible."
- **This is rounding error**: Computer speichern Zahlen immer mit endlich vielen Stellen, daher tauchen Rundungsfehler unvermeidlich auf und müssen gemanagt werden.
- **Warnung**: Diese kleinen Fehler können akkumulieren, sich verstärken und zu signifikanten Ungenauigkeiten führen — besonders in iterativen Algorithmen, wie sie in numerischen Methoden und Machine Learning üblich sind.
- **Lernziele des Kapitels:**
  - Die verschiedenen Typen numerischer Fehler verstehen: Modellierungs- (modeling), Trunkierungs- (truncation) und Rundungsfehler (rounding errors).
  - Gleitkommadarstellung, Maschinenepsilon (machine epsilon) und Auslöschung (loss of significance) verstehen.
  - Numerische Fehler in praktischen Berechnungen handhaben können.

**Randnotizen [S. 18]:**
- *Types of numerical representations in computers*:
  - **Integer (int):** 3
  - **Floating-point (float):** 3.3333333
  - **Double precision (double):** 3.3333333333333333 [UNSICHER: genaue Stellenzahl]
  - **Fixed-point (e.g. 4-digits):** 3.3333
- *Impossible?*: "Mathematical annotation helps us with period: $3.\overline{3}$." (Periodenschreibweise)

### [S. 19] Floating Point Representation and Precision
- **Gleitkommazahlen (floating-point numbers)**: Art, wie Computer reelle Zahlen mit endlich vielen Bits darstellen. Der **IEEE 754-Standard** (Fußnote 6) ist das meistgenutzte Format. Eine Gleitkommazahl wird typischerweise gespeichert als (Gleichung (10)):
$$x = (-1)^s \cdot m \cdot 2^e \quad (10)$$
  - $s$ = Vorzeichenbit (sign bit)
  - $m$ = Mantisse (mantissa, auch significand) — bestimmt die Präzision
  - $e$ = Exponent — bestimmt die Skala (Größenordnung/magnitude)
- Erlaubt einen weiten Wertebereich, aber **nur eine endliche Menge reeller Zahlen kann exakt dargestellt werden**.
- IEEE 754 single precision (float): 32 Bits = 1 Vorzeichenbit, 8 Exponentenbits, 23 Mantissenbits.
- **Abbildung (Figure 4):** "Bit layout of IEEE 754 **HALF (16)**: sign (dark), exponent (medium), mantissa (light)." — Balken mit Markierungen bei Bit 1, 6, 16 (1 Sign, 5 Exponent, 10 Mantisse).
- **Abbildung (Figure 5):** "Bit layout of IEEE 754 **SINGLE (32)**: sign (dark), exponent (medium), mantissa (light)." — Markierungen bei Bit 1, 9, 32 (1 Sign, 8 Exponent, 23 Mantisse).
- **Abbildung (Figure 6):** "Bit layout of IEEE 754 **DOUBLE (64)**: sign (dark), exponent (medium), mantissa (light)." — Markierungen bei Bit 1, 12, 64 (1 Sign, 11 Exponent, 52 Mantisse).
- **Der Exponent** wird mit einem **Bias** gespeichert, um positive und negative Exponenten zu erlauben → sehr kleine und sehr große Größenordnungen darstellbar. Beispiel IEEE 754 single precision: Exponent hat 8 Bits und Bias 127. Gespeicherter Exponent $E$ und wahrer Exponent $e$: $e = E - 127_{10}$. Grund für Bias 127: Mit 8 Bits kann das Exponentenfeld Werte von 0 ($2^0 - 1$) bis 255 ($2^8 - 1$) speichern. Durch Subtraktion des Bias (127) kann der tatsächliche Exponent $e$ positive und negative Werte annehmen, zentriert um Null. "This makes encoding and comparison of floating-point numbers easier in hardware."

**Randnotizen [S. 19]:**
- Fußnote 6: IEEE Computer Society. "IEEE standard for floating-point arithmetic." https://ieeexplore.ieee.org/document/4610935, August 2008. IEEE Std 754-2008 (Revision of IEEE Std 754-1985)
- *A Bit*: "short for binary digit, is the most basic unit of information in computing and digital communications. It can have a value of either 0 or 1."

### [S. 20] Constructing Scale & Mantisse & Machine Epsilon
- **Constructing scale** in Gleitkommadarstellung (Beispielrechnungen, Skala über Exponent):
$$10^1 = 10_{10} = 1010_2 = 1.010 \times 2^3, \quad E = 10000010_2$$
$$10^2 = 100_{10} = 1100100_2 = 1.100100 \times 2^6, \quad E = 10000101_2$$
$$10^3 = 1000_{10} = 1111101000_2 = 1.111101000 \times 2^9, \quad E = 10001000_2$$
- **Die Mantisse** bestimmt, wie fein Zahlen zwischen Zweierpotenzen dargestellt werden können.
- **2-bit Mantissa Example (unnormalized)** (vollständig durchgerechnet):
  - Mantissen-Bit-Kombinationen: 00, 01, 10, 11
  - Unnormalisierter Significand: $0.xx_2$
$$00: \quad 0.00_2 = 0 + 0 \times 2^{-1} + 0 \times 2^{-2} = 0.0$$
$$01: \quad 0.01_2 = 0 + 0 \times 2^{-1} + 1 \times 2^{-2} = 0.25$$
$$10: \quad 0.10_2 = 0 + 1 \times 2^{-1} + 0 \times 2^{-2} = 0.5$$
$$11: \quad 0.11_2 = 0 + 1 \times 2^{-1} + 1 \times 2^{-2} = 0.75$$
- **Eine 2-Bit-Mantisse** bedeutet: vier verschiedene Werte zwischen zwei beliebigen Zweierpotenzen darstellbar. 3-Bit-Mantisse: acht verschiedene Werte usw. Allgemein: Mit einer Mantisse von $t$ Bits können $2^t$ verschiedene Werte zwischen zwei Zweierpotenzen dargestellt werden, skaliert durch den Exponenten.
- **Maschinenepsilon** ($\varepsilon_{\text{mach}}$): kleinste positive Zahl, sodass $1 + \varepsilon_{\text{mach}} \neq 1$ in der Computerarithmetik. Quantifiziert die obere Schranke des relativen Fehlers durch Rundung in Gleitkommaarithmetik (Gleichung (11)):
$$\varepsilon_{\text{mach}} = 2^{-t} \quad (11)$$
  wobei $t$ = Anzahl Mantissenbits.
- Im 2-Bit-Mantissen-Beispiel: $\varepsilon_{\text{mach}} = 2^{-2} = 0.25$.
- **Das bedeutet**: Die relative Präzision von Gleitkommazahlen ist ca. $2^{-t}$, während die **absolute Präzision** von der Größenordnung der dargestellten Zahl abhängt (Gleichung (12)):
$$\varepsilon_{\text{mach}} \cdot |x| \quad (12)$$

**Randnotizen [S. 20]:**
- *The largest number in single precision*: "is about $10^{38}$, set by the largest exponent $e = +127$. The decimal exponent 38 comes from $\log_{10}(2^{128}) \approx 38.5$."
- *Remember (SI-Präfixe)*: "mega ($10^6$), giga ($10^9$), tera ($10^{12}$), peta ($10^{15}$), exa ($10^{18}$), zetta ($10^{21}$), yotta ($10^{24}$), ronna ($10^{27}$), quetta ($10^{30}$), **no official SI prefix** for ($10^{33}$)."
- *Konkrete Werte*: "For IEEE 754 single precision, $\varepsilon_{\text{mach}} \approx 1.19 \times 10^{-7}$; for double precision, $\varepsilon_{\text{mach}} \approx 2.22 \times 10^{-16}$."
- *Absolute precision*: "is just about to become clear, $1 : 2 = 0.5$ but $10 : 2 = 5$. Same number of steps (relative precision), but gaps of 0.5 vs 5." (Veranschaulichung relative vs. absolute Präzision)

### [S. 21] Absolute Lücken & Fixed-Point
- **In anderen Worten**: Große Zahlen haben größere absolute Lücken (gaps) zwischen darstellbaren Werten als kleine Zahlen.
- **Abbildung (Figure 7):** "Absolute error for single (black, labeled SINGLE) and double (gray, dashed, labeled DOUBLE) precision as a function of the represented value $x$. The error grows linearly with $x$ and is proportional to machine epsilon for each format." — Log-log-Plot: x-Achse von $10^{-16}$ bis $10^{16}$, y-Achse (Absolute error) von $10^{-23}$ bis $10^{7}$; zwei parallele Geraden (SINGLE oben, DOUBLE unten gestrichelt).
- **Fixed-Point-Darstellung (fixed-point representation)**: andere Art, reelle Zahlen zu speichern, besonders wenn man **vorhersagbare Präzision und Performance** will. Man legt im Voraus fest, wie viele Bits für den Ganzzahlteil und wie viele für den Bruchteil verwendet werden. Die Lücke zwischen darstellbaren Zahlen (Präzision) ist dadurch **immer gleich**, egal wie groß oder klein der Wert ist — "Which gives more control."
- **Beispiel (Fixed-Point/Skalierungsfaktor):** Zahlen zwischen $-1000$ und $1000$ mit 32-Bit signed Integer speichern. Normalerweise stellt ein 32-Bit-Integer Werte von $-2147483648$ bis $2147483647$ dar — viel mehr als benötigt. Für mehr Präzision: Skalierungsfaktor verwenden, z. B. jede reelle Zahl mit $10^6$ multiplizieren und das Ergebnis als Integer speichern. Die Zahl $1.234567$ wird so zu $1234567$ im Speicher.

**Randnotiz [S. 21]:** *Precision*: "with a scaling factor of $10^{-6}$, is equal to the smallest difference you can represent is $0.000001$. The maximum rounding error is half a step, or $0.5 \times 10^{-6} = 0.0000005$."

### [S. 22] Examples & Excercises: Loss of Significance (Auslöschung)
- **Loss of significance**, auch **catastrophic cancellation** (katastrophale Auslöschung) genannt: tritt auf beim Subtrahieren zweier nahezu gleicher Zahlen — führende Ziffern heben sich auf, nur die weniger signifikanten, rundungsfehleranfälligen Ziffern bleiben. "This can greatly amplify rounding errors."
- **Beispiel 1 (vollständig):** Zwei Zahlen $a$ und $b$, beide mit begrenzter Präzision gespeichert, jeweils auf 8 signifikante Stellen gerundet (fixed-point):
$$a = 12345678.5$$
$$b = 12345678.0$$
  Mit 8 signifikanten Stellen gespeichert als:
$$\tilde{a} = 12345679$$
$$\tilde{b} = 12345678$$
  Subtraktion:
$$\tilde{a} - \tilde{b} = 12345679 - 12345678 = 1$$
  Vergleich mit wahrer Differenz:
$$a - b = 12345678.5 - 12345678.0 = 0.5$$
- **Der Fehler im Ergebnis** ist 0.5, gleich dem Rundungsfehler in $\tilde{a}$ bzw. $\tilde{b}$ individuell auf Machine-Epsilon-Niveau 0.5.
- **Beispiel 2 (minimale Abweichung — Gegenstück):**
$$a = 12345678.4$$
$$b = 12345678.0$$
  Mit 8 signifikanten Stellen gespeichert (12345678.4 rundet ab!):
$$\tilde{a} = 12345678$$
$$\tilde{b} = 12345678$$
  Subtraktion:
$$\tilde{a} - \tilde{b} = 12345678 - 12345678 = 0$$
  Wahre Differenz:
$$a - b = 12345678.4 - 12345678.0 = 0.4$$

**Randnotizen [S. 22]:**
- *Pseudo-Accuracy*: "in general is a unjustifiably high level of detail, creating a misleading, and artificial sense of accuracy." (Warnung vor Scheingenauigkeit)
- *Infinity*: "in mathematics there is an infinity between 0 and 1. The difference between something and nothing." (philosophische Randbemerkung zum Unterschied Ergebnis 0 vs. 1)

### [S. 23] Relative Fehler, Hands-on Machine Epsilon, Loss-of-Significance-Demo
- **Vergleich der beiden Beispiele:** Die Differenz der wahren Ergebnisse ist 0.1 (0.5 vs. 0.4), aber die Maschinenergebnisse sind 0 in einem Fall und 1 im anderen — "which is a huge relative error. This shows how loss of significance can lead to large errors in computations, especially when the numbers being subtracted are very close to each other." (zentrale Warnung!)
- **Hands on machine epsilon** (Übungsauftrag): Überlegen, wie man das Maschinenepsilon eines beliebigen Systems für ein spezifisches Gleitkommaformat per Programm bestimmen würde. Definition von Machine Epsilon wiederholen, Gedanken in Pseudocode festhalten. Frage: "What would such a program show when run on a fixed-point system vs a floating-point system?" Dann verschiedene Typen auf der eigenen Maschine im Code ausprobieren, Beobachtungen notieren und reflektieren.
- Frage (prüfungsrelevant): "When you would build a calculator, which type would you choose and why?" (mit Fußnote 7)
- **Loss of significance example** (Übungsauftrag): Überlegen, wie man Auslöschung auf der eigenen Maschine demonstrieren würde; Pseudocode notieren, bevor man weiterliest.
- **Abbildung (Figure 8):** "Demonstration of catastrophic loss of significance: $1/(1 + \epsilon - 1)$ vs $\epsilon$ (log-x, linear-y scale). For large $\epsilon$, the result follows $1/\epsilon$. For very small $\epsilon$, rounding error dominates and the result becomes infinite." — Plot: x-Achse $\epsilon$ von $10^{-17}$ bis $10^{-14}$ (log), y-Achse $1/(1+\epsilon-1)$ von 0 bis $2 \times 10^{16}$; Kurve fällt von "$\uparrow \infty$" (links, bei kleinen $\epsilon$) hyperbelartig ab.
- **Reason about** (Denkaufgabe): wie das Berechnen von $f(\epsilon) = 1/(a + \epsilon - b)$ für kleines $\epsilon$ und $a = b$ den Zweck erfüllt. "What do you expect to see when $\epsilon$ is very small?"

**Randnotizen [S. 23]:**
- *Code*: "is again to be found here https://github.com/Quillstacks/lecturecode_numericalmethods.git."
- *Overflow*: "occurs when numbers with large magnitude are approximated as $+\infty$ or $-\infty$."
- *Underflow*: "occurs when numbers near zero are rounded to zero."
- *Is double enough?* mit Fußnote 7: D. Blochinger. "Numerische methoden – foliensatz." Zentrum für Angewandte Ökonomik (ZAÖ), DHBW Ravensburg, 2025. URL https://www.economicon.de/repository/index.html. Illustration: Prof. Dr. Daniel Blochinger. Lizenz: CC BY-NC-SA 4.0. Stand: 28. Mai 2025. Weitere Materialien: https://www.economicon.de/repository/index.html
- *What happens for $a > b$?* "Think along the lines of significant digits." (Denkanstoß/Grenzfall)

### [S. 24] Self-Reflection and Recap (Kapitel Floating-Point)
- **Selbstreflexionsfragen:**
  - "How is floating-point representation structured, and what are its components?"
  - "What is machine epsilon, and how does it relate to numerical precision?"
  - "How do these concepts impact numerical computations in practice?"
- **Recap of Key Concepts:**
  - Gleitkommadarstellung erlaubt Computern, einen weiten Bereich reeller Zahlen mit endlich vielen Bits zu speichern, führt aber Rundungsfehler ein.
  - Maschinenepsilon quantifiziert die kleinste darstellbare Differenz in Gleitkommaarithmetik und beeinflusst die Präzision numerischer Berechnungen.
  - Auslöschung (loss of significance) tritt beim Subtrahieren nahezu gleicher Zahlen auf, verstärkt Rundungsfehler und führt zu ungenauen Ergebnissen.
- **Knowing what can go wrong**: Überleitung — wir nähern uns dem Verständnis, wie wir Qualität von Methoden definieren. "We now know that there is a true function $f$ and an approximated function $\hat{f}$, further we have a true input $x$ and a rounded input $\tilde{x}$. These effect and characterize our numerical methods." (Notation: $\hat{f}$ = Methode, $\tilde{x}$ = gestörter Input)

**Randnotiz [S. 24]:** *Teaser*: "Can you think of metrics for numerical methods, based on the approximations and errors we discussed?" (Übungs-/Denkfrage als Brücke zum nächsten Kapitel)

---

# Kapitel 3: Error Analysis (S. 25–34)

### [S. 25] Kapitelbeginn
- Datums-/Build-Stempel: "2026-04-29 · lively date Hase"
- Abschnittstitel (humorvoll): **"Some call it Error. I call it Character." / The Why**
- **Conditioning, Stability, Consistency and Convergence** (Konditionierung, Stabilität, Konsistenz, Konvergenz) sind fundamentale Konzepte der numerischen Analysis, um Verhalten numerischer Algorithmen und ihre Zuverlässigkeit zu verstehen.
- **Understanding Concepts** — Ziele, um Verhalten/Charakteristik numerischer Methoden zu beschreiben:
  - Sensitivität gegenüber kleinen Änderungen der Eingabedaten beurteilen.
  - Sensitivität der numerischen Lösung gegenüber kleinen Änderungen der Eingabedaten bewerten.
  - Sicherstellen, dass numerische Methoden genaue und reproduzierbare Ergebnisse liefern.
  - Garantieren, dass Approximationen gegen die wahre Lösung konvergieren.
- **ML/AI-Bezug**: Besonders beim Training großer Modelle auf riesigen Datensätzen ist das Verständnis dieser Konzepte entscheidend. Training neuronaler Netze = große Optimierungsprobleme, oft mit iterativen numerischen Methoden. "In Deep Learning convergence has the center stage, then almost as an afterthought comes Complexity – the number of operations and amount of time it takes to get there."
- Allgemein: Man wird später AI-Modelle $\theta$ mit genau diesen Konzepten evaluieren und beschreiben können. "So the maths aside, this will come in handy."

**Randnotizen [S. 25]:**
- *One last word on model error*: "With $f(\cdot)$ we imply the exact model of a system. In practice, models are simplifications of reality, for a distance between two points A and B we might use a simplified Manhattan or Euclidean model that does not account for terrain, mode of travel, or obstacles. So keep in mind that our $f(\cdot)$ here, is another $f(\cdot)$." (Warnung Modellfehler; Beispiel Manhattan-/Euklidische Distanz)
- *Deep Learning by Goodfellow*: "does a great job kick-starting you into numerical computation (Ch. 4) for machine learning. Check it out for further reading:" — I. Goodfellow, Y. Bengio, A. Courville. *Deep Learning*. MIT Press, 2016. http://www.deeplearningbook.org (Literaturverweis, Kapitelhinweis Ch. 4)

### [S. 26] Hands On Experience: Intuition zu den 4 Konzepten
- Einstieg: intuitives Gefühl mit einfachen Beispielen; jedes Konzept mit **zwei** schnellen Übungen (von Hand oder im Kopf) — zwei Übungen, "as we want to highlight two sides of the same coin for each concept, introducing somewhat extremes on the spectrum." Wiederaufnahme des diskretisierten Sinus-Beispiels aus Kapitel 1.
- **Conditioning (Konditionierung)**: "is about how sensitive the solution is to small changes in the input data."
- **Abbildung (Figure 9):** "Continuous curve $\hat{f}(x) = \sin(x)$ on $[-3,1]$ with two highlighted transparent vertical bands at $x = -1.5$ and $x = 0$ (width 0.5)." — Sinuskurve mit zwei grauen vertikalen Bändern.
- Annahme: approximierte Funktion = wahre Funktion (Sinuskurve), aber $\tilde{x}$ ist eine leicht gestörte Version von $x$ durch Messfehler oder Rundung ($\pm 0.25$). Betrachte die zwei grauen Bänder bei $x = -1.5$ und $x = 0$:
  - Band bei $x = -1.5$: **gut konditionierte Region** (well-conditioned) — kleine Änderungen in $x$ führen zu kleinen Änderungen in $f(x)$.
  - Band bei $x = 0$: **schlecht konditioniert** (ill-conditioned) — kleine Änderungen in $x$ können zu großen relativen Änderungen in $f(x)$ führen.
- **Stability (Stabilität)**: "refers to the sensitivity of the numerical solution to the small changes in the input data."
- **Abbildung (Figure 10):** "Continuous curve $f(x)_{.2} = \sin(x)$ on $[-3,1]$ with a highlighted transparent vertical band at $x = 0$ (width 0.5), and discretized points with step size $h = 0.2$." — Sinuskurve mit dichten schwarzen Punkten ($h=0.2$).
- Beobachtung am grauen Band um $x = 0$: In der ersten Abbildung (Schrittweite $h = 0.2$) folgen die diskretisierten Punkte der Sinuskurve eng — das zeigt eine **Instabilität** gegenüber Änderungen in $\tilde{x} \pm 0.25$, resultierend in Fluktuationen der berechneten Werte $\hat{f}(\tilde{x})$. Im Kontrast: zweite Abbildung mit Schrittweite $h = 1$ … (Fortsetzung S. 27)

**Randnotiz [S. 26]:** *This is about floating-point representation*: "and not about step size or optimal approximation. Make sure to wrap your head around that, before moving on." (Wichtige Abgrenzung/Stolperfalle bei Conditioning!)

### [S. 27] Stabilität (Forts.), Konsistenz, Konvergenz (intuitiv)
- **Abbildung (Figure 11):** "Continuous curve $f(x)_{1.} = \sin(x)$ on $[-3,1]$ with a highlighted transparent vertical band at $x = 0$ (width 0.5), and discretized points with step size $h = 1$." — Sinuskurve mit wenigen Punkten ($h=1$).
- Fortsetzung: ... zeigt nur einen einzigen diskretisierten Punkt im grauen Band, was zu einer **stabilen Approximation** der Sinuskurve in dieser Region führt — "regardless of the deviations in $\tilde{x}$." (Paradox/Pointe: gröbere Diskretisierung = stabiler, aber weniger konsistent!)
- **Consistency (Konsistenz)**: "quantifies how well our numerical method matches the exact solution of the original problem." Zur Veranschaulichung: Diskretisierung mit Schrittweite $h = 1$ und mit $h = 0.2$.
- **Abbildung (Figure 12):** "Bar plot of discretized values $f(x)_{1.} = \sin(x)$ on $[-3,1]$ with step size $h = 1$." — Balkendiagramm (stückweise konstante Approximation), grobe Balken.
- **Abbildung (Figure 13):** "Bar plot of discretized values $f(x)_{.2} = \sin(x)$ on $[-3,1]$ with step size $h = 0.2$." — Balkendiagramm mit feinen Balken.
- Für infinitesimal kleine Schrittweiten $h \to 0$ kommen die diskretisierten Punkte der wahren Sinuskurve immer näher — am Ende perfekte Übereinstimmung zwischen numerischer Methode und exakter Lösung = **optimale Konsistenz**.
- **Convergence (Konvergenz)**: "emerges when we combine the ideas of stability and consistency. A numerical method is convergent if, as we refine our approximation $\hat{f}(x)$ (for example, by decreasing the step size $h$), the …" (Fortsetzung S. 28)

**Randnotiz [S. 27]:** *Intuitive convergence example with sine, wanted*: "If you have a better idea to have the examples stick to the sine context, let me know." (Anmerkung des Autors — Werkstattcharakter)

### [S. 28] Konvergenz (Forts.) & Lernziele
- Fortsetzung: "… computed solution approaches the exact solution of the problem regardless of the deviations in $\tilde{x}$, or by implicitly accounting for them."
- **Lernziele des Kapitels:**
  - Intuition über die Konzepte Konditionierung, Stabilität, Konsistenz und Konvergenz in numerischen Methoden haben.
  - Einfache numerische Probleme quantitativ bezüglich dieser Konzepte analysieren.
- Rest der Seite leer.

### [S. 29] Quantitative Characterization of Numerical Methods
- **Notation**: $f(\cdot)$ = exakte (analytische) Lösung eines Problems; $\hat{f}(\cdot)$ = numerische Methode (Algorithmus), die eine Approximation liefert. $x$ = exakte Eingabedaten; $\tilde{x}$ = tatsächlich verwendete Eingabedaten, evtl. gestört durch Messfehler oder Rundung.
- **Conditioning**: beschreibt, wie sensitiv die Lösung eines Problems auf kleine Änderungen der Eingabedaten reagiert. Formal: Konditionierung eines Problems bei $x$ quantifiziert durch die Konditionszahl $\kappa$ (Gleichung (13)):
$$\kappa = |f(x) - f(\tilde{x})| \quad (13)$$
  "$\kappa$ is often normalized to express it as a relative measure."
- **Stability**: gegeben, wenn kleine Fehler im Input oder in Zwischenschritten nicht zu unverhältnismäßig großen Fehlern im Output führen. Mathematisch: stabile Methode stellt sicher, dass der Fehler der berechneten Lösung $\hat{f}(\tilde{x})$ durch ein konstantes Vielfaches des Eingabefehlers beschränkt bleibt (Gleichung (14)):
$$\left|\hat{f}(\tilde{x}) - \hat{f}(x)\right| \leq s \cdot |\tilde{x} - x| \quad (14)$$
  $s$ = Konstante. "For $s \approx 1$, the error in the computed solution develops linearly with the error in the input data."
- **Consistency**: wie gut die numerische Lösung die exakte Lösung des Originalproblems approximiert (Gleichung (15)):
$$\left|\hat{f}(x) - f(x)\right| \leq c \quad (15)$$
  $c$ = Konstante, die den Konsistenzfehler quantifiziert.
- **Convergence**: bezieht sich allgemein darauf, dass unsere Approximation einen spezifischen stabilen Grenzwert erreicht. Eine Methode ist konvergent, wenn (Gleichung (16)):
$$\left|\hat{f}(\tilde{x}) - f(x)\right| \to \lim \quad (16)$$
  "That is, as both the real solution is approximated and deviations in data are controlled by an error margin."

**Randnotizen [S. 29]:**
- *Hat versus tilde* (Merkhilfe!): "The hat $\hat{}$ marks the numerical method (algorithm), while the tilde $\tilde{}$ marks a perturbed input. So $\hat{f}(\tilde{x})$ reads as: numerical method evaluated on perturbed input data."
- *Convergence*: "usually aims for zero error margin, which is often the exact solution $f(x)$. However, often we will experience non-zero convergence. If the method converges to a value different from $f(x)$, this indicates a systematic error (bias) in the method." (Wichtig: Bias/systematischer Fehler!)

### [S. 30] Examples & Excercises: Quantitative Analyse am Sinus-Beispiel
- **Aufgabe**: Minimum der Sinusfunktion auf $[-3,1]$ noch einmal. Diskretisierung mit zwei Schrittweiten $h = 1$ und $h = 0.2$. Annahme: Eingabe $x$ gestört durch $\tilde{x} = x \pm 0.25$ (Messfehler), Präzision von zwei Dezimalstellen. Analysiere Konditionierung, Stabilität, Konsistenz und Konvergenz der numerischen Methode in beiden Fällen; quantifiziere mit den Formeln des vorherigen Abschnitts.
- **Conditioning** ist unabhängig von der verwendeten numerischen Methode — beschreibt Sensitivität des Problems selbst. Analyse rein über die Wirkung kleiner Änderungen in $x$ auf $\sin(x)$. Um $x = -1$ (nahe Minimum) ist die Sinusfunktion relativ flach → gute Konditionierung. Zum Vergleich $x = 0$, wo sich die Sinusfunktion schnell ändert → schlechte Konditionierung. Fokus auf diese zwei Regionen.
- **Durchgerechnete Konditionszahlen bei $x = -1$:**
$$\kappa(-1, +0.25) = |\sin(-1) - \sin(-0.75)| \approx |-0.8415 - (-0.6816)| = 0.1599$$
$$\kappa(-1, -0.25) = |\sin(-1) - \sin(-1.25)| \approx |-0.8415 - (-0.9489)| = 0.1074$$
- Ergebnis: "well-conditioning with $0.1074 \leq \kappa \leq 0.1599$."
- **Bei $x = 0$:**
$$\kappa(0, +0.25) = |\sin(0) - \sin(0.25)| \approx |0 - 0.2474| = 0.2474$$
$$\kappa(0, -0.25) = |\sin(0) - \sin(-0.25)| \approx |0 - (-0.2474)| = 0.2474$$

### [S. 31] Stabilität quantitativ
- Schlussfolgerung von S. 30: "ill-conditioning with $\kappa \leq 0.247$." [Anm.: Original schreibt 0.247]
- **Stability** hängt von der numerischen Methode ab (Diskretisierung + Minimumsuche):
  - $h = 1$: Methode stabil — kleine Änderungen in $\tilde{x}$ führen zu kleinen Änderungen in $\hat{f}(\tilde{x})$.
  - $h = 0.2$: Methode weniger stabil — kleine Änderungen in $\tilde{x}$ können größere Fluktuationen in $\hat{f}(\tilde{x})$ verursachen.
- Quantifizierung über Konstante $s$ in der Stabilitätsungleichung (Gleichung (17)):
$$\left|\hat{f}(\tilde{x}) - \hat{f}(x)\right| \leq s \cdot |\tilde{x} - x| \quad (17)$$
- "Due to symmetry we only consider the case $\tilde{x} = x + 0.25$."
- **Für $h = 1$ (vollständige Rechnung):**
$$s_{h=1,x=-1} \cdot |\tilde{x} - x| = |\hat{f}(\tilde{x}) - \hat{f}(x)| = |\hat{f}_1(-0.75) - \hat{f}_1(-1)| = |\hat{f}_1(-1) - \hat{f}_1(-1)| \text{ (see A)}$$
$$s_{h=1,x=0} \approx 0 \div 0.25 \approx 0$$
  [Anm.: Indexwechsel von $x=-1$ zu $x=0$ so im Original — UNSICHER, vermutlich Tippfehler im Original]
- **Für $h = 0.2$ (vollständige Rechnung):**
$$s_{h=0.2,x=-1} \cdot |\tilde{x} - x| = |\hat{f}(\tilde{x}) - \hat{f}(x)| = |\hat{f}_{0.2}(-0.75) - \hat{f}_{0.2}(-1)| = |\hat{f}_{0.2}(-0.8) - \hat{f}_{0.2}(-1)| = |-0.71736 - (-0.84147)|$$
$$s_{h=0.2,x=-1} = 0.12411 \div 0.25 \approx 0.4964$$
- **Warnung (Stolperfalle)**: "Be aware that stability has anomalies in border regions of the discretization. This is especially a problem for piece-wise constant approximations." (Randregionen-Anomalien!)
- **Consistency**: bestimmt durch Vergleich der numerischen Lösung $\hat{f}(x)$ mit der exakten Lösung $f(x)$ für das Minimum des Sinus auf $[-3,1]$. Quantifizierung der Konstante $c$ in der Konsistenzungleichung (Gleichung (18)):
$$\left|\hat{f}(x) - f(x)\right| \leq c \quad (18)$$

**Randnotizen [S. 31]:**
- *Stability* (Übungsaufgabe!): "equals the conditioning of the system, for $h \to 0$. Show it." (Beweisaufgabe)
- *A)*: "See how the step size $h = 1$ leads to the same function value at both points. For reference, Fig. 12." (Erklärung des Rechenschritts $\hat{f}_1(-0.75) = \hat{f}_1(-1)$)
- *Remember*: "the analytical solution of min(sin(x)) on $[-3,1]$ – revisit Chapter 1." (= $-1$ bei $x = -\pi/2$)

### [S. 32] Konsistenz & Konvergenz quantitativ (vollständige Rechnungen)
- **Für $h = 1$:**
$$c_1 \geq \left|\hat{f}_1(-\tfrac{\pi}{2}) - f(-\tfrac{\pi}{2})\right| \geq \left|\hat{f}_1(-1) - f(-\tfrac{\pi}{2})\right| \geq |-0.84147 - (-1)| \geq 0.15853$$
- **Für $h = 0.2$:**
$$c_{0.2} \geq \left|\hat{f}_{0.2}(-\tfrac{\pi}{2}) - f(-\tfrac{\pi}{2})\right| \geq \left|\hat{f}_{0.2}(-1.2) - f(-\tfrac{\pi}{2})\right| \geq |-0.94898 - (-1)| \geq 0.05102$$
- Fazit: "Consistency improves with smaller step sizes, as expected." ($c_1 = 0.15853$ vs. $c_{0.2} = 0.05102$)
- **Convergence** kombiniert Stabilität und Konsistenz. Quantifizierung über Gesamtfehler zwischen numerischer Lösung $\hat{f}(\tilde{x})$ und exakter Lösung $f(x)$ (Gleichung (19)):
$$\left|\hat{f}(\tilde{x}) - f(x)\right| \quad (19)$$
- "Due to symmetry we only consider the case $\tilde{x} = x + 0.25$."
- **Für $h = 1$:**
$$\left|\hat{f}_1(\tilde{x}) - f(x)\right| = \left|\hat{f}_1(-1) - f(-\tfrac{\pi}{2})\right| \;\to\; \left|\hat{f}_1(-0.75) - f(-\tfrac{\pi}{2})\right| = \left|\hat{f}_1(-1) - f(-\tfrac{\pi}{2})\right| = |-0.84147 - (-1)| = 0.1599$$
  [Anm.: Notation der Zeilenfolge im Original gestapelt ohne Gleichheitszeichen: $|\hat{f}_1(\tilde{x}) - f(x)|$, $|\hat{f}_1(-1) - f(-\pi/2)|$, $|\hat{f}_1(-0.75) - f(-\pi/2)|$, $|\hat{f}_1(-1) - f(-\pi/2)|$, $|-0.84147-(-1)| = 0.1599$]
  [UNSICHER: Endwert 0.1599 vs. erwartet 0.15853 — so im Original gedruckt]
- **Für $h = 0.2$:**
$$\left|\hat{f}_{0.2}(\tilde{x}) - f(x)\right|: \; \left|\hat{f}_1(-1.2) - f(-\tfrac{\pi}{2})\right|, \; \left|\hat{f}_{0.2}(-0.95) - f(-\tfrac{\pi}{2})\right|, \; \left|\hat{f}_{0.2}(-1) - f(-\tfrac{\pi}{2})\right|, \; |-0.84147 - (-1)| = 0.1599$$
  [UNSICHER: gemischte Indizes $\hat{f}_1$ und $\hat{f}_{0.2}$ in den Zeilen sowie Punktwerte $-1.2$, $-0.95$, $-1$ — so im Original; Ergebnis beide Fälle 0.1599]

### [S. 33] Konvergenz-Interpretation, Compute-driven Error Analysis, Self-Reflection
- **Interpretation**: Wegen der Stabilitätsprobleme im Fall $h = 0.2$ verbessert sich die Konvergenz an diesem Operationspunkt **nicht** mit kleineren Schrittweiten. Zwei Erkenntnisse: beide numerischen Lösungen konvergieren zum gleichen Grenzwert; die Methode der iterativen Schrittweitenverkleinerung $h$ konvergiert ebenfalls zum gleichen Grenzwert. "Notice that we use the characteristics for both a numerical solution and the numerical method." (Begriffsdifferenzierung!)
- **Hands on compute-driven error analysis** (Übung): Brute-Force-Fehleranalyse des Zwei-Gleichungssystems aus Kapitel 1. "You will determine and optimize the conditioning, stability, consistency, and convergence of the numerical solution by optimizing the numerical method."
- **Self-Reflection and Recap** — Selbstreflexionsfragen:
  - "Compared to the numerical solution to the minimum of the sine function, how well conditioned is the two-equation system?"
  - "Does stability converge with smaller step sizes in the two-equation system? Against what?"
  - "How do perturbations in the input data affect the numerical solution of the two-equation system? Is there an interplay with step size?"
  - "Compare convergence with stability and consistency. What do you observe? Can you express your observations in terms of bias and variance?" (ML-Begriffe Bias/Varianz!)
  - "For ever smaller step sizes, do you observe a limit to the accuracy of the numerical solution? If so, why?"
  - "What is another problem you observe while refining the step size?"
- **Recap of Key Concepts:**
  - "Conditiioning [sic], Stability, Consistency, and Convergence" sind fundamentale Konzepte zum Verständnis des Verhaltens numerischer Algorithmen.
  - Diese Konzepte können qualitativ und quantitativ ausgedrückt werden, um numerische Lösungen und Methoden zu analysieren.

**Randnotizen [S. 33]:**
- *Code*: "is again to be found here https://github.com/Quillstacks/lecturecode_numericalmethods.git."
- *Teaser*: "So far we did brute-force numerical solutions. Can you think of a way to refine brute-force methods to get better results with less effort? Use the code of this lecture to design and test your idea." (Übungs-/Transferfrage → Überleitung zu effizienteren Methoden)

### [S. 34] Überleitung
- "Now that we understand and can characterize the behavior of individual numerical solutions, we can move on to understanding how to analyze entire numerical methods and algorithms. So far we have taken the assumption of where to look for a solution, inside a specific interval, for granted. This is usually not a given, and we will need to move away from local optimization methods in the next lecture."
- Rest der Seite leer.

---

# Kapitel 4: Newton Methods (S. 35–46)

### [S. 35] Kapitelbeginn
- Datums-/Build-Stempel: "2026-04-05 · regal coconut Wachtel"
- Abschnittstitel: **"A Step in the Right direction." / The Why**
- Rückblick: Im vorigen Kapitel wurden numerische Methoden mit Konditionierung, Stabilität, Konsistenz und Konvergenz charakterisiert. Aber die Brute-Force-Gittersuche ist fundamental limitiert: "it explores the solution space blindly, requiring $O(N^d)$ evaluations for $N$ grid points in $d$ dimensions." (Komplexitätsangabe — Fluch der Dimensionalität!)
- **The key insight** "is deceptively simple: instead of asking 'what is the value here?' at every grid point, we also ask 'which way should I go next?'. The function's slope, its derivative, tells us the direction towards the solution. This transforms search fundamentally."
- Diese Methoden zu verstehen erlaubt:
  - Lokale Information für ausgefeilte Schritte statt Brute-Force-Suchen nutzen.
  - Schnellere und optimalere Konvergenz erreichen.
- **ML/DL-Bezug**: "In Machine Learning and Deep Learning, Newton's method simplified to first order is also known as gradient descent. One could argue that the entire field of deep learning is built on the idea of using local gradient information to navigate toward minima in a high-dimensional loss landscape, to train models that are optimized towards specific objectives."

**Randnotiz [S. 35]:** *Backpropagation*: "is of course as vital to distribute gradient information through the layers of a neural network, but the core optimization step is still a form of gradient-based navigation."

### [S. 36] Hands On Experience: Grid Search vs. Newton
- Intuition für die Kraft lokaler Information: Vergleich Grid Search vs. Newton-Methode an derselben Sinusfunktion aus Kapitel 3, aber jetzt **Nullstellensuche**: $\sin(x) = 0$ auf dem Intervall $[2.5, 4]$ ("the solution is near $\pi \approx 3.14159$").
- **Abbildung (Figure 14):** "Continuous curve $f(x) = \sin(x)$ on $[2.5, 4]$, and discretized points with step size $h = 0.3$." — fallende Sinuskurve mit Punkten.
- **Grid Search auf $[2.5,4]$ mit Schritt $h = 0.3$ "evaluates blindly"** (vollständige Werte):
$$f(2.5) \approx 0.599$$
$$f(2.8) \approx 0.335$$
$$f(3.1) \approx 0.042 \quad \leftarrow \text{closest to zero}$$
$$f(3.4) \approx -0.256$$
$$f(3.7) \approx -0.530$$
$$f(4.0) \approx -0.757$$
- Ergebnis: "We found $x \approx 3.1$ with 6 evaluations, with an error $|3.1 - \pi| \approx 0.042$."
- **Newton's method** hat einen adaptiven Suchansatz: An jedem Punkt werden Funktion und Ableitung ausgewertet; diese lokale Information wird genutzt, um einen Schritt Richtung Lösung zu machen.
- **Abbildung (Figure 15):** "Newton's method iterations: starting from $x_0 = 3.5$, converging rapidly to $\pi \approx 3.14159$." — Kurve mit markierten Punkten: $x_0$ | 1st eval (bei 3.5, unterhalb der Achse), $x_1$ | 2nd eval, $x_2$ | 3rd eval (nahe $\pi$).
- **Derivative as source of local information**: $f'(x) = \cos(x)$ gibt die Steigung der Tangente an einem Punkt. "There are multiple …" (Fortsetzung S. 37)

**Randnotiz [S. 36]:** *We pay for this sophistication*: "with more hyperparameters that we need to determine and more complex computations (derivative evaluation and division), but we gain in convergence speed." (Trade-off-Warnung!)

### [S. 37] Newton-Iteration am Sinus (vollständige Rechnung) & Lernziele
- Fortsetzung: "… ways to use this information to derive the direction and the size of the next step: We for sure want to move in the direction where the function decreases, then we could take a step with fixed size, or we could make the step size proportional to the derivative. Let's just take the next guess where the tangent crosses zero for now – which is the solution to the linear approximation of $f$ at $x_n$."
- **Start bei $x_0 = 3.5$ (vollständige Rechnung):**
$$x_1 = x_0 - \frac{\sin(x_0)}{\cos(x_0)} = 3.5 - \frac{-0.351}{-0.936} = 3.5 - 0.375 = 3.125$$
$$x_2 = 3.125 - \frac{\sin(3.125)}{\cos(3.125)} = 3.125 - \frac{0.0008}{-0.9999} \approx 3.14159$$
  [Anm.: $0.0008/(-0.9999)$ ergibt negativen Wert, der subtrahiert wird → Zunahme; UNSICHER: Vorzeichendetails so im Original gedruckt]
$$x_3 \approx 3.14159, \quad \text{und } \sin(3.14159) \approx 0$$
- Fazit: "After just 2 iterations, to be fair this means 4 function/derivative evaluations, we have $x \approx 3.14159$ with error $< 10^{-5}$. The derivative told us where to look way more efficiently than we have been used to." (Vergleich: Grid Search 6 Evaluationen, Fehler 0.042 vs. Newton 4 Evaluationen, Fehler $<10^{-5}$)
- **Lernziele des Kapitels:**
  - Newton-Raphson-Iteration für 1D-Nullstellensuche herleiten und anwenden.
  - Taylor-Entwicklung und ihre Rolle in Newtons Methode herleiten und verstehen ("understnad" [sic] im Original).
  - Konvergenzraten und Fehlermodi (failure modes) für Newtons Methode analysieren.
  - Sekantenverfahren (Secant method) verstehen und anwenden, wenn Ableitungen nicht verfügbar sind.

**Randnotiz [S. 37]:** *"Newton-Rhapson"* [sic, Schreibweise im Original]: "because Isaac Newton came up with the general idea, while Joseph Raphson simplified the approach into a practical iterative method." (historische Anmerkung)

### [S. 38] Newton-Raphson and Taylor Expansion
- **Abbildung (Figure 16):** "Newton's method geometric intuition: For $f(x) = x^2 - 2$, the tangent line at $(x_0, f(x_0))$ intersects the $x$-axis at $x_1$, our next approximation." — Parabel mit Tangente (gestrichelt) bei $(x_0, f(x_0))$ mit $x_0 = 2$, Schnittpunkt nahe 1.5; x-Achse 1.4 bis 2.2.
- Geometrische Intuition für eine einzelne Iteration. Formalisierung: Finde $x^*$ mit $f(x^*) = 0$.
- **Lineare Approximation** (Gleichung (20)):
$$f(x) \approx f'(x_n) \cdot (x - x_n) \quad \text{for } x \text{ close to } x_n + f(x_n) \quad (20)$$
  [UNSICHER: Layout im Original: "$f(x) \approx f'(x_n)\cdot(x-x_n)$ for $x$ close to $x_n$" mit $+ f(x_n)$ — vermutlich $f(x) \approx f(x_n) + f'(x_n)(x-x_n)$ gemeint, Zeilenumbruch im Satz]
- **Finding the next guess**: Wir wollen finden, wo diese lineare Approximation null kreuzt — "because this is our best guess for where the actual function crosses zero." Approximation null setzen (vollständige Herleitung):
$$0 = f(x_n) + f'(x_n) \cdot (x_{n+1} - x_n)$$
$$f'(x_n) \cdot (x_{n+1} - x_n) = -f(x_n)$$
$$x_{n+1} - x_n = -\frac{f(x_n)}{f'(x_n)}$$
- **Newton-Raphson-Iterationsformel** (Gleichung (21)):
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \quad (21)$$
- **Algorithmus 1: Newton-Raphson Method** (Pseudocode, vollständig):
  - **Require:** Initial guess $x_0$, function $f$, derivative $f'$, tolerance $\varepsilon$
  - 1: $x \leftarrow x_0$
  - 2: **while** $|f(x)| > \varepsilon$ **do**
  - 3: Compute derivative: $d \leftarrow f'(x)$
  - 4: **if** $|d| < \varepsilon_{\text{machine}}$ **then**
  - 5: **error** "Derivative too small"
  - 6: **end if**
  - 7: Update: $x \leftarrow x - f(x)/d$
  - 8: **end while** — **return** $x$

**Randnotiz [S. 38]:** *Note*: "This linear approximation is the first-order Taylor expansion of $f$ around $x_n$. We'll return to Taylor expansions later when we study accuracy and approximation formally."

### [S. 39] Taylor Expansion
- Bisher haben wir der linearen Approximation bei $x_n$ einfach vertraut (Gleichung (22)):
$$f(x) \approx f'(x_n)(x - x_n) + f(x_n) \quad (22)$$
  um schnell den nächsten Guess $x_{n+1}$ zu finden und schließlich zur Wurzel zu konvergieren — "but is that trust well placed?"
- Antwort: **Taylor-Entwicklung** — "a fundamental tool that tells us how well polynomials approximate smooth functions at a given point." Herleitung "from first principles", um zu verstehen, warum die lineare Approximation eine gute Wahl für Newton ist und wie man sie systematisch verbessern kann. Illustration: schrittweise Approximation der Sinusfunktion.
- **Abbildung (Figure 17):** "Continuous curve $f(x) = \sin(x)$ and its discretized version (black dots) on $[-3,1]$ with step size $h = 1$." [Anm.: Bildunterschrift erwähnt Punkte; Plot zeigt durchgezogene Sinuskurve]
- **0th Order: Match the function value.** Gesucht Polynom $P(x)$, das $f(x)$ nahe $x_n$ approximiert. Start: Übereinstimmung am Punkt selbst (Gleichung (23)):
$$P(x_n) = f(x_n) \quad (23)$$
  "This comes very close to what grid search does: it only looks at the function value at discrete points, without any information about how the function behaves between those points." (Analogie Grid Search ↔ 0. Ordnung!)
- **1st Order: Match the first derivative.** Nahe $x_n$ zählt die Steigung. Wir wollen $P'(x_n) = f'(x_n)$. Linearen Term hinzufügen (Gleichung (24)):
$$P(x) = f(x_n) + f'(x_n)(x - x_n) \quad (24)$$

**Randnotizen [S. 39]:**
- *This error*: "occurs when the derivative $f'(x_k)$ approaches zero, which would cause division by zero or numerical instability in Newton's method." (bezieht sich auf den Fehlerfall im Algorithmus 1 von S. 38)
- *Smooth*: "A function is smooth if it has derivatives of all orders, and is thus differentiable." (Definition Glattheit)

### [S. 40] Taylor 2. Ordnung & allgemeines Muster
- **Abbildung (Figure 18):** "Continuous curve $f(x) = \sin(x)$ with constant approximation $P(x) = f(-1)$ (black dashed line) anchored at $x = -1$ (black dot)." — horizontale gestrichelte Linie bei $\approx -0.84$.
- **Abbildung (Figure 19):** "Continuous curve $f(x) = \sin(x)$ with linear approximation $P(x) = f(-1) + f'(-1)(x+1)$ (black dashed tangent line) anchored at $x = -1$ (black dot)." — Tangente.
- **2nd Order: Match the second derivative.** "The curvature captures how the slope changes." Wir wollen $P''(x_n) = f''(x_n)$. Quadratischen Term hinzufügen (Gleichung (25)):
$$P(x) = f(x_n) + f'(x_n)(x - x_n) + \frac{f''(x_n)}{2}(x - x_n)^2 \quad (25)$$
- **Abbildung (Figure 20):** "Continuous curve $f(x) = \sin(x)$ with quadratic approximation $P(x) = f(-1) + f'(-1)(x+1) + \frac{f''(-1)}{2}(x+1)^2$ (black dashed parabola) anchored at $x = -1$ (black dot)." — Parabel schmiegt sich an.
- **nth Order: General pattern.** Die **Taylor-Entwicklung** einer Funktion $f$ um einen Punkt $x_n$:
$$f(x) = f(x_n) + f'(x_n)(x - x_n) + \frac{f''(x_n)}{2!}(x - x_n)^2 + \frac{f'''(x_n)}{3!}(x - x_n)^3 + \cdots$$
  Oder kompakter (Gleichung (26)):
$$f(x) = \sum_{k=0}^{\infty} \frac{f^{(k)}(x_n)}{k!}(x - x_n)^k \quad (26)$$

**Randnotizen [S. 40]:**
- *Why divide by 2?*: "When we differentiate $(x - x_n)^2$ twice, we get 2. So if we want $P''(x_n) = f''(x_n)$, we need to divide by 2 to cancel this factor." (Begründung der Fakultätsfaktoren)
- *Around a point*: "Visually we can see that the approximations are anchored on a specific point $x_n$. The Taylor expansion is a local approximation." (Wichtig: lokale Approximation!)

### [S. 41] Warum linear reicht & Herleitung der Konvergenzrate
- **Why linear is enough for Newton?** "We want to solve $f(x^*) = 0$, not compute $f(x)$ as best as we can. Improving an approximation of course comes with a cost: We need to compute higher derivatives and evaluate more complex polynomials. In numerical computations we always need to decide where to cut off the Taylor series. We do so at some finite order, and the linear term is the first non-constant term that gives us directional information."
- **Deriving the convergence rate.** Erinnerung an Kapitel 3: Eine Methode ist konvergent, wenn die Approximation einen spezifischen stabilen Grenzwert erreicht. Für Newton mit Wurzel $x^*$, $f(x^*) = 0$, wollen wir (Gleichung (27)):
$$|x_n - x^*| \to 0 \quad \text{as } n \to \infty \quad (27)$$
- Dank Taylor können wir quantifizieren, **wie schnell** der Fehler abnimmt. Sei $e_n = x_n - x^*$ der Fehler bei Iteration $n$. 2.-Ordnung-Taylor von $f$ um die wahre Wurzel $x^*$ (Gleichung (28)):
$$f(x_n) = f(x^*) + f'(x^*)(x_n - x^*) + \frac{f''(\xi)}{2}(x_n - x^*)^2 \quad (28)$$
  wobei $\xi$ ein Punkt zwischen $x_n$ und $x^*$ ist (Lagrange-Restglied). Da $f(x^*) = 0$, vereinfacht sich das zu (Gleichung (29)):
$$f(x_n) = f'(x^*) \cdot e_n + \frac{f''(\xi)}{2} e_n^2 \quad (29)$$
  "Where $e_n = x_n - x^*$ is the error at iteration $n$."
- **Now apply Newton's formula** (vollständige Herleitung):
$$e_{n+1} = x_{n+1} - x^* = x_n - \frac{f(x_n)}{f'(x_n)} - x^* = (x_n - x^*) - \frac{f(x_n)}{f'(x_n)} = e_n - \frac{f(x_n)}{f'(x_n)}$$
- Vereinfachte Taylor-Entwicklung für $f(x_n)$ einsetzen (Gleichung (30)):
$$e_{n+1} = e_n - \frac{f'(x^*) \cdot e_n + \frac{f''(\xi)}{2} e_n^2}{f'(x_n)} \quad (30)$$
- **Für Punkte nahe $x^*$**: Annahme $f'(x_n) \approx f'(x^*)$ (Gleichung (31)):
$$e_{n+1} \approx e_n - \frac{f'(x^*) \cdot e_n + \frac{f''(\xi)}{2} e_n^2}{f'(x^*)} = e_n - e_n - \frac{f''(\xi)}{2 f'(x^*)} e_n^2 \quad (31)$$

**Randnotiz [S. 41]:** *Notice the assumption play out*: "$10^{-1} \to 10^{-2} \to 10^{-3} \to 10^{-6} \to 10^{-12}$. Once we're close enough and our assumptions hold (after iteration 2), the error squares perfectly, demonstrating quadratic convergence." (Beispielfolge der Fehlerentwicklung — anfangs nicht quadratisch, erst wenn nah genug!)

### [S. 42] Quadratische Konvergenz, $\sqrt{2}$-Beispiel & Fehlermodi
- Der Fehlerterm 1. Ordnung kürzt sich, übrig bleibt (Gleichung (32)):
$$e_{n+1} \approx -\frac{f''(\xi)}{2 f'(x^*)} e_n^2 \quad (32)$$
- **Abstrakter** (Gleichung (33)):
$$|e_{n+1}| \leq C \cdot |e_n|^2 \quad (33)$$
  "Which means that the error at the next iteration is approximately proportional to the square of the current error, where $C$ is a constant that depends on the function's curvature and slope at the root."
- **"This is quadratic convergence."**
- **Beispiel: Berechnung von $\sqrt{2}$** mit Newton ab $x_0 = 2$ ("our introductory example" [Anm.: Tabelle erscheint hier erstmals]):

**Tabelle (Table 2):** "Newton's method for computing $\sqrt{2}$. See how the error approximately squares each iteration."
| $n$ | $x_n$ | $|e_n|$ (error) |
|---|---|---|
| 0 | 2.000000000 | $5.86 \times 10^{-1}$ |
| 1 | 1.500000000 | $8.58 \times 10^{-2}$ |
| 2 | 1.416666667 | $2.45 \times 10^{-3}$ |
| 3 | 1.414215686 | $2.13 \times 10^{-6}$ |
| 4 | 1.414213562 | $4.5 \times 10^{-12}$ |

- **Newton's method can fail** "in several ways, which we will endure for now, and for which we will find solutions later on. As a brain teaser, it is a nice exercise to visualize the failure modes in this plot:"
- **Abbildung (Figure 21):** "$f(x) = x^3 - x$ has multiple roots. Newton's method can fail in several ways: zero derivative (if $f'(x_n) = 0$, the tangent is horizontal and doesn't cross the axis), oscillation (especially for symmetrical functions Newton can cycle between points), and ambiguous starting point selection ($x_0$, heavily influences which root is found)." — Kubik mit Nullstellen bei ca. $-0.2$/0 und 1 markiert (schwarze Punkte bei 0 und 1); x-Achse $-0.4$ bis $1.4$. (Drei Fehlermodi: Nullableitung, Oszillation, Startpunktabhängigkeit!)
- **"Now something we can not endure, is if we can't compute $f'(x)$."** (Überleitung zum Sekantenverfahren)

**Randnotiz [S. 42]:** *This can happen because*:
  - "The derivative is expensive to compute."
  - "The function is given as a black box (e.g., a simulation)."
  - "The function isn't differentiable everywhere."

### [S. 43] Secant Method (Sekantenverfahren)
- "Here comes a clever way to approximate the derivative using only function evaluations, eliminating the need for an explicit derivative."
- **A poor man's derivative.** Ableitung mit zwei letzten Punkten approximieren:
$$f'(x_n) \approx \frac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}$$
- Visuell: Steigung der Sekante durch die Punkte $(x_{n-1}, f(x_{n-1}))$ und $(x_n, f(x_n))$ auf dem Graphen von $f$.
- **Abbildung (Figure 22):** "Secant method: the line through $(x_0, f(x_0))$ and $(x_1, f(x_1))$ gives the next approximation $x_2$." — Kurve ($x^2-2$-artig) mit Sekante (gestrichelt) durch $(x_0, f(x_0))$ bei $x_0 \approx 1$ und $(x_1, f(x_1))$ bei $x_1 = 2$; offener Kreis beim Achsenschnitt ($x_2 \approx 1.33$).
- **Note**: Man braucht **zwei Startwerte** $x_0$ und $x_1$, statt nur einem wie bei Newton.
- Einsetzen in Newtons Formel ergibt die iterative Sekantenmethode (Gleichung (34)):
$$x_{n+1} = x_n - f(x_n) \cdot \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})} \quad (34)$$
- **Algorithmus 2: Secant Method** (Pseudocode, vollständig):
  - **Require:** Initial guesses $x_0$, $x_1$, function $f$, tolerance $\varepsilon$
  - 1: **while** $|f(x_1)| > \varepsilon$ **do**
  - 2: Compute secant slope: $s \leftarrow (f(x_1) - f(x_0))/(x_1 - x_0)$
  - 3: Store previous: $x_{\text{old}} \leftarrow x_1$
  - 4: Update: $x_1 \leftarrow x_1 - f(x_1)/s$
  - 5: $x_0 \leftarrow x_{\text{old}}$
  - 6: **end while** — **return** $x_1$

### [S. 44] Examples & Exercises: Newton by hand
- **Abbildung (Figure 23):** "$f(x) = x^3 - x$ has multiple roots. We assume the root at $x = 1$ is the target. The gray dashed line shows the derivative $f'(x) = 3x^2 - 1$." — Kubik (schwarz) und Ableitung (grau gestrichelt, Parabel) auf $[-0.4, 1.4]$; Punkt bei $x = 1$; offener Kreis bei $x_0 = 1.4$.
- **Newton by hand.** Aufgabe: Nullstelle von $f(x) = x^3 - x = 0$ — erst geometrisch, dann von Hand. "The roots are at $x = -1, 0, 1$. Let's find the root at $x = 1$ starting from $x_0 = 1.4$."
- 1.-Ordnung-Taylor um $x_n$:
$$f(x) \approx f(x_n) + f'(x_n)(x - x_n),$$
$$f(x_n) \approx f(x) - f'(x_n)(x - x_n)$$
- Mit $f(x) = x^3 - x = 0$, $f'(x) = 3x^2 - 1$, umstellen für den nächsten Guess ab $x_0 = 1.4$ (**vollständige Rechnung**):
$$x_1 = x_0 - \frac{f(x_0)}{f'(x_0)} = x_0 - \frac{x_0^3 - x_0}{3x_0^2 - 1} = 1.4 - \frac{2.744 - 1.4}{5.88 - 1} = 1.4 - \frac{1.344}{4.88} \approx 1.127$$
$$x_2 = 1.127 - \frac{1.127^3 - 1.127}{3(1.127)^2 - 1} \approx 1.127 - \frac{0.432}{2.808} \approx 0.976$$
$$x_3 = 0.976 - \frac{0.976^3 - 0.976}{3(0.976)^2 - 1} \approx 0.976 - \frac{-0.072}{1.857} \approx 1.014$$
- "The root at $x = 1$ is found quickly." (Beachte: Iterationen oszillieren leicht um 1: 1.127 → 0.976 → 1.014)
- **Secant by hand.** Sekantenverfahren auf dasselbe Problem anwenden mit $x_0 = 1.2$, $x_1 = 1.4$. "Again first geometrically, then by hand." (Fortsetzung S. 45)

**Randnotiz [S. 44]:** *Code*: "can be found at https://github.com/Quillstacks/lecturecode_numericalmethods.git."

### [S. 45] Secant by hand (Rechnung), Failure Search, Self-Reflection
- **Vollständige Sekanten-Rechnung** ($f(x) = x^3 - x$; $f(1.2) = 0.528$ [im Original als 0.128 in Differenz? siehe unten], $f(1.4) = 0.744$):
$$x_2 = x_1 - f(x_1) \cdot \frac{x_1 - x_0}{f(x_1) - f(x_0)} = 1.4 - (0.744) \cdot \frac{1.4 - 1.2}{0.744 - 0.128}$$
  [Anm.: Original verwendet $f(x_0) = f(1.2) = 0.128$; tatsächlich $1.2^3 - 1.2 = 0.528$. UNSICHER/möglicher Druckfehler im Original: 0.128 statt 0.528]
$$= 1.4 - 0.744 \cdot \frac{0.2}{0.616} \approx 1.4 - 0.241 \approx 1.159$$
$$x_3 = 1.159 - f(1.159) \cdot \frac{1.159 - 1.4}{f(1.159) - f(1.4)} \approx 1.159 - (0.283) \cdot \frac{-0.241}{0.283 - 0.744} \approx 1.159 - 0.283 \cdot \frac{-0.241}{-0.461} \approx 1.159 - 0.283 \cdot 0.522 \approx 1.159 - 0.148 \approx 1.011$$
- **Geometrical Failure Search** (Übungsaufgabe): "Find starting points $x_0$ for different failure modes: One where Newton's method fails due to zero derivative, one where it converges to a non-target root, and one where it oscillates between points."
- **Enter the machine** (Übung): Konvergenz und Konvergenzraten von Grid-Search, Newton und Sekantenverfahren in Python ansehen. Mit verschiedenen Startpunkten experimentieren ("differentstarting points" [sic]) und Fehlermodi in der Praxis beobachten. "Try to first find the starting points geometrically, then try finding them analytically, before finally moving over to verifying in code."
- **Self-Reflection and Recap** — Selbstreflexionsfragen:
  - "What is the main advantage of using Newton's method over Grid-Search?"
  - "Why is a linear approximation sufficient for finding roots? What does the Taylor expansion tell us about this choice?"
  - "Why is quadratic convergence so powerful? How many iterations would Newton need to go from error $10^{-1}$ to error $10^{-16}$?" (Rechenfrage — Antwort implizit: ca. 4 Iterationen wegen Quadrierung)

### [S. 46] Recap & Überleitung
- Weitere Selbstreflexionsfrage: "In what situations would you prefer Secant over Newton? Why not in others?"
- **Recap of Key Concepts:**
  - "Newton-Raphson gives (limited) convergence guarantees near simple roots."
  - "Taylor expansion provides a systematic way to approximate functions locally."
  - "You saw how Taylor expansion justifies the linear approximation in Newton's method and explains its quadratic convergence and allows to estimate the error in each iteration."
  - "In situations where the derivative is difficult to compute, the Secant method approximates the derivative from two points and converges."
- **Local methods find local solutions.** "Newton converges to whatever optimum is nearby, it is also prone to oscillate between points, or diverge if the derivative is zero or near zero. In the next chapter, we will reformulate the root finding into an optimization problem. And from there we'll explore how to go on and handle global optimization when the landscape has many valleys or is otherwise pathologically difficult."

**Randnotiz [S. 46]:** *Teaser*: "How can we make sure that we find the global solution, and not just a local one?"

---

# Kapitel 5: Global Optimization (S. 47–56)

### [S. 47] Kapitelbeginn
- Datums-/Build-Stempel: "2026-05-06 · feisty cranberry Hermelin"
- Abschnittstitel: **"And then there were many." / The Why**
- Rückblick: Newton-Methode und Gradient Descent für Nullstellensuche entwickelt. "The methods we learned about are local methods: They converge to whatever solution is nearby. But what if the nearby solution is bad? Or if another solution is much better but farther away?"
- **Time to do away with oversimplifications.** In diesem Kapitel:
  - "Learn about Shekel's foxholes, a classic test function for global optimization"
  - "Shortly show, how we can formulate an optimization problem as a root-finding problem."
  - "Introduce strategies for finding global minima"
- **ML/DL-Bezug**: "In machine learning and especially deep learning, understanding multi-dimensional and global optimization is crucial for training large models effectively, and to make them converge, and actually learn something useful. Neural network loss landscapes (Fußnote 8) are highly non-convex, do have flat regions, and contain many local minima, making optimization challenging."

**Randnotizen [S. 47]:**
- *Visualization of neural network loss landscapes*: "Li et al. (2018) shows the complex terrain of neural network optimization. Different initializations lead to different final solutions."
- Fußnote 8: H. Li, Z. Xu, G. Taylor, C. Studer, T. Goldstein. "Visualizing the loss landscape of neural nets." 31:6389–6399, 2018. URL https://proceedings.neurips.cc/paper_files/paper/2018/file/a41b3bb3e6b050b6c9067c67f663b915-Paper.pdf

### [S. 48] Hands On Experience: Shekel's Foxholes
- **Shekel's foxholes**: klassische Testfunktion für globale Optimierung mit kontrollierter Multimodalität. In 1D (Gleichung (35)):
$$f(x) = -\sum_{i=1}^{m} \frac{c_i}{(x - a_i)^2 + r_i} \quad (35)$$
  - $a_i$ = "Foxhole"-Positionen (Fuchsbau-Standorte)
  - $c_i$ = kontrolliert die Tiefe jedes Lochs
  - $r_i$ = kontrolliert die Breite
- Durch Anpassen dieser Parameter kann man eine Landschaft mit mehreren lokalen Minima und einem globalen Minimum erzeugen — "an ideal playground for testing optimization algorithms."
- **Konkretes Beispiel mit drei Foxholes:**
$$f(x) = -\frac{1}{(x-0)^2 + 0.7} - \frac{1.7}{(x-4)^2 + 0.2} - \frac{1.1}{(x-7)^2 + 0.4}$$
- **Abbildung (Figure 24):** "A 1D Shekel's foxholes function (black) with three local minima and its derivative (gray dashed). The function has valleys at $x = 0, 4, 7$, with the deepest (global minimum) at $x = 4$. The derivative (dashed line) crosses zero at each minimum." — Plot auf $[-2, 12]$, tiefste Talsohle bei $x=4$ (Wert ca. $-8.5$).
- **Das globale Minimum** ist bei $x = 4$. Die anderen beiden Minima bei $x = 0$ und $x = 7$ sind lokale Minima. "This information is of course not available to us when we run an optimization algorithm. We only see the function values and gradients at the points we evaluate. But the knowledge comes in handy for exploring the behavior of optimization methods."
- **The sensitivity to initial conditions** von $x_0$: "If we start Newton's method near $x = 0$ or $x = 7$, we'll converge to a local minimum, not the global one at $x = 4$."
- **Let's apply Newton's method** auf die 1D-Shekel-Funktion (Fußnote 9) von verschiedenen Startpunkten und beobachten, wohin die Methode konvergiert. "Let's show it for one starting point, try another one yourself, and then we will discuss the general behavior." (Übungsaufforderung!)

**Randnotizen [S. 48]:**
- *The derivative*: "illustrated as the dashed line is the answer to formulating optimization as root finding. The minima of $f(x)$ correspond to the roots of $f'(x)$." (Schlüsselidee!)
- Fußnote 9: J. Shekel. "Test functions for multimodal search techniques." 1971 (Literaturverweis)

### [S. 49] Newton zur Optimierung am Shekel-Beispiel (vollständige Rechnung)
- **Von $x_0 = 7.2$**: Newton konvergiert zum lokalen Minimum bei $x \approx 7$. Um Newton auf Optimierung anzuwenden, lösen wir das Nullstellenproblem auf $f'(x) = 0$ (Reformulierung des Optimierungsproblems). **Newton-Update wird** (Gleichung (36)):
$$x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)} \quad (36)$$
- **Abbildung (Figure 25):** "A 1D Shekel's foxholes function's first derivative (black), and second derivative (gray dashed). The function has valleys at $x = 0, 4, 7$, with the deepest (global minimum) at $x = 4$. The first derivative crosses zero at each minimum, and the second derivative is positive at minima (confirming local curvature)." — Plot auf $[-2,12]$.
- **Die Ableitungen vereinfachen sich zu** (vollständige Formeln):
$$f'(x) = \frac{2x}{(x^2 + 0.7)^2} + \frac{3.4(x-4)}{((x-4)^2 + 0.2)^2} + \frac{2.2(x-7)}{((x-7)^2 + 0.4)^2}$$
$$f'(7.2) \approx 0.005 + 0.100 + 2.27 = 2.38$$
$$f''(x) = \frac{2(0.7 - 3x^2)}{(x^2 + 0.7)^3} + \frac{3.4(0.2 - 3(x-4)^2)}{((x-4)^2 + 0.2)^3} + \frac{2.2(0.4 - 3(x-7)^2)}{((x-7)^2 + 0.4)^3}$$
$$f''(7.2) \approx -0.002 - 0.091 + 7.23 = 7.14$$
- **Iterationen:**
$$x_1 = 7.2 - \frac{2.38}{7.14} \approx 6.87$$
$$x_2 \approx 7.02$$
$$x_3 \approx 7.00$$
- "See how root finding methods can be used for optimization by applying them to the derivative of the function. The derivative $f'(x)$ is zero at extrema, so at this point we find minima or maxima." (Achtung: Minima ODER Maxima!)

**Randnotiz [S. 49]:** *Local minima notation*: "The asterisk (*) is conventionally reserved for global optima. To distinguish local from global minima, consider alternative notation like $x^\circ$ (x-circle) or $x_i$ for the $i$-th local minimum." (Notationskonvention)

### [S. 50] Das fundamentale Problem lokaler Optimierung & Lernziele
- "Here, we were unlucky, and the method is attracted to the nearby foxhole at $x^\circ \approx 7$."
- **The fundamental problem however is** "that local optimization only guarantees finding a nearby extrema. Even with convergence guarantees, we would have got lucky starting from $x_0 = 3$, but from $x_0 = -2$ or $x_0 = 8$, we miss the global minima. Enough motivation for the global optimization strategies we'll discuss next." (Konkrete Startpunkt-Beispiele: $x_0 = 3$ → Glück/global; $x_0 = -2$ oder $8$ → verfehlt)
- **Lernziele des Kapitels:**
  - "Explain why local methods cannot guarantee finding global minima"
  - "Apply strategies for finding global extrema"
  - "Understand how gradient descent helps to direct optimization towards minima"
- Rest der Seite leer.

### [S. 51] Global Optimization Strategies
- Formalisierung lokaler und globaler Extrema.
- **Lokale Optimierung** findet ein nahegelegenes Minimum (Gleichung (37)):
$$\mathbf{x}^* = \arg\min_{\mathbf{x} \in \mathcal{N}(\mathbf{x}_0)} f(\mathbf{x}) \quad (37)$$
  wobei $\mathcal{N}(\mathbf{x}_0)$ eine Nachbarschaft (neighborhood) des Startpunkts ist.
- **Globale Optimierung** findet das beste Minimum (Gleichung (38)):
$$\mathbf{x}^* = \arg\min_{\mathbf{x} \in \Omega} f(\mathbf{x}) \quad (38)$$
  wobei $\Omega$ die gesamte Suchdomäne ist. "It is easy to see how the search domain can be inifinitely [sic] large."
- **Convexity is the dividing line.** "For convex problems, any local method will find the global optimum. The difficulty arises in non-convex optimization, where the landscape contains multiple local minima, saddle points, and plateaus." (Konvexität als Trennlinie!)
- **Random restarts** — einfachste globale Strategie, "in its notion it feels like brute-forcing again":
- **Algorithmus 3: Random Restarts** (Pseudocode, vollständig):
  - **Require:** Search domain $\Omega$, local optimizer LocalOptimize, restarts $K$
  - 1: $\mathbf{x}_{\text{best}} \leftarrow$ None; $f_{\text{best}} \leftarrow +\infty$
  - 2: **for** $k = 1$ to $K$ **do**
  - 3: $\mathbf{x}_0 \leftarrow$ RandomPoint($\Omega$)
  - 4: $\mathbf{x}^* \leftarrow$ LocalOptimize($\mathbf{x}_0$)
  - 5: **if** $f(\mathbf{x}^*) < f_{\text{best}}$ **then**
  - 6: $\mathbf{x}_{\text{best}} \leftarrow \mathbf{x}^*$; $f_{\text{best}} \leftarrow f(\mathbf{x}^*)$
  - 7: **end if**
  - 8: **end for**
  - 9: **return** $\mathbf{x}_{\text{best}}$
- **Wahrscheinlichkeitsanalyse**: Wenn das Einzugsgebiet (basin of attraction) des globalen Minimums Wahrscheinlichkeit $p$ hat, dann mit $K$ Restarts (Gleichung (39)):
$$P(\text{find global}) = 1 - (1-p)^K \quad (39)$$
- **Zahlenbeispiel**: "For $p = 0.1$ and $K = 20$: $P = 1 - 0.9^{20} \approx 0.88$."
- **Praktischer Hinweis**: "Usually it is not possible to know $p$ in advance. A heuristic to set K without the knowledge of $p$ is to increase $K$ until the best solution stabilizes (no improvement after several restarts). **Patience**, is a common hyperparameter for this heuristic, which controls how many restarts we wait without improvement before stopping." (ML-Begriff Patience!)

**Randnotizen [S. 51]:**
- *$\mathcal{N}$ is a set*: "of points around $\mathbf{x}_0$. For example, $\mathcal{N}(\mathbf{x}_0) = \{\mathbf{x} : \|\mathbf{x} - \mathbf{x}_0\| < \epsilon\}$ for some radius $\epsilon$."
- *Convex vs. non-convex* (Definition!): "A function $f$ is *convex* if $f(\lambda x + (1-\lambda)y) \leq \lambda f(x) + (1-\lambda) f(y)$ for all $\lambda \in [0,1]$. For convex functions, every local minimum is the global minimum—local methods suffice. Non-convex functions (like Shekel's foxholes or neural network loss surfaces) are the hard case."
- *Neural network initialization*: "and training multiple networks with different seeds is implicit random restarts. However, this is not practical for large models." (ML-Bezug)

### [S. 52] Basin Hopping, Simulated Annealing, Stochastic Methods
- **Basin hopping** erkundet die Landschaft durch Abwechseln von lokaler Optimierung und zufälligen Sprüngen. "This is different from random restarts, which completely resets the search. Basin hopping allows us to escape local minima while still leveraging local optimization to find better solutions."
- **Algorithmus 4: Basin Hopping** (Pseudocode, vollständig):
  - **Require:** Initial point $\mathbf{x}_0$, local optimizer LocalOptimize, jump distribution for $\delta$, iterations $K$
  - 1: $\mathbf{x}_{\text{best}} \leftarrow \mathbf{x}_0$; $f_{\text{best}} \leftarrow f(\mathbf{x}_0)$
  - 2: $\mathbf{x}_{\text{current}} \leftarrow \mathbf{x}_0$
  - 3: **for** $k = 1$ to $K$ **do**
  - 4: $\mathbf{x}^* \leftarrow$ LocalOptimize($\mathbf{x}_{\text{current}}$)
  - 5: **if** $f(\mathbf{x}^*) < f_{\text{best}}$ **then**
  - 6: $\mathbf{x}_{\text{best}} \leftarrow \mathbf{x}^*$; $f_{\text{best}} \leftarrow f(\mathbf{x}^*)$
  - 7: **end if**
  - 8: Sample jump: $\delta \sim \mathcal{D}$
  - 9: $\mathbf{x}_{\text{current}} \leftarrow \mathbf{x}^* + \delta$ ▷ Random jump
  - 10: **end for**
  - 11: **return** $\mathbf{x}_{\text{best}}$
- Sprungverteilung (jump distribution): $\delta \sim \mathcal{D}$ — z. B. Gaußverteilung um Null zentriert oder Gleichverteilung über einen bestimmten Bereich.
- **Simulated annealing** kombiniert Basin Hopping mit einem probabilistischen Akzeptanzkriterium für Kandidatenpunkte. "In the beginning, when hopping into a worse solution, it is accepted with probability $\exp^{-\Delta f / T}$, where $T$ (temperature) decreases over time. Later on, the algorithm becomes more conservative and only accepts candidate points that improve the objective, allowing it to converge to an optimum."
- **Stochastic methods** fügen Rauschen hinzu, indem sie die Loss-Landschaft approximieren, um lokalen Optima zu entkommen. Beispielaufgabe: "Let's approximate the 1D shekels function as a second order function by picking three points on the foxhole curve."
- **The take away**: "the loss landscape is not static, but is to be engineered and formed. By approximating the loss landscape on mini-batches (different selection of points), we get a noisy estimate of the true loss landscape, which can help us escape local minima. The loss landscape is then of course heavily influenced by the choice …" (Fortsetzung S. 53)

**Randnotizen [S. 52]:**
- *Noisy Newton*: "follows the same idea around hopping, by adding Gaussian noise to the Newton step: $\mathbf{x}_{n+1} = ... + \boldsymbol{\xi}_n$."
- *$\Delta f$*: "is the increase in the objective function value when moving from the current solution to a worse candidate solution."

### [S. 53] Quadratische Approximation des Shekel & Newton für Minima
- **Abbildung (Figure 26):** "The original Shekel function (gray thin) with a second-order approximation (solid black) fitted through three sample points (dots). The derivative of the approximation is shown as a gray dashed line. The quadratic captures the general trend but smooths out the individual foxholes." — Parabel durch 3 Punkte (ca. bei $x \approx 4, 6.5, 8.5$) über die Foxholes hinweg.
- Fortsetzung von S. 52: "… of the loss function itself. That being said, the Newton step is very sensitive to noise, we will see other approaches that deal better with this." (Warnung: Newton rauschempfindlich!)
- **Newton's Method for finding Minima**: Im Hands-on gesehen — Reformulierung der Optimierung als Nullstellensuche erlaubt Newton zur Optimasuche (Gleichung (40)):
$$x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)} \quad (40)$$
- **Minima, maxima, and saddle points.** Newton findet Punkte mit $f''(x) = 0$ [Anm. so im Original gedruckt; gemeint ist $f'(x) = 0$ — UNSICHER/vermutlich Druckfehler], aber diese können Minima, Maxima oder Sattelpunkte sein. Der **Test mit der zweiten Ableitung (second derivative test)** unterscheidet sie:
  - (a) $f''(x^*) > 0$: lokales Minimum ("curve bends upward")
  - (b) $f''(x^*) < 0$: lokales Maximum ("curve bends downward")
  - (c) $f''(x^*) = 0$: nicht schlüssig ("inconclusive — possible saddle point or inflection point")
- **Um Newton nur Richtung Minima zu lenken**, Update modifizieren (Gleichung (41)):
$$x_{n+1} = x_n - \frac{f'(x_n)}{|f''(x_n)|} \quad (41)$$
- "In this way we ensure that we always move in the direction of decreasing $f(x)$. This forces the step to always move in the direction of the negative gradient (downhill so to speak)." (|f''|-Trick!)

**Randnotizen [S. 53]:**
- *In deep learning*: "we typically use local methods (SGD, Adam) but hope that: (1) most local minima are roughly equally good, (2) overparameterization makes bad minima rare, (3) mini-batch noise helps escape sharp minima, (4) adaptive learning rates help navigate plateaus." (Vier DL-Hoffnungen!)
- *How would you* (Übungsfrage): "modify the update to find maxima instead?"

### [S. 54] Abbildungen zum |f''|-Trick & Random-Restarts-Rechenbeispiele
- **Abbildung (Figure 27):** "Solid black: the first derivative $f'(x)$ of the 1D Shekel function; gray dashed: the second derivative $f''(x)$. The black marker at $x = 6.1$ is a sample location; the solid gray line is the tangent to $f'(x)$ at that point (slope $\approx -2.66$). The sign and magnitude of $f''(x)$ determine the Newton update direction and step size when solving $f'(x) = 0$."
- **Abbildung (Figure 28):** "Solid black: the first derivative $f'(x)$; gray dashed: the absolute curvature $|f''(x)|$. Marker at $x = 6.1$ shows the same sample point as above; the solid gray line illustrates replacing $f''(x)$ by $|f''(x)|$ (slope $\approx +2.66$). Using $|f''(x)|$ in the Newton denominator removes the curvature sign, enforcing downhill steps and reducing the chance of stepping toward a local maximum."
- **Examples & Exercises — "Let's put the strategies to work on concrete numbers":**
- **Aufgabe**: Funktion mit 5 lokalen Minima; Einzugsgebiet des globalen Minimums deckt 15 % der Suchdomäne ab ($p = 0.15$). "What is the probability of finding the global minimum with $K = 10$ random restarts?"
- **Vollständige Rechnung:**
$$P = 1 - (1 - 0.15)^{10} = 1 - 0.85^{10} = 1 - 0.1969 = 0.803$$
- "About 80% chance, not too bad, but far from certain. How many restarts do we need for 99%?"
$$K = \frac{\ln(1 - 0.99)}{\ln(1 - 0.15)} = \frac{\ln(0.01)}{\ln(0.85)} = \frac{-4.605}{-0.1625} \approx 28.3$$

**Randnotizen [S. 54]:**
- *Code*: "can be found at https://github.com/Quillstacks/lecturecode_numericalmethods.git."
- *Hint*: "Use $P = 1 - (1-p)^K$ and solve for $K$: $K = \frac{\ln(1-P)}{\ln(1-p)}$."

### [S. 55] Weitere Übungen (Global Optimization)
- "So $K = 29$ restarts." **Folgeaufgabe**: "Now compute $K$ for $p = 0.05$ and $p = 0.01$ at the same 99% target."
- **On your machine** (Übung): "you will first design your own custom 1D Shekel function. Keep it simple in the beginning, but come back later to make it more complex. Then first familiarize yourself with the local optimization methods you have learned so far, and apply them to your function. Show where Newton's method fails (again). Then explore different $x_0$ and see how the convergence behavior changes. Think again about the loss landscape and basin boundaries."
- **Directing the search towards minima** (Übung): "Remember the $|f''|$ trick, flips the sign of the curvature in the denominator, forcing the step to always go downhill. Think about what that means geometrically for the tangent line construction. Then try it in code."
- **Escaping Local Minima** (Übung): "by global optimization strategies. Deploy random restarts and basin hopping on your custom 1D Shekel function, and compare how many function iterations each method needs to find the global minimum. How prone are they to getting stuck in local minima? How does the choice of the step size distribution affect basin hopping's performance?"
- **Noise and landscape engineering** (Übung): "The loss landscape is not static, but is to be engineered and formed. By approximating the loss landscape on mini-batches (different selection of points)," [Anm.: Satz bricht im Original ab — unvollständiger Satz]
- **Code exercise**: "implement random restarts and basin hopping on the 1D Shekel function. Compare how many function evaluations each method needs to find the global minimum at $x \approx 4$."
- **Finally, let's map out the basins of attraction.** "Consider the 1D Shekel function and assume a local optimizer always converges to the nearest foxhole.2" [Anm.: ".2" vermutlich Tippfehler/Fußnotenrest im Original]
  - "(a) Sketch (roughly) the basins of attraction for the three foxholes at $x = 0, 4, 7$. Where are the basin boundaries?"
  - "(b) If basin hopping uses a jump of $\delta \sim \text{Uniform}(-3, 3)$ starting from the local minimum $x^\circ = 7$, what is the probability that a single jump lands in the basin of the global minimum?"
  - "(c) Why might basin hopping find the global minimum faster than random restarts here?"

**Randnotizen [S. 55]:**
- *Basin of Attraction* (Übung): "Revisit the plots of the Shekel function, mark the basins of attraction for each local minimum, and estimate their relative sizes. Which one is the global minimum? How does this relate to the probability of finding it with random restarts?"
- *Non-Convex Basins* (Übung): "Shekel in general is non-convex, however the basins are, note down a function, where the basins of attraction are not so easy to map out." (Aufgabe: Gegenbeispiel konstruieren!)
- *Can you think of* (Übung): "a smart way to automatically adjust the step size distribution during optimization? What would be a good heuristic to follow? How could you prevent disastrous jumps? Implement it."

### [S. 56] Self-Reflection and Recap (Global Optimization)
- **Selbstreflexionsfragen:**
  - "Why does local optimization fail on non-convex landscapes like Shekel's foxholes?"
  - "How does the required effort scale withthe [sic] size of the global basin when doing random restarts?"
  - "How do basin hopping differently from random restarts?" [sic — Grammatik im Original]
  - "What does $f''(x_n)$ tell us about the loss landscape, what does it characterize, and how can we put it to use?"
  - "How does approximating the loss landscape with noisy estimates (mini-batches) help escape local optima?"
  - "Choosing $x_0$ such that it lies in the basin of a local minimum, now find different ways such that your optimization method can escape it, how effective is what?"
- **Recap of Key Concepts:**
  - "Local optimization methods (like Newton's method) can get stuck in local minima on non-convex functions."
  - "Global optimization strategies (random restarts, basin hopping, simulated annealing, stochasticity) are designed to explore the search space more broadly to find the global optimum."
  - "Modifying optimization methods to use curvature information $f''(x)$ allows to specify the direction of descent more accurately."
  - "The loss landscape is ours to engineer through the choice of loss function and noise, such as stochastic gradients." (Loss Landscape Engineering!)
- **Gradient descent is prone to getting stuck.** "And so far our answer was merely better than brute-forcing out way out, yet again. In the next chapter, we will learn how to smoothen loss landscape to increase the robustness of our gradient descent approach."

**Randnotiz [S. 56]:** *Teaser*: "What if we now face a high-frequency version of Shekels foxholes. What is the problem that arises?"

---

# Kapitel 6: Numerical Integration (S. 57–69)

### [S. 57] Kapitelbeginn
- Datums-/Build-Stempel: "2026-05-04 · sneaky olive Falke"
- Abschnittstitel: **"Smooth Operator." / The Why** (Anspielung auf den Song)
- Rückblick: Globale Optimierungsstrategien zum Entkommen lokaler Minima. "Imagine you are optimizing a function with thousands of tiny, sharp local minima like a high-frequency version of Shekel's Foxholes. A gradient descent algorithm will get stuck instantly in the first microscopic pothole it finds."
- **Die Lösung**: "one that will feel familiar, but probably did go unnoticed until now: Numerical integration." (Gleichung (42)):
$$I = \int_a^b f(x)\,dx \quad (42)$$
- **Gute Gründe**, numerische Integration zu verstehen:
  - "as it allows us to smoothen the loss landscape and make optimization methods more robust."
  - "as it tends to find more robust optima due to the averaging effect (Fußnote 10) of a region."
- **DL-Bezug**: "In deep learning stochastic gradient descent (SGD) is the workhorse optimization algorithm. It is a Monte Carlo (Fußnoten 11, 12) method that estimates the gradient of the loss function by averaging over the gradient of a random mini-batch of data points. We are lucky to have numerical integration around, as it would be prohibitive expensive to train models on large-scale datasets."

**Randnotizen [S. 57]:**
- *Melts all your memories* "and change into gold" (grüner Text — Songzitat-Anspielung auf "Smooth Operator" von Sade)
- Fußnote 10: N. Keskar, D. Mudigere, J. Nocedal, M. Smelyanskiy, P. Tang. "On large-batch training for deep learning: Generalization gap and sharp minima." 09 2016. DOI: 10.48550/arXiv.1609.04836
- *Monte Carlo*: "is a strategy which basically solves problems by random sampling. Embrace the beauty:"
- Fußnote 11: J. Bergstra, Y. Bengio. "Random search for hyper-parameter optimization." *Journal of Machine Learning Research*, 13:281–305, 2012
- Fußnote 12: Y. Gal, Z. Ghahramani. "Dropout as a bayesian approximation: Representing model uncertainty in deep learning," 2016. URL https://arxiv.org/abs/1506.02142

### [S. 58] Hands On Experience: Hochfrequente Landschaften
- "We already know how to discretize a continuous function, and how to handle finite precision and systems with sparse information at discrete points."
- **Abbildung (Figure 29):** "Continuous curve $f(x) = \sin(x)$ and its discretized version (black dots) on $[-3,1]$ with step size $h = 0.2$."
- **Die Shekel-Funktion** als hochfrequente Funktion war eine Herausforderung für globale Optimierung, "yet did not render our general approaches obsolete. We still discretize and treat these functions as we are used to."
- **Abbildung (Figure 30):** "Continuous curve $f(x) = \sin(x) + \sin(2\pi x)$ and its discretized version (black dots) on $[-3,1]$ with step size $h = 0.2$." — stark oszillierende Kurve mit vielen lokalen Minima.
- "Taking a closer look at any local minima shows how the high-frequency loss landscape will nudge our optimization algorithm into the nearest local minimum. For example at $x = 0.6$ or $x = -0.4$." (konkrete Beispielstellen)
- **Abbildung (Figure 31):** "Continuous curve $f(x) = \sin(x) + \sin(2\pi x)$ and its discretized version (black dots) on $[-3,1]$ with step size $h = 0.2$." — [Anm.: Bildunterschrift identisch zu Fig. 30, aber Darstellung als graue Balken (Bar-Plot)]

### [S. 59] Glättung durch Integration (vollständiges Rechenbeispiel)
- **Consider approximation by numerical integration.** Betrachtung bei $x = -0.4$: statt direkt zu lösen (Gleichung (43)):
$$f(-0.4) = -0.97720 \quad (43)$$
  approximieren wir den Wert durch Integration mit Breite $h = 0.2$ (**vollständige Rechnung**, Trapez über $[-0.5, -0.3]$):
$$h \cdot f(-0.4) \approx \int_{-0.5}^{-0.3} f(x)\,dx \approx \frac{h}{2}[f(-0.5) + f(-0.3)] \approx 0.2 \cdot \frac{-1.14973 - 0.97720}{2} = -0.11285$$
$$f(-0.4) \approx \frac{-1.14973 - 0.97720}{2} = -1.06347$$
- **"This is a much better approximation having global optima in mind**, than the direct evaluation at $x = -0.4$ which gave us $-0.97720$. The numerical integration gave us a correction of the local loss landscape towards higher losses at this local minima. The next figure shows the effect of this smoothing on the whole curve."
- **Abbildung (Figure 32):** "Continuous curve $f(x) = \sin(x) + \sin(2\pi x)$ and its discretized version (black dots) on $[-3,1]$ with step size $h = 0.2$, and smoothed by numerical integration with interval length $h$." — geglättete Kurve, Oszillationen reduziert.
- **The smoothing** "becomes even more apparent when integrating over larger intervals in general, or in our engineered example when choosing $h$ such that the frequency of the noisy signal gets averaged out."
- **While you have seen** den Glättungseffekt durch die Intervallgröße: "the approximation of the interval so far is a pretty coarse approximation, relying on two points only." (Überleitung zu besseren Quadraturregeln)

**Randnotiz [S. 59]:** *What if* (Denkfrage/Grenzfall!): "we would be integrating over an interval which results in destructive inference [sic, gemeint: interference] of the underlying higher frequency sine curve? Think wavelengths."

### [S. 60] Geglättete Kurve & Lernziele
- **Abbildung (Figure 33):** "Continuous curve $f(x) = \sin(x) + \sin(2\pi x)$ and its discretized version (black dots) on $[-3,1]$ with step size $h = 0.2$, smoothed by neighbour averaging with $h = 0.48$ (so $h/2 = 0.24$ gets close to cancel the $\sin(2\pi x)$ component)." — fast glatte Sinuskurve: hochfrequenter Anteil durch geschickte Intervallwahl nahezu eliminiert. (Spezialfall: Wellenlängen-angepasste Glättung!)
- **Lernziele des Kapitels:**
  - "Derive and apply the midpoint method, trapezoid and Simpson's rules for numerical integration"
  - "Understand composite rules for improved accuracy"
  - "Know about Lagrange interpolation and how it relates to quadrature rules"
  - "Understand how the curse of dimensionality motivates Monte Carlo"
  - "Derive and apply Monte Carlo integration for high-dimensional problems"
  - "Apply Monte Carlo integration and recognize that batch averaging in ML is numerical integration"
- Rest der Seite leer.

### [S. 61] Methods of Numerical Intgration [sic — Tippfehler im Original]
- **Trivialste Approximation von Integralen**: ein einzelner diskretisierter Wert.
$$I = \int_a^b f(x)\,dx.$$
$$I = \frac{b-a}{n} \cdot f\left(\frac{a+b}{2}\right)$$
$$I = h \cdot f(m)$$
- "It is easy to see that the height of the rectangle is the value at the midpoint, and the width is $h$."
- **Verfeinerung**: $[a,b]$ in $n$ Teilintervalle gleicher Breite $h$ teilen und Beiträge summieren — **Riemann-Summen-Approximation (Riemann sum)**:
$$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n-1} \int_{x_i}^{x_{i+1}} f(x)\,dx \approx \sum_{i=0}^{n-1} h \cdot f(m_i)$$
  wobei $x_i = a + ih$ für $i = 0, 1, \ldots, n$.
- **Die Mittelpunktsregel (midpoint rule)** dieser zusammengesetzten Intervalle nutzt den Mittelpunkt (= Durchschnitt der Endpunkte) jedes Intervalls — "which often gives better results than left or right endpoint methods. Intuitively, this is because the midpoint approximates the curvature of the function better on the interval."
- **Abbildung (Figure 34):** "Continuous curve $f(x) = \sin(x)$ and midpoint rule integrals (gray bars) for $a = -2$, $b = -1$, $h = 0.5$. Black dots: midpoints. Circles: endpoints. The bars now touch, illustrating the midpoint rule without a gap." — zwei graue Rechtecke unter der Kurve auf $[-2,-1]$.
- "Increasing the number of subintervals reduces the error."

**Randnotizen [S. 61]:**
- *On the interval $[a,b]$*: "the midpoint value is $f(m)$. With left endpoint, the height is $f(a)$; with right endpoint, the height is $f(b)$."
- *Doubling the sub intervals*: "reduced error by $\sim 4\times$. This suggests $O(h^2)$ convergence." (empirische Konvergenzbeobachtung)

### [S. 62] Trapezregel & zusammengesetzte Trapezregel
- "This of course comes at the cost of more function evaluations, and thus more computational cost. So can we do better than approximating midpoints?"
- **Trapeze** "are more expressive geometrically than rectangles, and can capture linear changes in the function between the endpoints." (Gleichung (44)):
$$\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(a) + f(b)\right] \quad (44)$$
  wobei $h = b - a$.
- **Abbildung (Figure 35):** "Continuous curve $f(x) = \sin(x)$ and trapezoid rule areas (gray trapezoids) for $a = -2$, $b = -1$, $h = 0.5$. Black dots: endpoints. The area under the straight lines connecting endpoints illustrates the trapezoid rule approximation."
- **Composite Trapezoid Rule** (zusammengesetzte Trapezregel) wendet die Trapezregel auf jedes Teilintervall an und summiert (vollständige Herleitung):
$$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n-1} \int_{x_i}^{x_{i+1}} f(x)\,dx \approx \sum_{i=0}^{n-1} \frac{h}{2}\left[f(x_i) + f(x_{i+1})\right]$$
$$= \frac{h}{2}(f(x_0) + f(x_1)) + \frac{h}{2}(f(x_1) + f(x_2)) + \cdots + \frac{h}{2}(f(x_{n-1}) + f(x_n))$$
$$= \frac{h}{2}\left[f(x_0) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{n-1}) + f(x_n)\right]$$
$$= \frac{h}{2}\left[f(a) + 2\sum_{i=1}^{n-1} f(x_i) + f(b)\right]$$
  wobei $x_i = a + ih$ für $i = 0, 1, \ldots, n$.
- **Gewichtungserklärung**: "The function values at the endpoints $a$ and $b$ are each weighted by 1 in the formula, while all interior points are weighted by 2. Intuitively, this is because each interior point contributes to two adjacent trapezoids, while the endpoints only contribute to one trapezoid each. In your mind step through the circled enpoints [sic] in the figure above, and see how the interior points get counted twice, once as a right endpoint and once as a left endpoint, while the endpoints only get counted once."

**Randnotiz [S. 62]:** *Dividing the integral by $h$*: "gives us a weighted average of the function values, which is a better approximation to the integral than just using the midpoint or endpoints. Implicitly reflecting local curvature and information about the function's behavior across the interval."

### [S. 63] Simpson's Rule & Lagrange-Interpolation
- **Simpson's rule** "can capture curvature and thus often provides a much better approximation than the trapezoid rule. Following the idea of fitting a linear function, we fit a quadratic polynomial through 3 points instead of a line through 2. You will see Simpson's rule is exact for quadratic polynomials."
- **Abbildung (Figure 36):** "Continuous curve $f(x) = \sin(x)$ and Simpson's rule areas (gray, under the parabolas) for $a = -2$, $b = -1.5$, $h = 0.5$ and $a = -1.5$, $b = -1$, $h = 0.5$. Black dots: endpoints. Black dots: midpoints at $x = -1.75$ and $x = -1.25$. Solid line at $x = -1.5$ separates the two intervals. Each parabola illustrates the quadratic interpolant used by Simpson's rule on its subinterval."
- **Lagrange interpolation and quadrature.** "Lagrange interpolation constructs the unique polynomial of degree $\leq n$ that passes through given nodes $\{(x_j, y_j)\}_{j=0}^n$ using the basis" (Gleichung (45)):
$$L_j(x) = \prod_{\substack{m=0 \\ m \neq j}}^{n} \frac{x - x_m}{x_j - x_m} \quad (45)$$
- **Allgemeine Form eines quadratischen Polynoms** (durch $a$, $m$, $b$):
$$f(x) = f(a) \cdot \frac{(x-m)(x-b)}{(a-m)(a-b)} + f(m) \cdot \frac{(x-a)(x-b)}{(m-a)(m-b)} + f(b) \cdot \frac{(x-a)(x-m)}{(b-a)(b-m)}$$
- **Für ein symmetrisches Intervall**: Fläche unter $f(x)$ am besten approximiert mit Endpunkt-Gewichten $h/6$ und Mittelpunkt-Gewicht $2h/3$: "$A = C = h/6$, $B = 2h/3$ – we can verify this by integrating the Lagrange basis polynomials over $[a,b]$ and confirming that they yield these weights, but we omit the detailed calculation here. In a symmetric interval, the nodes are equally spaced: $x_0 = a$, $x_1 = m = \frac{a+b}{2}$, $x_2 = b$, so that the midpoint satisfies $m - a = b - m = h$."
- **Simpson-Formel**:
$$\int_a^b f(x)\,dx \approx \frac{h}{6} f(a) + \frac{2h}{3} f(m) + \frac{h}{6} f(b) = \frac{h}{6}[f(a) + 4f(m) + f(b)]$$
- **Composite Simpson's Rule**: wendet Simpson auf jedes Paar von Teilintervallen an und summiert ("assume $n$ is even and $x_i = a + ih$"). "Starting from the integral:" (Fortsetzung S. 64)

**Randnotiz [S. 63]:** *Try with some points*: "Start with $x = 0$ and see how the linear factors play out." (Übungshinweis zur Lagrange-Basis)

### [S. 64] Composite Simpson (Herleitung), Fehlertabelle & Curse of Dimensionality
- **Composite Simpson (vollständige Herleitung):**
$$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n-1} \int_{x_i}^{x_{i+1}} f(x)\,dx \approx \sum_{k=0}^{n/2-1} \frac{h}{6}\left[f(x_{2k}) + 4f(x_{2k+1}) + f(x_{2k+2})\right]$$
$$= \frac{h}{6}\left[f(x_0) + 4\sum_{k=0}^{n/2-1} f(x_{2k+1}) + 2\sum_{k=1}^{n/2-1} f(x_{2k}) + f(x_n)\right]$$
$$= \frac{h}{3}\left[f(x_0) + 4\sum_{\substack{i=1 \\ i \text{ odd}}}^{n-1} f(x_i) + 2\sum_{\substack{i=2 \\ i \text{ even}}}^{n-2} f(x_i) + f(x_n)\right]$$
  [Anm.: Faktorwechsel $h/6 \to h/3$ so im Original — bezieht sich vermutlich auf unterschiedliche $h$-Definitionen (Intervallbreite $2h$ vs. $h$); UNSICHER]
- **Practical advice: Stop at Simpson.** "For higher accuracy, use composite rules with more subintervals. High-degrees ($n \geq 8$) develop negative weights and become unstable." (Warnung!)
- **Tabelle (Table 3):** "Comparison of quadrature method accuracies. Higher-order methods achieve given accuracy with fewer function evaluations. $h$ is the step size, and $n$ is the number of evaluation points for Gaussian quadrature."

| Method | Single Interval Error | Accumulated Error |
|---|---|---|
| Left/Right | $O(h^2)$ | $O(h)$ |
| Midpoint | $O(h^3)$ | $O(h^2)$ |
| Trapezoid | $O(h^3)$ | $O(h^2)$ |
| Simpson's 1/3 | $O(h^5)$ | $O(h^4)$ |
| In General (Gaussian Quadrature) | $O(h^{2n})$ | $O(h^{2n-1})$ |

- **Monte Carlo & the Curse of Dimensionality**
- "For $d$-dimensional integrals, deterministic quadrature with $N$ points per dimension needs $N^d$ total points. There is no way to do this, let alone iterate on it during iterative optimization."
- **Random sampling** erlaubt Integralschätzung ohne volles Gitter. Integral als Erwartungswert (Gleichung (46)):
$$I = \int_\Omega f(\mathbf{x})\,d\mathbf{x} = |\Omega| \cdot \mathbb{E}_{\mathbf{X} \sim \text{Uniform}(\Omega)}[f(\mathbf{X})] \quad (46)$$
- "This identity means the definite integral equals the domain volume times the average value of $f$ under a uniform draw from $\Omega$. Practically this motivates a sampling estimator: draw points uniformly in $\Omega$, compute $f$ at those points, average the results, and multiply by $|\Omega|$ to estimate the integral."

**Randnotizen [S. 64]:**
- *What happens, when you approximate a linear function with a quadratic?* (Denkfrage/Grenzfall)
- *Runge's phenomenon*: "High-degree polynomial interpolation oscillates due to overfitting, leading to large errors at the edges of the interval." (Warnung; Begriff Overfitting als ML-Brücke)
- *A neural network with $d = 10^6$*: "or 1 million parameters would need $(N)^{10^6}$ grid points. Even $N = 2$ gives $2^{10^6}$, a number with 300,000 digits." (drastisches Curse-of-Dimensionality-Beispiel!)
- *$\Omega$*: "is the domain of integration, and $|\Omega|$ is its length. For a 1D integral over $[a,b]$, we have $|\Omega| = b - a$. For higher dimensions, it's the product of the lengths of each dimension."

### [S. 65] Monte Carlo: Bias, Varianz, Dimensionsunabhängigkeit, SGD
- **Monte Carlo uniform sampling auf $[-2,-1]$.** Sei $X \sim \text{Uniform}(-2,-1)$. Dann (Gleichung (47)):
$$I = \frac{|\Omega|}{N} \sum_{i=1}^{N} f(\mathbf{X}_i), \qquad \mathbf{X}_i \overset{\text{i.i.d.}}{\sim} \text{Uniform}(\Omega) \quad (47)$$
- **Abbildung (Figure 37):** "Continuous curve $f(x) = \sin(x)$ and midpoint rule integrals (gray bars) for $a = -2$, $b = -1$, $h = 0.5$. Circles: endpoints. The bars now touch, illustrating the midpoint rule without a gap." [Anm.: Caption ähnelt Fig. 34; Plot zeigt graues Band auf $[-2,-1]$ mit zufälligen Punkten (offene Kreise und gefüllter Punkt) — Monte-Carlo-Samples]
- **Bias.** "Because expectation is linear, this estimator is unbiased, meaning its expected value equals the true integral, for the number of $N \to \infty$:" (Gleichung (48)):
$$\mathbb{E}[\hat{I}_N] = I \quad (48)$$
- **Variance.** "The variance, a measure of the spread of the estimator around its mean, or how how [sic] large the error of the estimator can be, follows from independence of the samples:" (Gleichung (49)):
$$\text{Var}(\hat{I}_N) = \frac{|\Omega|^2}{N}\text{Var}(f(\mathbf{X})) = \frac{|\Omega|^2 \sigma_f^2}{N} \quad (49)$$
  wobei $\sigma_f^2 = \text{Var}(f(\mathbf{X}))$. Standardfehler (Gleichung (50)):
$$\text{SE}(\hat{I}_N) = \frac{|\Omega|\,\sigma_f}{\sqrt{N}} \quad (50)$$
- **Dimension independent.** "It is trivial to see, that for large $N$ the sampling error converges with, $O(1/\sqrt{N})$ for Monte Carlo, which makes it attractive in high dimensions. Quadrature rules outperform in terms of their convergence rates, but the convergence effort explodes with the dimension, as we need $N^d$ points to maintain the same accuracy." (Schlüssel-Trade-off: Quadratur schneller pro Dimension, MC dimensionsunabhängig!)
- **Convergence in SGD.** "Mini-batch gradients used in SGD are Monte Carlo estimates of the true gradient, based on a samples drawn into a batch. Increasing the batch size reduces variance roughly by $1/b$, directly analogous to the $1/N$ variance scaling above. This connection explains why batch size controls the noise–variance trade-off in training."

**Randnotizen [S. 65]:**
- *Midpoint rule*: "is a special case of Monte Carlo with $N = 1$ sample at the midpoint." (Spezialfall!)
- *i.i.d*: "independent and identically distributed, means that all $\mathbf{X}_i$ are not correlated and that they all come from the same underlying distribution."
- **Abbildung (Figure 38):** "Effect of batch size on gradient noise: smaller batches produce larger variance (showing up in the width of the training loss band) in the gradient estimate (Source: Stanford CS231n Note)." — verrauschte, abfallende Trainingskurve.
- Zusatznotiz zu Fig. 38: "As a beneficial side effect, computational cost is $n/b$ times cheaper per update step. For $n = 10^6$, and $b = 100$: SGD does 10,000 iterations with the compute GD needs for 1." (konkretes Zahlenbeispiel SGD vs. GD!)

### [S. 66] Examples & Exercises: Integration von Hand
- **Aufgabe**: Integral von $\sin(x)$ von $-2$ bis $-1$ mit verschiedenen Methoden berechnen. Für Fehlerquantifizierung zuerst der exakte Wert (**vollständige Rechnung**):
$$\tilde{I} = \int_{-2}^{-1} \sin(x)\,dx = [-\cos(x)]_{-2}^{-1} = -\cos(-1) + \cos(-2) \approx -0.9564491424$$
- **Midpoint rule by hand.** $\int_{-2}^{-1} \sin(x)\,dx$ mit $n = 1$ Intervall. Mittelpunkt $m = (-2 + (-1))/2 = -1.5$:
$$\hat{I} \approx (b - a) \cdot f(m) = 1 \cdot \sin(-1.5) \approx -0.99749$$
- Fehler: $|\tilde{I} - \hat{I}| \approx 0.04104$ — "which is the small difference between the midpoint estimate and the true value."
- **Midpoint rule with more intervals.** $n = 2$ Intervalle → zwei Mittelpunkte bei $-1.75$ und $-1.25$:
$$h = 0.5$$
$$\hat{I} \approx h \cdot [f(-1.75) + f(-1.25)] = 0.5 \cdot [\sin(-1.75) + \sin(-1.25)] \approx -0.927228$$
- Fehler: $|\tilde{I} - \hat{I}| \approx 0.02922$ — "which is smaller than the error with $n = 1$ interval, illustrating how composites, or increasing the number of intervals improves the approximation." [Anm.: 0.927228 weicht vom wahren Wert um ca. 0.0292 ab]
- **Trapezoid by hand.** Trapezregel für $\int_{-2}^{-1} \sin(x)\,dx$ mit $n = 2$ Intervallen. "The endpoints are $-2$, $-1.5$, and $-1$. The trape…" (Fortsetzung S. 67)

**Randnotiz [S. 66]:** *Further things worth trying*: "are to calculate the approximation on the endpoints of the interval, comparing the error." (Zusatzübung)

### [S. 67] Trapez, Simpson und Monte Carlo von Hand (vollständige Rechnungen)
- **Trapezregel (Forts. von S. 66)** — "…zoid rule gives us:":
$$h = 0.5$$
$$T_2 = \frac{h}{2}[f(-2) + 2f(-1.5) + f(-1)] = 0.25 \cdot [-0.90930 + 2(-0.99749) + (-0.84147)] \approx -0.927228$$
- **Wichtige Beobachtung**: "The error is the same as the midpoint rule with $n = 2$ intervals, which is not necessarily a coincidence, as both methods are second-order accurate and can yield similar results for certain functions and interval choices." (Spezialfall: gleiche Fehler bei Midpoint und Trapez!)
- **Simpson's rule by hand.** $\int_{-2}^{-1} \sin(x)\,dx$ mit $n = 2$ Intervallen, Endpunkte $-2$, $-1.5$, $-1$:
$$h = 0.5$$
$$S_2 = \frac{h}{3}[f(-2) + 4f(-1.5) + f(-1)] = \frac{0.5}{3} \cdot [-0.90930 + 4(-0.99749) + (-0.84147)] \approx -0.9564491424$$
- Fehler: "$|\tilde{I} - S_2| \approx 0.0000000000$, which is essentially zero, illustrating that Simpson's rule is exact for this particular integral, as $\sin(x)$ can be well approximated by a quadratic polynomial over the interval $[-2,-1]$." (Spezialfall: praktisch exakt!)
- **Monte Carlo by hand.** Monte-Carlo-Schätzung für $\int_{-2}^{-1} \sin(x)\,dx$ mit $N = 4$ Zufallsstichproben, "which is similar to the compute efforts of the trapezoid method." Angenommene Zufallsstichproben:
$$X_1 = -1.95, \quad f(X_1) = \sin(-1.95) \approx -0.92895,$$
$$X_2 = -1.55, \quad f(X_2) = \sin(-1.55) \approx -0.99978,$$
$$X_3 = -1.15, \quad f(X_3) = \sin(-1.15) \approx -0.91276,$$
$$X_4 = -1.05, \quad f(X_4) = \sin(-1.05) \approx -0.86742.$$
- **Monte-Carlo-Schätzwert:**
$$\hat{I} = (b - a) \cdot \frac{1}{N}\sum_{i=1}^{N} f(X_i) = 1 \cdot \frac{1}{4}(-0.92895 - 0.99978 - 0.91276 - 0.86742) \approx -0.927228$$

**Randnotiz [S. 67]:** *Try with more intervals*: "see how the error decreases and check whether you know your way around composites in Simpson's and Trapezoid rules." (Zusatzübung)

### [S. 68] Monte-Carlo-Fehlerschätzung & Hochdimensionale Übung
- Fehler des MC-Beispiels: "$|\tilde{I} - \hat{I}| \approx 0.02922$, which is the same as the midpoint method." (Zufall der Stichprobenwahl)
- **Alternative error estimation for Monte Carlo.** Für das konkrete Beispiel mit $N = 4$ und Stichprobenmittel $\bar{f} \approx -0.927228$. Mit dem **erwartungstreuen Stichprobenvarianz-Schätzer (unbiased sample variance estimator)** (Gleichung (51)):
$$Var(f(\mathbf{X})) = \frac{1}{N-1}\sum_{i=1}^{N}(f(X_i) - \bar{f})^2 \quad (51)$$
- **Stichprobenvarianz und Standardfehler des MC-Schätzers (vollständige Rechnung):**
$$\sigma_f^2 = Var(f(\mathbf{X})) \approx 0.003036,$$
$$\sigma_f \approx 0.05512,$$
$$\text{SE}(\hat{I}_N) \approx \frac{|\Omega|\,\sigma_f}{\sqrt{N}} = \frac{1 \cdot 0.05512}{2} \approx 0.02756.$$
- **Folgefrage**: "What happens if we increase $N$ to 16? The error should decrease by a factor of 2, since the standard error scales as $1/\sqrt{N}$. Briefly elaborate on how the error of the Monte Carlo estimator is dimension independant [sic]."
- **Enter higher dimensions on your machine** (Übung): "Implement Monte Carlo integration for a $d$-dimensional integral, such as integrating a multivariate Gaussian function over a hypercube. While slowly increasing $d$, observe how the error behaves for different methods. Even more, observe how grid-based quadrature methods become infeasible in terms of computational cost as $d$ grows. Optionally, see how similar effects arise in optimization by implementing gradient descent and mini-batch stochastic gradient descent on a high-dimensional function. Only watch compute times."

**Randnotiz [S. 68]:** *Code*: "can be found at https://github.com/Quillstacks/lecturecode_numericalmethods.git."

### [S. 69] Self-Reflection and Recap (Numerical Integration)
- **Selbstreflexionsfragen:**
  - "How does the error of the midpoint, trapezoid, Simpson's rule and Monte Carlo compare?"
  - "Why has the midpoint rule better accuracy than the left or right endpoint rules?"
  - "How does composite methods improve accuracy, and what is the trade-off?" [sic]
  - "Why do deterministic quadrature methods fail in high dimensions?"
  - "In which way, is the midpoint rule a special case of Monte Carlo estimation?"
  - "What is the intuition behind Monte Carlo not exploding in high dimensions?"
  - "When would you use Simpson's rule vs. Monte Carlo?"
  - "How is the mini-batch mean in SGD related to Monte Carlo estimation?"
  - "How does the gradient estimation in SGD help escape local minima?"
- **Recap of Key Concepts:**
  - "Deterministic quadrature methods (midpoint, trapezoid, Simpson's) approximate integrals using weighted sums of function values at specific points. They are accurate and converge fast for smooth, low-dimensional problems."
  - "Monte Carlo integration estimates integrals by averaging function values at random samples. It is unbiased and has a convergence rate of $O(1/\sqrt{N})$, making it independent of the dimensionality of the problem."
  - "In SGD, mini-batch gradients are Monte Carlo estimates of the true gradient."
- **Überleitung**: "So far stability referred to the sensitivity of the numerical solution to small changes in the input data. But we can also talk about stability in terms of the numerical method itself, and how it behaves …" (Fortsetzung S. 70)

**Randnotiz [S. 69]:** *Teaser*: "Why do high-order quadrature methods become unstable when approximating low-degree polynomials?" (Denkfrage, Bezug Runge/negative Gewichte)

### [S. 70] Abschluss-Überleitung
- Fortsetzung von S. 69: "… when approximating different types of functions. In the next chapter, we will see other types of stability issues that arise in numerical methods, and how to mitigate them by sophisticated method selection and configuration." (Ausblick auf nicht enthaltenes Folgekapitel — Notizen "unfinished")
- Rest der Seite leer.

### [S. 71] Index
Vollständiger Index mit Seitenverweisen (alphabetisch):
- absolute error, 21
- analytical, 10
- approximation, 12, 58
- basin hopping, 51
- brute-force method, 33
- catastrophic cancellation, 22–24
- complexity, 10
- complexity analysis, 46
- computation, 9
- conditioning, 25
- consistency, 25
- convergence, 25
- curse of dimensionality, 64
- derivative, 35
- discretization, 12, 58
- error, 14, 15
- error analysis, 24
- examples, 14
- exercises, 14, 54, 66
- fixed-point representation, 18, 21–23
- floating-point arithmetic, 17, 24
- floating-point representation, 17–19, 23, 24, 26
- global optimization, 46, 47, 51
- gradient descent, 35
- grid search, 14, 24
- hands-on, 48
- interval, 12, 58
- introduction, 9
- key concepts, 33
- license, 2
- linear approximation, 38
- linear systems, 10
- local information, 35
- local minima, 47
- local optimization, 51
- loss of significance, 18, 22–24
- machine epsilon, 18, 20, 23, 24
- model error, 25
- modeling error, 17, 18, 24
- Monte Carlo, 64
- Moore's Law, 9
- motivation, 9
- multimodal, 48
- Newton optimization, 53
- Newton failure modes, 42
- Newton method, 34
- Newton-Raphson, 38
- numerical algorithms, 33
- numerical integration, 56 (hands-on, 58; motivation, 57)
- numerical method, 33
- numerical solution, 33
- numerical stability, 17, 18, 23, 24
- pseudo-accuracy, 22, 24
- quadratic convergence, 41
- random restarts, 51
- recap, 15, 56, 69
- reflection, 15
- rounding error, 17, 18, 22–24
- Secant method, 42
- self-reflection, 33
- significant digits, 22, 24
- Simpson's rule, 62
- simulated annealing, 51
- stability, 25
- stepsize, 12, 58
- stochastic gradient descent, 56
- Taylor expansion, 39
- truncation error, 17, 18

---

## Abdeckungsübersicht (alle 71 Seiten)
- S. 1: Titelseite — erfasst
- S. 2: Copyright/Lizenz/Repo — erfasst
- S. 3: Mottozitat — erfasst
- S. 4: leer
- S. 5: Inhaltsverzeichnis — erfasst
- S. 6: leer
- S. 7: Introduction — erfasst
- S. 8: leer
- S. 9–16: Kapitel 1 "Enter Numerical Methods" — erfasst
- S. 17–24: Kapitel 2 "Floating-Point Arithmetic" — erfasst
- S. 25–34: Kapitel 3 "Error Analysis" — erfasst
- S. 35–46: Kapitel 4 "Newton Methods" — erfasst
- S. 47–56: Kapitel 5 "Global Optimization" — erfasst
- S. 57–70: Kapitel 6 "Numerical Integration" — erfasst
- S. 71: Index — erfasst
