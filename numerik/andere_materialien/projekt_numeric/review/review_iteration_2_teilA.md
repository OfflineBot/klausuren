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
