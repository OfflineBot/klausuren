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
