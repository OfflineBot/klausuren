# Review-Iteration 2 — konsolidiert

Datum: 2026-06-12. Vier frische Reviewer, vollständige Neuprüfung + Regressionscheck Iteration 1.
Bilanz: KRITISCH 2 · WICHTIG 2 · OPTIONAL 17. Behebungsstatus It. 1: alle KRITISCH/WICHTIG-Punkte verifiziert behoben (2 kleine Folgefehler, siehe 2A-K1, 2D-O1).

# Review Iteration 2 — Teil A (Themen 1–3)

**Reviewer-Vorgehen:** Vollständige Neuprüfung ohne Vorwissen über die Entstehung. Original-PDF S. 1–34 vollständig gelesen (Read, pages 1–18 und 19–34) und Seite für Seite gegen `zusammenfassung.tex` (inkl. neuer Einleitung) sowie `sections/thema_1.tex`–`thema_3.tex` abgeglichen. Jede Formel, jede Tabellenzeile und jeder Zahlenwert unabhängig nachgerechnet (Python-Skript `/tmp/review_calc/verify2.py`): alle 25 Zeilen der Grid-Search-Tabelle, Substitutionslösung samt Verifikation, alle sin-Werte, Binär-/Bias-Darstellungen (130/133/136), 2-Bit-Mantisse, ε_mach-Werte, log₁₀(2¹²⁸) ≈ 38.5, alle κ-, s-, c- und Konvergenzwerte inkl. Gitter-Snapping (−0.75→−0.8, −0.95→−1) und Gitterpunktmengen beider Schrittweiten. Alle Gleichungsnummern (Gl. 1–19) und Seitenreferenzen einzeln geprüft — alle korrekt. Kompiliertest: `pdflatex` läuft fehlerfrei durch (61 Seiten, keine Errors, keine undefined references). Zusätzlich: Regressionscheck aller 10 Befunde aus `review_iteration_1_teilA.md` und Gegenprüfung der einschlägigen Errata-Einträge (Nr. 2, 12 sowie Geringfügig-Eintrag „κ ≤ 0.247") — die Errata-Einträge selbst sind korrekt.

---

## KRITISCH

### K1 — Thema 3: Faktisch falsche Behauptung „Das numerische Minimum des 0.2er-Gitters liegt bei −1.2" (neuer Fehler, durch den Fix von Iteration-1-K2 eingeführt)
- **Datei/Fundstelle:** `output/sections/thema_3.tex`, Z. 127 (Konvergenzbox, h=0.2: „Das numerische Minimum des $0.2$er-Gitters liegt bei $-1.2$; …") und Folgestelle Z. 131 (Korrektur-Anmerkung: „… Auswertung am ungestörten **Minimum**, Wert $0.06796$ …").
- **PDF-Seite:** S. 32 (Konvergenzblock h=0.2; das PDF schreibt dort kommentarlos f̂₁(−1.2), ohne −1.2 als Minimum zu bezeichnen).
- **Beschreibung:** Die Aussage ist nachrechenbar falsch: Das Grid-Search-Minimum des h=0.2-Gitters auf [−3,1] liegt bei **x = −1.6** mit sin(−1.6) ≈ **−0.99957** (Gitterpunkte …,−1.6,−1.4,−1.2,…; sin(−1.2) = −0.93204 > sin(−1.4) = −0.98545 > sin(−1.6)). Analog wäre das numerische Minimum bei h=1 der Punkt −2 (Kapitel-1-Ergebnis −0.9093), nicht −1. Der Punkt −1.2 ist lediglich der Gitterpunkt, den das **Skript** −π/2 zuordnet — genau das stellt die eigene „Anmerkung zur Gitterpunkt-Zuordnung" (Z. 112) korrekt und transparent fest („die Zuordnung … wird im Original nicht erklärt"). Die Konvergenzbox widerspricht also der eigenen Anmerkung 15 Zeilen weiter oben und erfindet erneut eine Begründung, die die Rechnung nicht trägt — derselbe Fehlertyp, der in Iteration 1 als K3 kritisiert wurde (dort „nächster Gitterpunkt", hier „numerisches Minimum"). Eingeführt wurde der Satz erst mit dem Fix von Iteration-1-K2; die Rechenkette selbst ist davon nicht betroffen (alle „="-Glieder sind jetzt korrekt: −0.95 → Gitterpunkt −1 → 0.15853 ✓).
- **Vorschlag:** Z. 127 umformulieren zu: „Ausgangspunkt ist der Gitterpunkt $-1.2$, dem das Skript $-\pi/2$ zuordnet (vgl. Anmerkung zur Gitterpunkt-Zuordnung oben); die gestörte Eingabe ist $\tilde{x} = -1.2 + 0.25 = -0.95$, und diese fällt beim Auswerten auf den Gitterpunkt $-1$." In Z. 131 „(Auswertung am ungestörten Minimum, …)" ersetzen durch „(Auswertung am ungestörten Bezugspunkt $-1.2$, …)".

---

## WICHTIG

### W1 — Einleitung: Paraphrase weicht inhaltlich von der Introduction (S. 7) ab; unmarkierter Zusatz
- **Datei/Fundstelle:** `output/zusammenfassung.tex`, Z. 58.
- **PDF-Seite:** S. 7.
- **Beschreibung:** Zwei Punkte: (a) „sowie verschiedene numerische Techniken **etwa zur Nullstellensuche, Optimierung und Integration**" — die Beispielaufzählung steht nicht auf S. 7 (dort nur „various numerical techniques"); sie ist zwar aus dem Inhaltsverzeichnis ableitbar und sachlich richtig, aber entgegen der eigenen Kennzeichnungspolitik nicht als [Ergänzung] markiert. (b) „Ziel ist, dass man numerische Verfahren nicht nur anwenden, sondern ihr Verhalten — Genauigkeit, Zuverlässigkeit, Grenzen — verstehen und beurteilen kann." — Das Original formuliert das Ziel anders: „to equip you with the skills needed to **implement reliable and efficient algorithms in scientific computing and engineering applications**." Die Implementierungs-/Scientific-Computing-Dimension fällt weg und wird durch eine nicht belegte „verstehen und beurteilen"-Aussage ersetzt; ein Leser ordnet diese Zielbeschreibung fälschlich dem Skript zu.
- **Vorschlag:** Beispielaufzählung als „[Ergänzung]" kennzeichnen (oder streichen); Zielsatz am Original ausrichten, z. B.: „Ziel ist, die Fähigkeiten zu vermitteln, zuverlässige und effiziente Algorithmen im Scientific Computing und in Ingenieursanwendungen zu implementieren."

