# Review Iteration 2 — Teil D: Übungsblätter 4–6

Unabhängiger Review (Iteration 2) ausschließlich anhand der Dateien. Referenz: Original-PDF S. 35–70 (vollständig gelesen) und `review/errata_original_pdf.md` (korrigierte Werte maßgeblich). **Alle Musterlösungen wurden erneut vollständig numerisch nachgerechnet** (Python: `/tmp/review_calc/iter2_check.py`); zusätzlich Kompiliertest aller drei Blätter mit `pdflatex` (zwei Durchläufe, `/tmp/review_calc/compile_iter2.sh`) — **alle drei kompilieren fehlerfrei, keine unaufgelösten Referenzen**.

Geprüfte Dateien:
- `output/uebungen/uebung_04_newton_methods.tex` (8 Aufgaben, ausgewiesen 50 P — Teilpunkte nachsummiert: 50 ✓)
- `output/uebungen/uebung_05_global_optimization.tex` (8 Aufgaben, ausgewiesen 50 P — nachsummiert: 50 ✓)
- `output/uebungen/uebung_06_numerical_integration.tex` (8 Aufgaben, ausgewiesen 57 P — nachsummiert: 5+6+5+8+8+6+9+10 = 57 ✓)

---

## Behebungsstatus Iteration 1

