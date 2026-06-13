# Review-Iteration 3 — konsolidiert

Datum: 2026-06-12. Vier frische Reviewer, vollständige Neuprüfung + Regressionscheck Iteration 2.
Bilanz: KRITISCH 0 · WICHTIG 3 · OPTIONAL 13. Freigaben: Teil C ohne Auflagen; Teile A, B, D mit je einer Einzeiler-Auflage (alle unmittelbar danach behoben: Einleitungs-Kennzeichnung, f-Steigungswert S. 54 inkl. Erratum, Lagrange-Abweichungsterm Blatt 6 L8c).

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
# Review Iteration 3 — Teil B (Themen 4–6) — finale Prüfrunde

Reviewer: unabhängige Neuprüfung (Iteration 3) ausschließlich anhand der Dateien. Geprüft: Original-PDF S. 35–71 (vollständig, inkl. Index S. 71), `errata_original_pdf.md` (alle [Korrektur]/[Anm.]-Stellen nachgerechnet), `review_iteration_2_teilB.md` (Behebungsstatus), `thema_4.tex`, `thema_5.tex`, `thema_6.tex`, `zusammenfassung.tex`. Sämtliche Zahlenwerte wurden eigenständig per Python nachgerechnet (`/tmp/review_calc/check_it3.py`); Compile-Regressionstest: `pdflatex zusammenfassung.tex` zweimal, exit 0, keine Warnings, 61 Seiten.

**Gesamtbild:** Vollständigkeit lückenlos (Gl. 20–51, Algorithmen 1–4, Tabellen 2/3, alle Beispiele, alle Übungs-/Selbstreflexionsfragen, Figures 14–38, alle Randnotizen und Fußnoten 8–12). Alle fünf Befunde aus Iteration 2 (W1, O1–O4) sind sauber behoben, ohne Regressionen. Alle Errata-gestützten [Korrektur]-Stellen rechnen korrekt nach (Newton-Kette 1.1246/1.0181/1.0005 ✓, Sekante 1.0706/1.0272/1.0026/1.0001 ✓, Tabelle 2 2.12×10⁻⁶ / 1.6×10⁻¹² inkl. Residuum 4.51×10⁻¹² und C-Konsistenzcheck ✓, Glättung −0.47943/−1.24658/−0.17260/−0.86300 ✓, Midpoint n=2 −0.966485/0.010036 ✓, T₂ −0.93644/0.02001 ✓, S₂ −0.956788/3.39×10⁻⁴ ✓, MC −0.927228/0.02922 inkl. vier Abweichungsquadraten, Summe 0.009053, σ_f² 0.003018, σ_f 0.05493, SE 0.02747 ✓, P=0.803, K=28.34→29, 1−0.9²⁰=0.878 ✓, Shekel f′(7.2)=2.3778→2.38, f″(7.2)=7.138→7.14, Iterate 6.8669/7.0155/6.9907 ✓). Die erstmals in dieser Runde vollständige Nachrechnung der Figure-27/28-Captions fördert jedoch **einen neuen Befund** zutage: Der aus dem PDF übernommene Tangentensteigungswert ≈ −2.66 bei x = 6.1 ist falsch (exakt f″(6.1) = −2.977; −2.66 entspricht x ≈ 6.0). Dazu zwei neue Kleinigkeiten.

---

## KRITISCH (0 Befunde)

— keine. Keine fachlichen Fehler in Herleitungen (Gl. 20–34 Newton/Taylor/Konvergenz; Gl. 35–41 Shekel/Restarts/|f″|-Trick; Gl. 42–51 Quadratur/Monte Carlo), keine falschen Kernaussagen, keine sinnentstellend übernommenen Originalfehler.

---

## WICHTIG (1 Befund — neu)

### W1. Thema 5: Tangentensteigung „≈ −2.66 / +2.66“ bei x = 6.1 aus den PDF-Captions (Fig. 27/28) unverifiziert übernommen; exakt ist f″(6.1) ≈ −2.98
- **Datei/Fundstelle:** `output/sections/thema_5.tex`, Satzbox „Newton Richtung Minima lenken: der |f″|-Trick, Gl. (41)“, Z. 365–368: „Geometrisch (Figures 27/28 [S. 54], Beispiel am Punkt x = 6.1): Die Tangente an f′ hat dort Steigung ≈ −2.66; der Ersatz f″ → |f″| klappt die Steigung auf ≈ +2.66 um“.
- **PDF-Referenz:** S. 54, Captions Figure 27 („slope ≈ −2.66“) und Figure 28 („slope ≈ +2.66“).
- **Beschreibung:** Die Steigung der Tangente an f′ bei x ist f″(x). Eigenständige Nachrechnung (analytisch und per zentralem Differenzenquotienten gegengeprüft): f″(6.1) = −2.9772 ≈ **−2.98**, nicht −2.66. Der gedruckte Wert −2.66 gehört zu x ≈ 6.0 (f″(6.0) = −2.6304); das PDF paart also Markerposition und Steigungswert inkonsistent. Die Zusammenfassung übernimmt den Wert nicht nur als Caption-Zitat, sondern behauptet ihn affirmativ im eigenen didaktischen Fließtext — ein Verstoß gegen die Projektpolicy (alle Zahlen nachrechnen, Abweichungen markieren). Die konzeptionelle Aussage (Vorzeichen-Umklappen durch |f″|, erzwungene Bergab-Schritte) bleibt vollständig richtig; betroffen ist nur der illustrative Zahlenwert.
- **Behebung (Einzeiler):** Wert korrigieren und markieren, z. B. „… Steigung f″(6.1) ≈ −2.98 [Korrektur ggü. Original, S. 54: die Captions von Fig. 27/28 drucken ≈ ∓2.66 — das ist f″(6.0); bei x = 6.1 ist f″ ≈ −2.98]; der Ersatz f″ → |f″| klappt sie auf ≈ +2.98 um“. Zusätzlich Nachtrag in `errata_original_pdf.md` (Rubrik Rundungen/Geringfügiges oder Verifizierte Fehler).

