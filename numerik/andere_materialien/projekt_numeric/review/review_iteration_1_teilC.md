# Review Iteration 1 — Teil C: Übungsblätter 1–3

**Reviewer:** unabhängige Prüfung ausschließlich anhand der Dateien (Übungsblätter, Original-PDF S. 9–34, errata_original_pdf.md).
**Methode:** Jede Musterlösung wurde vollständig nachgerechnet (Python-Skripte unter `/tmp/review_calc/`, zusätzlich Handprüfung der Herleitungen); alle drei `.tex`-Dateien wurden testweise mit `pdflatex` kompiliert (2 Läufe, alle `\ref` aufgelöst, keine Fehler). Punktesummen, Struktur, Skript-Treue (S. 9–16 / 17–24 / 25–34) und Errata-Konformität wurden geprüft.

**Geprüfte Dateien:**
- `output/uebungen/uebung_01_enter_numerical_methods.tex` (8 Aufgaben, 40 P.)
- `output/uebungen/uebung_02_floating_point_arithmetic.tex` (8 Aufgaben, 38 P.)
- `output/uebungen/uebung_03_error_analysis.tex` (8 Aufgaben, 50 P.)

---

## KRITISCH

**Keine Befunde.**

Nachrechnungs-Protokoll (alle Werte unabhängig verifiziert, Auswahl der rechenintensiven Stellen):

- **Blatt 1, L2:** h = 2/8 = 0.25, 9 Gitterpunkte; N = 2/0.01 = 200, 201 Auswertungen ✓
- **Blatt 1, L4:** cos(0..4) = 1, 0.5403, −0.4161, −0.9900, −0.6536; Min bei x=3; Fehler |−1−(−0.9900)| = 0.0100; cos(3.1) = −0.99914 ✓
- **Blatt 1, L5:** exakte Lösung (w,b) = (4,−3) ✓; alle 9 Gitterzeilen nachgerechnet, Fehlersummen 19, 13, 7, 5, **3**, 7, 9, 15, 21 → Minimum 3 bei (2,2) ✓
- **Blatt 1, L6:** 3×3-System (Skript Gl. 2): per Cramer unabhängig bestätigt w = (−76/3, 2/3, 64/3); alle Zwischenschritte (II′: 7w₁+10w₃=36; III′: w₁=−4−w₃; 3w₃=64) und alle drei Verifikationen korrekt ✓
- **Blatt 1, L7:** 5²=25; 100²=10 000; 100¹⁰=10²⁰; 10²⁰/10⁹=10¹¹ s; 10¹¹/3.156·10⁷ = 3168.6 ≈ 3.17·10³ Jahre ✓
- **Blatt 1, L8:** Gittertabelle L(w) = 45, 23.5, 9, 1.5, **1**, 7.5, 21 ✓; L′(w)=28w−50, w*=25/14≈1.7857, L(w*)=5/14≈0.3571, |2−25/14|=3/14≈0.2143, |1−5/14|=9/14≈0.6429 ✓
- **Blatt 2, L2:** 10/3 − 3333/1000 = 1/3000 = 0.000333… ✓
- **Blatt 2, L4a:** E=10000010₂=130, e=3, 1.101₂=1.625, x=−1.625·8=**−13.0** ✓ (Mantissenfeld 23 Bit, nachgezählt)
- **Blatt 2, L4b:** 6.25=110.01₂=1.1001₂×2², E=129=10000001₂, m=1001+19 Nullen (23 Bit) ✓, Probe 1.5625·4=6.25 ✓
- **Blatt 2, L5:** 2⁻²³=1/8388608≈1.19·10⁻⁷; 2⁻⁵²≈2.22·10⁻¹⁶; 2-Bit-Mantisse 0/0.25/0.5/0.75 (deckungsgleich mit Skript S. 20); t=3 → 8 Werte ✓
- **Blatt 2, L6:** 10=1010₂, 100=1100100₂, 1000=1111101000₂; E = 130/133/136 = 10000010₂/10000101₂/10001000₂ — identisch mit Skript S. 20 ✓
- **Blatt 2, L7:** 1.234567·10⁶=1234567; Präzision 10⁻⁶, max. Rundungsfehler 0.5·10⁻⁶; 10⁹ < 2 147 483 647 < 10¹⁰ ✓
- **Blatt 2, L8a:** (i) 12345678.5→12345679, Maschinendifferenz 1 vs. wahr 0.5, abs. 0.5, rel. 100 %; (ii) 12345678.4→12345678, Differenz 0 vs. 0.4, rel. 100 % — per Decimal-Arithmetik bestätigt ✓ (deckt sich mit Skript S. 22–23)
- **Blatt 2, L8b:** 1+10⁻²⁰ rundet in double auf 1 (10⁻²⁰ < 2⁻⁵²), Nenner 0, IEEE-Ergebnis +∞; Umformung 1/ε = 10²⁰ ✓
- **Blatt 3, Wertetabelle:** alle 11 cos-Werte auf 5 Nachkommastellen unabhängig bestätigt (maximale Abweichung 0 in der 5. Stelle) ✓; alle für Aufg. 4–7c benötigten Stützstellen sind enthalten
- **Blatt 3, L4:** κ(3,+0.25)=0.00414; κ(3,−0.25)=0.06569; κ(1.5,+0.25)=0.24899; κ(1.5,−0.25)=0.24458 ✓; |sin(3)|=0.1411, |sin(1.5)|=0.9975 ✓
- **Blatt 3, L5:** nächste Gitterpunkte korrekt (h=1: 2.25→2; h=0.2: 2.25→2.2, Abstand 0.05<0.15); s₁=0; |cos(2.2)−cos(2)|=0.17235, s₀.₂=0.17235/0.25=0.6894 ✓
- **Blatt 3, L6:** π→3 (0.14159<0.85841) bzw. π→3.2 (0.05841<0.14159): c₁=0.01001, c₀.₂=0.00171 ✓; x̃=3.39159→3 bzw. →3.4 (0.00841<0.19159): Konvergenz 0.01001 bzw. 0.03320 ✓ — der „überraschende Befund" (Konsistenz besser, Konvergenz schlechter) ist rechnerisch korrekt und didaktisch wertvoll
- **Blatt 3, L7:** Beweis (a) via |x−xᵢ|≤h/2 und Mittelwertsatz korrekt; (b) umgekehrte Dreiecksungleichung korrekt angewendet (Schranke L·h); (c) h=0.05: 2 und 2.25 sind Gitterpunkte (40·h, 45·h), |cos(2.25)−cos(2)|=0.21202=κ(2,+0.25) ✓; Folge 0 → 0.17235 → 0.21202 ✓
- **Blatt 3, L8b:** cos(π+0.25)=−0.96891, Bias-Grenzwert 0.03109 ✓ — konsistent mit Tabellengrenzwert ≈0.031 aus Aufgabe 3 (sauberes Querbezugsdesign)

