# Review Iteration 2 — Teil C: Übungsblätter 1–3

**Reviewer:** unabhängige Neuprüfung (Iteration 2) ausschließlich anhand der Dateien: drei `.tex`-Übungsblätter, Original-PDF S. 9–34 (vollständig gelesen), `errata_original_pdf.md`, `review_iteration_1_teilC.md`.
**Methode:** Jede Musterlösung wurde erneut vollständig nachgerechnet (Python-Skript `/tmp/review_calc/iter2_check.py`, 100 Einzelprüfungen, zusätzlich Handprüfung aller Herleitungen und Beweise); alle drei Blätter wurden mit `pdflatex` kompiliert (je 2 Läufe: PDFs erzeugt, alle `\ref`/`\pageref` aufgelöst, 0 Fehler, 0 Warnungen). Punktesummen inkl. Teilpunkte, Struktur, Skript-Treue (S. 9–16 / 17–24 / 25–34), Errata-Konformität und Regressionscheck der Überarbeitung wurden geprüft.

**Geprüfte Dateien:**
- `output/uebungen/uebung_01_enter_numerical_methods.tex` (8 Aufgaben, 40 P.)
- `output/uebungen/uebung_02_floating_point_arithmetic.tex` (8 Aufgaben, 38 P.)
- `output/uebungen/uebung_03_error_analysis.tex` (8 Aufgaben, 50 P.)

---

## Behebungsstatus Iteration 1

| Befund It. 1 | Status | Verifikation |
|---|---|---|
| **W1** — Blatt 2, Lösung 8(c): Underflow-Folgebeispiel ($1/y^2$, wahrer Wert $10^{50}$ selbst nicht darstellbar) | **BEHOBEN** | Die Lösung verwendet jetzt exakt den vorgeschlagenen Fix $y/y^2$: Maschine $10^{-25}/0 = \infty$, wahrer Wert $10^{-25}/10^{-50} = 10^{25}$, mit explizitem Nachweis der Darstellbarkeit ($10^{25} < 10^{38}$; auch $y = 10^{-25} > 10^{-38}$ ist darstellbar) und dem Schlusssatz „Der Schaden entsteht hier also allein durch den Underflow im Nenner." Rechnung nachgeprüft — korrekt; der Underflow-Effekt ist nun sauber isoliert. Keine Folgefehler. |
| O2 — Blatt 2, Aufg. 4: implizites führendes Mantissenbit ohne Kennzeichnung | **BEHOBEN** | Aufgabentext enthält jetzt den Hinweis: „Die Konvention des impliziten führenden Mantissenbits geht leicht über die Skriptdarstellung (S. 19–20) hinaus und ist hier vollständig angegeben — eine kleine Transferkomponente." Fachlich korrekt formuliert. |
| O5 — Blatt 2: Schwierigkeitsstaffelung nicht im Kopf angekündigt | **BEHOBEN** | Kopftext nennt jetzt: „Aufgaben 1–3 … Begriffsverständnis, Aufgaben 4–7 … Standardaufgaben analog zum Skript, Aufgabe 8 … Transferaufgabe"; zusätzlich Verweis auf die Lösungsseite via `\pageref{sec:loesungen}` (kompiliert, aufgelöst). |
| O1 — Blatt 1: keine Teilpunkte je Teilaufgabe | nicht umgesetzt (optional, zulässig) | unverändert; Summe 40 weiterhin korrekt. |
| O3 — Blatt 3, Lösung 4(c): $|\sin|$-Werte nicht in Wertetabelle | nicht umgesetzt (optional, zulässig) | unverändert; Taschenrechner ist als Hilfsmittel deklariert, qualitative Begründung trägt die Punkte. |
| O4 — Blatt 3: `\author`-Feld zweckentfremdet | nicht umgesetzt (optional, zulässig) | unverändert; rein kosmetisch, kompiliert sauber. |
| O6 — Blatt 1, Lösung 7(a): Deutung der „100 operations" | nicht umgesetzt (optional, zulässig) | Formulierung inhaltlich unverändert („…, also etwa vier Rechenoperationen pro Kombination"). |

**Regressionscheck:** Die drei geänderten Stellen (Blatt 2: Lösung 8c, Aufgabenhinweis 4, Kopftext) wurden vollständig nachgerechnet bzw. gegen Skript S. 19–20 geprüft — **keine neuen Fehler durch die Überarbeitung.** Alle übrigen Inhalte stimmen mit dem in Iteration 1 geprüften Stand überein (vollständige Neurechnung aller 24 Aufgaben bestätigt sämtliche Werte erneut).

---

## KRITISCH

**Keine Befunde.**

Nachrechnungs-Protokoll Iteration 2 (alle 24 Aufgaben / 72 Teilaufgaben unabhängig neu verifiziert; Auswahl):

