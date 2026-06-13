# Review Iteration 1 — Teil D: Übungsblätter 4–6

Unabhängiger Review ausschließlich anhand der Dateien. Referenz: Original-PDF S. 35–70 (vollständig gelesen) und `review/errata_original_pdf.md`. **Alle Musterlösungen wurden vollständig numerisch nachgerechnet** (Python-Skripte unter `/tmp/review_calc/blatt{4,5,6}.py`).

Geprüfte Dateien:
- `output/uebungen/uebung_04_newton_methods.tex` (8 Aufgaben, 50 P)
- `output/uebungen/uebung_05_global_optimization.tex` (8 Aufgaben, 50 P)
- `output/uebungen/uebung_06_numerical_integration.tex` (8 Aufgaben, 54 P)

---

## KRITISCH

### K1 — Blatt 4, Aufgabe 7(b) (Aufgabentext): fachlich falsche Aussage über die Wurzelabstände
**Datei/Stelle:** `uebung_04_newton_methods.tex`, Aufgabe 7(b) (Zeile 174–175).
**Befund:** Der Aufgabentext behauptet, der Startwert $x_0 = 0.5$ sei „von allen drei Wurzeln höchstens $0.5$ entfernt". Nachrechnung: Abstände von $0.5$ zu den Wurzeln $-1, 0, 1$ sind $1.5$, $0.5$, $0.5$ — die Aussage ist für die Wurzel $-1$ falsch (Abstand $1.5$, nicht $\le 0.5$). Sie widerspricht zudem der eigenen Musterlösung, die korrekt formuliert, Newton springe „zur **entferntesten** Wurzel $-1$" und $x_0=0.5$ liege „genau mittig zwischen den Wurzeln $0$ und $1$".
**Hinweis:** Die eigentliche Rechnung in Aufgabe und Lösung ist korrekt ($f(0.5)=-0.375$, $f'(0.5)=-0.25$, $x_1 = 0.5 - (-0.375)/(-0.25) = -1$ exakt, nachgerechnet ✓); nur die Nebenbemerkung im Aufgabentext ist falsch.
**Behebung:** Formulierung ersetzen durch z. B. „… dass der Startwert $x_0 = 0.5$ — der von den beiden Wurzeln $0$ und $1$ jeweils genau $0.5$ entfernt ist — in einem einzigen Newton-Schritt exakt auf der **entfernten** Wurzel $x=-1$ landet …".

*(Keine weiteren KRITISCH-Befunde: Sämtliche Musterlösungen aller drei Blätter wurden Zwischenschritt für Zwischenschritt nachgerechnet und sind numerisch korrekt; alle Aufgaben sind mit den gegebenen Mitteln lösbar — die Wertetabelle in Blatt 6 deckt alle benötigten $e^x$-Werte ab; keine Lösungsleaks im Aufgabenteil; alle Errata-Korrekturen (Newton-Kette 1.4→1.1246→1.0181→1.0005, Sekante f(1.2)=0.528 / x₂≈1.0706, Gl.-(20)-Layout, f″/f′-Druckfehler S. 53, Composite-Simpson h/3, Midpoint n=2 ≈ −0.966485, T₂ ≈ −0.93644, S₂ ≈ −0.956788) sind korrekt übernommen und als „[Korrektur ggü. Original, S. n]" gekennzeichnet.)*

---

## WICHTIG

### W1 — Blatt 5, Aufgabe 8(d): widersprüchliche Annahmen führen zu zwei verschiedenen vertretbaren Ergebnissen
**Datei/Stelle:** `uebung_05_global_optimization.tex`, Aufgabe 8(d) (Zeile 240–246) und zugehörige Lösung (Zeile 591–602).
**Befund:** Der Aufgabentext kombiniert zwei nicht äquivalente Annahmen: (1) „ein lokaler Optimierer konvergiert stets zum **nächstgelegenen** Fuchsloch" und (2) „die lokalen Maxima liegen näherungsweise bei $x \approx 1.7$ und $x \approx 5.7$". Unter Annahme (1) liegen die Basin-Grenzen an den Mittelpunkten $2$ und $5.5$ → Sprung von $7$ mit $\mathrm{Uniform}(-3,3)$ landet in $[4,10]$, Überlapp mit $(2, 5.5)$ ist $1.5$ → $P = 1.5/6 = 0.25$. Die Musterlösung nutzt dagegen die Maxima als Grenzen → Überlapp $[4, 5.7)$, $P = 1.7/6 \approx 0.283$. Ein Studierender, der Annahme (1) wörtlich nimmt, erhält ein abweichendes, aber konsistentes Ergebnis. (Nachrechnung der echten Maxima von $f'$: $x \approx 1.685$ und $x \approx 5.681$ — die Angabe $\approx 1.7 / 5.7$ ist korrekt; die gradientenbasierten Basins haben tatsächlich ihre Grenzen an den Maxima, d. h. die Lösung ist die fachlich „richtigere" Lesart.)
**Behebung:** „nächstgelegenes Fuchsloch" streichen und ersetzen durch: „ein lokaler Optimierer konvergiert stets in das Minimum desjenigen Basins, in dem er startet; die Basin-Grenzen liegen an den lokalen Maxima $x \approx 1.7$ und $x \approx 5.7$". (Damit zugleich konsistent zur Lösungsaussage in Aufgabe 3(a), dass Basin-Grenzen an lokalen Maxima liegen.)

### W2 — Blatt 6: Themenlücke Lagrange-Interpolation (Gl. 45)
**Datei/Stelle:** `uebung_06_numerical_integration.tex`, gesamtes Blatt.
**Befund:** Das Skript führt Lagrange-Interpolation als eigenes Lernziel („Know about Lagrange interpolation and how it relates to quadrature rules", S. 60) mit Gl. (45) und der Herleitung der Simpson-Gewichte $h/6, 2h/3, h/6$ ein (S. 63). Das Blatt deklariert Abdeckung „(42)–(51)", prüft Gl. (45) aber nirgends; nur Lösung 8(b) erwähnt das quadratische Interpolationspolynom beiläufig. Alle übrigen Kerninhalte (Gl. 42–44, 46–51, Tab. 3, Monte Carlo, Curse of Dimensionality, SGD-Bezug) sind abgedeckt.
**Behebung:** Teilaufgabe ergänzen, z. B. in Aufgabe 2 oder 8: Lagrange-Basispolynome $L_j$ für drei äquidistante Knoten $a, m, b$ aufstellen und durch Integration die Simpson-Gewichte $h/6$ (Endpunkte) und $2h/3$ (Mittelpunkt) verifizieren.

### W3 — Blatt 6, Aufgabe 4(d) vs. Aufgabe 6: inkonsistente $h$-Definition bei Simpson
**Datei/Stelle:** `uebung_06_numerical_integration.tex`, Aufgabe 4(d) (Zeile 90) und Aufgabe 6 (Zeile 105).
**Befund:** Aufgabe 4(d) definiert die Einzel-Simpson-Regel mit $h = b - a = 2$ (Formel $\frac{h}{6}[f(a)+4f(m)+f(b)]$ — so korrekt). Aufgabe 6 bezeichnet denselben Fall dann als „Simpson: $h = 1 \to 0.5$" (Composite-Lesart mit Gitterweite $h=(b-a)/2$). Die Quotientenrechnung selbst ist eindeutig und korrekt (nachgerechnet: $0.031672/0.002154 \approx 14.7 \approx 2^4$), aber der stillschweigende Wechsel der $h$-Konvention kann Studierende verwirren — zumal das Skript an genau dieser Stelle selbst inkonsistent ist (Erratum 7).
**Behebung:** In Aufgabe 6 einen Halbsatz ergänzen: „(die Einzel-Simpson-Regel aus Aufgabe 4(d) wird hier als zusammengesetzte Regel mit $n=2$, Gitterweite $h = 1$ gelesen)".

---

## OPTIONAL (Stil/Rundung; Endergebnisse jeweils korrekt)

### O1 — Blatt 6, Lösung 7(b): letzte Nachkommastelle einzelner quadrierter Abweichungen
Mit den Tabellenwerten ergibt sich $(5.754603-3.409329)^2 = 5.500310$ (Blatt: $5.500308$); je nach Rundungsweg ebenso $1.670115$ statt $1.670114$ und $1.149955$ statt $1.149956$. Abweichungen $\le 2\cdot10^{-6}$, Summe ($12.837295$), Varianz ($4.279098$), $\sigma_f$ ($2.068598$) und SE ($2.068598$) sind korrekt. Behebung: Abweichungen aus den 6-stelligen Tabellenwerten neu runden.

### O2 — Blatt 6, Lösungen 4(d)/5(d): Klammersummen um $10^{-6}$ daneben
$1 + 4\cdot2.718282 + 7.389056 = 19.262184$ (Blatt: $19.262183$); $1+6.594884+5.436564+17.926756+7.389056 = 38.347260$ (Blatt: $38.347261$, entspricht dem ungerundeten Wert). Quotienten $6.420728$ bzw. $6.391210$ stimmen. Behebung: konsistent aus Tabellenwerten summieren.

### O3 — Blatt 6, Lösung 1(b): unklare Formulierung „nahe an der halben Periode pro Halbintervall"
$h/2 = 0.24$ ist $\approx T/4$ (Viertelperiode), nicht „halbe Periode pro Halbintervall"; die Klammerangabe „$h \approx T/2$ in der Nachbar-Mittelung" ist korrekt. Behebung: Formulierung straffen („$h = 0.48 \approx T/2$: benachbarte Auswertungspunkte liegen nahezu gegenphasig").

### O4 — Blatt 5, Lösung 7(b): Zwischenwert-Rundung
„$f(-0.0740) \approx 0.00003 - 0.01094$": korrekt wäre $2\cdot0.074^2 = 0.010952$; Endwert $-0.0109$ stimmt ($f(-0.07397) = -0.010914$). Behebung: Zwischenwert auf $0.01095$ korrigieren.

---

## Positivbefunde (Prüfprotokoll, Auswahl der Nachrechnungen)

- **Blatt 4, A3:** Newton an $x^2-5$, $x_0=3$: $2.3333333 \to 2.2380952 \to 2.2360689$; $f$-, $f'$-Spalten, Fehler $7.639\text{e-}1 / 9.727\text{e-}2 / 2.027\text{e-}3 / 9.18\text{e-}7$ und $C_n = 0.167/0.214/0.223 \to C_\text{theor} = 1/(2\sqrt5)=0.2236$ — alles exakt bestätigt.
- **Blatt 4, A4:** $\ln(1.2)=0.1823216$; Fehler $0.1823216 / 0.0176784 / 0.0023216$ ✓.
- **Blatt 4, A5(c):** Sekante: $x_2=2.2$, $x_3=2.2307692$ ($f=-0.0236686$), $x_4=2.2361111$, $|x_4-\sqrt5|=4.31\text{e-}5$ ✓.
- **Blatt 4, A6/A8:** Verhältnistabelle ($0.25/0.33/0.35/0.99$) ✓; Herleitung deckungsgleich mit Gl. (28)–(33) ✓.
- **Blatt 4, A7(c):** $N(x)=2x^3/(3x^2-1)$, Oszillationspunkte $\pm1/\sqrt5 = \pm0.4472136$, $N(1/\sqrt5)=-1/\sqrt5$ ✓.
- **Blatt 5, A2(c):** $f(4)=-8.6769$, $f(7)=-2.9549$, $f(5.5)=-1.1413$, Sehnenmittel $-5.8159$ ✓.
- **Blatt 5, A4:** $x_1=3.0833$, $x_2=3.0032$ bzw. $x_1=0.9167$, $x_2=0.9968$ ✓.
- **Blatt 5, A5:** $P=0.803$; $K=28.34\to29$; $1-0.8^8=0.832$; $K=13.43\to14$ (Probe $0.956/0.945$ ✓); $K=89.8\to90$, $K=458.2\to459$ ✓.
- **Blatt 5, A6:** $e^{-0.25}=0.779$, $e^{-1}=0.368$, $e^{-5}=0.0067$, $e^{-0.1}=0.905$, $e^{-1.2}=0.301$ ✓.
- **Blatt 5, A7(b):** $f'(0.3)=-1.092$, $f''(0.3)=-2.92$; Standard $x_1=-0.0740$ ($f=-0.0109$, bergauf), $|f''|$-Trick $x_1=0.674$ ($f=-0.7021$, bergab) ✓.
- **Blatt 5, A8(b,c):** $f'(7.2)$-Summanden $0.0052/0.0998/2.2727 \to 2.3778$; $f''(7.2)$-Summanden $-0.0021/-0.0912/7.2314 \to 7.1381$; $x_1 = 6.8669 \approx 6.87$ — deckungsgleich mit Skript S. 49 ✓.
- **Blatt 6, A4/A5:** exakt $6.389056$; $M_1=5.436564$ (Fehler $0.952492$), $T_1=8.389056$ ($2.000000$), $S_1=6.420728$ ($0.031672$); $M_2=6.130410$ ($0.258646$), $T_2=6.912810$ ($0.523754$), $S_4=6.391210$ ($0.002154$) — alle ✓.
- **Blatt 6, A6:** Quotienten $3.68 / 3.82 / 14.7$; Prognose $S_8 \approx 1.3\text{e-}4$ (tatsächlich $1.38\text{e-}4$) ✓.
- **Blatt 6, A7:** $\hat I_4 = 6.818659$ (Fehler $0.429602$), $\bar f = 3.409329$, Var $=4.279098$, $\sigma_f = 2.068598$, SE $=2.068598$, Halbierung bei $N=16$ ✓.
- **Blatt 6, A8(a):** Simpson an $\int_0^1 x^3 = 0.25$ exakt ✓; A3: $10^{20}/10^9$ s $\approx 3.2\cdot10^3$ Jahre, $2^{10^6}$ hat $301\,030$ Stellen ✓.
- **Struktur/Format (alle drei Blätter):** je 8 Aufgaben (Vorgabe 5–8 ✓); Punktsummen verifiziert: Teilpunkte je Aufgabe und Blattsummen stimmen (50/50/54 = ausgewiesene Gesamtsummen); ansteigende Schwierigkeit mit ausgewiesener Staffelung; Lösungen strikt nach `\newpage`; `\refstepcounter`/`\label{auf:n}`/`\ref` korrekt verknüpft; keine Lösungsleaks im Aufgabenteil (die in Blatt 5, A8(c) vorgegebenen $x_2 \approx 7.02$, $x_3 \approx 7.00$ sind bewusste Interpretationsvorgabe, $x_1$ wird nicht verraten).
- **Skript-Treue:** Kap. 4 (Gl. 20/21, Taylor 23–26, quadratische Konvergenz 27–33, Sekante 34, Failure Modes, Algorithmen 1/2) und Kap. 5 (Gl. 35–41, Alg. 3/4, Konvexität, Simulated Annealing, Basins, DL-Bezüge) vollständig abgedeckt; Kap. 6 bis auf Gl. 45 (→ W2) vollständig. Transferaufgaben (Konvexitätsbeweis, Oszillations-Fixpunkt, Simpson-Grad-3-Exaktheit) sind als Transfer gekennzeichnet und konsistent mit Skript/Errata; keine ungekennzeichneten Fremdkonzepte.

**Bilanz: 1 × KRITISCH, 3 × WICHTIG, 4 × OPTIONAL.**
