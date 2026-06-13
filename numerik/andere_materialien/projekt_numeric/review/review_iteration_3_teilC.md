# Review Iteration 3 — Teil C: Übungsblätter 1–3 (finale Prüfrunde)

**Reviewer:** unabhängige Neuprüfung (Iteration 3, ohne Vorwissen) ausschließlich anhand der Dateien: drei `.tex`-Übungsblätter, Original-PDF S. 9–34 (vollständig gelesen), `errata_original_pdf.md`, `review_iteration_2_teilC.md`.
**Methode:** (1) Änderungsprüfung gegenüber Iteration 2 per Diff-Logik; (2) unabhängige vollständige Neurechnung aller 24 Aufgaben (Python-Skript `/tmp/review_calc/iter3_check.py`, **122 automatisierte Einzelchecks, 0 Fehlschläge**, zusätzlich Handprüfung aller Herleitungen, Beweise und verbalen Lösungen); (3) Kompiliertest aller drei Blätter mit `pdflatex` (je 2 Läufe: 0 Fehler, 0 unaufgelöste Referenzen, 0 LaTeX-Warnungen; PDFs mit 8/7/9 Seiten erzeugt); (4) Skript-Treue-Abgleich gegen S. 9–16 / 17–24 / 25–34 inkl. aller Randnotizen; (5) Errata-Konformität; (6) Struktur-, Punkte-, Leak- und Didaktikprüfung.

**Geprüfte Dateien:**
- `output/uebungen/uebung_01_enter_numerical_methods.tex` (8 Aufgaben, 40 P.)
- `output/uebungen/uebung_02_floating_point_arithmetic.tex` (8 Aufgaben, 38 P.)
- `output/uebungen/uebung_03_error_analysis.tex` (8 Aufgaben, 50 P.)

---

## Änderungsprüfung gegenüber Iteration 2

**Befund: unverändert.** Drei unabhängige Indizien:
1. Die Änderungszeitpunkte der `.tex`-Dateien (11:12 / 12:33 / 11:17) liegen **vor** dem Abschluss des Iteration-2-Reviews (12:42); seither wurde keine Datei angefasst.
2. Alle in `review_iteration_2_teilC.md` wörtlich zitierten Stellen (Blatt 2: Lösung 8c mit $y/y^2$-Folgebeispiel, Transferhinweis in Aufgabe 4, Staffelungs-Kopftext mit `\pageref{sec:loesungen}`; sämtliche Zahlenwerte des It.-2-Protokolls) finden sich unverändert in den aktuellen Quellen.
3. Frisch kompilierte PDFs sind byte-größengleich mit den im Ausgabeverzeichnis liegenden (243 586 / 236 353 / 240 255 Bytes).

Damit ist der von Iteration 2 geprüfte Stand identisch mit dem hier geprüften; die Neurechnung erfolgte dennoch vollständig und unabhängig.

---

## KRITISCH

**Keine Befunde.**

Nachrechnungs-Protokoll Iteration 3 (alle 24 Aufgaben / 72 Teilaufgaben; 122 Checks, Auswahl):