| Befund Iteration 1 | Status | Verifikation |
|---|---|---|
| **K1** — Blatt 4, A7(b): falsche Distanzaussage („von allen drei Wurzeln höchstens 0.5 entfernt") | **BEHOBEN** | Aufgabentext (Z. 174–177) lautet jetzt „der von den beiden Wurzeln $0$ und $1$ jeweils genau $0.5$ entfernt ist … exakt auf der entferntesten Wurzel $x=-1$ landet" — fachlich korrekt, konsistent zur Lösung; Rechnung ($x_1 = -1$ exakt) erneut bestätigt. |
| **W1** — Blatt 5, A8(d): widersprüchliche Annahmen (nächstgelegenes Foxhole vs. Maxima als Grenzen) | **BEHOBEN** | Aufgabentext (Z. 240–247) jetzt: „konvergiert stets in das Minimum desjenigen Basins, in dem er startet; die Basin-Grenzen liegen an den lokalen Maxima … $x \approx 1.7$ und $x \approx 5.7$". Nachgerechnet: echte Maxima bei 1.6852 / 5.6815 (Angabe ≈1.7/5.7 korrekt); Basins $(-\infty,1.7)/(1.7,5.7)/(5.7,\infty)$; Sprungintervall $[4,10]$, Überlapp $[4,5.7)$, $P = 1.7/6 \approx 0.283$ ✓. Keine ambivalente Lesart mehr. |
| **W2** — Blatt 6: Themenlücke Lagrange-Interpolation (Gl. 45) | **BEHOBEN** | Neue Teilaufgabe 8(a) (3 P): $L_0, L_1, L_2$ für Knoten $0, h/2, h$ korrekt aufgestellt (Probe $L_j(x_k)=\delta_{jk}$ ✓); Integrale exakt nachgerechnet (Bruchrechnung): $w_0 = w_2 = h/6$, $w_1 = 2h/3$, Summe $= h$ ✓; Zwischenschritte $(4-9+6)h^3/12 = h^3/12$ und $-\frac{4}{h^2}(-\frac{h^3}{6}) = \frac{2h}{3}$ ✓. Punktsumme korrekt auf 57 angehoben (Kopf, A8-Summe 3+2+2+3=10, Blattsumme konsistent). |
| **W3** — Blatt 6, A6: inkonsistente $h$-Konvention bei Simpson | **BEHOBEN** | Klarstellung in A6 (Z. 105) eingefügt: Einzel-Simpson aus 4(d) wird als zusammengesetzte Regel mit $n=2$, Gitterweite $h=1$ gelesen. |
| **O1** — Blatt 6, Lösung 7(b): letzte Stelle quadrierter Abweichungen | **BEHOBEN** | Jetzt 4.516917 / 1.670114 / 1.149956 / 5.500310 — alle vier exakt reproduzierbar aus den gedruckten 6-stelligen Abweichungen (−2.125304² = 4.5169171 → 4.516917 usw.); Summe 12.837297, Var 4.279099, $\sigma_f$ = SE = 2.068598 in sich konsistent ✓. |
| **O2** — Blatt 6, Lösungen 4(d)/5(d): Klammersummen | **BEHOBEN** | Jetzt 19.262184 und 38.347260 — beide aus Tabellenwerten exakt bestätigt; Quotienten 6.420728 / 6.391210 ✓. |
| **O3** — Blatt 6, Lösung 1(b): Formulierung „halbe Periode" | **BEHOBEN** | Neue Formulierung „$h = 0.48 \approx T/2$ … Auswertungspunkte … nahezu gegenphasig" — sachlich korrekt. |
| **O4** — Blatt 5, Lösung 7(b): Zwischenwert 0.01094 | **BEHOBEN** | Jetzt $0.00003 - 0.01095 = -0.0109$ ✓ ($2 \cdot 0.074^2 = 0.010952$). |

Alle 8 Befunde aus Iteration 1 sind behoben. Eine Behebung (O-Niveau-Rundungen in Blatt 5, A8(b)) hat eine kleine Regression hinterlassen (→ O1 unten).

---

## KRITISCH

### K1 — Blatt 4, Aufgabe 6(b): Erratum-14-Werte unkorrigiert übernommen; Kernaussage der Musterlösung dadurch fachlich falsch
**Datei/Stelle:** `uebung_04_newton_methods.tex`, Aufgabentext A6(b) (Z. 146–155) und Lösung 6(b) (Z. 387–404).
**Befund:** Der Aufgabentext übernimmt die $\sqrt2$-Fehlerfolge aus Tabelle 2 des Skripts wörtlich, einschließlich $|e_3| = 2.13\times10^{-6}$ und $|e_4| = 4.5\times10^{-12}$. Genau diese beiden Werte sind laut **Erratum 14** (verbindliche Referenz, „korrigierte Werte sind maßgeblich") falsch: korrekt sind $|e_3| = 2.12\times10^{-6}$ und $|e_4| \approx 1.6\times10^{-12}$; das PDF druckt in der $n{=}4$-Zeile das **Residuum** $|x_4^2-2| \approx 4.5\times10^{-12}$ statt des Fehlers $|x_4-\sqrt2|$. Nachgerechnet (echte Newton-Iteration ab $x_0=2$): $|e_4| = 1.595\times10^{-12}$, Residuum $4.511\times10^{-12}$ — Erratum bestätigt. Folge: Die Musterlösung leitet aus den falschen Werten das Verhältnis $|e_4|/|e_3|^2 = 0.99$ ab und folgert „Ab Schritt $3 \to 4$ quadriert der Fehler praktisch exakt" — mit den korrekten Werten ist das Verhältnis $\approx 0.354$, d. h. die Aussage ist **falsch**. Sie widerspricht zudem der blatteigenen Theorie: Nach Gl. (32) (und analog Lösung 3(c) sowie Lösung 8(c)) muss sich das Verhältnis bei $C = \frac{1}{2\sqrt2} \approx 0.3536$ stabilisieren; die korrekte Verhältnisfolge ist $0.250 \to 0.333 \to 0.353 \to 0.354$ — der Sprung auf $0.99$ ist für die echte Iteration unmöglich und ein reines Artefakt der Residuum/Fehler-Verwechslung im PDF. Kein Korrekturvermerk „[Korrektur ggü. Original, S. 42]" vorhanden, obwohl alle übrigen Errata (4, 5, 9) in diesem Blatt vorbildlich gekennzeichnet sind.
**Behebung:** (1) Im Aufgabentext die korrigierte Folge verwenden: $|e_3| = 2.12\times10^{-6}$, $|e_4| \approx 1.6\times10^{-12}$, mit Vermerk „[Korrektur ggü. Original, S. 42: das PDF druckt in der letzten Zeile das Residuum $|x_4^2-2| \approx 4.5\times10^{-12}$ statt des Fehlers]". (2) Die Teilfrage „Ab welchem Schritt quadriert der Fehler praktisch exakt?" umformulieren, z. B.: „Gegen welchen Wert stabilisiert sich das Verhältnis $|e_{n+1}|/|e_n|^2$? Vergleichen Sie mit der theoretischen Konstante $C = \frac{1}{2\sqrt2} \approx 0.354$." (3) Lösungstabelle entsprechend: Verhältnisse $0.25 / 0.33 / 0.35 / 0.35$; das wäre didaktisch sogar stärker (perfekte Bestätigung der Theorie aus A8 statt eines unerklärlichen Ausreißers auf 0.99).

*(Keine weiteren KRITISCH-Befunde.)*

---

## WICHTIG

*(Keine Befunde in dieser Kategorie. Die drei WICHTIG-Befunde aus Iteration 1 sind behoben; bei der vollständigen Neurechnung aller Lösungen sowie dem Abgleich mit Skript-Gl. (20)–(51), Tab. 3, Alg. 1–4 und allen 15 Errata wurden keine neuen Befunde dieser Schwere gefunden — mit Ausnahme von K1, das als kritisch eingestuft ist.)*

---

## OPTIONAL (letzte Nachkommastelle / Mikro-Inkonsistenzen; Endaussagen jeweils unberührt)

### O1 — Blatt 5, Lösung 8(b): Summe der $f''(7.2)$-Summanden um $10^{-4}$ daneben (Regression)
Z. 575: „$-0.0021 - 0.0912 + 7.2314 = 7.1380$" — die angezeigte Summe ergibt $7.1381$; auch volle Präzision liefert $7.138077 \to 7.1381$. Iteration 1 hatte an dieser Stelle noch $7.1381$ protokolliert; die Revision hat hier offenbar eine Stelle verschluckt. Folgewerte ($\approx 7.14$, $x_1 = 7.2 - 0.3331 = 6.8669 \approx 6.87$) sind unberührt. Behebung: $7.1380 \to 7.1381$ (auch in Z. 580 den Nenner $7.1380 \to 7.1381$; Quotient bleibt $0.3331$).

### O2 — Blatt 5, Lösung 7(b): angezeigte Differenz $0.2063 - 0.9085 = -0.7021$
Z. 518: Die angezeigte Subtraktion ergibt $-0.7022$; der korrekte Funktionswert (mit ungerundetem $x_1 = 0.673973$) ist $-0.70214 \to -0.7021$. Die gedruckten Zwischenwerte und das Resultat passen also je für sich, aber nicht als Rechenkette. Behebung: z. B. „$f(0.6740) \approx -0.7021$" ohne die zweigliedrige Zerlegung, oder Zwischenwerte auf 5 Stellen ($0.20633 - 0.90848 = -0.70215$).

### O3 — Blatt 6, Lösung 7(a): Fehlerwert aus voller Präzision statt aus gedruckten Werten
Z. 258–259: $\hat I_4 = 6.818659$ und Fehler $0.429602$ stammen aus voller Präzision ($0.4296025$); aus den gedruckten gerundeten Werten ergäbe sich $6.818659 - 6.389056 = 0.429603$. Abweichung $10^{-6}$, rein kosmetisch. Behebung optional: Fehler als $0.429603$ aus Tabellenwerten oder Fußnote zum Rundungspfad.

---

## Prüfprotokoll (Positivbefunde, Auswahl)

- **Kompiliertest:** alle drei Blätter `pdflatex` exit 0 (2 Durchläufe), keine „undefined reference"-Warnungen; Lösungen strikt nach `\newpage`; `\label{auf:n}`/`\ref` konsistent; keine Lösungsleaks im Aufgabenteil (vorgegebene Werte in B5-A8(c) und B6-A8(a) sind bewusste „Zeigen Sie"-Vorgaben).
- **Blatt 4:** A3 komplett ($2.3333333/2.2380952/2.2360689$; $f$-, $f'$-Spalten; $|e_n| = 7.639\mathrm{e}{-1}/9.727\mathrm{e}{-2}/2.027\mathrm{e}{-3}/9.18\mathrm{e}{-7}$; $C_n = 0.167/0.214/0.223$, $C_\text{theor} = 0.2236$) ✓; A4 (Fehler $0.1823216/0.0176784/0.0023216$, Faktoren 10.3/7.6) ✓; A5(c) ($x_2 = 2.2$, $x_3 = 2.2307692$, $f = -0.0236686$ [= exakt $(29/13)^2-5$], $x_4 = 2.2361111$, Fehler $4.31\mathrm{e}{-5}$) ✓; A7 ($\pm 1/\sqrt3$; $x_1 = -1$ exakt; $N(x) = 2x^3/(3x^2-1)$, Oszillation $\pm 1/\sqrt5$, $N(1/\sqrt5) = -1/\sqrt5$) ✓; A8 deckungsgleich mit Gl. (28)–(33) ✓; Errata 4, 5, 9 korrekt eingearbeitet und gekennzeichnet ✓.
- **Blatt 5:** A2(c) ($f(4) = -8.6769$, $f(7) = -2.9549$, $f(5.5) = -1.1413$, Sehnenmittel $-5.8159$) ✓; Konvexitätsbeweis $\lambda(1-\lambda)(x-y)^2$ ✓; A4 ($x_1 = 3.0833$, $x_2 = 3.0032$; $x_1 = 0.9167$, $x_2 = 0.9968$; $g(1)=5$, $g(3)=1$) ✓; A5 ($0.803$; $K=28.34\to29$; $0.832$; $K=13.43\to14$, Proben $0.956/0.945$; $K=89.8\to90$, $458.2\to459$) ✓; A6 ($0.779/0.368/0.0067/0.905/0.301$) ✓; A7(b) (Standard $x_1=-0.0740$ bergauf, Trick $x_1=0.674$ bergab, $f$-Werte ✓); A8(b) $f'(7.2)$-Summanden $0.0052/0.0998/2.2727 \to 2.3777$ (exakt 2.377766) ✓, $f''$-Summanden $-0.0021/-0.0912/7.2314$ ✓ (nur Summe → O1); A8(c) $x_1 = 6.8669 \approx 6.87$, deckungsgleich Skript S. 49 inkl. Rundungsanmerkung 2.375/2.38 ✓; Erratum 6 als Fußnote korrekt ✓.
- **Blatt 6:** Wertetabelle stimmt mit $e^x$ auf 6 Stellen ✓; A4/A5 (exakt 6.389056; $M_1 = 5.436564/0.952492$; $T_1 = 8.389056/2.000000$; $S_1 = 6.420728/0.031672$; $M_2 = 6.130410/0.258646$; $T_2 = 6.912810/0.523754$; $S_4 = 6.391210/0.002154$) ✓; A6 (Quotienten 3.68/3.82/14.70; $S_8$-Prognose $1.3\mathrm{e}{-4}$, tatsächlich $1.38\mathrm{e}{-4}$) ✓; A7 ($\hat I_4 = 6.818659$, $\bar f = 3.409329$, Var $= 4.279099$, $\sigma_f = \text{SE} = 2.068598$, $\text{SE}_{16} = 1.034299$) ✓; A8(a) Lagrange-Gewichte exakt $h/6, 2h/3, h/6$ ✓; A8(b) Simpson an $x^3$ exakt 0.25 ✓; A8(c) Symmetrieargument korrekt ✓; A8(d) $n/b = 10^4$ ✓; A3 ($10^{20}$ Punkte, $\approx 3.2\cdot10^3$ Jahre; $301\,030$ Stellen) ✓; Tabelle-3-Zuordnung ✓; Errata 7, 8, 10, 11 korrekt im Schlusshinweis bzw. in A5(a)/A8(c) gekennzeichnet ✓.
- **Skript-Treue:** Kap. 4 (Gl. 20–34, drei Failure Modes, Alg. 1/2, Sekanten-Gründe, Konvergenztabelle), Kap. 5 (Gl. 35–41, Alg. 3/4, Patience, DL-Bezüge S. 51/53, Basin-Aufgabe S. 55) und Kap. 6 (Gl. 42–51 inkl. — neu — Gl. 45, Tab. 3, „Stop at Simpson", Runge, Curse of Dimensionality, MC, SGD) vollständig abgedeckt. Mit Behebung von W2 ist die einzige Abdeckungslücke aus Iteration 1 geschlossen.
- **Regressionscheck:** Außer O1 (7.1380) keine durch die Überarbeitung neu eingeführten Fehler gefunden; alle in Iteration 1 als korrekt protokollierten Werte wurden stichprobenfrei (vollständig) neu gerechnet und bestätigt.

**Bilanz Iteration 2: 1 × KRITISCH, 0 × WICHTIG, 3 × OPTIONAL. Behebungsstatus Iteration 1: 8/8 behoben.**
