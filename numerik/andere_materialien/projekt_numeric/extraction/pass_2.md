# Pass 2 — Formale Extraktion: "Numerical Methods" (Prof. Dr.-Ing. Mark Schutera)

Quelle: `Numerical Methods - notes_numerischemethoden.pdf` (71 Seiten, englischsprachige Vorlesungsnotizen, "Unfinished Lecture Notes").
Schwerpunkt dieses Passes: Formeln, Sätze, Beweise, Algorithmen, Notation, Konvergenzordnungen, Fehlerschranken, Konditionszahlen, exakte numerische Werte. Seitenangaben `[S. n]` beziehen sich auf die aufgedruckte Seitenzahl im PDF.

---

## Titelei und Vorspann

**[S. 1 (Titelblatt, ohne aufgedruckte Nummer)]** Titelseite: "PROF. DR.-ING. MARK SCHUTERA — NUMERICAL METHODS — UNFINISHED LECTURE NOTES". Kein mathematischer Inhalt.

**[S. 2 (Impressum, ohne aufgedruckte Nummer)]** Copyright © 2026 Prof. Dr.-Ing. Mark Schutera, published by unfinished lecture notes. Lizenz: Creative Commons Attribution-NonCommercial 4.0 International ("CC BY-NC-SA 4.0"). Hinweis, dass die Notizen mit Hilfe mehrerer LLM-getriebener Tools "combobulated" wurden. Repository: `https://github.com/Quillstacks/LectureMaterial/tree/main/lecturenotes/notes_numerischemethoden`. Datumszeile: *2026-05-06 · feisty cranberry Hermelin*. QR-Code. Kein mathematischer Inhalt.

**[S. 3]** Nur Zitat: "AN INFINITELY ACCURATE APPROXIMATION IS NO LONGER AN APPROXIMATION." — PROBABLY SOMEONE SMART. Sonst leer.

**[S. 4]** Leer.

**[S. 5]** Inhaltsverzeichnis (Contents):
- Enter Numerical Methods — 9
- Floating-Point Arithmetic — 17
- Error Analysis — 25
- Newton Methods — 35
- Global Optimization — 47
- Numerical Integration — 57
- Index — 71

**[S. 6]** Leer.

**[S. 7]** *Introduction*: Numerische Methoden (Numerical Methods) sind essenziell zur Lösung mathematischer Probleme, die nicht analytisch behandelt werden können. Der Kurs behandelt Grundkonzepte, Fehleranalyse (error analysis), Konditionierung von Problemen (problem conditioning), Stabilität (stability) und verschiedene numerische Techniken — für zuverlässige, effiziente Algorithmen in Scientific Computing, Machine Learning, Data Science und Engineering. Keine Formeln.

**[S. 8]** Leer.

---

## Kapitel 1: Enter Numerical Methods [S. 9–16]

**[S. 9]** Kapiteltitel *Enter Numerical Methods*, Datumszeile *2026-04-05 · regal coconut Wachtel*. Abschnitt "Tapping into Computational Power / The Why".

Definition (informell): Numerische Methoden sind ein Teilgebiet der Mathematik, in dem Lösungen nicht analytisch exakt, sondern approximativ berechnet werden.

Gründe:
- Viele Probleme sind analytisch nicht lösbar oder zu komplex, um praktikabel zu sein.
- Computational Power erlaubt effiziente approximative Lösungen.

Randnotizen [S. 9]:
- Literatur (Further Reading): ¹ T. Arens, F. Hettlich, C. Karpfinger, U. Kockelkorn, K. Lichtenegger, H. Stachel: *Mathematik*, Springer. ² W. Dahmen, A. Reusken: *Numerik für Ingenieure und Naturwissenschaftler*, Springer. ³ M. P. Deisenroth, A. A. Faisal, C. S. Ong: *Mathematics for Machine Learning*, Cambridge University Press. ⁴ P. Deuflhard, A. Hohmann: *Numerische Mathematik 1 – Eine algorithmisch orientierte Einführung*, De Gruyter.
- "Approximation" von lateinisch *approximare* = "to come near to" (sich nähern).
- **Moore's Law**: Rechenleistung verdoppelt sich ca. alle zwei Jahre. Heutige Consumer-GPUs haben Tausende Kerne und schaffen Billionen Gleitkommaoperationen pro Sekunde. (G. E. Moore: Cramming more components onto integrated circuits. *Electronics*, 38(8):114–117, 1965.)
- GPT-2: 1.5B release, `https://openai.com/index/gpt-2-1-5b-release/`.

ML/AI-Kontext: Numerische Methoden für Modelltraining, Parameteroptimierung, Simulation komplexer Systeme; besonders Deep Learning (Millionen Parameter).

**[S. 10]** *Hands On Experience*. Grenzen der Skalierung analytischer Lösungen. Beispiel: lineares Gleichungssystem 2×2, analytisch per Substitution.

Gleichung (1):
$$\begin{bmatrix} 2 & 1 \\ 5 & 1 \end{bmatrix} \begin{bmatrix} w_1 \\ w_2 \end{bmatrix} = \begin{bmatrix} 11 \\ 13 \end{bmatrix} \tag{1}$$

Vollständige Substitutionsrechnung [S. 10]:
- Aus der ersten Gleichung: $2w_1 + w_2 = 11 \Rightarrow w_2 = 11 - 2w_1$
- In zweite Gleichung einsetzen: $5w_1 + 1(11 - 2w_1) = 13$
- $5w_1 + 11 - 2w_1 = 13$
- $3w_1 + 11 = 13$
- $3w_1 = 2$
- $w_1 = \frac{2}{3}$
- Dann: $w_2 = 11 - 2\left(\frac{2}{3}\right) = 11 - \frac{4}{3} = \frac{33-4}{3} = \frac{29}{3}$
- Verifikation 1. Gleichung: $2\left(\frac{2}{3}\right) + \left(\frac{29}{3}\right) = \frac{4}{3} + \frac{29}{3} = \frac{33}{3} = 11$ ✓
- Verifikation 2. Gleichung: $5\left(\frac{2}{3}\right) + 1\left(\frac{29}{3}\right) = \frac{10}{3} + \frac{29}{3} = \frac{39}{3} = 13$ ✓

Randnotiz: "Analytics" umfasst Methoden wie Substitution, Elimination, Matrixinversion etc. aus der linearen Algebra.

Randnotiz mit Übungsaufgabe, Gleichung (2): Computational complexity steigt mit Systemgröße; größeres System 3×3 zum Selbstlösen:
$$\begin{bmatrix} 2 & 1 & 3 \\ 1 & 4 & 2 \\ 3 & 2 & 5 \end{bmatrix} \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix} = \begin{bmatrix} 14 \\ 20 \\ 32 \end{bmatrix} \tag{2}$$

**[S. 11]** Für 2 Gleichungen lösbar; mit wachsender Systemgröße (z. B. Tausende Gleichungen/Unbekannte) werden analytische Lösungen wegen Rechenkomplexität und Zeit unpraktikabel.

Grenzen analytischer Lösungen auch bei nichtlinearen Gleichungen, Gleichung (3) — Sigmoid:
$$\sigma(x) = \frac{1}{1 + e^{-x}} \tag{3}$$

Transzendente Funktionen (transcendental functions) lassen sich nicht als endliche Kombination algebraischer Operationen (Addition, Subtraktion, Multiplikation, Division, Wurzeln) ausdrücken und besitzen daher keine geschlossene Lösung (closed-form solution). Der Exponentialterm macht es unmöglich, $x$ mit elementaren Funktionen (Polynome, rationale, trigonometrische Funktionen) zu isolieren.

Randnotiz: $\sigma(x)$ ist die Sigmoid-Aktivierungsfunktion in neuronalen Netzen, eine transzendente Funktion. Eine geschlossene Lösung für $\sigma(x) = 0$ existiert nicht: $\sigma(x)$ nähert sich 0 asymptotisch für $x \to -\infty$, erreicht 0 aber nie für endliches $x$.

Lernziele des Kapitels [S. 11]:
- Erklären, wann numerische Methoden eingesetzt werden und welche Probleme analytisches Lösen mit sich bringt.
- Diskretisierung (discretization): kontinuierliche mathematische Probleme in diskrete, computerlösbare Approximationen transformieren.
- Grundlegende numerische Techniken von Hand auf einfache Probleme anwenden, größere am Computer.

**[S. 12]** *Discretization and Approximation*.

Abbildung 1 [S. 12]: Kontinuierliche Kurve $f(x) = \sin(x)$ und ihre diskretisierte Version (schwarze Punkte) auf $[-3, 1]$ mit Schrittweite $h = 1$. (Plot: x-Achse von −3 bis 1, y-Achse −1 bis 1; Sinuskurve mit Punkten bei den ganzzahligen Stützstellen.)

Diskretisierung: Kontinuierliche Domänen (Zeit, Raum, Funktionen) in endliche Schritte/Gitter zerlegen und Funktionen an diskreten Punkten mit endlicher Präzision auswerten:

$$\text{Kontinuierliche Funktion:}\quad f(x), \quad x \in [a, b],$$
$$\text{Diskretisierte Funktion:}\quad f(x_i), \quad x_i = a + ih, \quad i = 0, 1, \ldots, N,$$

wobei (Gleichung (4)) die Schrittweite (step size):
$$h = \frac{b - a}{N} \tag{4}$$
mit $N$ = Anzahl der Schritte auf dem Intervall.

Randnotiz: Die Klammern "[" und "]" bezeichnen ein abgeschlossenes Intervall (closed interval), das die Werte $a$ und $b$ einschließt.

Analytische Minimumsuche von $\sin(x)$ auf $[-3, 1]$: gesucht $\min_{x \in [-3,1]} \sin(x)$. Das Minimum liegt dort, wo die Ableitung verschwindet und die zweite Ableitung positiv ist:
$$f(x) = \sin(x)$$
$$f'(x) = \cos(x) = 0 \implies x^* = \frac{\pi}{2} + k\pi,\ k \in \mathbb{Z}$$

Abbildung 2 [S. 12]: Kontinuierliche Kurve $f(x) = \sin(x)$ (schwarz), Ableitung $f'(x) = \cos(x)$ (grau, gestrichelt) und das analytische Minimum (schwarzer Punkt) auf $[-3, 1]$. Gestrichelte graue Linie bei $x = -\frac{\pi}{2}$ markiert den kritischen Punkt mit $\cos(x) = 0$ und das Minimum von $\sin(x)$.

Randnotiz: Trigonometrische Regeln geben die allgemeine Lösung für $\cos(x) = 0$; herleitbar über den Einheitskreis.

**[S. 13]** Kritische Punkte in $[-3, 1]$:
$$x_1 = -\frac{\pi}{2} \approx -1.5708$$
$$x_2 = \frac{\pi}{2} \approx 1.5708 \ (> 1,\ \text{nicht im Intervall})$$

Hinweis (Theorie): Minimum/Maximum einer Funktion auf abgeschlossenem Intervall $[a,b]$ kann an einem kritischen Punkt (Ableitung null oder nicht definiert) im Inneren ODER an den Endpunkten $a$, $b$ auftreten — auch wenn die Ableitung dort nicht null ist. Daher müssen bei Extremwertsuche auf abgeschlossenen Intervallen stets kritische Punkte UND Endpunkte geprüft werden.

Endpunkte und $x_1$ prüfen:
$$\sin(-3) \approx -0.1411$$
$$\sin\left(-\frac{\pi}{2}\right) = -1$$
$$\sin(1) \approx 0.8415$$

Ergebnis: Minimum ist $-1$ bei $x = -\frac{\pi}{2} \approx -1.5708$.

*On To the Numerical Solution* — Brute-Force-Gittersuche (grid search): Funktion an diskreten Punkten über dem Intervall auswerten, Punkt mit minimalem Wert wählen. Diskretisierung von $[-3, 1]$ mit Schrittweite $h = 1$:

| $x_i$ | Wert |
|---|---|
| $x_0 = -3$ | $\sin(-3) \approx -0.1411$ |
| $x_1 = -2$ | $\sin(-2) \approx -0.9093$ |
| $x_2 = -1$ | $\sin(-1) \approx -0.8415$ |
| $x_3 = 0$ | $\sin(0) = 0$ |
| $x_4 = 1$ | $\sin(1) \approx 0.8415$ |

Minimum darunter: $\sin(-2) \approx -0.9093$ bei $x = -2$.

Abbildung 3 [S. 13]: wie Abbildung 1 (Sinuskurve mit diskreten Punkten auf $[-3,1]$, $h=1$).

Randnotizen [S. 13]:
- Brute Force = alle möglichen Optionen ausprobieren und die beste wählen, hier mit grid search.
- Die Wahl der Schrittweite $h$ beeinflusst die Genauigkeit; kleinere Schrittweite → bessere Approximation des wahren Minimums. Auch die Intervallwahl beeinflusst das Ergebnis.
- **Approximationsfehler (Approximation Error)** = Differenz zwischen analytischer und numerischer Lösung. Hier: $|-1 - (-0.9093)| = 0.0907$.

**[S. 14]** *Examples & Excercises*. Wiederaufnahme des Beispiels, Gleichung (5):
$$\begin{bmatrix} 2 & 1 \\ 5 & 1 \end{bmatrix} \begin{bmatrix} w \\ b \end{bmatrix} = \begin{bmatrix} 11 \\ 13 \end{bmatrix} \tag{5}$$

Lösung per Brute-Force-Diskretisierung: Variablen $w$ und $b$ über Gitter möglicher Werte diskretisieren, Fehler je Kombination berechnen, fehlerminimale Lösung wählen. Grid search für $w, b$ mit Schrittweite 2.5 über $w, b \in \{0, 2.5, 5, 7.5, 10\}$.

Fehlerdefinition (Gleichung (6)) — Summe der Absolutdifferenzen zwischen linker und rechter Seite der Gleichungen:
$$\text{error}_1 = |2w + b - 11|,$$
$$\text{error}_2 = |5w + b - 13| \tag{6}$$

Alle Kombinationen auswerten, $(w, b)$-Paar mit kleinstem akkumuliertem Fehler wählen. Hinweis im Text: Das waren nur 100 Operationen — zeigt den Rechenaufwand von Brute-Force-Methoden; später effizientere Verfahren.

Randnotizen [S. 14]:
- Lineare Regression: $xw + b$ bildet ein lineares Modell — auch als einfachste Form eines Single-Unit-Neural-Network $\theta$ auffassbar.
- Code als Jupyter-Notebooks unter `https://enlitenment.schutera.com/landing`.

**[S. 15]** Tabelle 1: Grid search für $w, b \in \{0, 2.5, 5, 7.5, 10\}$; Spalten: $w$, $b$, $2w+b$ (error₁), $5w+b$ (error₂), Error (akkumuliert). Vollständige Tabelle:

| $w$ | $b$ | $2w+b$ (error₁) | $5w+b$ (error₂) | Error |
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

Tabellenunterschrift: Minimaler Fehler bei $w = 0$, $b = 10$ mit Fehler 4 (markiert mit *).

*Self-Reflection and Recap* — Selbstreflexionsfragen [S. 15]:
- Warum ist die Wahl der Schrittweite $h$ wichtig beim Diskretisieren, und wie beeinflusst sie Genauigkeit und Rechenzeit?
- Wie beeinflusst die Wahl des Intervalls $[a, b]$ die Ergebnisse der Diskretisierung und die Lage numerisch gefundener Extrema?
- Hauptunterschiede zwischen kontinuierlicher Funktion und diskretisierter Version; Implikationen für numerisches Lösen?

**[S. 16]** Recap der Kernkonzepte:
- Numerische Methoden essenziell für komplexe Probleme ohne analytische Lösung.
- Diskretisierung transformiert kontinuierliche Probleme in diskrete Approximationen.
- Handrechnung für kleine Probleme (Mechanikverständnis), Computer für größere.

"Errors everywhere": Mathematische Modelle sind Vereinfachungen der Realität; numerische Methoden führen zusätzliche Fehler durch Approximation ein. Gleichung (7):
$$f(x) \approx f(x_i), \quad x_i = a + ih \tag{7}$$