---

## OPTIONAL (2 Befunde — neu)

### O1. Thema 6: Midpoint-n=1-Fehler „≈ 0.04104“ übernommen; korrekt gerundet 0.04105
- **Datei/Fundstelle:** `output/sections/thema_6.tex`, Z. 466 und 477 (Vergleichswert).
- **PDF-Referenz:** S. 66.
- **Beschreibung:** |Ĩ − Î| = |−0.9564491 + 0.9974950| = 0.0410458 → auf fünf Dezimalen **0.04105**; PDF (und Zusammenfassung) drucken 0.04104 (Abschneiden statt Runden). Letzte-Stelle-Fehler derselben Klasse wie die in Iteration 2 akzeptierten O2/O3; keinerlei Folgewirkung (alle Vergleiche „0.04104 vs. 0.010036“ bleiben qualitativ unverändert).
- **Behebung:** Belassen oder Mini-[Anm.]; Errata-Kandidat (Geringfügiges): „[S. 66] Midpoint-n=1-Fehler exakt 0.041046 → 0.04105 (gedruckt 0.04104)“.

### O2. Thema 5: Formulierung der Rundungs-Anmerkung zu f′(7.2) leicht missverständlich
- **Datei/Fundstelle:** `output/sections/thema_5.tex`, Z. 106–107: „Die drei Summanden ergeben arithmetisch 2.375; das PDF rundet zulässig auf 2.38“.
- **Beschreibung:** Faktisch korrekt (Summe der drei *gedruckten, gerundeten* Summanden 0.005 + 0.100 + 2.27 = 2.375; exakter Wert f′(7.2) = 2.3778 → 2.38 ist die korrekte Rundung). Die Formulierung kann aber so gelesen werden, als runde das PDF 2.375 auf 2.38; tatsächlich stammt 2.38 direkt aus dem exakten Wert 2.3778. Eine halbe Zeile („exakt 2.3778“) würde das eindeutig machen.
- **Behebung:** Optional ergänzen: „(exakt f′(7.2) = 2.3778 → 2.38; die Diskrepanz zu 2.375 entsteht nur durch die gerundeten Einzelsummanden)“.

---

## Behebungsstatus Iteration 2 (5/5 behoben, keine Regressionen)

| Befund It. 2 | Status | Verifikation |
|---|---|---|
| **W1** Gl. (47): Î_N statt I ohne Marker | **BEHOBEN** | `thema_6.tex` Z. 377: „[Anm.: Das PDF druckt links ‚I =‘; gemeint ist der Schätzer Î_N — das exakte Integral I ist Gl. (46), und Gl. (48) des Skripts verwendet selbst Î_N.]“ — sachlich korrekt, gegen PDF S. 65 geprüft ✓; Errata-Nachtrag vorhanden (`errata_original_pdf.md`, Geringfügiges, „[S. 65, Gl. 47]“) ✓ |
| **O1** Shekel-Newton x₃ = 6.9907 (PDF: 7.00) | **BEHOBEN** | `thema_5.tex` Z. 125: [Anm.] mit exakt 6.9907 und Begründung (Termüberlappung, Minimum knapp unter 7); nachgerechnet: Newton auf f′ ab 7.2 liefert 6.86689 → 7.01551 → 6.99068 ✓; Errata-Nachtrag „[S. 49]“ ✓ |
| **O2** f(2.5) = 0.598 (PDF: 0.599) | **BEHOBEN** | `thema_4.tex` Z. 24: [Anm.] korrekt (sin(2.5) = 0.598472) ✓; Errata-Nachtrag „[S. 36]“ ✓ |
| **O3** sin(−1.95) = −0.92896 (PDF: −0.92895) | **BEHOBEN** | `thema_6.tex` Z. 554: [Anm.] korrekt (sin(−1.95) = −0.9289597); Hinweis auf Konsistenz der Folgewerte zutreffend (Mittel −0.927228, Fehler 0.02922, alle vier Abweichungsquadrate mit gedruckten Werten reproduziert) ✓; Errata-Nachtrag „[S. 67]“ ✓ |
| **O4** Simpson „quadratisch“ vs. „Grad 3“ — Brücke | **BEHOBEN** | `thema_6.tex` Z. 205–207 (Defbox Simpson-Regel): „[Ergänzung: durch Symmetrie sogar exakt für alle Polynome bis Grad 3 — vgl. die S₂-Korrekturbox weiter unten; das ist kein Widerspruch, sondern eine stärkere Aussage]“ — fachlich korrekt, konsistent mit S₂-Box Z. 533 ✓ |

