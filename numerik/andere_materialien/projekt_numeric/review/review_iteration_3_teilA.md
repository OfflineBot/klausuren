# Review Iteration 3 — Teil A (Themen 1–3), finale Prüfrunde

**Reviewer-Vorgehen:** Vollständige Neuprüfung ohne Vorwissen über die Entstehung. Original-PDF S. 1–34 vollständig gelesen (Read, pages 1–18 und 19–34) und Seite für Seite gegen `output/zusammenfassung.tex` (inkl. Einleitung) sowie `output/sections/thema_1.tex`–`thema_3.tex` abgeglichen. Sämtliche Rechnungen unabhängig nachgerechnet (Python-Skript `/tmp/review_calc/verify3.py`, 49 Einzelchecks): Substitutionslösung samt Verifikation, alle 25 Zeilen der Grid-Search-Tabelle inkl. Minimum (w=0, b=10, Fehler 4), alle sin-Werte, Approximationsfehler 0.0907, Binär-/Bias-Darstellungen (130/133/136), log₁₀(2¹²⁸) ≈ 38.5, 2-Bit-Mantisse, ε_mach-Werte (2⁻²³ ≈ 1.19·10⁻⁷, 2⁻⁵² ≈ 2.22·10⁻¹⁶), Fixed-Point-Präzision, beide Loss-of-Significance-Beispiele, alle κ-, s- und c-Werte, beide Konvergenzketten inkl. Gitter-Snapping (−0.75→−0.8 bzw. −1; −0.95→−1), Gitterpunktmengen beider Schrittweiten (−1.25 ∉ 0.2er-Gitter, −1.2 ∈ 0.2er-Gitter), nächste Gitterpunkte zu −π/2 (−2 bzw. −1.6), Grid-Search-Minimum des 0.2er-Gitters (−1.6). Alle Gleichungsnummern (Gl. 1–19), Figure-Nummern (1–13) und Seitenreferenzen einzeln geprüft — alle korrekt. Einschlägige Errata-Einträge (Nr. 1, 2, 12 sowie Geringfügig-Eintrag „κ ≤ 0.247") gegen S. 30–32 gegengeprüft — die Errata sind korrekt. Kompiliertest: `pdflatex` läuft fehlerfrei durch (61 Seiten, keine Errors, keine undefined references). Regressionscheck aller 6 Befunde aus `review_iteration_2_teilA.md` durchgeführt; Fokusprüfung Konsistenz- vs. Konvergenzbox in `thema_3.tex` (zweimal nachgebesserte Stelle) im Detail.

---

## KRITISCH

Keine Befunde.

(Insbesondere: Der Iteration-2-Befund K1 — die faktisch falsche Behauptung „Das numerische Minimum des 0.2er-Gitters liegt bei −1.2" — ist vollständig und ohne neuen Folgefehler behoben; Details unter „Behebungsstatus Iteration 2".)

---

## WICHTIG

### W1 — Einleitung: verbleibender unmarkierter Zusatz im „Kursversprechen"-Satz
- **Datei/Fundstelle:** `output/zusammenfassung.tex`, Z. 58 (letzter Satz der Einleitung).
- **PDF-Seite:** S. 7.
- **Beschreibung:** Der Satz „Das Kursversprechen: Diese Werkzeuge sind unmittelbar relevant für Machine Learning, Data Science und Ingenieursanwendungen …, **in denen praktisch jede Berechnung -- vom Training neuronaler Netze bis zur Simulation -- auf numerischen Approximationen beruht**" enthält einen Relativsatz, der auf S. 7 nicht steht (das Original sagt nur: „This course will teach you everything you need to know to become proficient with numerical methods, and how to put them to good use in machine learning, data science, and engineering contexts."). Der Zusatz ist sachlich plausibel (Anklänge an S. 9: „training models … simulating complex systems"), wird aber durch die Rahmung „Das Kursversprechen:" dem Skript zugeschrieben und ist entgegen der eigenen Kennzeichnungspolitik nicht als [Ergänzung] markiert — derselbe Fehlertyp wie Iteration-2-W1(a), nur einen Satz weiter. (Nebenbefund ohne eigenes Gewicht: die „proficiency"-Dimension des Originalsatzes — „everything you need to know to become proficient" — entfällt in der Paraphrase.)
- **Vorschlag:** Relativsatz als [Ergänzung] kennzeichnen oder streichen, z. B.: „… und Ingenieursanwendungen (machine learning, data science, and engineering contexts) [Ergänzung: in denen praktisch jede Berechnung — vom Training neuronaler Netze bis zur Simulation — auf numerischen Approximationen beruht]." Optional „alles Nötige, um mit numerischen Methoden sicher umzugehen (proficient)" ergänzen.

---

## OPTIONAL

### O1 — Thema 2: Rest-Unschärfe „knapp unterhalb des double-precision-Epsilons" (Teil-Carry-over aus Iteration 2, O1)
- **Datei/Fundstelle:** `output/sections/thema_2.tex`, Z. 211. **PDF-Seite:** S. 23.
- **Beschreibung:** Die in Iteration 2 monierte Gleichsetzung („nahe 10⁻¹⁶·⁵, **also um** das double-precision-Epsilon") ist entschärft; die neue Formulierung „ab ca. 10⁻¹⁶·⁵ ≈ 3·10⁻¹⁷, also **knapp** unterhalb des double-precision-Epsilons ε_mach ≈ 2.22·10⁻¹⁶" bleibt aber unscharf: 3·10⁻¹⁷ liegt einen Faktor ≈ 7 (nachgerechnet: 7.02) unter ε_mach — „knapp" ist auf linearer Skala nicht haltbar, auf der log-Achse der Figur grenzwertig. Sachlich korrekt wäre der Bezug auf die Rundungsschwelle ε_mach/2 ≈ 1.1·10⁻¹⁶.
- **Vorschlag (wie It. 2):** „für ε unterhalb von ε_mach/2 ≈ 1.1·10⁻¹⁶ (in der Figur Blow-up ab ca. 10⁻¹⁶·⁵)".

### O2 — Fußnoten innerhalb der tcolorboxen (Carry-over aus It. 1/2)
- **Datei/Fundstelle:** `thema_1.tex` Z. 137; `thema_2.tex` Z. 43, Z. 68. Unverändert: Box-Fußnoten erscheinen mit Buchstabenmarken am Boxrand statt am Seitenfuß. Inhalt geht nicht verloren; bewusst so belassen ist vertretbar.

### O3 — Rest-Formatinkonsistenzen Thema 3 (Carry-over aus It. 1/2)
- **Datei/Fundstelle:** `thema_3.tex` durchgängig: `[nosep]` statt `[itemsep=1pt]`, Gedankenstrich „—" statt „--", `\tag{Gl.~13}`-Nummerierung statt Fließtext-Nennung, Lernziele als itemize statt enumerate. Rein kosmetisch.

### O4 — Abbildungen nur textlich referenziert (Carry-over aus It. 1/2)
- **Datei/Fundstelle:** alle drei Themen. Figures 1–13 weiterhin nur beschrieben (jeweils korrekt, 1–2 Sätze); keine TikZ-Reproduktionen. Nice-to-have, kein Mangel.

### O5 — Thema 3: sin(−1.25) ≈ −0.9489 ist Trunkierung, nicht Rundung (Original-treue Wiedergabe)
- **Datei/Fundstelle:** `thema_3.tex`, Z. 70 (Konditionierungsbox, κ(−1, −0.25)). **PDF-Seite:** S. 30.
- **Beschreibung:** sin(−1.25) = −0.948985…; auf 4 Dezimalstellen korrekt **gerundet** −0.9490 (damit κ = 0.1075), das PDF druckt die **abgeschnittene** Form −0.9489 (κ = 0.1074). Die Zusammenfassung übernimmt die PDF-Werte mit „≈" originalgetreu; die Kette ist in sich konsistent, der Befund „0.1074 ≤ κ ≤ 0.1599" bleibt qualitativ unberührt. Kein Handlungsbedarf; allenfalls Fußnote (analog zum Errata-Abschnitt „Rundungen/Geringfügiges", wo dieser Punkt bisher nicht gelistet ist).

---

## Behebungsstatus Iteration 2

| Befund It. 2 | Status | Verifikation |
|---|---|---|
| K1 (Konvergenzbox h=0.2: falsche Behauptung „numerisches Minimum bei −1.2") | **behoben, kein Folgefehler** | `thema_3.tex` Z. 127 exakt nach Vorschlag umformuliert: „Ausgangspunkt ist der Gitterpunkt −1.2, dem das Skript −π/2 zuordnet (vgl. Anmerkung zur Gitterpunkt-Zuordnung in der Konsistenzbox oben); die gestörte Eingabe ist x̃ = −1.2 + 0.25 = −0.95, und diese fällt beim Auswerten auf den Gitterpunkt −1." — alle drei Teilaussagen nachgerechnet ✓ (−1.2 + 0.25 = −0.95 ✓; −0.95 snapped auf −1.0 ✓; Zuordnungs-Aussage deckungsgleich mit Z. 112 ✓). Z. 131: „(Auswertung am ungestörten **Bezugspunkt** −1.2, Wert 0.06796)" statt „Minimum" ✓ (Wert nachgerechnet: \|−0.93204 − (−1)\| = 0.06796 ✓). Die zuvor falsche „Minimum"-Behauptung ist vollständig entfernt (das tatsächliche Grid-Search-Minimum des 0.2er-Gitters liegt bei −1.6, sin(−1.6) ≈ −0.99957 — wird korrekt nirgends mehr anders behauptet). |
| W1 (Einleitung: unmarkierte Beispielaufzählung; Zielsatz weicht ab) | **behoben** | (a) Aufzählung jetzt markiert: „[Ergänzung: etwa zur Nullstellensuche, Optimierung und Integration -- so die Kapitel des Skripts]" ✓. (b) Zielsatz wörtlich nach Vorschlag: „Ziel ist, die Fähigkeiten zu vermitteln, zuverlässige und effiziente Algorithmen im Scientific Computing und in Ingenieursanwendungen zu implementieren" + Originalzitat ✓ (deckungsgleich mit S. 7). **Aber:** Im Folgesatz verbleibt ein weiterer unmarkierter Zusatz → neuer Befund W1 dieser Iteration (geringeres Gewicht, gleicher Fehlertyp). |
| O1 (Figure-8-Verortung „um das ε_mach") | **überwiegend behoben** | Gleichsetzung entfernt; neue Formulierung mit Zahlenwert 3·10⁻¹⁷ und explizitem ε_mach-Wert ist deutlich besser, „knapp unterhalb" bleibt aber um Faktor ~7 unscharf → Rest als O1 weitergeführt. |
| O2 (Box-Fußnoten) | **nicht behoben** (optional; als O2 weitergeführt) |
| O3 (Stil Thema 3) | **nicht behoben** (optional; als O3 weitergeführt) |
| O4 (TikZ-Abbildungen) | **nicht behoben** (optional; als O4 weitergeführt) |

**Fokusprüfung Konsistenz-/Konvergenzbox `thema_3.tex` (zweimal nachgebesserte Stelle):** Beide Boxen sind jetzt widerspruchsfrei und in sich korrekt. Die Konsistenzbox stellt die Skript-Zuordnung −π/2 → −1 (h=1) bzw. → −1.2 (h=0.2) neutral dar, korrigiert den Originalfehler −0.94898/0.05102 → −0.93204/0.06796 mit [Korrektur]-Kennzeichnung (= Erratum 12 ✓) und legt in der Anmerkung (Z. 112) transparent offen, dass die Zuordnung vom Nächste-Nachbarn-Snapping abweicht (nächste Punkte wären −2 bzw. −1.6 — nachgerechnet ✓). Die Konvergenzbox verweist nun auf genau diese Anmerkung, nutzt −1.2 nur noch als „Ausgangspunkt der Herleitung", und beide „="-Ketten (h=1: −π/2+0.25 → −1; h=0.2: −0.95 → −1; Endwert je 0.15853) sind Glied für Glied korrekt ✓. Die [Korrektur]-Anmerkung (0.1599 → 0.15853, fehlende Relationszeichen, f̂₁(−1.2) statt f̂₀.₂(−1.2)) deckt sich mit S. 32 und Erratum 1 ✓. Auch die merkbox (Z. 160–162) ist konsistent dazu (0.06796/0.15853/0.4964; 0.1599 korrekt als κ(−1,+0.25)-Wert identifiziert ✓).

---

## Zusammenfassung der Befunde

| Kategorie | Anzahl |
|---|---|
| KRITISCH | 0 |
| WICHTIG | 1 |
| OPTIONAL | 5 |

**Positivbefund:** Vollständigkeit Themen 1–3 gegen PDF S. 1–34 lückenlos (Motto, Introduction, alle Definitionen, Gl. 1–19, beide Tabellen vollständig, alle Figures 1–13 textlich, alle Marginalien inkl. Meta-Notizen und abgebrochener Randnotiz S. 13, alle Übungs- und Selbstreflexionsfragen, Recaps, Teaser, Überleitung S. 34 wörtlich). Alle Rechnungen unabhängig verifiziert (49/49 Checks bestanden; einzige Auffälligkeit ist die unter O5 beschriebene Original-Trunkierung). Alle [Korrektur]-Kennzeichnungen fachlich richtig und deckungsgleich mit der Errata-Liste; alle [Ergänzung]-Kennzeichnungen bis auf den unter W1 genannten Satz vollständig. Kompiliert fehlerfrei (61 Seiten).

---

## Freigabe-Urteil

**Ja — Freigabe erteilt**, mit der Auflage, den einen WICHTIG-Punkt (W1: Einzeiler-Kennzeichnung in der Einleitung, Z. 58) vor Veröffentlichung noch umzusetzen. Es bestehen keine kritischen Befunde, keine Rechen- oder Übertragungsfehler und keine Regressionen aus den Iteration-2-Fixes; die zweimal nachgebesserte Konsistenz-/Konvergenzpassage in Thema 3 ist nun fachlich korrekt, intern widerspruchsfrei und transparent gekennzeichnet. Die fünf OPTIONAL-Punkte sind kosmetischer bzw. dokumentarischer Natur und nicht freigaberelevant.

*Hinweis: Durch den Kompiliertest liegen LaTeX-Hilfsdateien (`zusammenfassung.aux/.log/.toc/.out/.pdf`) im `output/`-Ordner; Verifikationsskript unter `/tmp/review_calc/verify3.py`.*
