# Review Iteration 4 (Bestätigungsrunde) — Teil B: Übungsblätter 1–6

**Reviewer:** unabhängige Schlussprüfung (Iteration 4, ohne Vorwissen) ausschließlich anhand der Dateien: sechs `.tex`-Übungsblätter, Original-PDF S. 9–70 (vollständig gelesen, inkl. aller Randnotizen), `errata_original_pdf.md`, `review_iteration_3_teilC.md` (Teil C: freigegeben ohne Auflagen), `review_iteration_3_teilD.md` (Teil D: freigegeben mit einer Auflage W1).
**Methode:** (1) Verifikation der einzigen seit Iteration 3 geänderten Stelle (Blatt 6, Lösung 8c) inkl. eigenständiger exakter Nachrechnung des Symmetriearguments; (2) vollständige unabhängige Neurechnung aller sechs Blätter (Python-Skripte `/tmp/review_calc/iter4_blatt6_w1_check.py`, `iter4_blatt6_full.py`, `iter4_blatt45_full.py`, `iter4_blatt123_full.py`; **zusammen 1047 automatisierte Einzelchecks, 0 echte Fehlschläge** — 4 anfängliche Prüf-Flags erwiesen sich als Artefakte meiner eigenen Toleranzannahmen und wurden mit exakter Bruchrechnung als korrekt bestätigt, s. u.); (3) Kompiliertest aller sechs Blätter (`bash /tmp/textest/compile_it4u.sh`, je 2 `pdflatex`-Läufe): **6 × OK, 0 Fehler, 0 LaTeX-Warnungen, 0 unaufgelöste Referenzen** (PDFs: 8/7/9/9/10/11 Seiten); (4) Struktur-, Punkte-, Leak- und Errata-Prüfung; (5) Regressionssicht auf alle in Iteration 3 protokollierten Werte.

**Geprüfte Dateien** (`output/uebungen/`):

| Blatt | Datei | Punkte ausgewiesen | nachsummiert |
|---|---|---|---|
| 1 | `uebung_01_enter_numerical_methods.tex` | 40 | 4+4+3+6+6+6+5+6 = 40 ✓ |
| 2 | `uebung_02_floating_point_arithmetic.tex` | 38 | 4+4+3+6+5+4+4+8 = 38 ✓ (Teilpunkte gehen je Aufgabe auf, inkl. halber Punkte) |
| 3 | `uebung_03_error_analysis.tex` | 50 | 4+6+4+6+7+9+8+6 = 50 ✓ |
| 4 | `uebung_04_newton_methods.tex` | 50 | 4+5+7+6+7+5+9+7 = 50 ✓ |
| 5 | `uebung_05_global_optimization.tex` | 50 | 4+6+5+7+7+5+6+10 = 50 ✓ |
| 6 | `uebung_06_numerical_integration.tex` | 57 | 5+6+5+8+8+6+9+10 = 57 ✓ |

Teilpunkte je Teilaufgabe wurden für alle Blätter 2–6 gegen die Aufgabensummen nachaddiert (stimmig); Blatt 1 weist wie bisher nur Punkte pro Aufgabe aus (Alt-OPTIONAL O1 aus Teil C, unverändert zulässig).

---

## Änderungsstand seit Iteration 3