**Weitere KRITISCH-Prüfungen ohne Befund:**
- Keine Lösungen oder starken Hinweise im Aufgabenteil (Blatt 3: f(x*)=−1/x*=π im Szenario und der Hinweis cos(π+0.25)=−0.96891 in Aufg. 8b sind notwendige Angaben, keine Leaks).
- Alle Aufgaben sind mit den deklarierten Hilfsmitteln eindeutig lösbar (Blatt 3 erlaubt explizit Taschenrechner; Wertetabelle deckt alle Pflicht-Stützstellen ab).
- Errata-Konformität: Blatt 3, L6c zitiert den Skriptwert korrekt als **0.15853** mit Kennzeichnung „[Korrektur ggü. Original, S. 32]" (Erratum 1). Kein Blatt übernimmt einen Originalfehler; die fehlerhaften PDF-Werte (0.1599 etc.) tauchen nur als gekennzeichnetes Zitat auf.

---

## WICHTIG

**1 Befund.**

### W1 — Blatt 2, Lösung 8(c): Underflow-Beispielrechnung demonstriert den Underflow-Schaden nicht sauber
- **Datei/Stelle:** `uebung_02_floating_point_arithmetic.tex`, Lösung zu Aufgabe 8(c) (Z. 340).
- **Beschreibung:** Die Lösung nennt als „gefährliche Folgerechnung" $1/y^2$ mit $y=10^{-25}$: Maschine liefert $1/0 = \infty$ „statt des wahren Werts $10^{50}$". Nachrechnung: Der wahre Wert $10^{50}$ liegt selbst oberhalb der größten darstellbaren single-precision-Zahl ($\approx 10^{38}$, vgl. Skript S. 20 und Aufgabenteil c selbst). Auch ohne Underflow ergäbe die Rechnung in single precision also $+\infty$ (Overflow) — das gewählte Zahlenbeispiel isoliert den Underflow-Effekt somit nicht; der demonstrierte Schaden tritt unabhängig vom Underflow ein. Die Benennung der Phänomene (Overflow/Underflow) und die Kernrechnung ($10^{40}>10^{38}$, $10^{-50}\to 0$) sind korrekt; nur die Folgerechnung ist als Beleg lückenhaft/irreführend.
- **Behebungsvorschlag:** Folgerechnung so wählen, dass der wahre Wert darstellbar ist, z. B. $y/y^2$ (wahr $10^{25}$, darstellbar; Maschine: $10^{-25}/0=\infty$) oder $x/y^2$ mit $x=10^{-20}$ (wahr $10^{30}$, darstellbar). Alternativ den Halbsatz „statt des wahren Werts $10^{50}$" ersetzen durch einen Hinweis, dass hier zusätzlich der wahre Wert selbst nicht darstellbar wäre.

---

## OPTIONAL (Stil/Konsistenz)