Randnotiz (Teaser): Gibt es einen einfachen Weg, das Verhältnis Genauigkeit/Rechenaufwand der Gittersuche zu verbessern?

---

## Kapitel 2: Floating-Point Arithmetic [S. 17–24]

**[S. 17]** Kapiteltitel *Floating-Point Arithmetic*, Datumszeile *2026-04-29 · lively date Hase*. Abschnitt "Getting used to Errors Everywhere / The Why".

Sei $f(x)$ eine kontinuierliche Funktion auf $[a, b]$. Die diskretisierte Version $f(x_i)$ approximiert $f(x)$ an diskreten Punkten $x_i$ mit einem Fehler, der von der Schrittweite $h$ und der Glattheit (smoothness) von $f$ abhängt. Numerische Werte können im Rechnerspeicher nur approximativ gespeichert werden (Gleitkommadarstellung / floating-point representation) → Rundungsfehler (rounding errors) bei arithmetischen Operationen, zusätzlich zu Trunkierungs-/Abschneidefehlern (truncation errors, auch approximation error genannt) aus der Approximation unendlicher Prozesse durch endliche.

Kernpunkte:
- Numerische Methoden führen Rundungs- und Trunkierungsfehler ein.
- Je nach Maschine wirken sich diese Fehler unterschiedlich aus, können sich verstärken und akkumulieren.

Randnotizen [S. 17]:
- **Modeling Error (Modellierungsfehler)**: Alle Modelle sind Vereinfachungen der Realität; Differenz zwischen Modell und realem System. Wird im Kurs nicht vertieft; Unterschied zwischen dem, was wir $f(x)$ nennen, und dem, was tatsächlich ein $f(x)$ ist, beachten.
- **On the Edge**-Modelle nutzen niedrigpräzise Arithmetik, z. B. 8-Bit-Integer oder binäre Gewichte/Aktivierungen.
- **Binary neural networks (BNNs)**: Gewichte und Aktivierungen auf $\{-1, +1\}$ beschränkt; drastisch reduzierter Speicher-/Rechenbedarf, macht Gleitkommadarstellung und Rundungseffekte kritisch. Referenz ⁵: M. Courbariaux, Y. Bengio: Binarynet: Training deep neural networks with weights and activations constrained to +1 or -1. *CoRR*, abs/1602.02830, 2016, `http://arxiv.org/abs/1602.02830`.

ML-Kontext: Floating-Point-Arithmetik relevant insbesondere bei Modellinferenz, compute-sparsamen Umgebungen (Edge), quantisierten Modellen.

**[S. 18]** *Hands On Experience* — Rundungsfehler-Beispiel: 10 geteilt durch 3, Dezimalentwicklung:
- $10 \div 3 = 3$, Rest 1
- "Bring down a 0": $10 \div 3 = 3$, Rest 1 (wiederholt sich)
- $\Rightarrow \frac{10}{3} = 3.333\ldots$

Die 3en wiederholen sich unendlich; beim Aufschreiben/Eingeben muss man irgendwo stoppen, Gleichung (8):
$$\frac{10}{3} \approx 3.333 \quad (\text{gerundet bzw. abgeschnitten nach 3 Stellen}) \tag{8}$$

Rundungsfehler = Differenz zwischen wahrem Wert und abgeschnittenem Wert, Gleichung (9):
$$\text{Rounding error} = |\,3.333333\ldots - 3.333\,| = 0.000333\ldots \tag{9}$$

Je mehr Stellen, desto kleiner der Fehler — er verschwindet aber nie vollständig (außer mit unendlich vielen Stellen, unmöglich).

Definition Rundungsfehler (rounding error): Computer speichern Zahlen stets mit endlich vielen Stellen; Rundungsfehler treten zwangsläufig auf und müssen gemanagt werden. Kleine Fehler können akkumulieren und sich verstärken — besonders in iterativen Algorithmen (numerische Methoden, ML).

Randnotizen [S. 18]:
- Typen numerischer Darstellungen in Computern: **Integer (int)**: 3; **Floating-point (float)**: 3.3333333; **Double precision (double)**: 3.3333333333333333; **Fixed-point (z. B. 4 Stellen)**: 3.3333.
- Mathematische Notation mit Periode: $3.\overline{3}$.

Lernziele [S. 18]:
- Fehlertypen verstehen: Modeling, truncation, rounding errors.
- Gleitkommadarstellung, Maschinenepsilon (machine epsilon), Auslöschung (loss of significance) verstehen.
- Numerische Fehler in praktischen Berechnungen handhaben.

**[S. 19]** *Floating Point Representation and Precision*.

Gleitkommazahlen (floating-point numbers): Darstellung reeller Zahlen mit endlicher Bitzahl. IEEE-754-Standard⁶ ist das verbreitetste Format. Eine Gleitkommazahl wird typischerweise gespeichert als (Gleichung (10)):
$$x = (-1)^s \cdot m \cdot 2^e \tag{10}$$
wobei $s$ das Vorzeichenbit (sign bit), $m$ die Mantisse (mantissa bzw. significand, bestimmt die Präzision) und $e$ der Exponent (bestimmt Skala/Größenordnung). Großer Wertebereich, aber nur eine endliche Menge reeller Zahlen exakt darstellbar. IEEE 754 single precision (float): 32 Bits = 1 Vorzeichenbit + 8 Exponentenbits + 23 Mantissenbits.

Abbildungen [S. 19]:
- Figure 4: Bit-Layout IEEE 754 **HALF (16)**: Sign (dunkel, Bit 1), Exponent (mittel, Bits bis 6), Mantissa (hell, Bits bis 16). D. h. 1 + 5 + 10 Bits.
- Figure 5: Bit-Layout IEEE 754 **SINGLE (32)**: Sign (Bit 1), Exponent (bis Bit 9), Mantissa (bis Bit 32). D. h. 1 + 8 + 23 Bits.
- Figure 6: Bit-Layout IEEE 754 **DOUBLE (64)**: Sign (Bit 1), Exponent (bis Bit 12), Mantissa (bis Bit 64). D. h. 1 + 11 + 52 Bits.

Exponent mit Bias: Der Exponent wird mit einem Bias gespeichert, um positive und negative Exponenten zu erlauben (sehr kleine und sehr große Beträge darstellbar). IEEE 754 single precision: 8 Exponentenbits, Bias 127. Gespeicherter Exponent $E$ und wahrer Exponent $e$: $e = E - 127_{10}$. Grund: mit 8 Bits kann das Exponentenfeld Werte von 0 ($2^0 - 1$) bis 255 ($2^8 - 1$) speichern; durch Subtraktion des Bias (127) kann $e$ positive und negative Werte um null zentriert annehmen — erleichtert Kodierung und Vergleich in Hardware.

Randnotizen [S. 19]:
- Referenz ⁶: IEEE Computer Society. IEEE standard for floating-point arithmetic. `https://ieeexplore.ieee.org/document/4610935`, August 2008. IEEE Std 754-2008 (Revision of IEEE Std 754-1985).
- **Bit** = binary digit, grundlegendste Informationseinheit, Wert 0 oder 1.

**[S. 20]** *Constructing scale* in Gleitkommadarstellung:
$$10^1 = 10_{10} = 1010_2 = 1.010 \times 2^3, \quad E = 10000010_2$$
$$10^2 = 100_{10} = 1100100_2 = 1.100100 \times 2^6, \quad E = 10000101_2$$
$$10^3 = 1000_{10} = 1111101000_2 = 1.111101000 \times 2^9, \quad E = 10001000_2$$

Die Mantisse bestimmt, wie fein Zahlen zwischen Zweierpotenzen dargestellt werden können.

**2-Bit-Mantissen-Beispiel (unnormalisiert)** [S. 20]:
- Mantissen-Bitkombinationen: 00, 01, 10, 11
- Unnormalisierter Significand: $0.xx_2$
$$00:\ 0.00_2 = 0 + 0 \times 2^{-1} + 0 \times 2^{-2} = 0.0$$
$$01:\ 0.01_2 = 0 + 0 \times 2^{-1} + 1 \times 2^{-2} = 0.25$$
$$10:\ 0.10_2 = 0 + 1 \times 2^{-1} + 0 \times 2^{-2} = 0.5$$
$$11:\ 0.11_2 = 0 + 1 \times 2^{-1} + 1 \times 2^{-2} = 0.75$$

2-Bit-Mantisse → 4 verschiedene Werte zwischen zwei beliebigen Zweierpotenzen; 3-Bit-Mantisse → 8 Werte. Allgemein: Mantisse mit $t$ Bits → $2^t$ verschiedene Werte zwischen zwei Zweierpotenzen, durch den Exponenten skaliert.

**Maschinenepsilon (machine epsilon, $\varepsilon_{\text{mach}}$)** [S. 20]: kleinste positive Zahl, sodass $1 + \varepsilon_{\text{mach}} \neq 1$ in der Rechnerarithmetik. Quantifiziert die obere Schranke des relativen Fehlers durch Rundung in Gleitkommaarithmetik (Gleichung (11)):
$$\varepsilon_{\text{mach}} = 2^{-t} \tag{11}$$
mit $t$ = Anzahl der Mantissenbits. Im 2-Bit-Mantissen-Beispiel:
$$\varepsilon_{\text{mach}} = 2^{-2} = 0.25$$

Relative Präzision von Gleitkommazahlen ≈ $2^{-t}$; absolute Präzision hängt von der Größenordnung der dargestellten Zahl ab (Gleichung (12)):
$$\varepsilon_{\text{mach}} \cdot |x| \tag{12}$$

Randnotizen [S. 20]:
- Größte Zahl in single precision ≈ $10^{38}$, gesetzt durch größten Exponenten $e = +127$; dezimaler Exponent 38 aus $\log_{10}(2^{128}) \approx 38.5$.
- SI-Präfixe: mega ($10^6$), giga ($10^9$), tera ($10^{12}$), peta ($10^{15}$), exa ($10^{18}$), zetta ($10^{21}$), yotta ($10^{24}$), ronna ($10^{27}$), quetta ($10^{30}$); **kein offizielles SI-Präfix** für $10^{33}$.
- IEEE 754 single precision: $\varepsilon_{\text{mach}} \approx 1.19 \times 10^{-7}$; double precision: $\varepsilon_{\text{mach}} \approx 2.22 \times 10^{-16}$.
- Absolute Präzision: $1 : 2 = 0.5$, aber $10 : 2 = 5$ — gleiche Anzahl Schritte (relative Präzision), aber Lücken (gaps) von 0.5 vs. 5.

**[S. 21]** Große Zahlen haben größere absolute Lücken zwischen darstellbaren Werten als kleine Zahlen.

Figure 7 [S. 21]: Absoluter Fehler für single (schwarz, "SINGLE") und double (grau gestrichelt, "DOUBLE") Präzision als Funktion des dargestellten Wertes $x$ (doppelt-logarithmische Darstellung; x-Achse $10^{-16}$ bis $10^{16}$, y-Achse ca. $10^{-23}$ bis $10^{7}$). Der Fehler wächst linear mit $x$ und ist proportional zum Maschinenepsilon des jeweiligen Formats.

**Fixed-point representation (Festkommadarstellung)** [S. 21]: Alternative Speicherung reeller Zahlen, v. a. für vorhersagbare Präzision und Performance. Bitzahl für Ganzzahl- und Bruchteil wird im Voraus festgelegt → Abstand zwischen darstellbaren Zahlen (Präzision) ist immer gleich, unabhängig von der Größe des Wertes → mehr Kontrolle.

Beispiel [S. 21]: Zahlen zwischen $-1000$ und $1000$ mit 32-Bit signed integer speichern. Normal stellt ein 32-Bit-Integer Werte von $-2147483648$ bis $2147483647$ dar (viel mehr als benötigt). Für mehr Präzision: Skalierungsfaktor — jede reelle Zahl mit $10^6$ multiplizieren und als Integer speichern. Die Zahl 1.234567 wird als 1234567 gespeichert.

Randnotiz: Präzision mit Skalierungsfaktor $10^{-6}$ = kleinste darstellbare Differenz 0.000001. Maximaler Rundungsfehler = halber Schritt: $0.5 \times 10^{-6} = 0.0000005$.

**[S. 22]** *Examples & Excercises* — **Auslöschung (loss of significance, catastrophic cancellation)**: tritt auf beim Subtrahieren zweier nahezu gleicher Zahlen; führende Ziffern heben sich auf, nur die weniger signifikanten, rundungsfehleranfälligen Ziffern bleiben → kann Rundungsfehler stark verstärken.

Beispiel 1 [S. 22]: Zwei Zahlen $a$, $b$ mit begrenzter Präzision, je auf 8 signifikante Stellen gerundet (Festkommadarstellung):
$$a = 12345678.5$$
$$b = 12345678.0$$
Mit 8 signifikanten Stellen gespeichert als:
$$\tilde{a} = 12345679$$
$$\tilde{b} = 12345678$$
Subtraktion: $\tilde{a} - \tilde{b} = 12345679 - 12345678 = 1$.
Wahre Differenz: $a - b = 12345678.5 - 12345678.0 = 0.5$.
Fehler im Ergebnis = 0.5, gleich dem Rundungsfehler in $\tilde{a}$ bzw. $\tilde{b}$ einzeln auf Maschinenepsilon-Niveau 0.5.

Beispiel 2 (minimale Abweichung) [S. 22]:
$$a = 12345678.4$$
$$b = 12345678.0$$
Gespeichert (8 signifikante Stellen):
$$\tilde{a} = 12345678$$
$$\tilde{b} = 12345678$$
Subtraktion: $\tilde{a} - \tilde{b} = 12345678 - 12345678 = 0$.
Wahre Differenz: $a - b = 12345678.4 - 12345678.0 = 0.4$.

Randnotizen [S. 22]:
- **Pseudo-Accuracy**: unbegründet hoher Detailgrad, erzeugt irreführendes, künstliches Genauigkeitsgefühl.
- "Infinity": In der Mathematik liegt eine Unendlichkeit zwischen 0 und 1 — der Unterschied zwischen etwas und nichts.

**[S. 23]** Differenz der wahren Ergebnisse beider Beispiele ist 0.1, aber die Maschinenergebnisse sind 0 bzw. 1 — riesiger relativer Fehler. Zeigt, wie Auslöschung zu großen Fehlern führt, besonders wenn die subtrahierten Zahlen sehr nahe beieinander liegen.

*Hands on machine epsilon* [S. 23]: Übung — Programm entwerfen (Pseudocode), das das Maschinenepsilon eines Systems für ein bestimmtes Gleitkommaformat bestimmt; Verhalten auf Fixed-Point- vs. Floating-Point-System überlegen; verschiedene Typen am eigenen Rechner testen. Frage: Welchen Typ würde man für einen Taschenrechner wählen und warum⁷?

*Loss of significance example* [S. 23]: Übung — überlegen, wie man Auslöschung auf der eigenen Maschine demonstriert (Pseudocode vor dem Weiterlesen).

Figure 8 [S. 23]: Demonstration katastrophaler Auslöschung: $1/(1 + \epsilon - 1)$ vs. $\epsilon$ (log-x, lineare y-Skala; x von $10^{-17}$ bis $10^{-14}$, y von 0 bis $2 \times 10^{16}$). Für große $\epsilon$ folgt das Ergebnis $1/\epsilon$; für sehr kleine $\epsilon$ dominiert der Rundungsfehler und das Ergebnis wird unendlich (Pfeil "$\uparrow \infty$" nahe $\epsilon \approx 10^{-16.5}$).

Aufgabe [S. 23]: Überlegen, wie die Berechnung von $f(\epsilon) = 1/(a + \epsilon - b)$ für kleines $\epsilon$ und $a = b$ dies demonstriert. Was erwartet man für sehr kleines $\epsilon$?

