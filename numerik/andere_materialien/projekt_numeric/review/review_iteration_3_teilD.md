# Review Iteration 3 (finale Prüfrunde) — Teil D: Übungsblätter 4–6

Unabhängiger Review (Iteration 3) ausschließlich anhand der Dateien. Referenz: Original-PDF S. 35–70 (vollständig gelesen) und `review/errata_original_pdf.md` (korrigierte Werte maßgeblich); Vorrunde `review/review_iteration_2_teilD.md`. **Alle Musterlösungen wurden erneut vollständig numerisch nachgerechnet** (Python: `/tmp/review_calc/iter3_teilD_check.py`, 177 Einzelchecks; Lagrange-Gewichte und Simpson-Kubik-Restterm zusätzlich exakt mit Bruchrechnung verifiziert). Kompiliertest aller drei Blätter mit `pdflatex` (zwei Durchläufe, `/tmp/review_calc/build_iter3/`): **alle drei exit 0, keine Fehler, keine unaufgelösten Referenzen** (Blatt 5: 10 Seiten).

Geprüfte Dateien:
- `output/uebungen/uebung_04_newton_methods.tex` — ausgewiesen 50 P; nachsummiert 4+5+7+6+7+5+9+7 = 50 ✓ (Teilpunkte je Aufgabe stimmen mit Aufgabensumme überein)
- `output/uebungen/uebung_05_global_optimization.tex` — ausgewiesen 50 P; nachsummiert 4+6+5+7+7+5+6+10 = 50 ✓
- `output/uebungen/uebung_06_numerical_integration.tex` — ausgewiesen 57 P; nachsummiert 5+6+5+8+8+6+9+10 = 57 ✓

---

## Behebungsstatus Iteration 2