Nur **Blatt 6** wurde verändert (mtime 13:06, eine Minute nach Abschluss von `review_iteration_3_teilD.md`, 13:05); die Blätter 1–5 tragen Änderungszeitpunkte **vor** Abschluss der Iteration-3-Reviews (11:12 / 12:33 / 11:17 / 12:49 / 12:50) und enthalten alle in Iteration 3 wörtlich zitierten Stellen unverändert (stichprobenhaft verifiziert: B4 Z. 146–156 K1-Fix, B5 Z. 396 „$0.5208$" [Alt-O1], B5 Z. 518 „$0.2063 - 0.9085 = -0.7022$" [Alt-O2], B5 Z. 575/580 „$7.1381$"). Die Änderung in Blatt 6 betrifft genau die von Iteration 3 beauflagte Stelle (Lösung 8c, Z. 304); der gesamte Rest von Blatt 6 wurde dennoch vollständig neu gerechnet und ist regressionsfrei.

---

## Behebungsstatus der Iteration-3-Auflage (W1)

| Auflage Iteration 3 | Status | Verifikation |
|---|---|---|
| **W1** — Blatt 6, Lösung 8(c): „Abweichung … proportional zu $(x-m)^3$" war mathematisch falsch; gefordert: Darstellung $c\,(x-a)(x-m)(x-b) = c\big[(x-m)^3 - \tfrac{h^2}{4}(x-m)\big]$ mit Symmetrieargument | **BEHOBEN** | Z. 304 lautet jetzt: „Für ein kubisches Polynom mit Leitkoeffizient $c$ betrachte man die Abweichung vom quadratischen Interpolanten: Da sie ein kubisches Polynom mit Nullstellen an den drei Knoten $a, m, b$ ist, gilt exakt $c\,(x-a)(x-m)(x-b) = c\left[(x-m)^3 - \tfrac{h^2}{4}(x-m)\right]$ — beide Summanden und damit die gesamte Abweichung sind \emph{ungerade} Funktionen bezüglich des Intervallmittelpunkts $m$. Ihr Integral über das (um $m$ symmetrische) Intervall verschwindet daher exakt …" — entspricht wörtlich dem Behebungsvorschlag aus Iteration 3. |

**Eigenständige Nachrechnung des Symmetriearguments** (`iter4_blatt6_w1_check.py`, 636 Checks, exakte Bruchrechnung):
1. **Identität:** $(x-a)(x-m)(x-b) = (x-m)^3 - \frac{h^2}{4}(x-m)$ mit $h = b-a$, $m = \frac{a+b}{2}$ — an 200 zufälligen rationalen Tripeln $(a,h,x)$ exakt bestätigt (Substitution $u = x-m$: $u\,(u+\frac h2)(u-\frac h2) = u^3 - \frac{h^2}{4}u$ ✓).
2. **Ungeradheit:** beide Summanden erfüllen $g(m+t) = -g(m-t)$ (je 100 exakte Checks) ✓; Stammfunktion $\frac{u^4}{4} - \frac{h^2}{8}u^2$ ist gerade → Integral über $[m-\frac h2,\, m+\frac h2]$ exakt $0$ (50 Checks) ✓.
3. **Verlangtes Beispiel $\int_0^1 x^3\,dx$:** exakt $\frac14$; Simpson $\frac16[0 + 4\cdot\frac18 + 1] = \frac{1.5}{6} = \frac14$ — **exakt**, deckungsgleich mit Blatt 6, Lösung 8(b) ✓. Quadratischer Lagrange-Interpolant von $x^3$ durch $0, \frac12, 1$ exakt aufgestellt: Abweichung $x^3 - p_2(x) = x(x-\frac12)(x-1) = (x-\frac12)^3 - \frac14(x-\frac12)$ (60 exakte Checks) ✓; Simpson-Quadratur der Abweichung selbst $= 0$ (Nullstellen an den Knoten) ✓.
4. **Gegenprobe zur alten Fassung:** bei $x = \frac14$ beträgt die Abweichung $+\frac{3}{64}$, während $(x-m)^3 = -\frac{1}{64}$ wäre — die alte Aussage war also tatsächlich falsch (sogar Vorzeichen entgegengesetzt), die neue ist exakt ✓.
5. **Allgemein:** Simpson exakt für 60 zufällige Grad-3-Polynome auf zufälligen Intervallen (exakte Bruchrechnung) ✓.

Die Behebung führt **keine neuen Fehler** ein; Kontext (Konstruktion via 8(a), Beispiel 8(b), $\sin$-Gegenbeispiel mit Erratum-11-Verweis $S_2 \approx -0.956788$, Fehler $3.4\cdot10^{-4}$) bleibt stimmig.

---

## KRITISCH

**Keine Befunde.**

## WICHTIG

**Keine Befunde.**

## OPTIONAL

**Keine neuen Befunde.** Aus den Vorrunden bleiben unverändert die bekannten, ausdrücklich zulässigen Stil-/Mikropunkte offen (Teil C: O1–O6, u. a. Blatt 1 ohne Teilpunkt-Aufschlüsselung, `\author`-Feld als Untertitel in Blättern 3–6; Teil D: O1 — Blatt 5, L4(b): angezeigtes Produkt $3(2.0833)(0.0833)$ ergäbe $0.5206$, gedruckt $0.5208$ aus ungerundetem $x_1 = 37/12$; O2 — Blatt 5, L7(b): Summanden $0.2063/0.9085$ folgen dem ungerundeten $x_1$). Alle ohne Einfluss auf Korrektheit, Endwerte oder Bewertbarkeit.

---

## Prüfprotokoll (Auswahl der Positivbefunde)

- **Blatt 6 vollständig neu gerechnet** (153 Checks): Wertetabelle $= e^x$ auf 6 NK exakt ✓; $\tilde I = e^2-1 = 6.389056$ ✓; $M_1 = 5.436564/0.952492$, $T_1 = 8.389056/2.000000$, $S_1 = 19.262184/6 \cdot 2 = 6.420728/0.031672$ ✓; $M_2 = 6.130410/0.258646$, $T_2 = 6.912810/0.523754$, $S_4 = 38.347260/6 = 6.391210/0.002154$ ✓; Quotienten $3.68/3.82/14.7$ ✓, $S_8$-Prognose $1.3\cdot10^{-4}$ vs. tatsächlich $1.38\cdot10^{-4}$ ✓; Monte Carlo: Summe $13.637317$, $\hat I_4 = 6.818659$, Fehler $0.429603$, $\bar f = 3.409329$, alle vier Abweichungen/Quadrate, Summe $12.837297$, Var $4.279099$, $\sigma_f = \mathrm{SE} = 2.068598$, $\mathrm{SE}_{16} = 1.034299$ ✓ (Erratum-15-konform); Lagrange-Gewichte $h/6, 2h/3, h/6$ exakt per Bruchrechnung inkl. der gedruckten Zwischenschritte $(4-9+6)h^3/12$ und $-\frac4{h^2}(-\frac{h^3}{6})$, $\delta_{jk}$-Probe, Summe $=h$ ✓; $N^d$-/Stellen-Rechnungen ($10^{20}$, $10^{11}$ s $\approx 3.2\cdot10^3$ Jahre, $301\,030$ Stellen) ✓; A1(b): $\int$ über volle Periode von $\sin(2\pi t)$ numerisch $0$ ✓, $h = 0.48$/Fig.-33-Deutung deckt Caption S. 60; Schlusshinweis-Errata 7/8/10/11 nachgerechnet ($M_2 = -0.966485/0.010036$; $T_2 = -0.93644/0.02001$; $S_2 = -0.956788/3.4\cdot10^{-4}$) ✓.
- **Blatt 4** (Regressionsteil, 60+ Checks): Newton-$\sqrt5$-Kette exakt als Brüche $3 \to \frac73 \to \frac{47}{21} \to \frac{2207}{987}$ (alle Tabellenspalten, Fehler $7.639\mathrm{e}{-1}/9.727\mathrm{e}{-2}/2.027\mathrm{e}{-3}/9.18\mathrm{e}{-7}$, $C_n = 0.167/0.214/0.223$, Theorie $0.2236$) ✓; Taylor-$\ln$ ($0.1823216/0.0176784/0.0023216$) ✓; Sekante ($2.2 \to 2.2307692 \to 2.2361111$, Fehler $4.3\mathrm{e}{-5}$; Erratum-5-Querbezug $0.528/1.344/1.0706$) ✓; A6 inkl. K1-Fix-Tabelle ($0.250/0.333/0.353/{\approx}0.35$; volle Präzision $0.250/0.333/0.353/0.354$; $C = 1/(2\sqrt2) = 0.3536$; Erratum 14: $|e_3| = 2.124\mathrm{e}{-6}$, $|e_4| = 1.595\mathrm{e}{-12}$, Residuum $4.511\mathrm{e}{-12}$) ✓; A7 ($\pm1/\sqrt3$; $x_1 = -1$ exakt; $N(x) = 2x^3/(3x^2-1)$, Oszillation $\pm1/\sqrt5 = 0.4472136$ mit Iterationsprobe; Erratum-9-Kette $1.4 \to 1.1246 \to 1.0181 \to 1.0005$ monoton von oben) ✓; Erratum-4-Kennzeichnung (Gl. 20) vorhanden ✓.
- **Blatt 5** (Regressionsteil, 60+ Checks): $f(4) = -8.6769$, $f(7) = -2.9549$, $f(5.5) = -1.1413$, Sehnenmittel $-5.8159$ (alle Einzelsummanden) ✓; Konvexitätsbeweis-Identität $\lambda(1-\lambda)(x-y)^2$ ✓; Newton auf $g$ ($3.0833 \to 3.0032$; $0.9167 \to {\approx}0.9968$; $g(1)=5$, $g(3)=1$) ✓; Random Restarts ($0.803$; $K=29$; $0.832$; $K=14$ mit Proben $0.956/0.945$; $90/459$; alle $\ln$-Werte) ✓; Annealing-Tabelle ($0.779/0.368/0.0067/0.905/0.301$) ✓; $|f''|$-Trick ($-1.092/-2.92$; $-0.0740$ bergauf $-0.0109$; $0.6740$ bergab $-0.7022$) ✓; Shekel bei $7.2$: alle sechs Summanden, $f' = 2.3777$ (angezeigte Summe; exakt $2.377766 \to$ im Blatt deklariert „exakter Wert $2.3778$"), $f'' = 7.1381$ (exakt $7.138077$), $x_1 = 6.8669 \approx 6.87$ = Skript S. 49 ✓; Basin-Grenzen numerisch als echte lokale Maxima bei $1.6852/5.6815 \to 1.7/5.7$, $P = 1.7/6 \approx 28\,\%$ ✓; Erratum-6-Fußnote korrekt ✓.
- **Blätter 1–3** (Regressionsteil, 124 Checks): B1 — Gitter/Komplexität, Grid-Search-Tabellen (alle 9 bzw. 7 Zeilen), $3\times3$-System exakt $(-\frac{76}3, \frac23, \frac{64}3)$ mit allen Proben, $w^\ast = \frac{25}{14}$, $L(w^\ast) = \frac5{14}$, Fehler $\frac3{14}/\frac9{14}$ ✓; B2 — $\frac1{3000}$, IEEE-754-De-/Kodierung ($-13.0$; $6.25 \to s{=}0, E{=}10000001_2$, 23-Bit-Mantissen nachgezählt), Machine-Epsilon-Werte, Zehnerpotenzen binär ($E = 130/133/136$), Fixed-Point ($10^9 < 2^{31}{-}1 < 10^{10}$), Auslöschung beider Paare (je 100 % rel. Fehler), $\mathrm{fl}(1+10^{-20}) - 1 = 0$ maschinell, Underflow $10^{-50} \to 0$ in float32 maschinell, Overflow $10^{40} > $ float32-Max ✓; B3 — alle 11 Tabellenwerte $\cos$ auf 5 NK exakt, $\kappa$-Werte ($0.00414/0.06569/0.24899/0.24458$), Stabilität ($0$ bzw. $0.17235/0.25 = 0.6894$ mit Nächste-Gitterpunkt-Logik), Konsistenz/Konvergenz ($0.01001/0.00171$; $0.01001/0.03320$), Beweisaufgabe-Grenzfolge $0 \to 0.17235 \to 0.21202 = \kappa(2,+0.25)$, $\cos(\pi{+}0.25) = -0.96891 \to 0.03109 \approx 0.031$ (konsistent zu A3) ✓; Erratum-1-Zitat $0.15853$ mit Kennzeichnung ✓.
- **Skript-/Errata-Treue:** Alle Seiten- und Gleichungsverweise (Gl. 1–51, Tabellen 1–3, Algorithmen 1–4, Randnotizen inkl. „Show it" S. 31, Bias-Notiz S. 29, „Stop at Simpson"/Tabelle 3 S. 64, Midpoint-als-MC-Randnotiz S. 65, „What if"-Randnotiz S. 59, Fig.-33-Caption $h = 0.48$ S. 60, SGD-Randnotiz $n/b$ S. 65, Patience S. 51, DL-Hoffnungen S. 53, Basin-Übung S. 55) gegen das vollständig gelesene PDF S. 9–70 geprüft — stimmig. Kein Blatt übernimmt einen der 15 dokumentierten Originalfehler; alle einschlägigen Errata (1, 2, 4–12, 14, 15 sowie die Geringfügig-Punkte S. 36/49/65/66) sind korrekt umgesetzt bzw. als „[Korrektur ggü. Original, S. n]" gekennzeichnet.
- **Struktur:** Lösungen in allen sechs Blättern strikt nach `\newpage` (B1 Z. 190, B2 Z. 139, B3 Z. 174, B4 Z. 212, B5 Z. 255, B6 Z. 143); `\label{auf:N}`/`\ref` durchgängig aufgelöst (0 Warnungen in allen Logs, inkl. Vorwärtsreferenzen B4-A5/A6→A8); keine Lösungsleaks im Aufgabenteil (Vorgabedaten in B4-A6b, B5-A8c, B6-A8a sind deklarierte Aufgabendaten); deklarierter Schwierigkeitsanstieg und Hilfsmittelangaben vorhanden; Wertetabellen decken alle benötigten Stützstellen.
- **Hinweis zu 4 anfänglichen Prüf-Flags:** Meine erste automatische Prüfung meldete vier Abweichungen (B4-A3 $f(x_1)/f(x_2)$-Spalten, B4-A3 $C_2$, B5-A8b $f'(7.2)$-Summe). Nachprüfung mit exakter Bruchrechnung ergab: alle vier Blatt-Angaben sind korrekt — die Blätter rechnen die $f$-Spalten und $|e_3|$ konsistent aus den **ungerundeten** Werten ($\frac49 = 0.4444444$, $\frac4{441} = 0.0090703$, $x_3 = \frac{2207}{987} \Rightarrow |e_3| = 9.18\cdot10^{-7}$, $C_2 = 0.223$ aus den gedruckten Fehlern), und B5 summiert deklariert die angezeigten gerundeten Summanden ($0.0052 + 0.0998 + 2.2727 = 2.3777$) bei gleichzeitig ausgewiesenem exakten Wert $2.3778$. Keine Befunde.

---

## Zusammenfassende Bewertung

| Kriterium | Befund |
|---|---|
| Iteration-3-Auflage (W1, Blatt 6 L8c) | **Behoben** — wortgleich mit Behebungsvorschlag, Identität/Ungeradheit/Integral exakt nachgerechnet, Beispiel $\int_0^1 x^3$ via Simpson exakt $\frac14$ |
| Änderungsumfang seit It. 3 | Nur Blatt 6 Z. 304; Blätter 1–5 nachweislich unverändert; keine Regressionen |
| Korrektheit aller Musterlösungen | 1047 automatisierte Checks über alle 48 Aufgaben, 0 Fehlschläge; Beweise/Herleitungen handgeprüft |
| Punktsummen | 40/38/50/50/50/57 ✓ (Teilpunkte aufgehend) |
| Struktur/Kompilat | 6 × `pdflatex` OK (2 Läufe), 0 Fehler/Warnungen/unaufgelöste Referenzen; `\newpage`-Trennung, keine Lösungsleaks |
| Skript-/Errata-Treue | Alle Verweise gegen PDF S. 9–70 verifiziert; kein Originalfehler übernommen, alle Korrekturen gekennzeichnet |

**Befundzahlen Iteration 4: 0 × KRITISCH, 0 × WICHTIG, 0 × neue OPTIONAL** (Alt-OPTIONAL aus den Vorrunden bleiben als zulässige Stilnotizen dokumentiert). **Behebungsstatus: 1/1 Auflage aus Iteration 3 behoben.**

## Freigabe-Urteil: **JA — alle sechs Übungsblätter sind ohne Auflagen freigegeben.**

Die Serie ist frei von KRITISCH- und WICHTIG-Befunden, fachlich korrekt, vorgabenkonform, kompiliert sauber und kann in der vorliegenden Form ausgegeben werden.