Randnotizen [S. 23]:
- Code: `https://github.com/Quillstacks/lecturecode_numericalmethods.git`.
- **Overflow**: Zahlen mit großem Betrag werden als $+\infty$ oder $-\infty$ approximiert.
- **Underflow**: Zahlen nahe null werden auf null gerundet.
- "Is double enough?" Referenz ⁷: D. Blochinger. Numerische methoden – foliensatz. Zentrum für Angewandte Ökonomik (ZAÖ), DHBW Ravensburg, 2025. URL `https://www.economicon.de/repository/index.html`. Illustration: Prof. Dr. Daniel Blochinger. Lizenz: CC BY-NC-SA 4.0. Stand: 28. Mai 2025.
- Frage: Was passiert für $a > b$? (Stichwort: signifikante Stellen.)

**[S. 24]** *Self-Reflection and Recap*.

Selbstreflexionsfragen:
- Wie ist die Gleitkommadarstellung aufgebaut, was sind ihre Komponenten?
- Was ist das Maschinenepsilon und wie hängt es mit numerischer Präzision zusammen?
- Wie wirken sich diese Konzepte in der Praxis auf numerische Berechnungen aus?

Recap:
- Gleitkommadarstellung: großer Wertebereich reeller Zahlen mit endlicher Bitzahl, aber Rundungsfehler.
- Maschinenepsilon quantifiziert die kleinste darstellbare Differenz in Gleitkommaarithmetik und beeinflusst die Präzision.
- Auslöschung beim Subtrahieren nahezu gleicher Zahlen verstärkt Rundungsfehler.

*Knowing what can go wrong*: Notation für das Folgende — es gibt eine wahre Funktion $f$ und eine approximierte Funktion $\hat{f}$, ferner eine wahre Eingabe $x$ und eine gerundete Eingabe $\tilde{x}$. Diese beeinflussen und charakterisieren numerische Methoden.

Randnotiz (Teaser): Metriken für numerische Methoden basierend auf den diskutierten Approximationen und Fehlern?

---

## Kapitel 3: Error Analysis [S. 25–34]

**[S. 25]** Kapiteltitel *Error Analysis*, Datumszeile *2026-04-29 · lively date Hase*. Motto: "Some call it Error. I call it Character." Abschnitt "The Why".

**Conditioning, Stability, Consistency, Convergence** (Konditionierung, Stabilität, Konsistenz, Konvergenz) sind Grundkonzepte der numerischen Analysis zum Verständnis des Verhaltens numerischer Algorithmen und ihrer Zuverlässigkeit.

Ziele:
- Sensitivität gegenüber kleinen Änderungen der Eingabedaten bewerten (Problem).
- Sensitivität der numerischen Lösung gegenüber kleinen Änderungen der Eingabedaten bewerten (Methode).
- Sicherstellen, dass numerische Methoden genaue, reproduzierbare Ergebnisse liefern.
- Garantieren, dass Approximationen zur wahren Lösung konvergieren.

ML-Kontext: Beim Training großer Modelle (Large-scale Optimization, iterative numerische Methoden) ist Konvergenz zentral, danach Komplexität (Anzahl Operationen, Zeit). Bewertung von AI-Modellen $\theta$ mit genau diesen Konzepten.

Randnotizen [S. 25]:
- Modellfehler: Mit $f(\cdot)$ wird das exakte Modell eines Systems impliziert; Modelle sind in der Praxis Vereinfachungen (z. B. Manhattan- oder euklidisches Distanzmodell zwischen Punkten A und B ohne Terrain, Fortbewegungsart, Hindernisse). Unser $f(\cdot)$ hier ist ein anderes $f(\cdot)$.
- Literatur: I. Goodfellow, Y. Bengio, A. Courville: *Deep Learning*, MIT Press, 2016, `http://www.deeplearningbook.org` (Kap. 4: numerical computation).

**[S. 26]** *Hands On Experience*. Konzepte am diskretisierten Sinus-Beispiel aus Kapitel 1; je Konzept zwei Übungen (zwei Seiten derselben Medaille, Extreme des Spektrums).

**Conditioning (Konditionierung)**: Wie empfindlich reagiert die Lösung auf kleine Änderungen der Eingabedaten?

Figure 9 [S. 26]: Kontinuierliche Kurve $\hat{f}(x) = \sin(x)$ auf $[-3, 1]$ mit zwei hervorgehobenen transparenten vertikalen Bändern bei $x = -1.5$ und $x = 0$ (Breite 0.5).

Annahme: approximierte Funktion = wahre Funktion (Sinuskurve), aber $\tilde{x}$ ist eine leicht gestörte Version von $x$ durch Messfehler oder Rundung ($\pm 0.25$). Zwei graue Bänder: bei $x = -1.5$ gut konditionierter Bereich (well-conditioned; kleine Änderungen in $x$ → kleine Änderungen in $f(x)$); bei $x = 0$ schlecht konditioniert (ill-conditioned; kleine Änderungen in $x$ → große relative Änderungen in $f(x)$).

**Stability (Stabilität)**: Sensitivität der numerischen Lösung gegenüber kleinen Änderungen der Eingabedaten.

Figure 10 [S. 26]: Kontinuierliche Kurve $f(x)_{.2} = \sin(x)$ auf $[-3, 1]$ mit hervorgehobenem Band bei $x = 0$ (Breite 0.5) und diskretisierten Punkten mit Schrittweite $h = 0.2$.

Randnotiz: Hier geht es um Gleitkommadarstellung, nicht um Schrittweite oder optimale Approximation.

Beobachtung: Im Band um $x = 0$ folgen bei $h = 0.2$ die diskretisierten Punkte der Sinuskurve eng → Instabilität durch Änderungen in $\tilde{x} \pm 0.25$, Fluktuationen in den berechneten Werten $\hat{f}(\tilde{x})$. Dagegen zeigt die zweite Abbildung mit $h = 1$ …

**[S. 27]** … nur einen einzigen diskretisierten Punkt im grauen Band → stabile Approximation der Sinuskurve in dieser Region, unabhängig von Abweichungen in $\tilde{x}$.

Figure 11 [S. 27]: Kontinuierliche Kurve $f(x)_{1.} = \sin(x)$ auf $[-3, 1]$ mit Band bei $x = 0$ (Breite 0.5) und diskretisierten Punkten mit Schrittweite $h = 1$.

**Consistency (Konsistenz)**: quantifiziert, wie gut die numerische Methode die exakte Lösung des Originalproblems trifft. Diskretisierungen mit $h = 1$ und $h = 0.2$.

Figure 12 [S. 27]: Balkendiagramm der diskretisierten Werte $f(x)_{1.} = \sin(x)$ auf $[-3, 1]$ mit Schrittweite $h = 1$ (stückweise konstante Balken).
Figure 13 [S. 27]: Balkendiagramm der diskretisierten Werte $f(x)_{.2} = \sin(x)$ auf $[-3, 1]$ mit Schrittweite $h = 0.2$ (feinere Balken).

Für infinitesimal kleine Schrittweiten $h \to 0$ kommen die diskretisierten Punkte der wahren Sinuskurve immer näher → perfekte Übereinstimmung zwischen numerischer Methode und exakter Lösung = optimale Konsistenz.

**Convergence (Konvergenz)**: entsteht aus Kombination von Stabilität und Konsistenz. Eine numerische Methode ist konvergent, wenn beim Verfeinern der Approximation $\hat{f}(x)$ (z. B. kleinere Schrittweite $h$) …

Randnotiz [S. 27]: "Intuitive convergence example with sine, wanted" — Aufruf für bessere Beispielideen.

**[S. 28]** … die berechnete Lösung sich der exakten Lösung des Problems nähert — unabhängig von Abweichungen in $\tilde{x}$ oder indem diese implizit berücksichtigt werden.

Lernziele [S. 28]:
- Intuition zu Konditionierung, Stabilität, Konsistenz, Konvergenz.
- Einfache numerische Probleme quantitativ bezüglich dieser Konzepte analysieren.

**[S. 29]** *Quantitative Characterization of Numerical Methods*.

**Notation** [S. 29]: $f(\cdot)$ = exakte (analytische) Lösung eines Problems; $\hat{f}(\cdot)$ = numerische Methode (Algorithmus), die eine Approximation liefert; $x$ = exakte Eingabedaten; $\tilde{x}$ = tatsächlich verwendete (gestörte) Eingabedaten, z. B. durch Messfehler oder Rundung.

Randnotiz: "Hat versus tilde" — Hut ^ markiert die numerische Methode (Algorithmus), Tilde ~ markiert gestörte Eingabe. $\hat{f}(\tilde{x})$ liest sich: numerische Methode ausgewertet auf gestörten Eingabedaten.

**Conditioning** — Konditionszahl (condition number) $\kappa$ eines Problems bei $x$ (Gleichung (13)):
$$\kappa = |f(x) - f(\tilde{x})| \tag{13}$$
$\kappa$ wird oft normalisiert, um es als relatives Maß auszudrücken.

**Stability** — gegeben, wenn kleine Fehler in Eingabe oder Zwischenschritten nicht zu unverhältnismäßig großen Fehlern im Output führen. Eine stabile Methode stellt sicher, dass der Fehler der berechneten Lösung $\hat{f}(\tilde{x})$ durch ein konstantes Vielfaches des Eingabefehlers beschränkt bleibt (Gleichung (14)):
$$\left|\hat{f}(\tilde{x}) - \hat{f}(x)\right| \leq s \cdot |\tilde{x} - x| \tag{14}$$
mit Konstante $s$. Für $s \approx 1$ entwickelt sich der Fehler der berechneten Lösung linear mit dem Eingabefehler.

**Consistency** — wie gut approximiert die numerische Lösung die exakte Lösung des Originalproblems (Gleichung (15)):
$$\left|\hat{f}(x) - f(x)\right| \leq c \tag{15}$$
mit Konstante $c$, die den Konsistenzfehler quantifiziert.

**Convergence** — Approximation erreicht einen spezifischen stabilen Grenzwert. Eine Methode ist konvergent, wenn (Gleichung (16)):
$$\left|\hat{f}(\tilde{x}) - f(x)\right| \to \lim \tag{16}$$
D. h. sowohl die echte Lösung wird approximiert als auch Abweichungen in den Daten werden durch eine Fehlermarge kontrolliert.

Randnotiz [S. 29]: Konvergenz zielt üblicherweise auf Fehlermarge null, also exakte Lösung $f(x)$. Oft tritt aber Konvergenz gegen einen anderen Wert auf (non-zero convergence) — konvergiert die Methode gegen einen von $f(x)$ verschiedenen Wert, deutet das auf einen systematischen Fehler (Bias) der Methode hin.

**[S. 30]** *Examples & Excercises* — Minimum der Sinusfunktion auf $[-3, 1]$, diskretisiert mit $h = 1$ und $h = 0.2$; Eingabe $x$ gestört: $\tilde{x} = x \pm 0.25$, Präzision zwei Dezimalstellen. Analyse von Konditionierung, Stabilität, Konsistenz, Konvergenz mit den Formeln des vorigen Abschnitts.

**Conditioning** [S. 30]: unabhängig von der numerischen Methode — beschreibt die Sensitivität des Problems selbst. Analyse rein über die Wirkung kleiner Änderungen von $x$ auf $\sin(x)$. Um $x = -1$ (nahe Minimum) ist die Sinusfunktion relativ flach → gute Konditionierung; bei $x = 0$ ändert sie sich schnell → schlechte Konditionierung.

Rechnungen:
$$\kappa(-1, +0.25) = |\sin(-1) - \sin(-0.75)| \approx |-0.8415 - (-0.6816)| = 0.1599$$
$$\kappa(-1, -0.25) = |\sin(-1) - \sin(-1.25)| \approx |-0.8415 - (-0.9489)| = 0.1074$$

→ Gute Konditionierung (well-conditioning) mit $0.1074 \leq \kappa \leq 0.1599$.

$$\kappa(0, +0.25) = |\sin(0) - \sin(0.25)| \approx |0 - 0.2474| = 0.2474$$
$$\kappa(0, -0.25) = |\sin(0) - \sin(-0.25)| \approx |0 - (-0.2474)| = 0.2474$$

**[S. 31]** → Schlechte Konditionierung (ill-conditioning) mit $\kappa \leq 0.247$. [Anm.: Text sagt "ill-conditioning with κ ≤ 0.247".]

**Stability** [S. 31]: abhängig von der Methode. Für $h = 1$ stabil (kleine Änderungen in $\tilde{x}$ → kleine Änderungen in $\hat{f}(\tilde{x})$); für $h = 0.2$ weniger stabil (kleine Änderungen in $\tilde{x}$ → größere Fluktuationen). Quantifizierung über Konstante $s$ in der Stabilitätsungleichung (Gleichung (17)):
$$\left|\hat{f}(\tilde{x}) - \hat{f}(x)\right| \leq s \cdot |\tilde{x} - x| \tag{17}$$

Aus Symmetriegründen nur Fall $\tilde{x} = x + 0.25$.

Für $h = 1$:
$$s_{h=1, x=-1} \cdot |\tilde{x} - x| = |\hat{f}(\tilde{x}) - \hat{f}(x)| = |\hat{f}_1(-0.75) - \hat{f}_1(-1)| = |\hat{f}_1(-1) - \hat{f}_1(-1)| \text{ (siehe A)}$$
$$s_{h=1, x=0} \approx 0 \div 0.25 \approx 0$$
[UNSICHER: Indexnotation im PDF wechselt zwischen $s_{h=1,x=-1}$ und $s_{h=1,x=0}$ in derselben Rechnung; exakt wie abgedruckt übernommen.]

Randnotiz A): Schrittweite $h = 1$ führt an beiden Punkten zum selben Funktionswert (stückweise konstant; Referenz Fig. 12).

Für $h = 0.2$:
$$s_{h=0.2, x=-1} \cdot |\tilde{x} - x| = |\hat{f}(\tilde{x}) - \hat{f}(x)| = |\hat{f}_{0.2}(-0.75) - \hat{f}_{0.2}(-1)| = |\hat{f}_{0.2}(-0.8) - \hat{f}_{0.2}(-1)|$$
$$= |-0.71736 - (-0.84147)|$$
$$s_{h=0.2, x=-1} = 0.12411 \div 0.25 \approx 0.4964$$

Hinweis: Stabilität hat Anomalien in Randbereichen der Diskretisierung — besonders ein Problem für stückweise konstante Approximationen (piece-wise constant approximations).

Randnotiz [S. 31]: Stabilität gleicht der Konditionierung des Systems für $h \to 0$ — "Show it." (Übung.)

**Consistency** [S. 31]: Vergleich numerische Lösung $\hat{f}(x)$ mit exakter Lösung $f(x)$ für das Minimum der Sinusfunktion auf $[-3, 1]$. Konstante $c$ in der Konsistenzungleichung (Gleichung (18)):
$$\left|\hat{f}(x) - f(x)\right| \leq c \tag{18}$$

Randnotiz: Analytische Lösung von $\min(\sin(x))$ auf $[-3,1]$ — siehe Kapitel 1.

**[S. 32]** Für $h = 1$:
$$c_1 \geq \left|\hat{f}_1\left(-\frac{\pi}{2}\right) - f\left(-\frac{\pi}{2}\right)\right| \geq \left|\hat{f}_1(-1) - f\left(-\frac{\pi}{2}\right)\right| \geq |-0.84147 - (-1)| \geq 0.15853$$

Für $h = 0.2$:
$$c_{0.2} \geq \left|\hat{f}_{0.2}\left(-\frac{\pi}{2}\right) - f\left(-\frac{\pi}{2}\right)\right| \geq \left|\hat{f}_{0.2}(-1.2) - f\left(-\frac{\pi}{2}\right)\right| \geq |-0.94898 - (-1)| \geq 0.05102$$

Konsistenz verbessert sich mit kleineren Schrittweiten, wie erwartet.

**Convergence** [S. 32]: kombiniert Stabilität und Konsistenz. Quantifizierung über Gesamtfehler zwischen numerischer Lösung $\hat{f}(\tilde{x})$ und exakter Lösung $f(x)$ (Gleichung (19)):
$$\left|\hat{f}(\tilde{x}) - f(x)\right| \tag{19}$$

Aus Symmetriegründen nur $\tilde{x} = x + 0.25$.

