# Pass 4: Abdeckungsaudit (Coverage Audit)

Quelle: `Numerical Methods - notes_numerischemethoden.pdf` (71 Seiten, Prof. Dr.-Ing. Mark Schutera).
Geprüft wurde **jede einzelne Seite** des PDFs (Blöcke S. 1–18, 19–36, 37–54, 55–71) gegen die drei Extraktionspässe:
- `pass_1.md` (Struktur & Konzepte)
- `pass_2.md` (Formeln/Sätze/Algorithmen)
- `pass_3.md` (Beispiele/Randnotizen/Details)

Legende: ✅ = vollständig abgedeckt (Fließtext, Formeln, Algorithmen, Tabellen, Abbildungen, Randnotizen, Fußnoten, Übungen, Selbstreflexionsfragen, Teaser). „P1/P2/P3" = pass_1/pass_2/pass_3.

| Seite | Abgedeckt | Fehlende/unvollständige Inhalte | Gefunden in |
|---|---|---|---|
| 1 | ✅ | — (Titelseite) | P1, P2, P3 |
| 2 | ✅ | — (Impressum, Lizenz CC BY-NC-SA 4.0, Repo-URL, QR-Code, Versionszeile) | P1, P2, P3 |
| 3 | ✅ | — (Motto-Zitat) | P1, P2, P3 |
| 4 | ✅ | — (leer) | P1, P2, P3 |
| 5 | ✅ | — (Inhaltsverzeichnis) | P1, P2, P3 |
| 6 | ✅ | — (leer) | P1, P2, P3 |
| 7 | ✅ | — (Introduction) | P1, P2, P3 |
| 8 | ✅ | — (leer) | P1, P2, P3 |
| 9 | ✅ (1 Mikro-Detail) | Nebensatz „ensuring that models can learn effectively from data while managing computational resources" nur paraphrasiert → Nachextraktion N1 | P1, P2, P3 |
| 10 | ✅ | — (Gl. 1, vollständige Substitution, Verifikation, Randnotizen Analytics/Computational complexity, Gl. 2) | P1, P2, P3 |
| 11 | ✅ | — (Gl. 3, Transzendenz, Randnotiz Sigma, Lernziele) | P1, P2, P3 |
| 12 | ✅ | — (Fig. 1–2, Diskretisierung, Gl. 4, analytische Minimumsuche, Randnotizen) | P1, P2, P3 |
| 13 | ✅ | — (kritische Punkte, Endpunkt-Regel, Grid Search, Fig. 3, Randnotizen inkl. abgebrochenem Satz, Approximationsfehler 0.0907) | P1, P2, P3 |
| 14 | ✅ | — (Gl. 5–6, „100 operations", Enter the machine, Jupyter, Randnotizen) | P1, P2, P3 |
| 15 | ✅ | — (Tabelle 1 vollständig, alle 25 Zeilen; Self-Reflection-Fragen) | P1, P2, P3 |
| 16 | ✅ | — (Recap, Gl. 7, Teaser) | P1, P2, P3 |
| 17 | ✅ | — (The Why, Randnotizen Modeling Error/On the Edge/BNNs, Fußnote 5) | P1, P2, P3 |
| 18 | ✅ (1 Mikro-Detail) | Ziffernzahl der double-precision-Randnotiz war als UNSICHER markiert → bestätigt in Nachextraktion N2 | P1, P2, P3 |
| 19 | ✅ | — (Gl. 10, Fig. 4–6, Bias-Erklärung, Fußnote 6, Randnotiz Bit) | P1, P2, P3 |
| 20 | ✅ | — (Constructing scale, 2-Bit-Mantisse, Gl. 11–12, alle 4 Randnotizen) | P1, P2, P3 |
| 21 | ✅ | — (Fig. 7, Fixed-Point, Skalierungsfaktor-Beispiel, Randnotiz Precision) | P1, P2, P3 |
| 22 | ✅ | — (Auslöschung Beispiel 1+2 vollständig, Randnotizen Pseudo-Accuracy/Infinity) | P1, P2, P3 |
| 23 | ✅ | — (Diskussion 0 vs. 1, Übungen, Fig. 8, Randnotizen Code/Overflow/Underflow/Fußnote 7/a>b) | P1, P2, P3 |
| 24 | ✅ | — (Self-Reflection, Recap, Knowing what can go wrong, Teaser) | P1, P2, P3 |
| 25 | ✅ | — (The Why, 4 Konzepte, ML-Bezug, Randnotizen model error/Goodfellow) | P1, P2, P3 |
| 26 | ✅ | — (Fig. 9–10, Conditioning/Stability intuitiv, Randnotiz floating-point representation) | P1, P2, P3 |
| 27 | ✅ | — (Fig. 11–13, Consistency, Convergence-Beginn, Randnotiz „example wanted") | P1, P2, P3 |
| 28 | ✅ | — (Convergence-Abschluss, Lernziele) | P1, P2, P3 |
| 29 | ✅ | — (Notation, Gl. 13–16, Randnotizen Hat vs. tilde/non-zero convergence) | P1, P2, P3 |
| 30 | ✅ | — (Aufgabe, alle κ-Rechnungen bei x=−1 und x=0) | P1, P2, P3 |
| 31 | ✅ | — (ill-conditioning κ≤0.247, Gl. 17, s-Rechnungen h=1/h=0.2, Randregion-Warnung, Gl. 18, Randnotizen A)/Stability/Remember) | P1, P2, P3 |
| 32 | ✅ | — (c₁=0.15853, c₀.₂=0.05102, Gl. 19, Konvergenz-Rechnungen beide h, Druck-Inkonsistenz 0.1599 dokumentiert) | P1, P2, P3 |
| 33 | ✅ | — (Interpretation, Hands on, 6 Self-Reflection-Fragen, Recap inkl. „Conditiioning"-Tippfehler, Randnotizen Code/Teaser) | P1, P2, P3 |
| 34 | ✅ | — (Überleitungsabsatz) | P1, P2, P3 |
| 35 | ✅ | — (The Why, O(N^d), key insight, ML-Bezug, Randnotiz Backpropagation) | P1, P2, P3 |
| 36 | ✅ | — (Fig. 14–15, Grid-Search-Werte vollständig, Randnotiz sophistication) | P1, P2, P3 |
| 37 | ✅ | — (Newton-Iteration komplett, Lernziele inkl. „understnad"-Tippfehler, Randnotiz Newton-Rhapson) | P1, P2, P3 |
| 38 | ✅ | — (Fig. 16, Gl. 20–21 inkl. Layout-Anomalie, Herleitung, Algorithmus 1 vollständig) | P1, P2, P3 |
| 39 | ✅ | — (Gl. 22–24, Fig. 17, Randnotizen This error/Smooth) | P1, P2, P3 |
| 40 | ✅ | — (Fig. 18–20, Gl. 25–26, Randnotizen Why divide by 2/Around a point) | P1, P2, P3 |
| 41 | ✅ | — (Why linear, Gl. 27–31, vollständige Fehlerherleitung, Randnotiz Fehlerfolge) | P1, P2, P3 |
| 42 | ✅ | — (Gl. 32–33, Tabelle 2 √2 vollständig, Fig. 21, Failure Modes, Randnotiz This can happen) | P1, P2, P3 |
| 43 | ✅ | — (Differenzenquotient, Fig. 22, Gl. 34, Algorithmus 2 vollständig) | P1, P2, P3 |
| 44 | ✅ | — (Fig. 23, Newton by hand x₁–x₃ komplett, Secant-Aufgabe, Randnotiz Code) | P1, P2, P3 |
| 45 | ✅ | — (Sekanten-Rechnung x₂/x₃ inkl. f(1.2)=0.128-Druckfehler dokumentiert, Failure Search, Enter the machine, Self-Reflection) | P1, P2, P3 |
| 46 | ✅ | — (letzte Frage, Recap, Überleitung, Teaser) | P1, P2, P3 |
| 47 | ✅ | — (The Why, Kapitelinhalte, Randnotiz Li et al./Fußnote 8) | P1, P2, P3 |
| 48 | ✅ | — (Gl. 35, konkretes 3-Foxhole-Beispiel, Fig. 24, Sensitivität, Randnotizen derivative/Fußnote 9) | P1, P2, P3 |
| 49 | ✅ | — (Gl. 36, Fig. 25, f′/f″-Formeln, f′(7.2)/f″(7.2), Iterationen, Randnotiz Notation) | P1, P2, P3 |
| 50 | ✅ | — (x°≈7, fundamentales Problem mit x₀-Beispielen, Lernziele) | P1, P2, P3 |
| 51 | ✅ | — (Gl. 37–39, Konvexität, Algorithmus 3 vollständig, Patience, alle 3 Randnotizen) | P1, P2, P3 |
| 52 | ✅ | — (Algorithmus 4 vollständig, Simulated Annealing, Stochastic methods, Randnotizen Noisy Newton/Δf) | P1, P2, P3 |
| 53 | ✅ | — (Fig. 26, Gl. 40–41, Second-Derivative-Test (a)–(c), Randnotizen Deep-Learning-Hoffnungen/Maxima-Frage) | P1, P2, P3 |
| 54 | ✅ | — (Fig. 27–28 inkl. Steigung ±2.66, Rechnung P=0.803, K≈28.3, Randnotizen Code/Hint) | P1, P2, P3 |
| 55 | ✅ | — (K=29, alle Übungen inkl. Basins (a)–(c), „foxhole.2"-Artefakt, alle 3 Randnotizen) | P1, P2, P3 |
| 56 | ✅ | — (6 Self-Reflection-Fragen inkl. Grammatikfehler, Recap, Überleitung, Teaser) | P1, P2, P3 |
| 57 | ✅ | — (Gl. 42, Gründe, SGD/Monte-Carlo, Randnotizen Songzitat/Fußnoten 10–12) | P1, P2, P3 |
| 58 | ✅ | — (Fig. 29–31, Hochfrequenz-Diskussion, Beispielstellen x=0.6/−0.4) | P1, P2, P3 |
| 59 | ✅ | — (Gl. 43, vollständige Glättungsrechnung, Fig. 32, Randnotiz destructive inference) | P1, P2, P3 |
| 60 | ✅ | — (Fig. 33 mit h=0.48-Begründung, 6 Lernziele) | P1, P2, P3 |
| 61 | ✅ | — (Mittelpunkts-/Riemann-Formeln, Fig. 34, Randnotizen interval/Doubling) | P1, P2, P3 |
| 62 | ✅ | — (Gl. 44, Fig. 35, Composite-Trapez-Herleitung komplett, Gewichtungserklärung, Randnotiz Dividing by h) | P1, P2, P3 |
| 63 | ✅ | — (Fig. 36, Gl. 45, quadratisches Lagrange-Polynom, Simpson-Gewichte h/6 u. 2h/3, Simpson-Formel, Randnotiz Try with some points) | P1, P2, P3 |
| 64 | ✅ | — (Composite-Simpson-Herleitung inkl. h/6→h/3, Stop at Simpson, Tabelle 3, Gl. 46, Randnotizen linear/Runge/d=10⁶/Ω) | P1, P2, P3 |
| 65 | ✅ | — (Gl. 47–50, Fig. 37, Bias/Varianz/SE, Dimension independent, SGD, Randnotizen Midpoint-Spezialfall/i.i.d./Fig. 38 inkl. n/b-Beispiel) | P1, P2, P3 |
| 66 | ✅ | — (exakter Wert −0.9564491424, Midpoint n=1 und n=2 inkl. Fehler, Trapez-Beginn, Randnotiz Further things) | P1, P2, P3 |
| 67 | ✅ | — (T₂, S₂ inkl. „essentially zero", Monte Carlo mit 4 Samples vollständig, Randnotiz Try with more intervals) | P1, P2, P3 |
| 68 | ✅ | — (Gl. 51, σ²=0.003036, σ=0.05512, SE≈0.02756, N→16-Frage, Higher-dimensions-Übung, Randnotiz Code) | P1, P2, P3 |
| 69 | ✅ | — (9 Self-Reflection-Fragen, Recap, Stabilitäts-Überleitung, Teaser) | P1, P2, P3 |
| 70 | ✅ | — (Abschlusssatz der Überleitung) | P1, P2, P3 |
| 71 | ✅ | — (Index vollständig, alle Einträge mit Seitenzahlen identisch zum PDF) | P1, P2, P3 |

## LÜCKEN

**Es wurden keine substanziellen Lücken gefunden.** Jeder Inhalt jeder Seite (Fließtext, Formeln, Algorithmen, Tabellen, Abbildungsbeschreibungen, Randnotizen, Fußnoten, Übungsaufgaben, Selbstreflexionsfragen, Teaser, Versionszeilen, Tippfehler-Dokumentation) ist in mindestens einem der drei Pässe erfasst — meist redundant in allen dreien.

Zwei Mikro-Punkte (Detailgrad-/Unsicherheits-Niveau, keine echten Lücken) werden vorsorglich nachextrahiert:
1. **[S. 9]** Ein Nebensatz des ML/AI-Absatzes war in den Pässen nur paraphrasiert, nicht vollständig wiedergegeben.
2. **[S. 18]** Die Randnotiz zur double-precision-Darstellung war in P1/P3 als „UNSICHER: genaue Ziffernzahl" markiert — nun gegen das PDF verifiziert.

Zusätzlich dokumentierte **Auffälligkeiten/Widersprüche** (bereits in den Pässen korrekt als UNSICHER geflaggt, im PDF bestätigt — kein Handlungsbedarf):
- [S. 13] Randnotiz „The minimum": Satz bricht im Original ab („…the interval selection matters, in a sense that it .").
- [S. 31] Indexwechsel in der Stabilitätsrechnung ($s_{h=1,x=-1}$ → $s_{h=1,x=0}$) — Druckfehler im Original, exakt so im PDF.
- [S. 32] Konvergenz-Rechnungen ohne verbindende Gleichheitszeichen gestapelt; Endwert 0.1599 statt arithmetisch 0.15853 — so im PDF gedruckt; in der h=0.2-Rechnung steht $\hat{f}_1(-1.2)$ statt $\hat{f}_{0.2}(-1.2)$ — so im PDF.
- [S. 38] Gl. (20) mit verrutschtem „$+ f(x_n)$" hinter der Bedingung — so im PDF; Algorithmen enden mit „end whilereturn x" (Layout-Artefakt).
- [S. 45] Sekanten-Rechnung nutzt $f(1.2) = 0.128$ (tatsächlich $1.2^3-1.2 = 0.528$) — Druckfehler im Original, von P3 korrekt geflaggt.
- [S. 49] $f'(7.2) \approx 0.005 + 0.100 + 2.27 = 2.38$ (arithmetisch 2.375) — so im PDF.
- [S. 53] „Newton's method finds points where $f''(x) = 0$" — sachlich müsste es $f'(x)=0$ heißen; Druckfehler im Original, von allen Pässen geflaggt.
- [S. 64] Faktorwechsel $h/6 \to h/3$ in der Composite-Simpson-Herleitung — so im PDF.
- [S. 65/66] Fig. 37 trägt eine recycelte Mittelpunktsregel-Bildunterschrift; Midpoint-n=2-Wert $-0.927228$ (arithmetisch wäre ≈ $-0.96637$) — so im PDF gedruckt, von P2 geflaggt.
- Widersprüche **zwischen den Pässen**: keine inhaltlichen Widersprüche gefunden; die drei Pässe sind konsistent und ergänzen sich (P2 am formelgenauesten, P3 am zitatgenauesten, P1 strukturell vollständig).

## NACHEXTRAKTION

### N1 — [S. 9] Vollständiger Wortlaut des ML/AI-Absatzes (fehlender Nebensatz)
Der Absatz „In machine learning and artificial intelligence" enthält den in den Pässen nur paraphrasierten Nebensatz vollständig wie folgt: Numerische Methoden sind entscheidend für das Training von Modellen, die Optimierung von Parametern und die Simulation komplexer Systeme, in denen analytische Lösungen unmöglich (infeasible) sind. „They enable efficient handling of large datasets and complex algorithms, **ensuring that models can learn effectively from data while managing computational resources.**" — d. h.: Sie ermöglichen effizienten Umgang mit großen Datensätzen und komplexen Algorithmen **und stellen dabei sicher, dass Modelle effektiv aus Daten lernen können, während die Rechenressourcen (computational resources) im Rahmen gehalten werden.** Besonders im Deep Learning, wo Modelle Millionen Parameter umfassen und umfangreiche Berechnungen erfordern, erleichtern numerische Methoden die Optimierungsprozesse, die dem Modelltraining zugrunde liegen — „making them indispensable for advancing models." [S. 9]

### N2 — [S. 18] Verifizierte Randnotiz „Types of numerical representations in computers"
Exakter Wortlaut der Randnotiz, gegen das PDF verifiziert (löst die UNSICHER-Markierung in P1/P3 auf):
- **Integer (int):** $3$
- **Floating-point (float):** $3.3333333$ (7 Nachkommastellen)
- **Double precision (double):** $3.3333333333333333$ (16 Nachkommastellen)
- **Fixed-point (e.g. 4-digits):** $3.3333$ (4 Nachkommastellen)
[S. 18]

**Ergebnis: Nach dieser Nachextraktion ist die Abdeckung aller 71 Seiten zu 100 % bestätigt. Es fehlt nichts.**