### O1 — Blatt 1: keine Teilpunkt-Aufschlüsselung je Teilaufgabe
Blätter 2 und 3 weisen Punkte pro Teilaufgabe (a/b/c) aus, Blatt 1 nur pro Aufgabe. Kein Verstoß gegen die Vorgabe (Punkte pro Aufgabe + Summe vorhanden, Summe 40 stimmt), aber inkonsistent über die Serie. Vorschlag: Teilpunkte in Blatt 1 ergänzen.

### O2 — Blatt 2, Aufgabe 4: implizites führendes Mantissenbit geht leicht über das Skript hinaus
Das Skript (S. 19–20) führt IEEE 754, Bias 127 und normalisierte Form $1.xxx_2\times2^e$ ein, erwähnt aber die Konvention „führende 1 wird nicht mitgespeichert" nicht. Die Aufgabe definiert dies vollständig selbst im Aufgabentext (damit eigenständig lösbar), ist aber nicht als über das Skript hinausgehend gekennzeichnet. Vorschlag: kurze Fußnote „erweitert die Skriptdarstellung" oder Kennzeichnung als leichte Transferkomponente.

### O3 — Blatt 3, Lösung 4(c): Sinuswerte nicht in der Wertetabelle
Die quantitative Begründung nutzt $|\sin(3)|\approx0.141$ und $|\sin(1.5)|\approx0.997$; beide stehen nicht in der Wertetabelle. Da Taschenrechner explizit erlaubt ist und eine qualitative Begründung (flach am Minimum, steil an der Nullstelle) zur Punktevergabe genügt, kein WICHTIG-Mangel. Vorschlag: die beiden $|\sin|$-Werte in die Wertetabelle aufnehmen oder die Musterlösung als „qualitativ ausreichend, quantitativ mit Taschenrechner" kennzeichnen.

### O4 — Blatt 3: `\author`-Feld zweckentfremdet
Die Zeile „Konditionierung, Stabilität, Konsistenz und Konvergenz (Skript S. 25–34)" steht im `\author{}`-Feld statt im `\subtitle`. Rein kosmetisch (rendert als Untertitel-artige Zeile). Vorschlag: in `\subtitle` integrieren.

### O5 — Blatt 2: Schwierigkeitsstaffelung nicht im Kopf angekündigt
Blätter 1 und 3 benennen die Staffelung (Verständnis → Standard → Transfer) explizit im Hinweistext; Blatt 2 nicht (die Staffelung ist faktisch vorhanden: A1–A3 Verständnis, A4–A7 Standard, A8 Transfer, im Titel als „Transfer" markiert). Vorschlag: einen Satz analog zu Blatt 1/3 ergänzen.

### O6 — Blatt 1, Lösung 7(a): Interpretation der „100 operations" spekulativ
Die Deutung „25 Kombinationen × etwa vier Rechenoperationen" der Skriptangabe „only 100 operations" (S. 14) ist plausibel, aber nicht belegt. Vorschlag: vorsichtiger formulieren („vermutlich gemeint: …").

---

## Zusammenfassende Bewertung

| Kriterium | Befund |
|---|---|
| Korrektheit aller Musterlösungen | Alle 24 Aufgaben (72 Teilaufgaben) nachgerechnet — **keine falsche Musterlösung**; einzige inhaltliche Schwäche: W1 (suboptimales Underflow-Folgebeispiel in einer Lösung) |
| Lösbarkeit/Eindeutigkeit | Alle Aufgaben eindeutig und mit deklarierten Hilfsmitteln lösbar |
| Skript-Treue | Kerninhalte der Kap. 1–3 vollständig abgedeckt (Diskretisierung, Grid Search, LGS, Fehlerarten, IEEE 754, ε_mach, Fixed-Point, Auslöschung, Hut/Tilde, κ/s/c/Konvergenz inkl. Skript-Randnotizen „Show it" und Bias/Varianz); Transfer-Inhalte (O(N^d), Mittelwertsatz-Beweis, Loss-Minimierung) als Transfer gekennzeichnet; Errata korrekt umgesetzt (0.15853 statt 0.1599, gekennzeichnet) |
| Struktur/Format | Je 8 Aufgaben, ansteigende Schwierigkeit, Punkte je Aufgabe + korrekte Summen (40/38/50), Lösungen strikt nach `\newpage` mit klarer Überschrift, Label/Ref-Verknüpfung funktioniert (Kompiliertest), keine Lösungsleaks |
| Didaktik | Lösungswege durchgängig vollständig (Zwischenschritte, Tabellen, Verifikationen, Begründungen); Querbezüge zwischen Aufgaben (Blatt 3: A3↔A8b, A5↔A7c) sauber konstruiert |

**Befunde: KRITISCH 0 · WICHTIG 1 · OPTIONAL 6.**
Die drei Übungsblätter sind in der vorliegenden Form fachlich korrekt und einsatzfähig; W1 sollte vor Veröffentlichung behoben werden.