Für $h = 1$:
$$\left|\hat{f}_1(\tilde{x}) - f(x)\right| = \left|\hat{f}_1(-1) - f\left(-\frac{\pi}{2}\right)\right|,\ \left|\hat{f}_1(-0.75) - f\left(-\frac{\pi}{2}\right)\right| = \left|\hat{f}_1(-1) - f\left(-\frac{\pi}{2}\right)\right|$$
$$= |-0.84147 - (-1)| = 0.1599$$
[UNSICHER: Im PDF stehen die Zeilen ohne verbindende Gleichheits-/Relationszeichen untereinander: „$|\hat{f}_1(\tilde{x}) - f(x)|\ |\hat{f}_1(-1) - f(-\frac{\pi}{2})|$“, dann „$|\hat{f}_1(-0.75) - f(-\frac{\pi}{2})|$“, „$|\hat{f}_1(-1) - f(-\frac{\pi}{2})|$“, „$|-0.84147 - (-1)|$“, „$= 0.1599$“. Zudem inkonsistent: $|-0.84147-(-1)| = 0.15853$, im PDF steht aber als Ergebnis 0.1599.]

Für $h = 0.2$:
$$\left|\hat{f}_{0.2}(\tilde{x}) - f(x)\right| = \left|\hat{f}_1(-1.2) - f\left(-\frac{\pi}{2}\right)\right|,\ \left|\hat{f}_{0.2}(-0.95) - f\left(-\frac{\pi}{2}\right)\right|,\ \left|\hat{f}_{0.2}(-1) - f\left(-\frac{\pi}{2}\right)\right|$$
$$= |-0.84147 - (-1)| = 0.1599$$
[UNSICHER: Gleiche Darstellungsweise wie oben; erste Zeile referenziert $\hat{f}_1(-1.2)$ obwohl Kontext $\hat{f}_{0.2}$ nahelegt; Endwert 0.1599 vs. arithmetisch 0.15853 — exakt wie abgedruckt übernommen.]

**[S. 33]** Wegen der Stabilitätsprobleme im Fall $h = 0.2$ verbessert sich die Konvergenz in diesem Operationspunkt nicht mit kleineren Schrittweiten. Beide numerischen Lösungen konvergieren zum selben Grenzwert; auch die Methode des iterativen Verkleinerns der Schrittweite $h$ konvergiert zum selben Grenzwert. Beachte: Charakteristiken werden sowohl für eine numerische Lösung als auch für die numerische Methode verwendet.

*Hands on compute-driven error analysis* [S. 33]: Brute-Force-Fehleranalyse des Zwei-Gleichungs-Systems aus Kapitel 1; Konditionierung, Stabilität, Konsistenz und Konvergenz der numerischen Lösung bestimmen und durch Optimierung der numerischen Methode verbessern. Code: `https://github.com/Quillstacks/lecturecode_numericalmethods.git`.

*Self-Reflection and Recap* [S. 33] — Fragen:
- Wie gut konditioniert ist das Zwei-Gleichungs-System verglichen mit der numerischen Lösung des Sinus-Minimums?
- Konvergiert Stabilität mit kleineren Schrittweiten im Zwei-Gleichungs-System? Gegen was?
- Wie wirken Störungen der Eingabedaten auf die numerische Lösung des Zwei-Gleichungs-Systems? Wechselspiel mit Schrittweite?
- Vergleiche Konvergenz mit Stabilität und Konsistenz. Beobachtungen in Begriffen von Bias und Varianz ausdrücken?
- Gibt es für immer kleinere Schrittweiten eine Grenze der Genauigkeit der numerischen Lösung? Warum?
- Welches weitere Problem tritt beim Verfeinern der Schrittweite auf?

Recap [S. 33]:
- Konditionierung, Stabilität, Konsistenz, Konvergenz sind Grundkonzepte zum Verständnis numerischer Algorithmen.
- Diese Konzepte können qualitativ und quantitativ ausgedrückt werden.

Randnotiz (Teaser): Bisher Brute-Force-Lösungen — Wege, Brute-Force-Methoden zu verfeinern für bessere Ergebnisse mit weniger Aufwand? Code der Vorlesung zum Testen nutzen.

**[S. 34]** Abschlussabsatz: Nachdem das Verhalten einzelner numerischer Lösungen charakterisiert werden kann, geht es weiter mit der Analyse ganzer numerischer Methoden und Algorithmen. Bisher wurde die Annahme, wo (in welchem Intervall) nach einer Lösung zu suchen ist, als gegeben vorausgesetzt — das ist üblicherweise nicht der Fall; in der nächsten Vorlesung geht es weg von lokalen Optimierungsmethoden. Sonst keine weiteren Inhalte auf der Seite.

---

## Kapitel 4: Newton Methods [S. 35–46]

**[S. 35]** Kapiteltitel *Newton Methods*, Datumszeile *2026-04-05 · regal coconut Wachtel*. Motto: "A Step in the Right direction." Abschnitt "The Why".

Die Brute-Force-Gittersuche ist fundamental begrenzt: Sie erkundet den Lösungsraum blind und benötigt $O(N^d)$ Auswertungen für $N$ Gitterpunkte in $d$ Dimensionen (Komplexitätsangabe!).

Kerneinsicht: Statt an jedem Gitterpunkt nur "Was ist der Wert hier?" zu fragen, fragen wir auch "In welche Richtung soll ich als Nächstes gehen?". Die Steigung (Ableitung) der Funktion zeigt die Richtung zur Lösung — das transformiert die Suche fundamental.

Nutzen:
- Lokale Information für anspruchsvolle Schritte statt Brute-Force-Suchen.
- Schnellere und optimalere Konvergenz.

ML/DL-Kontext: Newtons Methode, auf erste Ordnung vereinfacht, ist als Gradient Descent (Gradientenabstieg) bekannt. Das gesamte Feld Deep Learning baut auf der Idee auf, lokale Gradienteninformation zu nutzen, um in hochdimensionalen Loss-Landschaften zu Minima zu navigieren.

Randnotiz [S. 35]: **Backpropagation** ist vital zur Verteilung der Gradienteninformation durch die Schichten eines neuronalen Netzes, aber der Kern-Optimierungsschritt ist weiterhin gradientenbasierte Navigation.

**[S. 36]** *Hands On Experience*. Vergleich Gittersuche vs. Newton-Verfahren an der Sinusfunktion aus Kapitel 3, jetzt Nullstellensuche: $\sin(x) = 0$ auf $[2.5, 4]$ (Lösung nahe $\pi \approx 3.14159$).

Figure 14 [S. 36]: Kontinuierliche Kurve $f(x) = \sin(x)$ auf $[2.5, 4]$ und diskretisierte Punkte mit Schrittweite $h = 0.3$.

Gittersuche auf $[2.5, 4]$ mit Schritt $h = 0.3$ wertet blind aus:
$$f(2.5) \approx 0.599$$
$$f(2.8) \approx 0.335$$
$$f(3.1) \approx 0.042 \quad \leftarrow \text{am nächsten an null}$$
$$f(3.4) \approx -0.256$$
$$f(3.7) \approx -0.530$$
$$f(4.0) \approx -0.757$$

Ergebnis: $x \approx 3.1$ mit 6 Auswertungen, Fehler $|3.1 - \pi| \approx 0.042$.

**Newtons Methode** hat einen adaptiven Suchansatz: An jedem Punkt werden Funktion und Ableitung ausgewertet; mit dieser lokalen Information wird ein Schritt Richtung Lösung gemacht.

Figure 15 [S. 36]: Newton-Iterationen: Start bei $x_0 = 3.5$, schnelle Konvergenz zu $\pi \approx 3.14159$. (Markiert: $x_0$ | 1st eval unterhalb der Achse bei ca. 3.5; $x_1$ | 2nd eval und $x_2$ | 3rd eval nahe 3.1–3.2.)

Ableitung als Quelle lokaler Information: $f'(x) = \cos(x)$ gibt die Tangentensteigung an einem Punkt.

Randnotiz [S. 36]: Preis der Raffinesse — mehr Hyperparameter und komplexere Berechnungen (Ableitungsauswertung und Division), aber Gewinn an Konvergenzgeschwindigkeit.

**[S. 37]** Mehrere Möglichkeiten, aus der Ableitung Richtung und Schrittweite abzuleiten: Schritt fester Größe in Abstiegsrichtung, Schrittweite proportional zur Ableitung, oder (hier) nächster Schätzwert dort, wo die Tangente die Null kreuzt — das ist die Lösung der linearen Approximation von $f$ bei $x_n$.

Newton von Hand, Start bei $x_0 = 3.5$:
$$x_1 = x_0 - \frac{\sin(x_0)}{\cos(x_0)} = 3.5 - \frac{-0.351}{-0.936} = 3.5 - 0.375 = 3.125$$
$$x_2 = 3.125 - \frac{\sin(3.125)}{\cos(3.125)} = 3.125 - \frac{0.0008}{-0.9999} \approx 3.14159$$
$$x_3 \approx 3.14159$$
$$\text{und } \sin(3.14159) \approx 0$$

Nach nur 2 Iterationen (fairerweise: 4 Funktions-/Ableitungsauswertungen) ist $x \approx 3.14159$ mit Fehler $< 10^{-5}$.

Lernziele [S. 37]:
- Newton-Raphson-Iteration für 1D-Nullstellensuche herleiten und anwenden.
- Taylorentwicklung (Taylor expansion) herleiten/verstehen und ihre Rolle in Newtons Methode.
- Konvergenzraten und Fehlermodi (failure modes) von Newtons Methode analysieren.
- Sekantenverfahren (Secant method) verstehen und anwenden, wenn Ableitungen nicht verfügbar sind.

Randnotiz [S. 37]: "Newton-Rhapson" [sic, so im PDF geschrieben]: Isaac Newton hatte die allgemeine Idee, Joseph Raphson vereinfachte den Ansatz zu einer praktischen iterativen Methode.

**[S. 38]** *Newton-Raphson and Taylor Expansion*.

Figure 16 [S. 38]: Geometrische Intuition von Newtons Methode: Für $f(x) = x^2 - 2$ schneidet die Tangente bei $(x_0, f(x_0))$ (mit $x_0 = 2$, $f(x_0) = 2$) die x-Achse bei $x_1$, der nächsten Approximation (Plotbereich x ca. 1.3–2.2, y ca. −2 bis 2; gestrichelte Tangente schneidet Achse bei ca. 1.5).

Ziel formalisieren: finde $x^*$ mit $f(x^*) = 0$.