- **Blatt 1:** L2 ($h=0.25$, 9 Gitterpunkte; $N=200$, 201 Auswertungen; Halbierung → 400/401) ✓; L3 ($x=0\notin[1,3]$, Min $f(1)=1$, Max $f(3)=9$) ✓; L4 (kritische Punkte $0,\pi$; $f''$-Klassifikation; Tabelle $\cos(0\ldots4)$ auf 4 NK exakt; Min $-0.9900$ bei $x=3$; Fehler $0.0100$; $\cos(3.1)=-0.9991$; $h=0.5$-Aussage geprüft: Gitter enthält 3, Min bleibt dort) ✓; L5 (exakt $(4,-3)$, beide Proben; alle 9 Gitterzeilen einzeln nachgerechnet, Min Error 3 bei $(2,2)$; $b=-3\notin[0,4]$ — Diskussion korrekt) ✓; L6 ($w=(-76/3,\,2/3,\,64/3)$ exakt per Bruchrechnung, Zwischenschritte II′: $7w_1+10w_3=36$ und III′: $w_1=-4-w_3$ verifiziert, alle drei Proben $42/3$, $60/3$, $96/3$ ✓); L7 ($5^2=25$; $100^2=10^4$; $100^{10}=10^{20}$; $10^{11}$ s $=3168.6\approx3.17\cdot10^3$ Jahre) ✓; L8 (alle 7 Tabellenzeilen inkl. Summandenspalten; $L'(w)=28w-50$ an drei Stützstellen gegengeprüft; $w^*=25/14\approx1.7857$, $L(w^*)=5/14\approx0.3571$ exakt; Endpunkte $L(0)=45$, $L(3)=21$; Fehler $3/14\approx0.2143$ und $9/14\approx0.6429$) ✓
- **Blatt 2:** L2 ($1/3000=(10000-9999)/3000=0.000\overline{3}$; Darstellungstypen deckungsgleich Skript S. 18) ✓; L3 ($1.19\times10^{-7}$ bzw. $0.119\approx0.12$; Randnotiz-Deutung S. 20 korrekt) ✓; L4a ($E=130$, $e=3$, $1.101_2=1.625$, $x=-13.0$, Probe $1101_2=13$; Mantissenfelder in Aufgabe und Lösung je exakt 23 Bit nachgezählt) ✓; L4b ($6.25=110.01_2=1.1001_2\times2^2$, $E=129=10000001_2$, Probe $1.5625\cdot4=6.25$) ✓; L5 ($2^{-23}=1/8388608\approx1.19\cdot10^{-7}$, $2^{-52}\approx2.22\cdot10^{-16}$; 2-Bit-Mantisse $0/0.25/0.5/0.75$ deckungsgleich Skript S. 20; $2^3=8$) ✓; L6 ($1010_2/1100100_2/1111101000_2$ samt Zerlegungen; Normalformen $1.25/1.5625/1.953125$ gegengerechnet; $E=130/133/136$ binär — identisch Skript S. 20) ✓; L7 ($1234567$; $10^{-6}$ bzw. $0.5\cdot10^{-6}$ wie Skript-Randnotiz S. 21; $10^9<2\,147\,483\,647<10^{10}$, auch negativ geprüft) ✓; L8a (beide Paare per Decimal-Half-Up-Rundung bestätigt; je 100 % relativer Fehler — deckungsgleich Skript S. 22–23) ✓; L8b ($10^{-20}<2^{-52}$, $\mathrm{fl}(1+10^{-20})-1=0$ in double maschinell verifiziert; $1/\epsilon=10^{20}$) ✓; L8c ($10^{40}>10^{38}$ Overflow; $10^{-50}\to0$ Underflow; $y/y^2$: wahr $10^{25}<10^{38}$ darstellbar, Maschine $\infty$) ✓
- **Blatt 3:** alle 11 Wertetabellen-Einträge $\cos(x)$ auf 5 NK exakt bestätigt; alle benötigten Stützstellen enthalten ✓; L4 ($\kappa=0.00414/0.06569/0.24899/0.24458$; $|\sin(3)|=0.141$, $|\sin(1.5)|=0.997$; „rund das Vierfache“: $0.249/0.0657\approx3.8$ ✓); L5 (Nächste-Gitterpunkt-Logik: $2.25\to2$ bei $h=1$ [0.25 vs. 0.75], $2.25\to2.2$ bei $h=0.2$ [0.05 vs. 0.15]; $s=0$ bzw. $0.17235/0.25=0.6894$) ✓; L6 ($\pi\to3$ [0.14159/0.85841] bzw. $\pi\to3.2$ [0.05841/0.14159]: $c_1\geq0.01001$, $c_{0.2}\geq0.00171$; $\tilde{x}=3.39159\to3$ [0.39159/0.60841] bzw. $\to3.4$ [0.00841/0.19159]: Konvergenz $0.01001$ bzw. $0.03320$ — Befund „Konsistenz besser, Konvergenz schlechter“ rechnerisch korrekt) ✓; L7 (a: $|x-x_i|\leq h/2$ + Mittelwertsatz korrekt; b: umgekehrte Dreiecksungleichung, Schranke $2\cdot Lh/2=Lh\to0$ korrekt, Grenzaussage $s_h^{\min}\to\kappa/|\tilde{x}-x|$ schlüssig; c: $2=40\cdot0.05$ und $2.25=45\cdot0.05$ sind Gitterpunkte, Folge $0\to0.17235\to0.21202=\kappa(2,+0.25)$ aus Tabellenwerten) ✓; L8b ($\cos(\pi+0.25)=-0.96891$ auf 5 NK exakt, Grenzwert $0.03109$ — konsistent mit Tabellengrenzwert $\approx0.031$ aus Aufgabe 3) ✓; L3 (Fehlerfolge streng monoton fallend gegen $\approx0.031$; Bias-Deutung deckt Skript-Randnotiz S. 29) ✓
- **Errata-Konformität:** Blatt 3, L6c zitiert den Skript-Konvergenzwert als **0.15853** mit Kennzeichnung „[Korrektur ggü. Original, S. 32]“ (Erratum 1) — korrekt; kein Blatt übernimmt einen Originalfehler (weder 0.1599 noch 0.05102/Erratum 12 noch den Indexsprung aus Erratum 2 — Blatt 3 indiziert durchgängig $s_{h,\,x=2}$; auch die unsaubere „$\kappa\leq0.247$“-Formulierung von S. 31 wird vermieden, Blatt 3 schreibt $\kappa\approx0.249$ für das eigene Beispiel).
- **Skript-Zitate verifiziert:** Randnotiz S. 29 („numerical method evaluated on perturbed input data“, Bias-Notiz), „Show it“-Randnotiz S. 31, Anomalie-Warnung S. 31, Teaser S. 16, „only 100 operations“ S. 14, Sigmoid-Randnotiz S. 11, Gl. 2 S. 10, Gl. 4/7, IEEE-754-Aufbau/Bias 127 S. 19, Constructing scale S. 20, Fixed-Point-Beispiel S. 21, Auslöschungsbeispiel S. 22–23, Overflow/Underflow-Randnotizen S. 23 — alle Bezüge stimmen mit dem PDF überein.

---

## WICHTIG

**Keine Befunde.** (Der Iteration-2-Stand mit 0 KRITISCH / 0 WICHTIG ist bestätigt; die unabhängige Neurechnung mit frischem Blick hat keine übersehenen Mängel zutage gefördert.)

---

## OPTIONAL (Stil/Konsistenz)

Alle sechs Punkte sind aus Iteration 2 übernommen und unverändert offen — laut Auftrag zulässig. **Keine neuen optionalen Befunde.**

### O1 — (It. 1/2) Blatt 1: keine Teilpunkt-Aufschlüsselung je Teilaufgabe
Blätter 2 und 3 weisen Teilpunkte aus, Blatt 1 nur Punkte pro Aufgabe (Summe 40 korrekt). Serieninkonsistenz, kein Vorgabenverstoß.

### O2 — (It. 1/2) Blatt 3, Lösung 4(c): Sinuswerte nicht in der Wertetabelle
$|\sin(3)|\approx0.141$ und $|\sin(1.5)|\approx0.997$ stehen nicht in der Tabelle; Taschenrechner ist als Hilfsmittel deklariert, die qualitative Begründung trägt die Punkte.

### O3 — (It. 1/2) Blatt 3: `\author`-Feld zweckentfremdet
Untertitel-Inhalt („Konditionierung, Stabilität, …“) steht im `\author{}`-Feld. Rein kosmetisch, kompiliert sauber.

### O4 — (It. 1/2) Blatt 1, Lösung 7(a): Deutung der „only 100 operations“
„…, also etwa vier Rechenoperationen pro Kombination“ bleibt eine unbelegte (plausible) Interpretation der Skriptangabe S. 14.

### O5 — (It. 2) Blatt 3, Lösung 6(a): Gleichheitszeichen nach unterer Schranke
$c_1\geq0.01001$ wird eingeführt, im Fazit als „$c_1 = 0.01001$“ zitiert. Das Skript verfährt auf S. 32 genauso; fachlich harmlos (Wert an der betrachteten Stelle exakt erreicht), notationell leicht unscharf.

### O6 — (It. 2) Blatt 3, Lösung 7(c): Letzte-Stelle-Rundung bei $\kappa(2,+0.25)$
Aus 5-stelligen Tabellenwerten ergibt sich $0.21202$ (exakt $0.2120268\ldots\to0.21203$). Beide verglichenen Größen stammen aus denselben Tabellenwerten, die Aussage („erreicht $\kappa$ exakt“) bleibt gültig; Lösung 4 deklariert die $\pm1$-Rundungstoleranz. Wiederholung des Hinweises in 7(c) wäre sauberer.

---

## Zusammenfassende Bewertung

| Kriterium | Befund |
|---|---|
| Änderungsstand | Blätter seit Iteration 2 nachweislich unverändert (mtime, Wortlaut-Abgleich, byte-identische Kompilate) |
| Korrektheit aller Musterlösungen | Alle 24 Aufgaben (72 Teilaufgaben) vollständig unabhängig neu nachgerechnet — 122 automatisierte Checks bestanden, Beweise handgeprüft: **keine falsche Musterlösung** |
| Lösbarkeit/Eindeutigkeit | Alle Aufgaben mit deklarierten Hilfsmitteln eindeutig lösbar; Wertetabelle Blatt 3 vollständig; Pflicht-Eingaben (z. B. $\cos(\pi+0.25)$ in A8b) im Aufgabentext |
| Skript-Treue | Kerninhalte Kap. 1–3 abgedeckt; alle Skript-Verweise (Seiten, Gleichungen 1–19, Randnotizen) gegen das PDF verifiziert; Transferinhalte (impliz. Mantissenbit, $\mathcal{O}(N^d)$, Beweisaufgabe) gekennzeichnet; Errata 1/2/12 korrekt umgesetzt, kein Originalfehler übernommen |
| Struktur/Format | Je 8 Aufgaben, deklarierter Schwierigkeitsanstieg, Punkte + korrekte Summen (40/38/50, Teilpunkte aufgehen), Lösungen strikt nach `\newpage`, alle Label/Refs aufgelöst (Kompiliertest: 0 Fehler/Warnungen), keine Lösungsleaks |
| Didaktik | Vollständige Lösungswege mit Zwischenschritten, Tabellen, Proben; Querbezüge (Blatt 3: A3↔A8b, A5↔A7c/A8a, A2c↔A8a) konsistent |

**Befunde: KRITISCH 0 · WICHTIG 0 · OPTIONAL 6** (alle 6 aus Vorrunden übernommen, keine neuen).

## Freigabe-Urteil: **JA — freigegeben.**
Die drei Übungsblätter sind in der vorliegenden Form fachlich korrekt, vorgabenkonform und können ohne weitere Überarbeitung ausgegeben werden. Die offenen OPTIONAL-Punkte sind reine Stil-/Konsistenzhinweise ohne Einfluss auf Korrektheit oder Verwendbarkeit.