**Regressionscheck:** Alle fünf Fixes sind reine Hinzufügungen/Marker; die umgebenden Zahlen und Aussagen wurden erneut nachgerechnet (Grid-Search-Werte, Shekel-Iterate, MC-Kette inkl. Varianz, Simpson-Boxen inkl. h-Konventions-Anmerkung) — keine neuen Fehler. Auch alle Iteration-1-Fixes weiterhin intakt (Stichproben: Glättungsbox, Tabelle 2, MC-Varianz, Simpson-h-Konvention, Gl.-48-Anmerkung, Fig.-25-/Fig.-37-Referenzen, 0.297/0.2977/0.304). Dokument kompiliert fehler- und warnungsfrei (61 Seiten).

## Explizite Negativ-Befunde (geprüft, in Ordnung)

- **Vollständigkeit:** Gl. 20–34 (`thema_4`), 35–41 (`thema_5`), 42–51 (`thema_6`) sämtlich vorhanden, korrekt nummeriert, paginiert und originalgetreu wiedergegeben; Algorithmen 1–4 zeilengetreu (inkl. „end whilereturn“-Hinweis); Tabellen 2 und 3 vollständig und PDF-identisch (Tab. 3 inkl. Gauß-Zeile O(h²ⁿ)/O(h²ⁿ⁻¹)); alle Beispiele beider Seitenbereiche; Übungen (4/13/7 Items) und Selbstreflexionsfragen (4/6/9) vollständig inkl. [sic]-Markierungen; Figures 14–38 alle referenziert mit zutreffenden Inhaltsangaben; Randnotizen/Fußnoten (Backprop, Trade-off, Newton-Raphson-Historie, „This can happen because“, Smoothness, „Why divide by 2“, „Around a point“, „Notice the assumption play out“, N-Menge, Konvexität, implizite Restarts, Noisy Newton, Δf, DL-Hoffnungen, Notation x°, Hints, Sade, Fußnoten 8–12, Ω, i.i.d., Midpoint-als-MC, CS231n/n/b, Teaser S. 69–70, abgebrochene Sätze S. 55 als [Anm.] dokumentiert) abgedeckt. — keine Befunde.
- **Korrektheit:** Alle Handrechnungen S. 36–68 unabhängig reproduziert (38 Einzelchecks, Skript `/tmp/review_calc/check_it3.py`); alle [Korrektur ggü. Original]- und [Anm.]-Marker stimmen mit `errata_original_pdf.md` überein und rechnen nach; f′/f″-Formeln der Shekel-Instanz symbolisch verifiziert; Simpson-Gewichte (h/6, 4h/6) und Composite-Faktor h/3 korrekt; Bessel-Korrektur, Gl.-48-Klarstellung, O(1/√N)-Aussagen korrekt. — keine Befunde über W1/O1/O2 hinaus.
- **Didaktik:** Boxen-Systematik konsistent, jede Formel mit „In eigenen Worten“, [Ergänzung]-Kennzeichnung durchgängig, Merkboxen mit Fehlerquellen und Merksätzen in allen drei Themen, Querbezüge (Kap. 3 → 4 → 5 → 6, Teaser-Auflösung Hochfrequenz-Shekel) vorhanden; ohne Originalvorlesung verständlich. — keine Befunde.
- **Präambel/Build:** pdflatex zweimal, exit 0, „Output written … (61 pages)“, keine LaTeX-Warnings, Labels aufgelöst. — keine Befunde.

## Empfohlene Nachträge zur Errata-Liste

1. **[S. 54, Fig. 27/28]** Caption-Steigung ≈ ∓2.66 bei x = 6.1 ist inkonsistent: f″(6.1) = −2.977 (≈ −2.98); −2.66 entspricht x ≈ 6.0 (siehe W1).
2. **[S. 66]** Midpoint-n=1-Fehler exakt 0.041046 → korrekt gerundet 0.04105 (gedruckt 0.04104) (siehe O1, Rubrik Geringfügiges).

## Freigabe-Urteil

**Nein — noch nicht, aber unmittelbar erreichbar.** Es verbleibt genau ein WICHTIG-Befund (W1: falscher Steigungswert −2.66 statt −2.98 unmarkiert im eigenen Fließtext, `thema_5.tex` Z. 365–368) — eine Einzeilen-Korrektur plus Errata-Nachtrag. Nach dessen Behebung kann Teil B ohne weitere Prüfrunde freigegeben werden; alle übrigen Kriterien (Vollständigkeit, Korrektheit, Didaktik, Markierungs-Policy, Build) sind erfüllt, und die beiden OPTIONAL-Punkte sind nicht freigabe-relevant.
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