Lineare Approximation (Gleichung (20)):
$$f(x) \approx f'(x_n) \cdot (x - x_n) \quad \text{für } x \text{ nahe } x_n + f(x_n) \tag{20}$$
[UNSICHER: Layout im PDF: "f(x) ≈ f′(xₙ) · (x − xₙ)   for x close to xₙ + f(xₙ)" — gemeint ist offenbar $f(x) \approx f(x_n) + f'(x_n)(x - x_n)$ für $x$ nahe $x_n$; der Term $+ f(x_n)$ ist in der Druckzeile hinter die Bedingung gerutscht. Exakt wie abgedruckt wiedergegeben.]

Randnotiz: Diese lineare Approximation ist die Taylorentwicklung erster Ordnung von $f$ um $x_n$; Taylorentwicklungen folgen später formal.

Nächsten Schätzwert finden — Nullsetzen der Approximation:
$$0 = f(x_n) + f'(x_n) \cdot (x_{n+1} - x_n)$$
$$f'(x_n) \cdot (x_{n+1} - x_n) = -f(x_n)$$
$$x_{n+1} - x_n = -\frac{f(x_n)}{f'(x_n)}$$

**Newton-Raphson-Iterationsformel** (Gleichung (21)):
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \tag{21}$$

**Algorithmus 1: Newton-Raphson Method** [S. 38] (exakt):
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

**[S. 39]** *Taylor Expansion*.

Bisher wurde der linearen Approximation bei $x_n$ vertraut (Gleichung (22)):
$$f(x) \approx f'(x_n)(x - x_n) + f(x_n) \tag{22}$$
um schnell den nächsten Schätzwert $x_{n+1}$ zu finden. Rechtfertigung: die Taylorentwicklung — fundamentales Werkzeug dafür, wie gut Polynome glatte Funktionen an einem Punkt approximieren. Herleitung von Grundprinzipien; Illustration an der Sinusfunktion.

Randnotizen [S. 39]:
- Der Fehler "Derivative too small" (Algorithmus 1) tritt auf, wenn $f'(x_k)$ gegen null geht → Division durch null oder numerische Instabilität.
- **Smooth (glatt)**: Eine Funktion ist glatt, wenn sie Ableitungen aller Ordnungen besitzt, und ist somit differenzierbar.

Figure 17 [S. 39]: Kontinuierliche Kurve $f(x) = \sin(x)$ und diskretisierte Version (schwarze Punkte) auf $[-3, 1]$ mit Schrittweite $h = 1$. [Anm.: Bildunterschrift wie abgedruckt; gezeigt ist die Sinuskurve.]

**0. Ordnung — Funktionswert treffen**: Gesucht Polynom $P(x)$, das $f(x)$ nahe $x_n$ approximiert. Start: am Punkt selbst übereinstimmen (Gleichung (23)):
$$P(x_n) = f(x_n) \tag{23}$$
Das entspricht fast dem, was Gittersuche tut: nur Funktionswerte an diskreten Punkten, ohne Information über das Verhalten dazwischen.

**1. Ordnung — erste Ableitung treffen**: Nahe $x_n$ zählt die Steigung. Gefordert $P'(x_n) = f'(x_n)$. Linearer Term (Gleichung (24)):
$$P(x) = f(x_n) + f'(x_n)(x - x_n) \tag{24}$$

**[S. 40]** Abbildungen:
- Figure 18: $f(x) = \sin(x)$ mit konstanter Approximation $P(x) = f(-1)$ (schwarze gestrichelte horizontale Linie) verankert bei $x = -1$ (schwarzer Punkt).
- Figure 19: $f(x) = \sin(x)$ mit linearer Approximation $P(x) = f(-1) + f'(-1)(x + 1)$ (schwarze gestrichelte Tangente) verankert bei $x = -1$.
- Figure 20: $f(x) = \sin(x)$ mit quadratischer Approximation $P(x) = f(-1) + f'(-1)(x+1) + \frac{f''(-1)}{2}(x+1)^2$ (schwarze gestrichelte Parabel) verankert bei $x = -1$.

**2. Ordnung — zweite Ableitung treffen**: Krümmung erfasst, wie sich die Steigung ändert. Gefordert $P''(x_n) = f''(x_n)$. Quadratischer Term (Gleichung (25)):
$$P(x) = f(x_n) + f'(x_n)(x - x_n) + \frac{f''(x_n)}{2}(x - x_n)^2 \tag{25}$$

Randnotiz: Warum durch 2 teilen? Zweimaliges Differenzieren von $(x - x_n)^2$ ergibt Faktor 2; für $P''(x_n) = f''(x_n)$ muss durch 2 geteilt werden, um diesen Faktor zu kürzen.

**n-te Ordnung — allgemeines Muster. Taylorentwicklung** von $f$ um einen Punkt $x_n$:
$$f(x) = f(x_n) + f'(x_n)(x - x_n) + \frac{f''(x_n)}{2!}(x - x_n)^2 + \frac{f'''(x_n)}{3!}(x - x_n)^3 + \cdots$$

Kompakt (Gleichung (26)):
$$f(x) = \sum_{k=0}^{\infty} \frac{f^{(k)}(x_n)}{k!}(x - x_n)^k \tag{26}$$

Randnotiz: "Around a point" — die Approximationen sind an einem spezifischen Punkt $x_n$ verankert; die Taylorentwicklung ist eine lokale Approximation.

**[S. 41]** *Why linear is enough for Newton?* Ziel ist $f(x^*) = 0$ zu lösen, nicht $f(x)$ bestmöglich zu berechnen. Bessere Approximation kostet: höhere Ableitungen, komplexere Polynome. In numerischen Berechnungen muss die Taylorreihe bei endlicher Ordnung abgeschnitten werden; der lineare Term ist der erste nicht-konstante Term mit Richtungsinformation.

**Herleitung der Konvergenzrate** [S. 41]. (Aus Kap. 3: Methode konvergent, wenn die Approximation einen stabilen Grenzwert erreicht.) Für Newton mit Nullstelle $x^*$, $f(x^*) = 0$, gewünscht (Gleichung (27)):
$$|x_n - x^*| \to 0 \quad \text{als } n \to \infty \tag{27}$$

Sei $e_n = x_n - x^*$ der Fehler bei Iteration $n$. Taylorentwicklung 2. Ordnung von $f$ um die wahre Nullstelle $x^*$ (Gleichung (28)):
$$f(x_n) = f(x^*) + f'(x^*)(x_n - x^*) + \frac{f''(\xi)}{2}(x_n - x^*)^2 \tag{28}$$
wobei $\xi$ ein Punkt zwischen $x_n$ und $x^*$ ist (Lagrange-Restglied-Form). Da $f(x^*) = 0$, vereinfacht sich dies zu (Gleichung (29)):
$$f(x_n) = f'(x^*) \cdot e_n + \frac{f''(\xi)}{2}e_n^2 \tag{29}$$
mit $e_n = x_n - x^*$.

Newtons Formel anwenden:
$$e_{n+1} = x_{n+1} - x^* = x_n - \frac{f(x_n)}{f'(x_n)} - x^* = (x_n - x^*) - \frac{f(x_n)}{f'(x_n)} = e_n - \frac{f(x_n)}{f'(x_n)}$$

Vereinfachte Taylorentwicklung für $f(x_n)$ einsetzen (Gleichung (30)):
$$e_{n+1} = e_n - \frac{f'(x^*) \cdot e_n + \frac{f''(\xi)}{2}e_n^2}{f'(x_n)} \tag{30}$$

Für Punkte nahe $x^*$ Annahme $f'(x_n) \approx f'(x^*)$ (Gleichung (31)):
$$e_{n+1} \approx e_n - \frac{f'(x^*) \cdot e_n + \frac{f''(\xi)}{2}e_n^2}{f'(x^*)} = e_n - e_n - \frac{f''(\xi)}{2f'(x^*)}e_n^2 \tag{31}$$

Randnotiz [S. 41]: Annahme in Aktion: $10^{-1} \to 10^{-2} \to 10^{-3} \to 10^{-6} \to 10^{-12}$. Sobald nah genug und die Annahmen gelten (nach Iteration 2), quadriert sich der Fehler perfekt — quadratische Konvergenz.

**[S. 42]** Der Fehlerterm erster Ordnung kürzt sich, übrig bleibt (Gleichung (32)):
$$e_{n+1} \approx -\frac{f''(\xi)}{2f'(x^*)}e_n^2 \tag{32}$$

Abstrakter (Gleichung (33)):
$$|e_{n+1}| \leq C \cdot |e_n|^2 \tag{33}$$
Der Fehler der nächsten Iteration ist näherungsweise proportional zum Quadrat des aktuellen Fehlers; $C$ ist eine Konstante, die von Krümmung und Steigung der Funktion an der Nullstelle abhängt. **Das ist quadratische Konvergenz (quadratic convergence)** — Konvergenzordnung 2.

Tabelle 2 [S. 42]: Newton zur Berechnung von $\sqrt{2}$, Start $x_0 = 2$ ("introductory example"):

| $n$ | $x_n$ | $|e_n|$ (error) |
|---|---|---|
| 0 | 2.000000000 | $5.86 \times 10^{-1}$ |
| 1 | 1.500000000 | $8.58 \times 10^{-2}$ |
| 2 | 1.416666667 | $2.45 \times 10^{-3}$ |
| 3 | 1.414215686 | $2.13 \times 10^{-6}$ |
| 4 | 1.414213562 | $4.5 \times 10^{-12}$ |

Bildunterschrift: Der Fehler quadriert sich näherungsweise mit jeder Iteration.

**Fehlermodi (failure modes) von Newtons Methode** [S. 42]: kann auf mehrere Arten scheitern (Visualisierungsübung am Plot).

Figure 21 [S. 42]: $f(x) = x^3 - x$ hat mehrere Nullstellen (Plot x ca. −0.4 bis 1.4; Nullstellen-Punkte bei 0 und 1 markiert). Fehlermodi: Null-Ableitung (wenn $f'(x_n) = 0$, ist die Tangente horizontal und schneidet die Achse nicht), Oszillation (besonders bei symmetrischen Funktionen kann Newton zwischen Punkten zyklisch springen), und mehrdeutige Startpunktwahl ($x_0$ beeinflusst stark, welche Nullstelle gefunden wird).

Nicht hinnehmbar ist, wenn $f'(x)$ nicht berechnet werden kann. Randnotiz — Gründe:
- Ableitung ist teuer zu berechnen.
- Funktion ist eine Black Box (z. B. eine Simulation).
- Funktion ist nicht überall differenzierbar.

**[S. 43]** *Secant Method (Sekantenverfahren)* — Ableitung nur über Funktionsauswertungen approximieren, kein expliziter Ableitungsausdruck nötig.

"A poor man's derivative" — Ableitung aus zwei letzten Punkten approximieren (Differenzenquotient):
$$f'(x_n) \approx \frac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}$$

Visuell: Steigung der Sekante durch die Punkte $(x_{n-1}, f(x_{n-1}))$ und $(x_n, f(x_n))$ auf dem Graphen von $f$.

Figure 22 [S. 43]: Sekantenverfahren: Die Gerade durch $(x_0, f(x_0))$ und $(x_1, f(x_1))$ liefert die nächste Approximation $x_2$ (Plot: Kurve mit Punkten bei ca. (1, f(1)) und (2, f(2)), Sekante schneidet Achse bei ca. 1.35).

Hinweis: Es werden zwei Startwerte $x_0$ und $x_1$ benötigt (statt nur einem bei Newton).

In Newtons Formel eingesetzt ergibt sich das iterative **Sekantenverfahren** (Gleichung (34)):
$$x_{n+1} = x_n - f(x_n) \cdot \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})} \tag{34}$$

**Algorithmus 2: Secant Method** [S. 43] (exakt):
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

**[S. 44]** *Examples & Exercises*.

Figure 23 [S. 44]: $f(x) = x^3 - x$ hat mehrere Nullstellen; angenommenes Ziel ist die Nullstelle bei $x = 1$. Graue gestrichelte Linie zeigt die Ableitung $f'(x) = 3x^2 - 1$.

**Newton von Hand** [S. 44]: Nullstelle von $f(x) = x^3 - x = 0$, erst geometrisch, dann von Hand. Nullstellen bei $x = -1, 0, 1$. Ziel: Nullstelle bei $x = 1$, Start $x_0 = 1.4$. Taylorentwicklung 1. Ordnung um $x_n$:
$$f(x) \approx f(x_n) + f'(x_n)(x - x_n),$$
$$f(x_n) \approx f(x) - f'(x_n)(x - x_n)$$

Mit $f(x) = x^3 - x = 0$ und $f'(x) = 3x^2 - 1$, Start $x_0 = 1.4$:
$$x_1 = x_0 - \frac{f(x_0)}{f'(x_0)} = x_0 - \frac{x_0^3 - x_0}{3x_0^2 - 1} = 1.4 - \frac{2.744 - 1.4}{5.88 - 1} = 1.4 - \frac{1.344}{4.88} \approx 1.127$$
$$x_2 = 1.127 - \frac{1.127^3 - 1.127}{3(1.127)^2 - 1} \approx 1.127 - \frac{0.432}{2.808} \approx 0.976$$
$$x_3 = 0.976 - \frac{0.976^3 - 0.976}{3(0.976)^2 - 1} \approx 0.976 - \frac{-0.072}{1.857} \approx 1.014$$

Die Nullstelle bei $x = 1$ wird schnell gefunden.

**Sekante von Hand** [S. 44]: gleiche Aufgabe mit $x_0 = 1.2$, $x_1 = 1.4$ (erst geometrisch, dann von Hand).

**[S. 45]** Sekantenrechnung:
$$x_2 = x_1 - f(x_1) \cdot \frac{x_1 - x_0}{f(x_1) - f(x_0)} = 1.4 - (0.744) \cdot \frac{1.4 - 1.2}{0.744 - 0.128} = 1.4 - 0.744 \cdot \frac{0.2}{0.616} \approx 1.4 - 0.241 \approx 1.159$$
$$x_3 = 1.159 - f(1.159) \cdot \frac{1.159 - 1.4}{f(1.159) - f(1.4)} \approx 1.159 - (0.283) \cdot \frac{-0.241}{0.283 - 0.744} \approx 1.159 - 0.283 \cdot \frac{-0.241}{-0.461}$$
$$\approx 1.159 - 0.283 \cdot 0.522 \approx 1.159 - 0.148 \approx 1.011$$

**Geometrical Failure Search** [S. 45]: Startpunkte $x_0$ für verschiedene Fehlermodi finden: (a) Newton scheitert wegen Null-Ableitung, (b) Konvergenz zu einer Nicht-Ziel-Nullstelle, (c) Oszillation zwischen Punkten.

*Enter the machine* [S. 45]: Konvergenz und Konvergenzraten von Grid-Search, Newton und Sekantenverfahren in Python betrachten; mit verschiedenen Startpunkten experimentieren, Fehlermodi in der Praxis beobachten. Startpunkte erst geometrisch, dann analytisch finden, dann im Code verifizieren.

*Self-Reflection and Recap* [S. 45] — Fragen:
- Hauptvorteil von Newtons Methode gegenüber Grid-Search?
- Warum reicht eine lineare Approximation für Nullstellensuche? Was sagt die Taylorentwicklung über diese Wahl?
- Warum ist quadratische Konvergenz so mächtig? Wie viele Iterationen braucht Newton von Fehler $10^{-1}$ zu Fehler $10^{-16}$?

**[S. 46]** Weitere Frage:
- In welchen Situationen Sekante statt Newton bevorzugen? Warum nicht in anderen?

Recap [S. 46]:
- Newton-Raphson gibt (begrenzte) Konvergenzgarantien nahe einfachen Nullstellen (simple roots).
- Taylorentwicklung: systematischer Weg, Funktionen lokal zu approximieren.
- Taylorentwicklung rechtfertigt die lineare Approximation in Newtons Methode, erklärt die quadratische Konvergenz und erlaubt Fehlerschätzung je Iteration.
- Wenn die Ableitung schwer zu berechnen ist, approximiert das Sekantenverfahren die Ableitung aus zwei Punkten und konvergiert.

*Local methods find local solutions*: Newton konvergiert zu welchem Optimum auch immer in der Nähe; neigt zu Oszillation zwischen Punkten oder Divergenz bei (nahe) null Ableitung. Nächstes Kapitel: Nullstellensuche als Optimierungsproblem umformulieren; globale Optimierung bei Landschaften mit vielen Tälern oder pathologisch schwierigen Fällen.

Randnotiz (Teaser): Wie sicherstellen, dass die globale Lösung gefunden wird, nicht nur eine lokale?

---

## Kapitel 5: Global Optimization [S. 47–56]

**[S. 47]** Kapiteltitel *Global Optimization*, Datumszeile *2026-05-06 · feisty cranberry Hermelin*. Motto: "And then there were many." Abschnitt "The Why".

Rückblick: Newton und Gradient Descent sind lokale Methoden — sie konvergieren zur nächstgelegenen Lösung. Was, wenn die nahe Lösung schlecht ist oder eine viel bessere weiter entfernt liegt?

Kapitelinhalte:
- Shekels Foxholes (Shekel's foxholes), klassische Testfunktion für globale Optimierung.
- Kurz: Optimierungsproblem als Nullstellenproblem formulieren.
- Strategien zum Finden globaler Minima.

ML/DL-Kontext: Multi-dimensionale und globale Optimierung ist entscheidend für effektives Training großer Modelle. Loss-Landschaften neuronaler Netze⁸ sind hochgradig nicht-konvex, haben flache Regionen und viele lokale Minima.

Randnotiz [S. 47]: Visualisierung von Loss-Landschaften: Li et al. (2018) zeigen das komplexe Terrain neuronaler Netzoptimierung; verschiedene Initialisierungen führen zu verschiedenen Endlösungen. Referenz ⁸: H. Li, Z. Xu, G. Taylor, C. Studer, T. Goldstein: Visualizing the loss landscape of neural nets. 31:6389–6399, 2018. URL `https://proceedings.neurips.cc/paper_files/paper/2018/file/a41b3bb3e6b050b6c9067c67f663b915-Paper.pdf`.

**[S. 48]** *Hands On Experience*. **Shekels Foxholes**: klassische Testfunktion für globale Optimierung mit kontrollierter Multimodalität. In 1D (Gleichung (35)):
$$f(x) = -\sum_{i=1}^{m} \frac{c_i}{(x - a_i)^2 + r_i} \tag{35}$$
wobei $a_i$ die "Foxhole"-Positionen, $c_i$ die Tiefe jedes Lochs und $r_i$ die Breite steuert. Durch Anpassen entsteht eine Landschaft mit mehreren lokalen Minima und einem globalen Minimum — ideales Testfeld für Optimierungsalgorithmen.

Konkretes Beispiel mit drei Foxholes [S. 48]:
$$f(x) = -\frac{1}{(x - 0)^2 + 0.7} - \frac{1.7}{(x - 4)^2 + 0.2} - \frac{1.1}{(x - 7)^2 + 0.4}$$

Figure 24 [S. 48]: 1D-Shekel-Foxholes-Funktion (schwarz) mit drei lokalen Minima und ihre Ableitung (grau gestrichelt). Täler bei $x = 0, 4, 7$, tiefstes (globales Minimum) bei $x = 4$ (Funktionswert dort ca. −8.5 laut Plot-Skala bis −5 sichtbar). Die Ableitung (gestrichelt) kreuzt null an jedem Minimum. Plotbereich x von −2 bis 12.

Globales Minimum bei $x = 4$; die anderen beiden Minima bei $x = 0$ und $x = 7$ sind lokale Minima. Diese Information ist beim Lauf eines Optimierungsalgorithmus nicht verfügbar — sichtbar sind nur Funktionswerte und Gradienten an den ausgewerteten Punkten.

Sensitivität gegenüber Anfangsbedingungen $x_0$: Start von Newtons Methode nahe $x = 0$ oder $x = 7$ → Konvergenz zu lokalem Minimum, nicht zum globalen bei $x = 4$.

Randnotizen [S. 48]:
- Die Ableitung (gestrichelte Linie) ist die Antwort auf die Formulierung der Optimierung als Nullstellensuche: Die Minima von $f(x)$ entsprechen den Nullstellen von $f'(x)$.
- Referenz ⁹: J. Shekel: Test functions for multimodal search techniques. 1971.

**[S. 49]** Von $x_0 = 7.2$: Newton konvergiert zum lokalen Minimum bei $x \approx 7$. Für Optimierung mit Newton wird das Nullstellenproblem auf $f'(x) = 0$ gelöst — Reformulierung des Optimierungsproblems. **Newton-Update für Optimierung** (Gleichung (36)):
$$x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)} \tag{36}$$

Figure 25 [S. 49]: Erste Ableitung (schwarz) und zweite Ableitung (grau gestrichelt) der 1D-Shekel-Funktion. Täler der Funktion bei $x = 0, 4, 7$, tiefstes (global) bei $x = 4$. Erste Ableitung kreuzt null an jedem Minimum; zweite Ableitung ist an Minima positiv (bestätigt lokale Krümmung). Plotbereich x von −2 bis 12.

Die Ableitungen vereinfachen sich zu:
$$f'(x) = \frac{2x}{(x^2 + 0.7)^2} + \frac{3.4(x - 4)}{((x - 4)^2 + 0.2)^2} + \frac{2.2(x - 7)}{((x - 7)^2 + 0.4)^2}$$
$$f'(7.2) \approx 0.005 + 0.100 + 2.27 = 2.38$$
[UNSICHER: Im PDF steht "f′(7.2) ≈ 0.005 + 0.100 + 2.27 = 2.38" — Summe arithmetisch 2.375, gerundet 2.38.]

$$f''(x) = \frac{2(0.7 - 3x^2)}{(x^2 + 0.7)^3} + \frac{3.4(0.2 - 3(x - 4)^2)}{((x - 4)^2 + 0.2)^3} + \frac{2.2(0.4 - 3(x - 7)^2)}{((x - 7)^2 + 0.4)^3}$$
$$f''(7.2) \approx -0.002 - 0.091 + 7.23 = 7.14$$

Newton-Schritte:
$$x_1 = 7.2 - \frac{2.38}{7.14} \approx 6.87$$
$$x_2 \approx 7.02$$
$$x_3 \approx 7.00$$

Nullstellenverfahren können also zur Optimierung genutzt werden, indem man sie auf die Ableitung anwendet: $f'(x)$ ist an Extrema null — gefunden werden Minima oder Maxima.

Randnotiz [S. 49]: Notation lokaler Minima: Der Asterisk (*) ist konventionell für globale Optima reserviert. Zur Unterscheidung lokale Minima z. B. mit $x^\circ$ (x-circle) oder $x_i$ für das $i$-te lokale Minimum bezeichnen.

**[S. 50]** Hier hatten wir Pech: Die Methode wird vom nahen Foxhole bei $x^\circ \approx 7$ angezogen.

Fundamentales Problem: Lokale Optimierung garantiert nur das Finden eines nahegelegenen Extremums. Selbst mit Konvergenzgarantien: Start von $x_0 = 3$ wäre Glück gewesen, aber von $x_0 = -2$ oder $x_0 = 8$ wird das globale Minimum verfehlt. Motivation für die folgenden globalen Optimierungsstrategien.

Lernziele [S. 50]:
- Erklären, warum lokale Methoden das Finden globaler Minima nicht garantieren können.
- Strategien zum Finden globaler Extrema anwenden.
- Verstehen, wie Gradient Descent die Optimierung Richtung Minima lenkt.

**[S. 51]** *Global Optimization Strategies* — Formalisierung lokaler und globaler Extrema.

**Lokale Optimierung** findet ein nahegelegenes Minimum (Gleichung (37)):
$$\mathbf{x}^* = \arg \min_{\mathbf{x} \in \mathcal{N}(\mathbf{x}_0)} f(\mathbf{x}) \tag{37}$$
wobei $\mathcal{N}(\mathbf{x}_0)$ eine Umgebung (neighborhood) des Startpunkts ist.

Randnotiz: $\mathcal{N}$ ist eine Menge von Punkten um $\mathbf{x}_0$, z. B. $\mathcal{N}(\mathbf{x}_0) = \{\mathbf{x} : \|\mathbf{x} - \mathbf{x}_0\| < \epsilon\}$ für einen Radius $\epsilon$.

**Globale Optimierung** findet das beste Minimum (Gleichung (38)):
$$\mathbf{x}^* = \arg \min_{\mathbf{x} \in \Omega} f(\mathbf{x}) \tag{38}$$
wobei $\Omega$ die gesamte Suchdomäne ist — die Suchdomäne kann "inifinitely" [sic] groß sein.

**Konvexität als Trennlinie**: Für konvexe Probleme findet jede lokale Methode das globale Optimum. Schwierigkeit bei nicht-konvexer Optimierung: Landschaft mit mehreren lokalen Minima, Sattelpunkten (saddle points) und Plateaus.

Randnotiz — Definition konvex: Eine Funktion $f$ ist *konvex*, wenn $f(\lambda x + (1 - \lambda)y) \leq \lambda f(x) + (1 - \lambda) f(y)$ für alle $\lambda \in [0, 1]$. Für konvexe Funktionen ist jedes lokale Minimum das globale Minimum — lokale Methoden genügen. Nicht-konvexe Funktionen (wie Shekels Foxholes oder Loss-Flächen neuronaler Netze) sind der schwierige Fall.

**Random Restarts** — einfachste globale Strategie ("fühlt sich wieder wie Brute-Force an").

**Algorithmus 3: Random Restarts** [S. 51] (exakt):
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

Erfolgswahrscheinlichkeit [S. 51]: Hat das Einzugsgebiet (basin of attraction) des globalen Minimums Wahrscheinlichkeit $p$, dann gilt mit $K$ Restarts (Gleichung (39)):
$$P(\text{find global}) = 1 - (1 - p)^K \tag{39}$$
Für $p = 0.1$ und $K = 20$: $P = 1 - 0.9^{20} \approx 0.88$. Üblicherweise ist $p$ vorab unbekannt. Heuristik zur Wahl von $K$ ohne Kenntnis von $p$: $K$ erhöhen, bis sich die beste Lösung stabilisiert (keine Verbesserung nach mehreren Restarts). **Patience** ist ein üblicher Hyperparameter dieser Heuristik: wie viele Restarts ohne Verbesserung abgewartet werden, bevor gestoppt wird.

Randnotiz [S. 51]: Initialisierung neuronaler Netze und Training mehrerer Netze mit verschiedenen Seeds = implizite Random Restarts; für große Modelle aber unpraktisch.

**[S. 52]** **Basin Hopping**: erkundet die Landschaft durch Abwechseln von lokaler Optimierung und zufälligen Sprüngen. Anders als Random Restarts (kompletter Reset) erlaubt Basin Hopping das Entkommen aus lokalen Minima bei gleichzeitiger Nutzung lokaler Optimierung.

**Algorithmus 4: Basin Hopping** [S. 52] (exakt):
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

Sprungverteilung (jump distribution) $\delta \sim \mathcal{D}$: z. B. Gaußverteilung mit Zentrum null oder Gleichverteilung über einen bestimmten Bereich.

**Simulated Annealing** [S. 52]: kombiniert Basin Hopping mit probabilistischem Akzeptanzkriterium für Punktkandidaten. Anfangs wird ein Sprung in eine schlechtere Lösung mit Wahrscheinlichkeit $\exp^{-\Delta f / T}$ akzeptiert, wobei $T$ (Temperatur) über die Zeit abnimmt. Später wird der Algorithmus konservativer und akzeptiert nur noch verbessernde Kandidaten → Konvergenz zu einem Optimum.

Randnotizen [S. 52]:
- **Noisy Newton**: gleiche Hopping-Idee durch Addieren von Gauß-Rauschen zum Newton-Schritt: $\mathbf{x}_{n+1} = \ldots + \boldsymbol{\xi}_n$.
- $\Delta f$ = Zunahme des Zielfunktionswerts beim Wechsel von der aktuellen Lösung zu einem schlechteren Kandidaten.

**Stochastische Methoden** [S. 52]: fügen Rauschen hinzu, indem die Loss-Landschaft approximiert wird, um lokalen Optima zu entkommen. Beispiel: 1D-Shekel-Funktion als Funktion zweiter Ordnung approximieren durch Wahl dreier Punkte auf der Foxhole-Kurve.

Take-away: Die Loss-Landschaft ist nicht statisch, sondern kann konstruiert und geformt werden ("engineered and formed"). Durch Approximation der Loss-Landschaft auf Mini-Batches (verschiedene Punktauswahlen) erhält man eine verrauschte Schätzung der wahren Loss-Landschaft — hilft, lokalen Minima zu entkommen. Die Loss-Landschaft wird stark von der Wahl …

**[S. 53]** … der Loss-Funktion selbst beeinflusst. Der Newton-Schritt ist allerdings sehr rauschempfindlich; andere Ansätze gehen besser damit um.

Figure 26 [S. 53]: Original-Shekel-Funktion (grau dünn) mit einer Approximation zweiter Ordnung (durchgezogen schwarz) durch drei Stützpunkte (Punkte) gefittet. Ableitung der Approximation als grau gestrichelte Linie. Die Quadratik erfasst den Gesamttrend, glättet aber die einzelnen Foxholes weg.

*Newton's Method for finding Minima* [S. 53]: Reformulierung der Optimierung als Nullstellensuche, Newton-Update (Gleichung (40)):
$$x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)} \tag{40}$$