---

## OPTIONAL

### O1 — Thema 2: Verortung des Blow-ups in Figure 8 („nahe 10⁻¹⁶·⁵, also um das double-precision-Epsilon")
- **Datei/Fundstelle:** `output/sections/thema_2.tex`, Z. 211. **PDF-Seite:** S. 23.
- **Beschreibung:** 10⁻¹⁶·⁵ ≈ 3.2·10⁻¹⁷ liegt einen Faktor ~7 unter ε_mach ≈ 2.2·10⁻¹⁶ (und ~3.5 unter der eigentlichen Rundungsschwelle ε_mach/2 ≈ 1.1·10⁻¹⁶, ab der 1+ε im Speicher exakt 1 wird). Die Lagebeschreibung passt zur gedruckten Figur, die Gleichsetzung „also um das double-precision-Epsilon" ist aber um etwa eine halbe Größenordnung unscharf. Der [Ergänzung]-Mechanismus (Nenner löscht zu 0 aus) ist korrekt.
- **Vorschlag:** Präzisieren: „für ε unterhalb von ε_mach/2 ≈ 1.1·10⁻¹⁶ (in der Figur ab ca. 10⁻¹⁶·⁵)".

### O2 — Fußnoten innerhalb der tcolorboxen (Carry-over aus Iteration 1, O1)
- **Datei/Fundstelle:** `thema_1.tex` Z. 137; `thema_2.tex` Z. 43, Z. 68 (zwei Fußnoten). Unverändert: Box-Fußnoten erscheinen mit Buchstabenmarken am Boxrand statt am Seitenfuß. Inhalt geht nicht verloren; bewusst so belassen ist vertretbar.

