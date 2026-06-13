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