**Minima, Maxima und Sattelpunkte**: Newtons Methode findet Punkte mit $f''(x) = 0$ [UNSICHER: so im PDF — „Newton's method finds points where $f''(x) = 0$"; sachlich gemeint sind Punkte mit $f'(x) = 0$]. Diese können Minima, Maxima oder Sattelpunkte sein. Der Test mit der zweiten Ableitung (second derivative test) unterscheidet:
- (a) $f''(x^*) > 0$: lokales Minimum (Kurve biegt sich nach oben)
- (b) $f''(x^*) < 0$: lokales Maximum (Kurve biegt sich nach unten)
- (c) $f''(x^*) = 0$: nicht schlüssig (möglicher Sattelpunkt oder Wendepunkt)

Um Newton nur Richtung Minima zu lenken, modifiziertes Update (Gleichung (41)):
$$x_{n+1} = x_n - \frac{f'(x_n)}{|f''(x_n)|} \tag{41}$$
So bewegt sich der Schritt immer in Richtung abnehmenden $f(x)$ — stets in Richtung des negativen Gradienten ("downhill").

Randnotizen [S. 53]:
- In Deep Learning werden typischerweise lokale Methoden (SGD, Adam) genutzt, in der Hoffnung: (1) die meisten lokalen Minima sind ungefähr gleich gut, (2) Überparametrisierung macht schlechte Minima selten, (3) Mini-Batch-Rauschen hilft, scharfen Minima zu entkommen, (4) adaptive Lernraten helfen bei Plateaus.
- Frage: Wie müsste das Update modifiziert werden, um stattdessen Maxima zu finden?

**[S. 54]** Abbildungen:
- Figure 27: Durchgezogen schwarz: erste Ableitung $f'(x)$ der 1D-Shekel-Funktion; grau gestrichelt: zweite Ableitung $f''(x)$. Schwarzer Marker bei $x = 6.1$ als Beispielposition; durchgezogene graue Linie ist die Tangente an $f'(x)$ dort (Steigung $\approx -2.66$). Vorzeichen und Größe von $f''(x)$ bestimmen Richtung und Schrittweite des Newton-Updates beim Lösen von $f'(x) = 0$.
- Figure 28: Durchgezogen schwarz: $f'(x)$; grau gestrichelt: absolute Krümmung $|f''(x)|$. Marker bei $x = 6.1$ (gleicher Punkt); die durchgezogene graue Linie illustriert das Ersetzen von $f''(x)$ durch $|f''(x)|$ (Steigung $\approx +2.66$). $|f''(x)|$ im Newton-Nenner entfernt das Krümmungsvorzeichen, erzwingt Abwärtsschritte und reduziert die Gefahr, Richtung lokales Maximum zu laufen.

*Examples & Exercises* [S. 54]. Konkrete Zahlen: Funktion mit 5 lokalen Minima; das Einzugsgebiet des globalen Minimums deckt 15 % der Suchdomäne ($p = 0.15$).

Wahrscheinlichkeit, das globale Minimum mit $K = 10$ Random Restarts zu finden:
$$P = 1 - (1 - 0.15)^{10} = 1 - 0.85^{10} = 1 - 0.1969 = 0.803$$
Ca. 80 % Chance. Wie viele Restarts für 99 %?
$$K = \frac{\ln(1 - 0.99)}{\ln(1 - 0.15)} = \frac{\ln(0.01)}{\ln(0.85)} = \frac{-4.605}{-0.1625} \approx 28.3$$

Randnotizen [S. 54]:
- Code: `https://github.com/Quillstacks/lecturecode_numericalmethods.git`.
- Hinweis (Hint): $P = 1 - (1-p)^K$ nach $K$ auflösen: $K = \frac{\ln(1-P)}{\ln(1-p)}$.

**[S. 55]** Also $K = 29$ Restarts. Übung: $K$ für $p = 0.05$ und $p = 0.01$ beim gleichen 99 %-Ziel berechnen.

Übungen [S. 55]:
- *On your machine*: eigene 1D-Shekel-Funktion entwerfen (erst einfach, später komplexer); lokale Optimierungsmethoden anwenden; zeigen, wo Newton (wieder) scheitert; verschiedene $x_0$ erkunden und Konvergenzverhalten beobachten; über Loss-Landschaft und Basin-Grenzen nachdenken.
- *Directing the search towards minima*: Der $|f''|$-Trick flippt das Krümmungsvorzeichen im Nenner und erzwingt Abwärtsschritte. Geometrische Bedeutung für die Tangentenkonstruktion überlegen; im Code ausprobieren.
- *Escaping Local Minima*: Random Restarts und Basin Hopping auf der eigenen 1D-Shekel-Funktion einsetzen; Anzahl der Funktionsiterationen bis zum globalen Minimum vergleichen. Wie anfällig sind sie für lokale Minima? Einfluss der Schrittweitenverteilung auf Basin Hopping?
- *Noise and landscape engineering*: Loss-Landschaft ist formbar; Approximation auf Mini-Batches (verschiedene Punktauswahlen). [Satz endet im PDF mit Komma — unvollständig im Original.]
- *Code exercise*: Random Restarts und Basin Hopping auf der 1D-Shekel-Funktion implementieren; Funktionsauswertungen bis zum globalen Minimum bei $x \approx 4$ vergleichen.
- *Finally, let's map out the basins of attraction*: 1D-Shekel-Funktion, Annahme: lokaler Optimierer konvergiert immer zum nächstgelegenen Foxhole. [Im PDF: "foxhole.2" — Druckartefakt.]
  - (a) Einzugsgebiete der drei Foxholes bei $x = 0, 4, 7$ skizzieren. Wo liegen die Basin-Grenzen?
  - (b) Wenn Basin Hopping einen Sprung $\delta \sim \text{Uniform}(-3, 3)$ vom lokalen Minimum $x^\circ = 7$ nutzt: Wahrscheinlichkeit, dass ein einzelner Sprung im Einzugsgebiet des globalen Minimums landet?
  - (c) Warum könnte Basin Hopping hier das globale Minimum schneller finden als Random Restarts?

Randnotizen [S. 55]:
- *Basin of Attraction*: Plots der Shekel-Funktion erneut betrachten, Einzugsgebiete je lokalem Minimum markieren, relative Größen schätzen. Welches ist das globale Minimum? Zusammenhang mit der Wahrscheinlichkeit, es per Random Restarts zu finden?
- *Non-Convex Basins*: Shekel ist im Allgemeinen nicht-konvex, die Basins aber schon [UNSICHER: Wortlaut „however the basins are"]; eine Funktion notieren, bei der die Einzugsgebiete nicht so leicht zu kartieren sind.
- Frage: Intelligenter Weg, die Schrittweitenverteilung während der Optimierung automatisch anzupassen? Gute Heuristik? Wie katastrophale Sprünge verhindern? Implementieren.

**[S. 56]** *Self-Reflection and Recap* — Fragen:
- Warum scheitert lokale Optimierung auf nicht-konvexen Landschaften wie Shekels Foxholes?
- Wie skaliert der nötige Aufwand mit der Größe des globalen Basins bei Random Restarts?
- Wie unterscheidet sich Basin Hopping von Random Restarts? [Im PDF grammatisch: "How do basin hopping differently from random restarts?"]
- Was sagt $f''(x_n)$ über die Loss-Landschaft, was charakterisiert es, wie nutzen?
- Wie hilft die Approximation der Loss-Landschaft durch verrauschte Schätzungen (Mini-Batches) beim Entkommen aus lokalen Optima?
- Bei $x_0$ im Basin eines lokalen Minimums: verschiedene Wege finden, wie die Optimierungsmethode entkommen kann; wie effektiv ist was?

Recap [S. 56]:
- Lokale Optimierungsmethoden (wie Newton) können auf nicht-konvexen Funktionen in lokalen Minima stecken bleiben.
- Globale Optimierungsstrategien (Random Restarts, Basin Hopping, Simulated Annealing, Stochastizität) erkunden den Suchraum breiter.
- Modifikation von Optimierungsmethoden mit Krümmungsinformation $f''(x)$ erlaubt genauere Spezifikation der Abstiegsrichtung.
- Die Loss-Landschaft kann durch Wahl der Loss-Funktion und Rauschen (z. B. stochastische Gradienten) gestaltet werden.

*Gradient descent is prone to getting stuck*: Bisher war die Antwort nur besser als Brute-Force. Nächstes Kapitel: Glättung der Loss-Landschaft zur Erhöhung der Robustheit des Gradientenabstiegs.

Randnotiz (Teaser): Was bei einer hochfrequenten Version von Shekels Foxholes? Welches Problem entsteht?

---

## Kapitel 6: Numerical Integration [S. 57–70]

**[S. 57]** Kapiteltitel *Numerical Integration*, Datumszeile *2026-05-04 · sneaky olive Falke*. Motto: "Smooth Operator." Abschnitt "The Why".

Motivation: Funktion mit Tausenden winziger, scharfer lokaler Minima (hochfrequente Version von Shekels Foxholes) — Gradient Descent bleibt sofort im ersten mikroskopischen Schlagloch stecken. Lösung: Numerische Integration (Gleichung (42)):
$$I = \int_a^b f(x)\,dx \tag{42}$$

Gründe, numerische Integration zu verstehen:
- Glättung der Loss-Landschaft → robustere Optimierungsmethoden.
- Findet tendenziell robustere Optima durch den Mittelungseffekt¹⁰ einer Region.

Deep-Learning-Kontext: Stochastic Gradient Descent (SGD) ist der Arbeitspferd-Optimierungsalgorithmus; eine Monte-Carlo-Methode¹¹,¹², die den Gradienten der Loss-Funktion durch Mittelung über den Gradienten eines zufälligen Mini-Batches von Datenpunkten schätzt. Numerische Integration macht das praktikabel — Training auf vollem Datensatz wäre prohibitiv teuer.

Randnotizen [S. 57]:
- "Melts all your memories and change into gold" (Songzitat, Verweis).
- Referenz ¹⁰: N. Keskar, D. Mudigere, J. Nocedal, M. Smelyanskiy, P. Tang: On large-batch training for deep learning: Generalization gap and sharp minima. 09 2016. doi: 10.48550/arXiv.1609.04836.
- **Monte Carlo**: Strategie, die Probleme durch Zufallsstichproben (random sampling) löst.
- Referenz ¹¹: J. Bergstra, Y. Bengio: Random search for hyper-parameter optimization. *Journal of Machine Learning Research*, 13:281–305, 2012.
- Referenz ¹²: Y. Gal, Z. Ghahramani: Dropout as a bayesian approximation: Representing model uncertainty in deep learning, 2016. URL `https://arxiv.org/abs/1506.02142`.

**[S. 58]** *Hands On Experience*. Bekannt: Diskretisierung kontinuierlicher Funktionen, endliche Präzision, Systeme mit spärlicher Information an diskreten Punkten.

Abbildungen:
- Figure 29: Kontinuierliche Kurve $f(x) = \sin(x)$ und diskretisierte Version (schwarze Punkte) auf $[-3, 1]$ mit Schrittweite $h = 0.2$.
- Figure 30: Kontinuierliche Kurve $f(x) = \sin(x) + \sin(2\pi x)$ und diskretisierte Version (schwarze Punkte) auf $[-3, 1]$ mit Schrittweite $h = 0.2$ — hochfrequente, oszillierende Kurve mit vielen lokalen Minima.
- Figure 31: Gleiche Funktion $f(x) = \sin(x) + \sin(2\pi x)$ als Balkendarstellung (diskretisiert, $h = 0.2$). [Bildunterschrift identisch zu Fig. 30 formuliert.]

Die Shekel-Funktion als hochfrequente Funktion war eine Herausforderung für globale Optimierung, machte die allgemeinen Ansätze aber nicht obsolet — wir diskretisieren und behandeln diese Funktionen wie gewohnt.

Nähere Betrachtung lokaler Minima zeigt, wie die hochfrequente Loss-Landschaft den Optimierungsalgorithmus ins nächstgelegene lokale Minimum drängt, z. B. bei $x = 0.6$ oder $x = -0.4$.

**[S. 59]** *Approximation durch numerische Integration* bei $x = -0.4$: Statt direkt zu lösen (Gleichung (43)):
$$f(-0.4) = -0.97720 \tag{43}$$
Approximation des Wertes durch Integration mit Breite $h = 0.2$:
$$h \cdot f(-0.4) \approx \int_{-0.5}^{-0.3} f(x)\,dx \approx \frac{h}{2}[f(-0.5) + f(-0.3)] \approx 0.2 \cdot \frac{-1.14973 - 0.97720}{2} = -0.11285$$
$$f(-0.4) \approx \frac{-1.14973 - 0.97720}{2} = -1.06347$$

Das ist (mit Blick auf globale Optima) eine viel bessere Approximation als die direkte Auswertung bei $x = -0.4$ ($-0.97720$). Die numerische Integration korrigiert die lokale Loss-Landschaft Richtung höherer Losses an diesem lokalen Minimum [UNSICHER: Formulierung im PDF: "gave us a correction of the local loss landscape towards higher losses at this local minima"].

Figure 32 [S. 59]: $f(x) = \sin(x) + \sin(2\pi x)$ und diskretisierte Version (schwarze Punkte) auf $[-3, 1]$ mit $h = 0.2$, geglättet durch numerische Integration mit Intervalllänge $h$ — die Kurve mit Punkten zeigt die geglättete Version.

Die Glättung wird noch deutlicher bei Integration über größere Intervalle, oder im konstruierten Beispiel bei Wahl von $h$ so, dass die Frequenz des Rauschsignals herausgemittelt wird.

Bisherige Intervall-Approximation ist grob (nur zwei Punkte).

Randnotiz [S. 59]: Was, wenn über ein Intervall integriert würde, das destruktive Interferenz ("destructive inference" [sic]) der zugrundeliegenden hochfrequenten Sinuskurve ergibt? Stichwort Wellenlängen.

**[S. 60]** Figure 33: $f(x) = \sin(x) + \sin(2\pi x)$, diskretisiert auf $[-3,1]$ mit $h = 0.2$, geglättet durch Nachbar-Mittelung (neighbour averaging) mit $h = 0.48$ (sodass $h/2 = 0.24$ die $\sin(2\pi x)$-Komponente nahezu auslöscht) — die Kurve sieht fast wie der reine $\sin(x)$ aus.

Lernziele [S. 60]:
- Mittelpunktsmethode (midpoint method), Trapezregel (trapezoid rule) und Simpson-Regel (Simpson's rule) herleiten und anwenden.
- Zusammengesetzte Regeln (composite rules) für höhere Genauigkeit verstehen.
- Lagrange-Interpolation kennen und ihren Bezug zu Quadraturregeln.
- Verstehen, wie der Fluch der Dimensionalität (curse of dimensionality) Monte Carlo motiviert.
- Monte-Carlo-Integration für hochdimensionale Probleme herleiten und anwenden.
- Monte-Carlo-Integration anwenden und erkennen, dass Batch-Mittelung in ML numerische Integration ist.

**[S. 61]** *Methods of Numerical Intgration* [sic, Tippfehler im Original].

Trivialste Integral-Approximation mit einem einzigen diskretisierten Wert (Mittelpunktsregel, ein Intervall):
$$I = \int_a^b f(x)\,dx.$$
$$I = \frac{b - a}{n} \cdot f\left(\frac{a + b}{2}\right)$$
$$I = h \cdot f(m)$$
Die Höhe des Rechtecks ist der Wert am Mittelpunkt $m$, die Breite ist $h$.

Verfeinerung: $[a, b]$ in $n$ Teilintervalle gleicher Breite $h$ teilen und Beiträge summieren — **Riemann-Summen-Approximation (Riemann sum)**:
$$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n-1} \int_{x_i}^{x_{i+1}} f(x)\,dx \approx \sum_{i=0}^{n-1} h \cdot f(m_i)$$
wobei $x_i = a + ih$ für $i = 0, 1, \ldots, n$.

**Mittelpunktsregel (midpoint rule)** dieser zusammengesetzten Intervalle: nutzt den Mittelpunkt (Durchschnitt der Endpunkte) jedes Intervalls — oft bessere Ergebnisse als Links-/Rechts-Endpunkt-Methoden, weil der Mittelpunkt die Krümmung der Funktion auf dem Intervall besser approximiert.

Randnotizen [S. 61]:
- Auf dem Intervall $[a, b]$: Mittelpunktswert $f(m)$; mit linkem Endpunkt Höhe $f(a)$; mit rechtem Endpunkt Höhe $f(b)$.
- Figure 34: $f(x) = \sin(x)$ mit Mittelpunktsregel-Integralen (graue Balken) für $a = -2$, $b = -1$, $h = 0.5$. Schwarze Punkte: Mittelpunkte. Kreise: Endpunkte. Die Balken berühren sich (Mittelpunktsregel ohne Lücke).
- Verdopplung der Teilintervalle reduzierte den Fehler um $\sim 4\times$ → deutet auf $O(h^2)$-Konvergenz hin.

Mehr Teilintervalle → kleinerer Fehler.

**[S. 62]** Kosten: mehr Funktionsauswertungen. Besser als Mittelpunkte?

**Trapezregel (trapezoid rule)**: Trapeze sind geometrisch ausdrucksstärker als Rechtecke und erfassen lineare Änderungen der Funktion zwischen den Endpunkten (Gleichung (44)):
$$\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(a) + f(b)\right] \tag{44}$$
mit $h = b - a$.

Figure 35 [S. 62]: $f(x) = \sin(x)$ mit Trapezregel-Flächen (graue Trapeze) für $a = -2$, $b = -1$, $h = 0.5$. Schwarze Punkte: Endpunkte. Fläche unter den Verbindungsgeraden der Endpunkte illustriert die Trapezregel.

**Zusammengesetzte Trapezregel (Composite Trapezoid Rule)** — Trapezregel je Teilintervall, Summation (vollständige Herleitung):
$$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n-1} \int_{x_i}^{x_{i+1}} f(x)\,dx$$
$$\approx \sum_{i=0}^{n-1} \frac{h}{2}\left[f(x_i) + f(x_{i+1})\right]$$
$$= \frac{h}{2}\left(f(x_0) + f(x_1)\right) + \frac{h}{2}\left(f(x_1) + f(x_2)\right) + \cdots + \frac{h}{2}\left(f(x_{n-1}) + f(x_n)\right)$$
$$= \frac{h}{2}\left[f(x_0) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{n-1}) + f(x_n)\right]$$
$$= \frac{h}{2}\left[f(a) + 2\sum_{i=1}^{n-1} f(x_i) + f(b)\right]$$
mit $x_i = a + ih$, $i = 0, 1, \ldots, n$.