### O3 — Rest-Formatinkonsistenzen Thema 3 (Carry-over aus Iteration 1, O2 — teilbehoben)
- **Datei/Fundstelle:** `thema_3.tex` durchgängig. Sektionstitel ist jetzt vereinheitlicht („Error Analysis (Fehleranalyse) (S.~25--34)") ✓; weiterhin abweichend: `[nosep]` statt `[itemsep=1pt]`, Gedankenstrich „—" statt „--", `\tag{Gl.~13}`-Nummerierung statt Fließtext-Nennung, Lernziele als itemize statt enumerate. Rein kosmetisch.

### O4 — Abbildungen nur textlich referenziert (Carry-over aus Iteration 1, O4)
- **Datei/Fundstelle:** alle drei Themen. Figures 1–13 werden weiterhin nur beschrieben (jeweils korrekt und in 1–2 Sätzen); keine TikZ-Reproduktionen ergänzt. Nice-to-have, kein Mangel.

---

## Behebungsstatus Iteration 1

| Befund It. 1 | Status | Verifikation |
|---|---|---|
| K1 (Konsistenz h=0.2: −0.94898/0.05102 falsch) | **behoben** | `thema_3.tex` Z. 108–110: sin(−1.2) = −0.93204, c₀.₂ ≈ 0.06796, korrekt als [Korrektur ggü. Original, S. 32] gekennzeichnet; nachgerechnet ✓. Befund-Satz (Z. 114) und merkbox (Z. 160) angepasst ✓. Erratum Nr. 12 in `errata_original_pdf.md` aufgenommen und korrekt ✓. |
| K2 (Konvergenzkette h=0.2: falsches „=") | **behoben, aber Folgefehler** | Falsches Kettenglied f̂₀.₂(−1.2) aus der „="-Kette entfernt; verbleibende Kette −0.95 → −1 → 0.15853 ist mathematisch korrekt (nachgerechnet ✓); redaktionelle Klarstellung in Z. 131 vorhanden und zutreffend. **Aber:** Der neu eingefügte Erklärsatz „numerisches Minimum bei −1.2" ist faktisch falsch → neuer Befund K1 dieser Iteration. |
| K3 (falsche „nächster Gitterpunkt"-Begründung) | **behoben** | Neutral formuliert („das Skript ordnet … zu", Z. 106/108) plus transparente Anmerkung Z. 112 (nächste Gitterpunkte wären −2 bzw. −1.6 — nachgerechnet ✓). |
| W1 (Motto/Introduction fehlen) | **behoben** | `zusammenfassung.tex` Z. 49–58: Abschnitt „Einleitung (S. 3–7)" mit Motto-Zitat (wörtlich korrekt, S. 3 ✓) und Introduction-Zusammenfassung; im TOC verankert. Rest-Paraphrasefehler → neuer Befund W1 dieser Iteration. |
| W2 (κ ≤ 0.247 unkorrigiert) | **behoben** | `thema_3.tex` Z. 77: κ ≈ 0.2474 mit [Korrektur ggü. Original, S. 31] und korrekter Doppelbegründung (numerisch + konzeptionell) ✓. |
| W3 (unmarkierte Zusätze) | **behoben** | Tabellenspalte „Präzision [Ergänzung]" + Klarstellung „signifikante Dezimalstellen" (`thema_2.tex` Z. 54, 57–58, 63) ✓; Figure-8-Kausalerklärung als [Ergänzung] markiert (Z. 211) ✓; Stabilitäts-Pointe als [Ergänzung] markiert (`thema_3.tex` Z. 18) ✓. |
| O1 (Box-Fußnoten) | **nicht behoben** (optional; als O2 weitergeführt) |
| O2 (Stil Thema 3) | **teilweise behoben** (Sektionstitel vereinheitlicht; Rest als O3 weitergeführt) |
| O3 (zwei Marginalien) | **behoben** | Autoren-Aufruf S. 27 in `thema_3.tex` Z. 20 erwähnt ✓; „Is double enough?" als Marginalientitel in `thema_2.tex` Z. 232 ergänzt ✓. |
| O4 (TikZ-Abbildungen) | **nicht behoben** (optional; als O4 weitergeführt) |

---

## Zusammenfassung der Befunde

| Kategorie | Anzahl |
|---|---|
| KRITISCH | 1 |
| WICHTIG | 1 |
| OPTIONAL | 4 |

**Positivbefund:** Die drei kritischen und drei wichtigen Punkte aus Iteration 1 sind sämtlich umgesetzt; die Korrekturen sind fachlich richtig, korrekt gekennzeichnet und in der Errata-Liste nachgeführt. Vollständigkeit Themen 1–3 gegen PDF S. 1–34: lückenlos (alle Definitionen, Gl. 1–19, beide Tabellen, alle Figures 1–13 textlich, alle Marginalien inkl. Meta-Notizen, alle Übungs- und Selbstreflexionsfragen, Recaps, Teaser, Überleitungen; Motto und Introduction jetzt abgedeckt). Sämtliche Zahlenwerte unabhängig nachgerechnet — bis auf den unter K1 beschriebenen neuen Erklärsatz keine Rechen- oder Übertragungsfehler. Gleichungsnummern und Seitenreferenzen: alle korrekt. Dokument kompiliert fehlerfrei (61 Seiten). Der einzige KRITISCH-Punkt ist ein lokal begrenzter, durch einen Iteration-1-Fix eingeschleppter Erklärsatz; die Rechenketten selbst sind durchgängig korrekt.

*Hinweis: Durch den Kompiliertest liegen LaTeX-Hilfsdateien (`zusammenfassung.aux/.log/.toc/.out/.pdf`) im `output/`-Ordner.*
# Review Iteration 2 — Teil B (Themen 4–6)

Reviewer: unabhängige Neuprüfung (Iteration 2) ausschließlich anhand der Dateien (Original-PDF S. 35–71 vollständig gelesen, `errata_original_pdf.md`, `review_iteration_1_teilB.md`, `thema_4/5/6.tex`, `zusammenfassung.tex`). Alle Formeln, Herleitungen und Zahlenwerte wurden eigenständig nachgerechnet (Python, `/tmp/review_calc/`); der Seitenabgleich erfolgte lückenlos. Zusätzlich Compile-Regressionstest: `pdflatex zusammenfassung.tex` läuft fehler- und warnungsfrei durch (61 Seiten).

**Gesamtbild:** Die drei Kapitel sind vollständig (Gl. 20–51 sämtlich vorhanden, Algorithmen 1–4, Tabellen 2 und 3, alle Beispiele, alle Übungs- und Selbstreflexionsfragen, alle Abbildungsverweise 14–38, alle relevanten Randnotizen). Sämtliche [Korrektur ggü. Original]-Stellen wurden nachgerechnet und sind korrekt — insbesondere die in der Aufgabenstellung genannten Werte: Newton-Kette 1.1246 → 1.0181 → 1.0005 ✓, Sekante 1.0706 → 1.0272 → 1.0026 → 1.0001 ✓, Tabelle 2 |e₃| = 2.124×10⁻⁶ → 2.12×10⁻⁶ ✓ und |e₄| = 1.595×10⁻¹² ≈ 1.6×10⁻¹² ✓ (Residuum |f(x₄)| = 4.51×10⁻¹² ✓, Konsistenzcheck C = 1/(2√2) = 0.3536, 0.354·(2.12×10⁻⁶)² = 1.60×10⁻¹² ✓), Glättung f(−0.5) = −0.47943 / f(−0.3) = −1.24658 / Integral −0.17260 / geglättet −0.86300 ✓, T₂ = −0.93644 (Fehler 0.02001) ✓, S₂ = −0.956788 (Fehler 3.39×10⁻⁴) ✓, Midpoint n=2 = −0.966485 (Fehler 0.010036) ✓, MC-Varianz 0.009053/3 = 0.003018, σ_f = 0.05493, SE = 0.02747 ✓ (inkl. der vier ausgewiesenen Abweichungsquadrate 0.0000030/0.0052638/0.0002093/0.0035770 ✓). Alle acht Befunde aus Iteration 1 sind behoben, ohne neue Fehler einzuschleppen. Es verbleiben ein Policy-Befund (unmarkierte Abweichung bei Gl. 47) und vier Kleinigkeiten.

---

## KRITISCH (0 Befunde)

— keine. Alle Herleitungen (Gl. 20–34: Newton/Taylor/Konvergenz; Gl. 35–41: Shekel/Restarts/Newton-Optimierung; Gl. 42–51: Quadratur/Monte Carlo) und alle Zahlenwerte wurden unabhängig nachgerechnet und sind korrekt; keine fachlichen Fehler, keine unverifiziert übernommenen Originalfehler mit inhaltlicher Tragweite.

---

## WICHTIG (1 Befund)

### W1. Thema 6: Gl. (47) stillschweigend gegenüber dem Original geändert (Î_N statt I) — Abweichung nicht gekennzeichnet
- **Datei/Fundstelle:** `output/sections/thema_6.tex`, Satzbox „Integral als Erwartungswert und Monte-Carlo-Schätzer“ (Z. 369–374).
- **PDF-Referenz:** S. 65, Gl. (47).
- **Beschreibung:** Das PDF druckt Gl. (47) als „$I = \frac{|\Omega|}{N}\sum_{i=1}^N f(\mathbf{X}_i)$“ — links steht (fälschlich) das exakte Integral $I$, obwohl rechts der Schätzer steht. Die Zusammenfassung schreibt korrekt „$\hat{I}_N = \ldots$“ (konsistent mit Gl. 48, die im PDF selbst $\hat{I}_N$ verwendet), kennzeichnet diese Abweichung aber nicht. Inhaltlich ist die Änderung richtig und sogar geboten; sie verstößt jedoch gegen die Projektpolicy „fachlich korrekte Version verwenden, Abweichung als [Korrektur/Anm.] kennzeichnen“ — wer mit dem PDF vergleicht, findet eine unerklärte Diskrepanz, was das Vertrauen in das Markierungssystem untergräbt.
- **Behebung:** Kurze Anmerkung ergänzen, z. B. „[Anm.: Das PDF schreibt links $I$; gemeint ist der Schätzer $\hat{I}_N$ — das exakte Integral $I$ ist Gl. (46), und Gl. (48) des Skripts verwendet selbst $\hat{I}_N$.]“ Optional als Geringfügiges in `errata_original_pdf.md` aufnehmen.

---

## OPTIONAL (4 Befunde)

### O1. Thema 5: Newton-Iterate „x₃ ≈ 7.00“ aus dem PDF übernommen; exakt ist x₃ = 6.9907 (→ 6.99)
- **Datei/Fundstelle:** `output/sections/thema_5.tex`, Beispielbox „Newton auf der Shekel-Funktion ab x₀ = 7.2“ (Z. 119–124).
- **PDF-Referenz:** S. 49.
- **Beschreibung:** Eigenständige Nachrechnung der Newton-Iteration auf f′: x₁ = 6.8669 (✓ ≈ 6.87), x₂ = 7.0155 (✓ ≈ 7.02), aber x₃ = 6.9907 — auf zwei Dezimalen 6.99, nicht 7.00. Die Wurzel von f′ (das lokale Minimum) liegt wegen der Überlappung der drei Foxhole-Terme bei x ≈ 6.9907, nicht exakt bei 7. Die qualitative Kernaussage („konvergiert zum lokalen Minimum x° ≈ 7“) bleibt uneingeschränkt richtig.
- **Behebung:** Entweder unverändert lassen (≈-Angabe vertretbar) oder Fußnote: „exakt x₃ ≈ 6.9907; das Minimum liegt durch die Termüberlappung knapp unterhalb von 7“. Errata-Kandidat (Rubrik Geringfügiges).

### O2. Thema 4: Grid-Search-Wert f(2.5) ≈ 0.599 aus dem PDF übernommen; korrekt gerundet 0.598
- **Datei/Fundstelle:** `output/sections/thema_4.tex`, Beispielbox „Grid Search zur Nullstellensuche“ (Z. 24).
- **PDF-Referenz:** S. 36.
- **Beschreibung:** sin(2.5) = 0.598472 → auf drei Dezimalen 0.598; das PDF (und die Zusammenfassung) drucken 0.599. Alle übrigen fünf Gitterwerte sind korrekt gerundet. Letzte-Stelle-Fehler ohne jede Folgewirkung.
- **Behebung:** 0.598 mit Mini-Marker, oder belassen; Errata-Kandidat (Geringfügiges).

### O3. Thema 6: MC-Sample f(X₁) = sin(−1.95) ≈ −0.92895 übernommen; korrekt gerundet −0.92896
- **Datei/Fundstelle:** `output/sections/thema_6.tex`, Beispielbox „Monte Carlo von Hand“ (Z. 546).
- **PDF-Referenz:** S. 67.
- **Beschreibung:** sin(−1.95) = −0.9289597 → −0.92896; PDF/Zusammenfassung: −0.92895 (letzte Stelle). Alle Folgewerte (Mittel −0.927228, Fehler 0.02922, Varianzrechnung) sind mit dem gedruckten Wert konsistent gerechnet und auf der angegebenen Genauigkeit unverändert. Da die Samples ohnehin „angenommen“ sind, ist das praktisch bedeutungslos.
- **Behebung:** Belassen oder Fußnote; Errata-Kandidat (Geringfügiges).

### O4. Thema 6: „Simpson exakt für quadratische Polynome“ (Definitionsbox) vs. „exakt bis Grad 3“ (S₂-Korrekturbox) — kleine Brücke fehlt
- **Datei/Fundstelle:** `output/sections/thema_6.tex`, Defbox „Simpson-Regel“ (Z. 201–206) vs. S₂-Box (Z. 530).
- **PDF-Referenz:** S. 63 bzw. Erratum 11.
- **Beschreibung:** Die Defbox gibt (originalgetreu) „exakt für quadratische Polynome“ wieder; die S₂-Korrektur sagt später korrekt „exakt für Polynome bis Grad 3“. Beides ist wahr (Grad ≤ 2 ⊂ Grad ≤ 3), aber ein Lernender könnte die Angaben als Widerspruch lesen.
- **Behebung:** Eine Zeile [Ergänzung] in der Defbox: „durch Symmetrie sogar exakt bis Grad 3“.

---

## Behebungsstatus Iteration 1 (8/8 behoben, keine Regressionen)

| Befund It. 1 | Status | Verifikation |
|---|---|---|
| **K1** Glättungsbeispiel S. 59 (falsche Stützwerte) | **BEHOBEN** | `thema_6.tex` Z. 67–103: f(−0.5) = −0.47943, f(−0.3) = −1.24658, Integral −0.17260, geglättet −0.86300 — alle vier Werte nachgerechnet ✓; [Korrektur ggü. Original, S. 59] gesetzt; Fehlbeschriftung (−1.14973 = f(−0.2), −0.97720 = f(−0.4)) erklärt ✓ (nachgerechnet: f(−0.2) = −1.149726 ✓); Schlussfolgerung („höhere Losses“, −0.86300 > −0.97720) jetzt in sich stimmig ✓; Erratum 13 nachgetragen ✓ |
| **K2** Tabelle 2, Zeilen n = 3/4 | **BEHOBEN** | `thema_4.tex` Z. 165–184: 2.12×10⁻⁶ und 1.6×10⁻¹² eingesetzt (nachgerechnet: 2.124×10⁻⁶, 1.595×10⁻¹² ✓), Residuum-Erklärung (4.51×10⁻¹² = |f(x₄)| ✓) und Konsistenzcheck C ≈ 0.354 korrekt ✓; Marker gesetzt; Erratum 14 nachgetragen ✓; Merkbox-Eintrag konsistent ✓ |
| **W1** MC-Varianz/SE | **BEHOBEN** | `thema_6.tex` Z. 568–596: vier Abweichungsquadrate ausgewiesen (alle vier nachgerechnet ✓), Summe 0.009053 ✓, σ_f² = 0.003018, σ_f = 0.05493, SE = 0.02747 ✓; Marker gesetzt; [Ergänzung] korrekt auf 0.02747 angepasst ✓; Erratum 15 nachgetragen ✓ |
| **W2** Simpson-h-Konvention | **BEHOBEN** | `thema_6.tex` Z. 231–267: h := b − a durchgängig definiert, „m − a = b − m = h/2“ korrekt, Konventions-Anmerkung zur Composite-Lesart (h/3-Paar-Formel) sachlich richtig ✓; kein Widerspruch mehr in der Box; konsistent mit Composite-Herleitung (h/3 ✓) und Merkbox ✓ |
| **W3** Gl. (48) „für N → ∞“ | **BEHOBEN** | `thema_6.tex` Z. 390–398: klarstellende Anmerkung (Erwartungstreue für jedes endliche N, N → ∞ betrifft Konsistenz) vorhanden und fachlich korrekt ✓ |
| **O1** Figure 25 unreferenziert | **BEHOBEN** | `thema_5.tex` Z. 116–118: Figure 25 [S. 49] mit korrekter Inhaltsangabe (f′ schwarz, f″ grau gestrichelt, f″ > 0 an Minima) referenziert ✓ |
| **O2** Figure 37 unreferenziert / defekte Caption | **BEHOBEN** | `thema_6.tex` Z. 376–380: Figure 37 erwähnt, Copy-Paste-Fehler der Original-Caption (identisch mit Figure 34) angemerkt ✓ |
| **O3** Rundungs-Inkonsistenz 0.305/0.3044 | **BEHOBEN** | `thema_4.tex` Z. 249: jetzt einheitlich „≈ 0.297 / 0.2977 / 0.304“ (nachgerechnet: f(1.1246) = 0.29771, f(1.127) = 0.30444 ✓) |

**Regressionscheck:** Die Fixes haben keine neuen Fehler eingeführt. Alle umgebenden Zahlen und Aussagen der geänderten Boxen erneut nachgerechnet (u. a. Newton-/Sekanten-Zwischenwerte f, f′ in jeder Iteration; T₂-Klammer −3.74575; S₂-Klammer −5.74073; Midpoint-Fehlervergleich 0.04104 vs. 0.010036; SE-zu-Fehler-Vergleich 0.02747 vs. 0.02922). Dokument kompiliert fehlerfrei (pdflatex, exit 0, keine Warnings, 61 Seiten).

## Explizite Negativ-Befunde (geprüft, in Ordnung)

- **Vollständigkeit:** Gl. 20–51 sämtlich vorhanden, korrekt nummeriert und paginiert; Algorithmen 1–4 zeilengetreu (inkl. „end whilereturn“-Hinweis); Tabellen 2 und 3 vollständig; alle Beispiele, alle Übungen (4/13/7 Items) und Selbstreflexionsfragen (4/6/9); Figures 14–38 alle referenziert; Randnotizen inkl. Sade-Zitat, Backprop, Noisy Newton, Δf, CS231n, Code-Links abgedeckt. — keine Befunde.
- **Korrektheit:** Alle Handrechnungen beider PDF-Seitenbereiche unabhängig reproduziert (Grid Search, sin-Newton, √2-Tabelle inkl. Residuen, x³−x Newton+Sekante, Shekel f′/f″/Iterate, P = 0.803, K = 28.34 → 29, 1−0.9²⁰ = 0.878, Glättung, Ĩ = −0.9564491, Midpoint n=1/2, T₂, S₂, MC inkl. Varianz). — keine Befunde über W1/O1–O3 hinaus.
- **Didaktik:** Motivation, Lernziele, Boxen-Systematik, durchgerechnete Beispiele, Merkboxen mit Fehlerquellen/Merksätzen in allen drei Themen; ohne Originalvorlesung verständlich. — keine Befunde über O4 hinaus.
- **Präambel/Build:** Alle verwendeten Konstrukte (tcolorbox-Optionen, algpseudocode, booktabs, enumitem, \glqq, \url, \boldsymbol, \overset) durch die Präambel gedeckt; Labels `alg:randomrestarts`/`alg:basinhopping` aufgelöst. — keine Befunde.

## Empfohlene Nachträge zur Errata-Liste (Rubrik „Geringfügiges“)

1. **[S. 65, Gl. 47]** Linke Seite müsste $\hat{I}_N$ heißen, nicht $I$ (siehe W1).
2. **[S. 49]** x₃ der Newton-Optimierungskette ist 6.9907 (≈ 6.99), gedruckt 7.00; Minimum liegt bei x ≈ 6.9907 (siehe O1).
3. **[S. 36]** f(2.5) = 0.598 (gedruckt 0.599) (siehe O2).
4. **[S. 67]** sin(−1.95) = −0.92896 (gedruckt −0.92895); Folgewerte konsistent (siehe O3).
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