- **Blatt 1:** L2 (h=0.25, 9 Punkte; N=200, 201 Auswertungen) ✓; L4 (cos-Tabelle, Min −0.9900 bei x=3, Fehler 0.0100, cos(3.1)=−0.9991) ✓; L5 (exakt (4,−3); alle 9 Gitterzeilen identisch nachgerechnet, Min 3 bei (2,2); b=−3 außerhalb des Suchbereichs — Diskussion korrekt) ✓; L6 (per Cramer: w=(−76/3, 2/3, 64/3), det=3; alle Zwischenschritte II′/III′ und drei Verifikationen korrekt) ✓; L7 (25; 10⁴; 10²⁰; 10¹¹ s; 3168.6 ≈ 3.17·10³ Jahre) ✓; L8 (Tabelle 45/23.5/9/1.5/**1**/7.5/21; L′=28w−50, w*=25/14, L(w*)=5/14 exakt per Bruchrechnung bestätigt; Fehler 3/14 bzw. 9/14) ✓
- **Blatt 2:** L2 (1/3000 = (10000−9999)/3000) ✓; L4a (E=130, e=3, 1.101₂=1.625, x=−13.0; Mantissenfelder in Aufgabe und Lösung je exakt 23 Bit nachgezählt) ✓; L4b (110.01₂ → 1.1001₂×2², E=129=10000001₂, Probe 1.5625·4=6.25) ✓; L5 (2⁻²³=1/8388608≈1.19·10⁻⁷, 2⁻⁵²≈2.22·10⁻¹⁶; 2-Bit-Mantisse 0/0.25/0.5/0.75 deckungsgleich Skript S. 20; 2³=8) ✓; L6 (1010₂/1100100₂/1111101000₂, Zerlegungen geprüft; E=130/133/136 binär korrekt, identisch Skript S. 20) ✓; L7 (1234567; 10⁻⁶ bzw. 0.5·10⁻⁶; 10⁹ < 2 147 483 647 < 10¹⁰) ✓; L8a (beide Paare per Decimal-Rundung bestätigt, je 100 % relativer Fehler — deckungsgleich Skript S. 22–23) ✓; L8b (10⁻²⁰ < 2⁻⁵² → Nenner 0 → +∞; Umformung 1/ε = 10²⁰) ✓; L8c (Overflow 10⁴⁰ > 10³⁸; Underflow 10⁻⁵⁰ → 0; **neues** Folgebeispiel y/y² = 10²⁵ < 10³⁸ korrekt) ✓
- **Blatt 3:** alle 11 Tabellenwerte cos(x) auf 5 Nachkommastellen exakt bestätigt; alle für Aufg. 4–7c benötigten Stützstellen enthalten ✓; L4 (κ = 0.00414 / 0.06569 / 0.24899 / 0.24458; |sin(3)|=0.141, |sin(1.5)|=0.997) ✓; L5 (Nächste-Gitterpunkt-Logik geprüft: 2.25→2 bei h=1, 2.25→2.2 bei h=0.2; s=0 bzw. 0.17235/0.25=0.6894) ✓; L6 (π→3 bzw. π→3.2, Abstände 0.14159/0.85841 und 0.05841/0.14159 ✓; c₁=0.01001, c₀.₂=0.00171; x̃=3.39159→3 bzw. →3.4, Abstände 0.39159/0.60841 und 0.00841/0.19159 ✓; Konvergenz 0.01001 bzw. 0.03320 — Befund „Konsistenz besser, Konvergenz schlechter" rechnerisch korrekt) ✓; L7 (Beweis a via |x−xᵢ|≤h/2 + Mittelwertsatz korrekt; b umgekehrte Dreiecksungleichung, Schranke L·h korrekt; c: 2=40·0.05 und 2.25=45·0.05 sind Gitterpunkte, Folge 0 → 0.17235 → 0.21202 = κ(2,+0.25)) ✓; L8b (cos(π+0.25)=−0.96891, Grenzwert 0.03109 — konsistent mit Tabellengrenzwert ≈0.031 aus Aufg. 3) ✓
- **Errata-Konformität:** Blatt 3, L6c zitiert den Skript-Konvergenzwert korrekt als **0.15853** mit Kennzeichnung „[Korrektur ggü. Original, S. 32]" (Erratum 1). Kein Blatt übernimmt einen Originalfehler (insbes. weder 0.1599 noch 0.05102/Erratum 12 noch den Indexfehler aus Erratum 2 — Blatt 3 nutzt durchgängig konsistente Indizes $s_{h,\,x=2}$).
- **Keine Lösungsleaks:** Aufgabenteile enthalten nur notwendige Angaben (Blatt 3: $f(x^*)=-1$ bei $x^*=\pi$ im Szenario und der Hinweis $\cos(\pi+0.25)=-0.96891$ in Aufg. 8b sind Pflicht-Eingaben, da nicht in der Wertetabelle). Alle Aufgaben mit deklarierten Hilfsmitteln eindeutig lösbar.

---

## WICHTIG

**Keine Befunde.** (W1 aus Iteration 1 ist behoben und verifiziert; bei der vollständigen Neuprüfung wurden keine weiteren Mängel dieser Kategorie gefunden.)

---

## OPTIONAL (Stil/Konsistenz)

### O1 — (übernommen aus It. 1) Blatt 1: keine Teilpunkt-Aufschlüsselung je Teilaufgabe
Blätter 2 und 3 weisen Teilpunkte aus, Blatt 1 nur Punkte pro Aufgabe. Kein Vorgabenverstoß (Summe 40 korrekt), aber serieninkonsistent.

### O2 — (übernommen, It.-1-O3) Blatt 3, Lösung 4(c): Sinuswerte nicht in der Wertetabelle
$|\sin(3)|\approx 0.141$ und $|\sin(1.5)|\approx 0.997$ stehen nicht in der Tabelle; Taschenrechner ist erlaubt und die qualitative Begründung genügt — daher nur optional.

### O3 — (übernommen, It.-1-O4) Blatt 3: `\author`-Feld zweckentfremdet
Untertitel-Inhalt („Konditionierung, Stabilität, …") steht im `\author{}`-Feld. Rein kosmetisch, kompiliert sauber.

### O4 — (übernommen, It.-1-O6) Blatt 1, Lösung 7(a): Deutung der „only 100 operations"
„…, also etwa vier Rechenoperationen pro Kombination" bleibt eine unbelegte (wenn auch plausible) Interpretation der Skriptangabe S. 14. Vorsichtigere Formulierung („vermutlich") wäre sauberer.

### O5 — (neu) Blatt 3, Lösung 6(a): Gleichheitszeichen nach unterer Schranke
Die Konstanten werden korrekt als untere Schranken eingeführt ($c_1 \geq 0.01001$, $c_{0.2} \geq 0.00171$), im Fazit-Satz dann aber als „$c_1 = 0.01001$ gegenüber $c_{0.2} = 0.00171$" zitiert. Das Skript verfährt auf S. 32 genauso; fachlich harmlos (an der betrachteten Stelle ist der Wert exakt erreicht), notationell aber leicht unscharf.

### O6 — (neu) Blatt 3, Lösung 7(c)/4: Letzte-Stelle-Rundung bei $\kappa(2,+0.25)$
Aus den 5-stelligen Tabellenwerten ergibt sich $|{-0.62817}+0.41615| = 0.21202$; der exakte Wert ist $0.2120268\ldots \to 0.21203$. Da beide verglichenen Größen in Lösung 7c aus denselben Tabellenwerten gebildet werden, bleibt die Aussage („erreicht $\kappa$ exakt") gültig, und Lösung 4 deklariert „$\pm 1$ in der letzten Nachkommastelle" ausdrücklich. Optional: den Rundungshinweis auch in Lösung 7c wiederholen.

---

## Zusammenfassende Bewertung

| Kriterium | Befund |
|---|---|
| Korrektheit aller Musterlösungen | Alle 24 Aufgaben (72 Teilaufgaben) vollständig neu nachgerechnet (100 automatisierte Einzelchecks + Handprüfung der Beweise) — **keine falsche Musterlösung, kein verbleibender inhaltlicher Mangel** |
| Behebung Iteration 1 | W1 vollständig und korrekt behoben; zusätzlich O2 und O5 aus It. 1 umgesetzt; keine Regression |
| Lösbarkeit/Eindeutigkeit | Alle Aufgaben eindeutig und mit deklarierten Hilfsmitteln lösbar; Wertetabelle Blatt 3 deckt alle Pflicht-Stützstellen |
| Skript-Treue | Kerninhalte Kap. 1–3 vollständig abgedeckt (analytisch vs. numerisch, Diskretisierung/h, Extrema auf [a,b], Grid Search, LGS Gl. 1/2, Fehlerarten, 10/3, IEEE 754/Bias 127, ε_mach Gl. 11/12, Fixed-Point, Auslöschung, 1/(1+ε−1), Hut/Tilde, κ/s/c/Konvergenz Gl. 13–19 inkl. Randnotizen „Show it", Bias, Anomalie-Warnung); Fremd-/Transferinhalte gekennzeichnet (O(N^d), implizites Mantissenbit, Beweisaufgabe); Errata korrekt umgesetzt |
| Struktur/Format | Je 8 Aufgaben (Vorgabe 5–8), deklarierter und faktischer Schwierigkeitsanstieg, Punkte je (Teil-)Aufgabe + korrekte Summen (40/38/50), Lösungen strikt nach `\newpage`, Label/Ref vollständig aufgelöst (Kompiliertest 2 Läufe, 0 Fehler/Warnungen), keine Lösungsleaks |
| Didaktik | Vollständige Lösungswege mit Zwischenschritten, Tabellen, Proben; Querbezüge (Blatt 3: A3↔A8b, A5↔A7c, A2c↔A8a) konsistent; Blatt 2 nun mit Staffelungshinweis und Lösungs-Seitenverweis |

**Befunde: KRITISCH 0 · WICHTIG 0 · OPTIONAL 6** (davon 4 aus Iteration 1 übernommen, 2 neue Geringfügigkeiten).
Die drei Übungsblätter sind in der vorliegenden überarbeiteten Form fachlich korrekt, vorgabenkonform und **freigabefähig**.