Gewichte: Endpunkte $a$ und $b$ je mit 1 gewichtet, alle inneren Punkte mit 2 — jeder innere Punkt gehört zu zwei benachbarten Trapezen (einmal als rechter, einmal als linker Endpunkt), die Endpunkte nur zu einem.

Randnotiz [S. 62]: Division des Integrals durch $h$ ergibt einen gewichteten Mittelwert der Funktionswerte — bessere Approximation des Integrals als nur Mittelpunkt oder Endpunkte; reflektiert implizit lokale Krümmung und Information über das Funktionsverhalten über das Intervall.

**[S. 63]** **Simpson-Regel (Simpson's rule)**: erfasst Krümmung, daher oft viel bessere Approximation als die Trapezregel. Statt einer Geraden durch 2 Punkte wird ein quadratisches Polynom durch 3 Punkte gefittet. Simpson-Regel ist exakt für quadratische Polynome.

Figure 36 [S. 63]: $f(x) = \sin(x)$ mit Simpson-Regel-Flächen (grau, unter den Parabeln) für $a = -2$, $b = -1.5$, $h = 0.5$ und $a = -1.5$, $b = -1$, $h = 0.5$. Schwarze Punkte: Endpunkte; schwarze Punkte: Mittelpunkte bei $x = -1.75$ und $x = -1.25$. Durchgezogene Linie bei $x = -1.5$ trennt die zwei Intervalle. Jede Parabel illustriert den quadratischen Interpolanten der Simpson-Regel auf ihrem Teilintervall.

**Lagrange-Interpolation und Quadratur** [S. 63]: Lagrange-Interpolation konstruiert das eindeutige Polynom vom Grad $\leq n$, das durch gegebene Knoten $\{(x_j, y_j)\}_{j=0}^{n}$ geht, mit der Basis (Gleichung (45)):
$$L_j(x) = \prod_{\substack{m=0 \\ m \neq j}}^{n} \frac{x - x_m}{x_j - x_m} \tag{45}$$

Allgemeine Form eines quadratischen Polynoms (durch Punkte bei $a$, $m$, $b$):
$$f(x) = f(a) \cdot \frac{(x - m)(x - b)}{(a - m)(a - b)} + f(m) \cdot \frac{(x - a)(x - b)}{(m - a)(m - b)} + f(b) \cdot \frac{(x - a)(x - m)}{(b - a)(b - m)}$$

Für ein symmetrisches Intervall wird die Fläche unter $f(x)$ am besten approximiert, indem die Endpunkte je Gewicht $h/6$ und der Mittelpunkt Gewicht $2h/3$ erhalten: $A = C = h/6$, $B = 2h/3$ — verifizierbar durch Integration der Lagrange-Basispolynome über $[a, b]$ (detaillierte Rechnung im Text ausgelassen). Im symmetrischen Intervall sind die Knoten äquidistant: $x_0 = a$, $x_1 = m = \frac{a+b}{2}$, $x_2 = b$, sodass der Mittelpunkt $m - a = b - m = h$ erfüllt.

**Simpson-Regel** (einfaches Intervall):
$$\int_a^b f(x)\,dx \approx \frac{h}{6}f(a) + \frac{2h}{3}f(m) + \frac{h}{6}f(b) = \frac{h}{6}\left[f(a) + 4f(m) + f(b)\right]$$

Randnotiz: "Try with some points" — bei $x = 0$ starten und sehen, wie die Linearfaktoren wirken.

**Zusammengesetzte Simpson-Regel (Composite Simpson's Rule)**: Simpson-Regel auf jedes Paar von Teilintervallen anwenden und summieren (Annahme: $n$ gerade, $x_i = a + ih$). Beginnend beim Integral:

**[S. 64]** Vollständige Herleitung:
$$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n-1} \int_{x_i}^{x_{i+1}} f(x)\,dx$$
$$\approx \sum_{k=0}^{n/2-1} \frac{h}{6}\left[f(x_{2k}) + 4f(x_{2k+1}) + f(x_{2k+2})\right]$$
$$= \frac{h}{6}\left[f(x_0) + 4\sum_{k=0}^{n/2-1} f(x_{2k+1}) + 2\sum_{k=1}^{n/2-1} f(x_{2k}) + f(x_n)\right]$$
$$= \frac{h}{3}\left[f(x_0) + 4\sum_{\substack{i=1 \\ i \text{ odd}}}^{n-1} f(x_i) + 2\sum_{\substack{i=2 \\ i \text{ even}}}^{n-2} f(x_i) + f(x_n)\right].$$
[UNSICHER: Faktorwechsel von $\frac{h}{6}$ auf $\frac{h}{3}$ zwischen den letzten beiden Zeilen exakt wie im PDF abgedruckt; üblich ist $\frac{h}{3}$ bei Schrittweite $h$ zwischen Knoten bzw. $\frac{h}{6}$ bei Intervalllänge $h = x_{2k+2} - x_{2k}$.]

**Praktischer Rat**: "Stop at Simpson." Für höhere Genauigkeit zusammengesetzte Regeln mit mehr Teilintervallen nutzen. Hohe Grade ($n \geq 8$) entwickeln negative Gewichte und werden instabil.

Randnotizen [S. 64]:
- Frage: Was passiert, wenn man eine lineare Funktion mit einer Quadratik approximiert?
- **Runges Phänomen (Runge's phenomenon)**: Polynominterpolation hohen Grades oszilliert durch Overfitting → große Fehler an den Intervallrändern.

**Tabelle 3 [S. 64] — Vergleich der Quadraturgenauigkeiten** (höhere Ordnung erreicht gegebene Genauigkeit mit weniger Funktionsauswertungen; $h$ = Schrittweite, $n$ = Anzahl Auswertungspunkte bei Gauß-Quadratur):

| Method | Single Interval Error | Accumulated Error |
|---|---|---|
| Left/Right | $O(h^2)$ | $O(h)$ |
| Midpoint | $O(h^3)$ | $O(h^2)$ |
| Trapezoid | $O(h^3)$ | $O(h^2)$ |
| Simpson's 1/3 | $O(h^5)$ | $O(h^4)$ |
| In General (Gaussian Quadrature) | $O(h^{2n})$ | $O(h^{2n-1})$ |

*Monte Carlo & the Curse of Dimensionality* [S. 64]:

Für $d$-dimensionale Integrale braucht deterministische Quadratur mit $N$ Punkten pro Dimension $N^d$ Punkte insgesamt — unmöglich, erst recht nicht iterierbar während iterativer Optimierung.

Randnotiz: Ein neuronales Netz mit $d = 10^6$ (1 Million Parameter) bräuchte $(N)^{10^6}$ Gitterpunkte. Schon $N = 2$ ergibt $2^{10^6}$, eine Zahl mit 300.000 Stellen.

**Random Sampling**: Integral ohne volles Gitter schätzen. Integral als Erwartungswert (Gleichung (46)):
$$I = \int_\Omega f(\mathbf{x})\,d\mathbf{x} = |\Omega| \cdot \mathbb{E}_{\mathbf{X} \sim \text{Uniform}(\Omega)}[f(\mathbf{X})] \tag{46}$$
Das bestimmte Integral = Volumen der Domäne × Mittelwert von $f$ unter gleichverteilter Ziehung aus $\Omega$. Praktisch: Punkte gleichverteilt in $\Omega$ ziehen, $f$ dort auswerten, mitteln, mit $|\Omega|$ multiplizieren.

Randnotiz: $\Omega$ ist die Integrationsdomäne, $|\Omega|$ ihre Länge. Für 1D-Integral über $[a, b]$: $|\Omega| = b - a$. In höheren Dimensionen: Produkt der Längen je Dimension.

**[S. 65]** **Monte-Carlo-Gleichverteilungs-Sampling auf $[-2, -1]$**: Sei $X \sim \text{Uniform}(-2, -1)$. Dann (Gleichung (47)):
$$I = \frac{|\Omega|}{N} \sum_{i=1}^{N} f(\mathbf{X}_i), \qquad \mathbf{X}_i \overset{\text{i.i.d.}}{\sim} \text{Uniform}(\Omega) \tag{47}$$

Figure 37 [S. 65]: $f(x) = \sin(x)$ mit Mittelpunktsregel-Integralen (graue Balken) für $a = -2$, $b = -1$, $h = 0.5$. Kreise: Endpunkte/Stichprobenpunkte. [Bildunterschrift wie Fig. 34 formuliert: "The bars now touch, illustrating the midpoint rule without a gap"; gezeigt sind Zufallsstichprobenpunkte im Intervall.]

**Bias** [S. 65]: Da der Erwartungswert linear ist, ist der Schätzer erwartungstreu (unbiased) — sein Erwartungswert gleicht dem wahren Integral, für $N \to \infty$ (Gleichung (48)):
$$\mathbb{E}[\hat{I}_N] = I \tag{48}$$

**Varianz** [S. 65]: Maß der Streuung des Schätzers um den Mittelwert (wie groß der Fehler des Schätzers sein kann); folgt aus Unabhängigkeit der Stichproben (Gleichung (49)):
$$\text{Var}(\hat{I}_N) = \frac{|\Omega|^2}{N}\text{Var}(f(\mathbf{X})) = \frac{|\Omega|^2 \sigma_f^2}{N} \tag{49}$$
mit $\sigma_f^2 = \text{Var}(f(\mathbf{X}))$. Daher Standardfehler (standard error) (Gleichung (50)):
$$\text{SE}(\hat{I}_N) = \frac{|\Omega|\,\sigma_f}{\sqrt{N}} \tag{50}$$

**Dimensionsunabhängig**: Für großes $N$ konvergiert der Sampling-Fehler mit $O(1/\sqrt{N})$ für Monte Carlo — attraktiv in hohen Dimensionen. Quadraturregeln sind in den Konvergenzraten überlegen, aber der Konvergenzaufwand explodiert mit der Dimension ($N^d$ Punkte für gleiche Genauigkeit).

**Konvergenz in SGD** [S. 65]: Mini-Batch-Gradienten in SGD sind Monte-Carlo-Schätzungen des wahren Gradienten, basierend auf in einen Batch gezogenen Stichproben. Erhöhung der Batch-Größe reduziert die Varianz grob um $1/b$ — direkt analog zur $1/N$-Varianzskalierung oben. Erklärt, warum die Batch-Größe den Rausch-Varianz-Trade-off im Training steuert.

Randnotizen [S. 65]:
- Mittelpunktsregel ist ein Spezialfall von Monte Carlo mit $N = 1$ Stichprobe am Mittelpunkt.
- **i.i.d.** (independent and identically distributed): alle $\mathbf{X}_i$ sind unkorreliert und stammen aus derselben zugrundeliegenden Verteilung.
- Figure 38: Effekt der Batch-Größe auf Gradientenrauschen: kleinere Batches erzeugen größere Varianz (sichtbar in der Breite des Trainings-Loss-Bandes) in der Gradientenschätzung (Quelle: Stanford CS231n Note). Gezeigt: stark verrauschte, abfallende Trainingskurve.
- Vorteilhafter Nebeneffekt: Rechenkosten pro Update-Schritt $n/b$-mal günstiger. Für $n = 10^6$ und $b = 100$: SGD macht 10.000 Iterationen mit dem Compute, das GD für 1 braucht.

**[S. 66]** *Examples & Exercises* — Integral von $\sin(x)$ von $-2$ bis $-1$ mit verschiedenen Methoden; exakter Wert zur Fehlerquantifizierung:
$$\tilde{I} = \int_{-2}^{-1} \sin(x)\,dx = [-\cos(x)]_{-2}^{-1} = -\cos(-1) + \cos(-2) \approx -0.9564491424.$$

**Mittelpunktsregel von Hand** ($n = 1$ Intervall): Mittelpunkt $m = (-2 + (-1))/2 = -1.5$:
$$\hat{I} \approx (b - a) \cdot f(m) = 1 \cdot \sin(-1.5) \approx -0.99749.$$
Fehler: $|\tilde{I} - \hat{I}| \approx 0.04104$ (kleine Differenz zwischen Mittelpunktschätzung und wahrem Wert).

**Mittelpunktsregel mit mehr Intervallen** ($n = 2$, Mittelpunkte bei $-1.75$ und $-1.25$):
$$h = 0.5$$
$$\hat{I} \approx h \cdot [f(-1.75) + f(-1.25)] = 0.5 \cdot [\sin(-1.75) + \sin(-1.25)] \approx -0.927228.$$
Fehler: $|\tilde{I} - \hat{I}| \approx 0.02922$ — kleiner als bei $n = 1$; zeigt, wie zusammengesetzte Regeln bzw. mehr Intervalle die Approximation verbessern.
[UNSICHER: Numerisch wäre $0.5(\sin(-1.75)+\sin(-1.25)) \approx -0.96637$ mit Fehler ≈ 0.0099; im PDF stehen die Werte $-0.927228$ und $0.02922$ — exakt wie abgedruckt übernommen.]

Randnotiz [S. 66]: Weiterführend: Approximation an den Endpunkten des Intervalls berechnen und Fehler vergleichen.

**Trapezregel von Hand** ($n = 2$ Intervalle): Endpunkte $-2$, $-1.5$ und $-1$. (Fortsetzung auf S. 67.)

**[S. 67]** Trapezregel-Rechnung:
$$h = 0.5$$
$$T_2 = \frac{h}{2}\left[f(-2) + 2f(-1.5) + f(-1)\right] = 0.25 \cdot \left[-0.90930 + 2(-0.99749) + (-0.84147)\right] \approx -0.927228.$$

Der Fehler ist derselbe wie bei der Mittelpunktsregel mit $n = 2$ Intervallen — nicht zwingend Zufall, da beide Methoden zweite Ordnung genau sind (second-order accurate) und für bestimmte Funktionen und Intervallwahlen ähnliche Ergebnisse liefern können.

**Simpson-Regel von Hand** [S. 67]: $\int_{-2}^{-1} \sin(x)\,dx$ mit $n = 2$ Intervallen, Endpunkte $-2$, $-1.5$, $-1$:
$$h = 0.5$$
$$S_2 = \frac{h}{3}\left[f(-2) + 4f(-1.5) + f(-1)\right] = \frac{0.5}{3} \cdot \left[-0.90930 + 4(-0.99749) + (-0.84147)\right] \approx -0.9564491424.$$

Fehler: $|\tilde{I} - S_2| \approx 0.0000000000$ — im Wesentlichen null. Illustriert, dass die Simpson-Regel für dieses spezielle Integral exakt ist, da $\sin(x)$ über $[-2, -1]$ gut durch ein quadratisches Polynom approximiert werden kann.

Randnotiz [S. 67]: Mit mehr Intervallen probieren; sehen, wie der Fehler abnimmt; prüfen, ob man Composite-Varianten von Simpson- und Trapezregel beherrscht.

**Monte Carlo von Hand** [S. 67]: $\int_{-2}^{-1} \sin(x)\,dx$ per Monte-Carlo-Schätzung mit $N = 4$ Zufallsstichproben (ähnlicher Rechenaufwand wie Trapezmethode). Angenommene Zufallsstichproben:
$$X_1 = -1.95, \quad f(X_1) = \sin(-1.95) \approx -0.92895,$$
$$X_2 = -1.55, \quad f(X_2) = \sin(-1.55) \approx -0.99978,$$
$$X_3 = -1.15, \quad f(X_3) = \sin(-1.15) \approx -0.91276,$$
$$X_4 = -1.05, \quad f(X_4) = \sin(-1.05) \approx -0.86742.$$
[Anm.: Im PDF steht bei der dritten Zeile "$X_3 = -1.15$, $f(X_3) = \ldots$", in der zweiten Spalte aber Indexfehler nicht vorhanden — Werte exakt übernommen.]

Monte-Carlo-Schätzung:
$$\hat{I} = (b - a) \cdot \frac{1}{N} \sum_{i=1}^{N} f(X_i) = 1 \cdot \frac{1}{4}(-0.92895 - 0.99978 - 0.91276 - 0.86742) \approx -0.927228.$$

**[S. 68]** Fehler: $|\tilde{I} - \hat{I}| \approx 0.02922$ — gleich wie bei der Mittelpunktsmethode.

**Alternative Fehlerschätzung für Monte Carlo** [S. 68]: Für das konkrete Beispiel mit $N = 4$ und Stichprobenmittel $\bar{f} \approx -0.927228$. Erwartungstreuer Stichprobenvarianz-Schätzer (Gleichung (51)):
$$Var(f(\mathbf{X})) = \frac{1}{N - 1} \sum_{i=1}^{N} (f(X_i) - \bar{f})^2 \tag{51}$$

Stichprobenvarianz und Standardfehler des Monte-Carlo-Schätzers:
$$\sigma_f^2 = Var(f(\mathbf{X})) \approx 0.003036,$$
$$\sigma_f \approx 0.05512,$$
$$\text{SE}(\hat{I}_N) \approx \frac{|\Omega|\,\sigma_f}{\sqrt{N}} = \frac{1 \cdot 0.05512}{2} \approx 0.02756.$$

Was passiert bei Erhöhung von $N$ auf 16? Der Fehler sollte um Faktor 2 sinken, da der Standardfehler mit $1/\sqrt{N}$ skaliert. (Übung: kurz erläutern, wie der Fehler des Monte-Carlo-Schätzers dimensionsunabhängig ["dimension independant", sic] ist.)

*Enter higher dimensions on your machine* [S. 68]: Monte-Carlo-Integration für ein $d$-dimensionales Integral implementieren (z. B. multivariate Gaußfunktion über einen Hyperwürfel integrieren). Bei langsam wachsendem $d$ das Fehlerverhalten verschiedener Methoden beobachten; sehen, wie gitterbasierte Quadraturmethoden mit wachsendem $d$ rechnerisch unmöglich werden. Optional: ähnliche Effekte in der Optimierung durch Implementierung von Gradient Descent und Mini-Batch-SGD auf einer hochdimensionalen Funktion — nur Rechenzeiten betrachten.

Randnotiz [S. 68]: Code: `https://github.com/Quillstacks/lecturecode_numericalmethods.git`.

**[S. 69]** *Self-Reflection and Recap* — Fragen:
- Wie vergleichen sich die Fehler von Mittelpunkts-, Trapez-, Simpson-Regel und Monte Carlo?
- Warum hat die Mittelpunktsregel bessere Genauigkeit als Links-/Rechts-Endpunkt-Regeln?
- Wie verbessern Composite-Methoden die Genauigkeit, was ist der Trade-off?
- Warum scheitern deterministische Quadraturmethoden in hohen Dimensionen?
- Inwiefern ist die Mittelpunktsregel ein Spezialfall der Monte-Carlo-Schätzung?
- Intuition, warum Monte Carlo in hohen Dimensionen nicht explodiert?
- Wann Simpson-Regel vs. Monte Carlo verwenden?
- Wie hängt das Mini-Batch-Mittel in SGD mit Monte-Carlo-Schätzung zusammen?
- Wie hilft die Gradientenschätzung in SGD beim Entkommen aus lokalen Minima?

Recap [S. 69]:
- Deterministische Quadraturmethoden (Mittelpunkt, Trapez, Simpson) approximieren Integrale durch gewichtete Summen von Funktionswerten an spezifischen Punkten — genau und schnell konvergent für glatte, niedrigdimensionale Probleme.
- Monte-Carlo-Integration schätzt Integrale durch Mittelung von Funktionswerten an Zufallsstichproben; erwartungstreu, Konvergenzrate $O(1/\sqrt{N})$ — unabhängig von der Dimensionalität des Problems.
- In SGD sind Mini-Batch-Gradienten Monte-Carlo-Schätzungen des wahren Gradienten.

Ausblick [S. 69]: Bisher bezog sich Stabilität auf die Sensitivität der numerischen Lösung gegenüber kleinen Änderungen der Eingabedaten. Man kann auch über Stabilität der numerischen Methode selbst sprechen und ihr Verhalten …

Randnotiz (Teaser): Warum werden Quadraturmethoden hoher Ordnung instabil beim Approximieren von Polynomen niedrigen Grades?

**[S. 70]** … beim Approximieren verschiedener Funktionstypen. Im nächsten Kapitel: weitere Arten von Stabilitätsproblemen in numerischen Methoden und deren Milderung durch ausgefeilte Methodenwahl und -konfiguration. Sonst leer.

---

## Index [S. 71]

**[S. 71]** Vollständiger Index (Begriff, Seitenzahl(en)):
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

## Anhang der Extraktion: Seitenabdeckung (Audit-Hilfe)

| PDF-Seite (aufgedruckt) | Inhalt |
|---|---|
| Titelblatt (o. Nr.) | Titel |
| Impressum (o. Nr.) | Lizenz/Copyright |
| 3 | Zitat |
| 4 | leer |
| 5 | Inhaltsverzeichnis |
| 6 | leer |
| 7 | Introduction |
| 8 | leer |
| 9–16 | Kap. 1 Enter Numerical Methods (Gl. 1–7, Tab. 1, Fig. 1–3) |
| 17–24 | Kap. 2 Floating-Point Arithmetic (Gl. 8–12, Fig. 4–8) |
| 25–34 | Kap. 3 Error Analysis (Gl. 13–19, Fig. 9–13) |
| 35–46 | Kap. 4 Newton Methods (Gl. 20–34, Alg. 1–2, Tab. 2, Fig. 14–23) |
| 47–56 | Kap. 5 Global Optimization (Gl. 35–41, Alg. 3–4, Fig. 24–28) |
| 57–70 | Kap. 6 Numerical Integration (Gl. 42–51, Tab. 3, Fig. 29–38) |
| 71 | Index |

Hinweis zur Seitenzählung: Die aufgedruckte Paginierung beginnt mit "3" auf der dritten physischen Seite; physische und aufgedruckte Seitenzahlen stimmen ab S. 3 überein (71 Seiten gesamt).