| Befund Iteration 2 | Status | Verifikation |
|---|---|---|
| **K1** — Blatt 4, A6(b): Erratum-14-Werte unkorrigiert; Folgerung „Verhältnis 0.99 / quadriert praktisch exakt" falsch | **BEHOBEN** | Aufgabentext (Z. 146–156) verwendet jetzt die korrigierte Folge $|e_3| = 2.12\times10^{-6}$, $|e_4| \approx 1.6\times10^{-12}$ **mit** Korrekturvermerk „[Korrektur ggü. Original, S. 42: Residuum $|x_4^2-2| \approx 4.5\times10^{-12}$ statt Fehler; außerdem $2.13$ statt $2.12\times10^{-6}$]" — beide Angaben gegen die echte Newton-Iteration bestätigt ($|e_4| = 1.595\times10^{-12}$, Residuum $4.511\times10^{-12}$, $|e_3| = 2.124\times10^{-6}$). Die Teilfrage ist wie empfohlen auf die Stabilisierung des Verhältnisses umformuliert. **Neue Verhältnistabelle vollständig nachgerechnet:** aus den gedruckten Werten $8.58\mathrm{e}{-2}/3.43\mathrm{e}{-1} = 0.250$ ✓, $2.45\mathrm{e}{-3}/7.36\mathrm{e}{-3} = 0.333$ ✓, $2.12\mathrm{e}{-6}/6.00\mathrm{e}{-6} = 0.353$ ✓, $1.6\mathrm{e}{-12}/4.49\mathrm{e}{-12} = 0.356 \to$ gedruckt „$\approx 0.35$" ✓; die $|e_n|^2$-Spalte ($3.43\mathrm{e}{-1}$, $7.36\mathrm{e}{-3}$, $6.00\mathrm{e}{-6}$, $4.49\mathrm{e}{-12}$) reproduziert sich exakt aus den Aufgabenwerten. Volle Präzision: $0.250009 \to 0.333328 \to 0.352940 \to 0.353525$, gedruckt „$0.250 \to 0.333 \to 0.353 \to 0.354$" ✓. Theoretische Konstante $C = \frac{2}{2\cdot 2\sqrt2} = \frac{1}{2\sqrt2} = 0.353553 \to$ „$\approx 0.3536$" ✓, konsistent mit Gl. (32) sowie den Querverweisen auf A3 ($1/(2\sqrt5) \approx 0.2236$ ✓) und A8. Didaktisch nun widerspruchsfrei zur Theorie. |
| **O1** — Blatt 5, L8(b): Summe $7.1380$ statt $7.1381$ (Regression) | **BEHOBEN** | Z. 575: „$-0.0021 - 0.0912 + 7.2314 = 7.1381$" ✓ (exakt; voller Wert $f''(7.2) = 7.138077$); Nenner in Z. 580 ebenfalls $7.1381$ ✓; Quotient $0.3331$, $x_1 = 6.8669 \approx 6.87$ ✓ (deckungsgleich Skript S. 49). |
| **O2** — Blatt 5, L7(b): angezeigte Differenz $\ne$ Resultat | **BEHOBEN** | Z. 518 jetzt „$f(0.6740) \approx 0.2063 - 0.9085 = -0.7022$": die angezeigte Subtraktion stimmt, und $-0.7022$ ist der korrekt gerundete Wert von $f$ am gedruckten Argument $0.6740$ ($f(0.6740) = -0.702185$). Endaussage ($< -0.1719$, bergab Richtung $x = 1$) unberührt. (Kleine Rest-Mikroinkonsistenz der beiden Summanden → neues O2 unten.) |
| **O3** — Blatt 6, L7(a): Fehler $0.429602$ aus voller Präzision | **BEHOBEN** | Z. 259: Fehler jetzt $0.429603 = 6.818659 - 6.389056$ aus den gedruckten 6-stelligen Werten ✓; konsistent weiterverwendet in L7(c) („tatsächlicher Fehler $0.429603$") ✓. |

Alle 4 Befunde aus Iteration 2 sind behoben; die K1-Behebung folgt exakt dem Behebungsvorschlag und ist numerisch einwandfrei.

---

## KRITISCH

*(Keine Befunde in dieser Kategorie.)*

---

## WICHTIG

### W1 — Blatt 6, Lösung 8(c): Restterm-Behauptung „proportional zu $(x-m)^3$" ist mathematisch falsch (Endaussage bleibt richtig)
**Datei/Stelle:** `uebung_06_numerical_integration.tex`, Z. 304.
**Befund:** Die Musterlösung schreibt: „Für ein kubisches Polynom betrachte man die Abweichung vom quadratischen Interpolanten: Sie ist **proportional zu $(x-m)^3$**, also eine ungerade Funktion bezüglich des Intervallmittelpunkts $m$." Die Abweichung eines kubischen Polynoms von seinem quadratischen Lagrange-Interpolanten durch die drei Knoten $a$, $m$, $b$ ist jedoch $c\,(x-a)(x-m)(x-b) = c\,\big[(x-m)^3 - (\tfrac{h}{2})^2 (x-m)\big]$ — **nicht** proportional zu $(x-m)^3$. Exakt nachgerechnet an $f(x) = x^3$ auf $[0,1]$: Abweichung $x(x-\tfrac12)(x-1)$, am Punkt $x = \tfrac14$ beträgt sie $+\tfrac{3}{64}$, während $(x-m)^3 = -\tfrac{1}{64}$ wäre (sogar entgegengesetztes Vorzeichen). Richtig — und für die Schlussfolgerung allein tragend — ist die zweite Hälfte des Satzes: Die Abweichung **ist** ungerade um $m$ (verifiziert), ihr Integral über das symmetrische Intervall verschwindet, und da sie an allen drei Knoten null ist, liefert die Simpson-Regel automatisch $\int p_2$; daher ist Simpson exakt bis Grad 3. Fazit und Punktevergabe-Logik der Teilaufgabe sind also korrekt, aber die Musterlösung enthält eine falsifizierbare Fehlaussage, die Studierende übernehmen würden.
**Behebung (Halbsatz):** „… die Abweichung vom quadratischen Interpolanten: Sie ist proportional zu $(x-a)(x-m)(x-b) = (x-m)^3 - \frac{h^2}{4}(x-m)$, also eine ungerade Funktion bezüglich des Intervallmittelpunkts $m$." (Alternativ: Zerlegung $p_3(x) = q(x) + \gamma\,(x-m)^3$ mit quadratischem $q$ verwenden — dann ist „proportional zu $(x-m)^3$" korrekt, aber es muss „Abweichung vom quadratischen *Anteil*" heißen und zusätzlich erwähnt werden, dass auch die Quadratur von $(x-m)^3$ wegen $(a-m)^3 = -(b-m)^3$ null ergibt.)

*(Keine weiteren WICHTIG-Befunde.)*

---

## OPTIONAL (letzte Nachkommastelle / Mikro-Inkonsistenzen; Endaussagen jeweils unberührt)

### O1 — Blatt 5, Lösung 4(b): angezeigtes Produkt $3(2.0833)(0.0833)$ ergibt $0.5206$, gedruckt $0.5208$
Z. 396: $3 \cdot 2.0833 \cdot 0.0833 = 0.520617 \to 0.5206$; der gedruckte Wert $0.5208$ stammt aus dem ungerundeten $x_1 = 37/12 = 3.08\overline{3}$ ($3 \cdot 2.08\overline{3} \cdot 0.08\overline{3} = 0.520833$). Folgewerte unberührt: $x_2 = 3.0833 - 0.5206/6.5 = 3.0032$ ebenso wie mit $0.5208$. Behebung optional: Faktoren fünfstellig ($3(2.08333)(0.08333) = 0.5208$) oder $0.5206$ drucken.

### O2 — Blatt 5, Lösung 7(b): Summanden $0.2063/0.9085$ passen zum ungerundeten $x_1$, nicht zum gedruckten Argument $0.6740$
Z. 518: Mit dem Argument $0.6740$ wären die Summanden $0.6740^4 = 0.206367 \to 0.2064$ und $2 \cdot 0.6740^2 = 0.908552 \to 0.9086$; die gedruckten $0.2063/0.9085$ entsprechen dem ungerundeten $x_1 = 0.673973$ ($0.206333/0.908478$). Resultat $-0.7022$ und angezeigte Subtraktion sind in sich stimmig (Behebung von Iteration-2-O2 erfolgreich); nur der Rundungspfad der Summanden ist gemischt. Rein kosmetisch.

*(Keine weiteren OPTIONAL-Befunde.)*

---

## Prüfprotokoll (Positivbefunde, Auswahl)

- **Kompiliertest:** alle drei Blätter `pdflatex` exit 0 (2 Durchläufe), keine „undefined reference"-Warnungen, keine `!`-Fehler; Lösungen strikt nach `\newpage` (B4 Z. 212, B5 Z. 255, B6 Z. 143); `\label{auf:n}`/`\ref` konsistent (auch Vorwärtsreferenzen A6(b)→A8 aufgelöst); keine Lösungsleaks im Aufgabenteil (Vorgaben in B4-A6(b) [Fehlerfolge als Datenbasis], B5-A8(c) [$x_2, x_3$] und B6-A8(a) [Zielgewichte, „Zeigen Sie"] sind bewusste Aufgabendaten).
- **Blatt 4 (alle Lösungen neu gerechnet):** A3 vollständig ✓ ($x_1 = 2.3333333$, $x_2 = 2.2380952$, $x_3 = 2.2360689$; $f$/$f'$-Spalten inkl. $0.0090703/4.4761905/0.0000041/4.4721378$; Fehler $7.639\mathrm{e}{-1}/9.727\mathrm{e}{-2}/2.027\mathrm{e}{-3}/9.18\mathrm{e}{-7}$ [letzter aus ungerundetem $x_3$, korrekt]; $C_n = 0.167/0.214/0.223$, $C_\text{theor} = 0.2236$). A4 ✓ ($0.1823216/0.0176784/0.0023216$; Faktoren 10.3/7.6). A5(c) ✓ ($x_2 = 2.2$, $f = -0.16$; $x_3 = 2.2307692$, $f = -4/169 = -0.0236686$; Schrittweite $0.0307692$, $\Delta f = 0.1363314$ [aus ungerundetem $x_3 = 29/13$, konsistent]; $x_4 = 2.2361111$, Fehler $4.3\mathrm{e}{-5}$); Querbezug Erratum 5 ($0.528/1.344/1.0706$) ✓. A6(a) $10^{-1}\to10^{-2}\to10^{-4}\to10^{-8}\to10^{-16}$, 4 Iterationen ✓; A6(b) siehe Behebungsstatus K1 ✓; A6(c) konsistent mit Randnotiz S. 41 ✓. A7 ✓ ($\pm1/\sqrt3 \approx 0.5774$; $f(0.5) = -0.375$, $f'(0.5) = -0.25$, $x_1 = -1$ exakt; $N(x) = 2x^3/(3x^2-1)$, Oszillation $x_0^2 = 1/5$, $N(1/\sqrt5) = -1/\sqrt5$ exakt; Vergleichskette $1.4 \to 1.1246 \to 1.0181 \to 1.0005$ = Erratum 9 ✓). A8 deckungsgleich mit Gl. (28)–(33) ✓. Errata 4, 5, 9, 14 alle korrekt eingearbeitet und gekennzeichnet ✓.
- **Blatt 5:** A2(c) ✓ ($f(4) = -8.6769$ [$-0.0599-8.5-0.1170$], $f(7) = -2.9549$, $f(5.5) = -1.1413$, Sehnenmittel $-5.8159$); Konvexitätsbeweis $\lambda(1-\lambda)(x-y)^2 \ge 0$ ✓; allgemeines Zwei-Minima-Argument korrekt ✓. A4 ✓ ($x_1 = 3.0833$, $x_2 = 3.0032$; $x_1 = 0.9167$, $x_2 = 0.9968$; $g(1) = 5$, $g(3) = 1$; nur O1). A5 ✓ ($0.85^{10} = 0.1969 \to 0.803$; $K = -4.6052/-0.1625 = 28.3 \to 29$; $0.8^8 = 0.1678 \to 0.832$; $K = 13.43 \to 14$, Proben $0.956/0.945$; $89.8 \to 90$; $458.2 \to 459$; $1/p$-Skalierung). A6 ✓ ($e^{-0.25} = 0.779$, $e^{-1} = 0.368$, $e^{-5} = 0.0067$, $e^{-0.1} = 0.905$, $e^{-1.2} = 0.301$). A7(b) ✓ ($f'(0.3) = -1.092$, $f''(0.3) = -2.92$; Standard $x_1 = -0.0740$, $f = 0.00003 - 0.01095 = -0.0109$ bergauf; Trick $x_1 = 0.6740$, $f = -0.7022$ bergab; nur O2). A8(b) ✓ (alle sechs Summanden inkl. Potenzen $2760.45/108.99/0.1936/145034/1137.89/0.08518$ und Zähler $-309.64/-103.768/0.616$ einzeln bestätigt; $f'(7.2) = 2.3777$, $f''(7.2) = 7.1381$, exakte Werte $2.377766/7.138077$). A8(c) ✓ ($x_1 = 6.8669 \approx 6.87$, deckungsgleich Skript S. 49 inkl. Rundungsanmerkung $2.375/2.38$ und Erratum-32-konformem „$x^\circ \approx 7$"). A8(d) ✓ (echte lokale Maxima numerisch bei $1.6852/5.6815 \to$ Angabe $\approx 1.7/5.7$ korrekt; Basins, Überlapp $[4, 5.7)$, $P = 1.7/6 = 0.2833 \approx 28\,\%$). Erratum 6 als Fußnote korrekt ✓; Patience/DL-Bezüge skripttreu (S. 51–53) ✓.
- **Blatt 6:** Wertetabelle = $e^x$ auf 6 Stellen ✓. A4/A5 ✓ (exakt $e^2 - 1 = 6.389056$; $M_1 = 5.436564/0.952492$; $T_1 = 8.389056/2.000000$; $S_1 = 19.262184/3 = 6.420728/0.031672$; $M_2 = 6.130410/0.258646$; $T_2 = 13.825620/2 = 6.912810/0.523754$; $S_4 = 38.347260/6 = 6.391210/0.002154$; Konvexitäts-/Vorzeichenargument korrekt). A6 ✓ (Quotienten $3.68/3.82/14.7$; $S_8$-Prognose $1.3\mathrm{e}{-4}$, tatsächlicher $S_8$-Fehler $1.38\mathrm{e}{-4}$). A7 ✓ (Summe $13.637317$, $\hat I_4 = 6.818659$, Fehler $0.429603$; $\bar f = 3.409329$; alle vier quadrierten Abweichungen $4.516917/1.670114/1.149956/5.500310$ exakt aus den gedruckten Abweichungen; Summe $12.837297$, Var $4.279099$, $\sigma_f = \mathrm{SE} = 2.068598$, $\mathrm{SE}_{16} = 1.034299$; Erratum-15-konform). A8(a) ✓ (Lagrange-Basispolynome inkl. vereinfachter Formen und $\delta_{jk}$-Probe; Gewichte exakt $h/6, 2h/3, h/6$ per Bruchrechnung; Zwischenschritte $(4-9+6)h^3/12$ und $-\frac{4}{h^2}(-\frac{h^3}{6}) = \frac{2h}{3}$ ✓; Summe $= h$). A8(b) ✓ (Simpson an $x^3$: $1.5/6 = 0.25$ exakt). A8(c): Fazit korrekt, aber Restterm-Formulierung → W1. A8(d) ✓ ($1/b$-Varianz, $n/b = 10^4$). A3 ✓ ($10^{20}$ Punkte, $10^{11}$ s $= 3.17\cdot10^3 \approx 3.2\cdot10^3$ Jahre; $10^6 \log_{10}2 = 301\,030$ Stellen). A2(b)-Zuordnung = Tabelle 3 ✓ (die 8 gemischten Ordnungen sind genau die 8 Tabellenwerte). Schlusshinweis: Errata 7, 8, 10, 11 korrekt ($M_2 = -0.966485/0.010036$; $T_2 = -0.93644/0.02001$; $S_2 = -0.956788$ [erratumkonform aus den 5-stelligen Skript-Sinuswerten; volle Präzision $-0.956791$, Fehler in beiden Lesarten $3.4\cdot10^{-4}$] ✓).
- **Skript-Treue:** Alle zitierten Gleichungsnummern (20)–(51), Tabellen 2/3, Algorithmen 1–4, Seitenangaben und wörtliche Zitate gegen S. 35–70 geprüft — stimmig; sämtliche einschlägigen Errata (4, 5, 6, 7, 8, 9, 10, 11, 14, 15 sowie Geringfügiges S. 36/49) sind eingearbeitet bzw. gekennzeichnet.
- **Regressionscheck Iteration 2:** Alle dort als korrekt protokollierten Werte vollständig neu gerechnet und bestätigt; die drei Fixes (B4-A6(b), B5-L8(b)/L7(b), B6-L7(a)) haben **keine neuen Fehler** eingeführt (O2 ist eine Restspur des alten Befunds, keine Regression). W1 und O1 sind Altbestand, der in den Vorrunden unentdeckt blieb.

---

## Freigabe-Urteil

**Ja — Freigabe erteilt, mit einer Auflage:** der Halbsatz-Korrektur W1 in Blatt 6, Lösung 8(c) („proportional zu $(x-a)(x-m)(x-b)$" statt „proportional zu $(x-m)^3$"). Es verbleiben **0 × KRITISCH, 1 × WICHTIG (W1), 2 × OPTIONAL**; sämtliche Zahlenwerte, Punktsummen (50/50/57), Struktur und Skript-/Errata-Treue sind freigabefähig. Alle Befunde der Iterationen 1 (8/8) und 2 (4/4) sind behoben.

**Bilanz Iteration 3: 0 × KRITISCH, 1 × WICHTIG, 2 × OPTIONAL. Behebungsstatus Iteration 2: 4/4 behoben.**
