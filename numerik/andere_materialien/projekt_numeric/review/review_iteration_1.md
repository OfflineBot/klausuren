# Review-Iteration 1 — konsolidiert

Datum: 2026-06-12. Vier unabhängige Reviewer (A: Zusammenfassung T1–3, B: Zusammenfassung T4–6, C: Übungsblätter 1–3, D: Übungsblätter 4–6).
Bilanz: KRITISCH 6 · WICHTIG 10 · OPTIONAL 17. Neue verifizierte Errata: 12–15 (siehe errata_original_pdf.md).

# Review Iteration 1 — Teil A (Themen 1–3)

**Reviewer-Vorgehen:** Seiten-für-Seiten-Abgleich der tex-Dateien gegen das Original-PDF S. 1–34 (vollständig gelesen). Jede Formel, jede Tabellenzeile und jeder Zahlenwert wurde unabhängig nachgerechnet (nicht nur gegen das PDF verglichen). Gleichungsnummern- und Seitenreferenzen einzeln geprüft. Errata-Liste (`review/errata_original_pdf.md`) als Kontext herangezogen; die dort dokumentierten Korrekturen wurden auf eigene Korrektheit geprüft. Zusätzlich Kompiliertest: `zusammenfassung.tex` kompiliert mit pdflatex fehlerfrei (keine Errors, keine undefined references); Verhalten von Fußnoten in tcolorboxen per Minimaltest verifiziert.

**Geprüfte Rechnungen, die korrekt sind (Auswahl):** Substitutionslösung w₁=2/3, w₂=29/3 inkl. Verifikation; alle 25 Zeilen der Grid-Search-Tabelle (S. 15); sin-Werte des Minimum-Beispiels; Approximationsfehler 0.0907; Binärdarstellungen 10¹/10²/10³ inkl. Bias-Kontrolle (130/133/136); 2-Bit-Mantisse (0/0.25/0.5/0.75); ε_mach-Werte (2⁻²³≈1.19·10⁻⁷, 2⁻⁵²≈2.22·10⁻¹⁶); log₁₀(2¹²⁸)≈38.5; Loss-of-Significance-Beispiele; κ(−1,±0.25)=0.1599/0.1074, κ(0,±0.25)=0.2474; Stabilität s_{h=1}≈0, s_{h=0.2}=0.12411/0.25≈0.4964 (sin(−0.8)=−0.71736 ✓); Konsistenz c₁=0.15853; Konvergenz-Endwerte 0.15853 (Korrektur ggü. PDF-Wert 0.1599 ist korrekt und korrekt gekennzeichnet). Alle Gleichungsnummern (Gl. 1–19) und Seitenreferenzen stimmen mit dem Skript überein.

---

## KRITISCH

### K1 — Thema 3: Unentdeckter Originalfehler reproduziert — Konsistenzwert für h=0.2 ist falsch (−0.94898 ist nicht sin(−1.2))
- **Datei/Fundstelle:** `output/sections/thema_3.tex`, Beispielbox „Konsistenz für h=1 und h=0.2", Z. 108–110 (Rechnung und „Befund"), Folgestellen Z. 157 (merkbox: „c_{0.2}=0.05102") .
- **PDF-Referenz:** S. 32 (Konsistenzblock h=0.2).
- **Beschreibung:** Die Zusammenfassung übernimmt ungeprüft die PDF-Kette `|f̂₀.₂(−1.2) − f(−π/2)| ≥ |−0.94898 − (−1)| ≥ 0.05102`. Nachgerechnet: **sin(−1.2) = −0.93204**, nicht −0.94898. Der gedruckte Wert −0.94898 ist exakt **sin(−1.25)** — aber −1.25 ist kein Punkt des 0.2-Gitters auf [−3,1] (…,−1.4, −1.2, −1.0,…). Mit dem im Skript genannten Gitterpunkt −1.2 wäre c₀.₂ = |−0.93204 − (−1)| = **0.06796**, nicht 0.05102. Dieser Originalfehler ist NICHT in der Errata-Liste dokumentiert und wurde ohne Korrektur oder Kennzeichnung übernommen — das verletzt die Projektpolitik („fachlich korrekte Version verwenden, Abweichung kennzeichnen") und ist ein fachlicher Fehler im Prüfgegenstand. Die qualitative Aussage („Konsistenz verbessert sich mit kleinerem h") bleibt mit 0.06796 < 0.15853 gültig.
- **Behebung:** Wert korrigieren auf sin(−1.2) = −0.93204 → c₀.₂ ≈ 0.06796, als „[Korrektur ggü. Original, S. 32]" kennzeichnen; Befund-Satz und merkbox (Z. 157) anpassen; neuen Eintrag in `errata_original_pdf.md` aufnehmen (PDF S. 32: −0.94898 = sin(−1.25) statt sin(−1.2) = −0.93204; Endwert 0.05102 → 0.06796).

### K2 — Thema 3: Konvergenzkette h=0.2 enthält eine mathematisch falsche Gleichung (durch eingefügte „="-Zeichen)
- **Datei/Fundstelle:** `output/sections/thema_3.tex`, Beispielbox „Konvergenz für h=1 und h=0.2", Z. 124–128.
- **PDF-Referenz:** S. 32 (Konvergenzblock h=0.2; im PDF stehen die Zeilen ohne Relationszeichen gestapelt — vgl. Errata Nr. 1).
- **Beschreibung:** Die Zusammenfassung füllt die im PDF fehlenden Relationszeichen durchgängig mit „=" auf: `|f̂₀.₂(−1.2) − f(−π/2)| = |f̂₀.₂(−0.95) − f(−π/2)| = |f̂₀.₂(−1) − f(−π/2)| = 0.15853`. Das erste Gleichheitszeichen ist falsch: |f̂₀.₂(−1.2) − f(−π/2)| = |−0.93204 + 1| = **0.06796 ≠ 0.15853** (selbst mit dem fehlerhaften PDF-Wert −0.94898 wären es 0.05102 ≠ 0.15853). Inhaltlich beschreibt die erste Zeile die ungestörte Auswertung am numerischen Minimum (−1.2), die zweite die gestörte Eingabe x̃ = −1.2 + 0.25 = −0.95, die dritte deren Snap auf den Gitterpunkt −1. Das sind Substitutions-/Herleitungsschritte, keine Gleichheiten. Die [Korrektur ggü. Original]-Anmerkung (Z. 128) deckt nur Endwert und f̂₁→f̂₀.₂ ab, nicht diese falsche Gleichung. (Die h=1-Kette ist hingegen zufällig korrekt, da dort alle Glieder denselben Wert 0.15853 haben.)
- **Behebung:** Erstes Kettenglied streichen oder die Schritte textlich erklären, z. B.: „Numerisches Minimum bei −1.2; gestörte Eingabe x̃ = −1.2 + 0.25 = −0.95; diese fällt auf den Gitterpunkt −1: |f̂₀.₂(−0.95) − f(−π/2)| = |f̂₀.₂(−1) − f(−π/2)| = |−0.84147 − (−1)| = 0.15853." Kennzeichnung als redaktionelle Klarstellung ggü. Original ergänzen.

### K3 — Thema 3: Faktisch falsche Zusatzerklärung „nächster Gitterpunkt" bei der Konsistenzrechnung
- **Datei/Fundstelle:** `output/sections/thema_3.tex`, Z. 106 („das grobe Gitter wertet dort effektiv am nächsten Gitterpunkt −1 aus") und Z. 108 („Das feine Gitter wertet näher an −π/2 ≈ −1.5708 aus, nämlich am Gitterpunkt −1.2").
- **PDF-Referenz:** S. 32 (das PDF schreibt nur f̂₁(−1) bzw. f̂₀.₂(−1.2), ohne Begründung).
- **Beschreibung:** Die Erklärung ist von der Zusammenfassung hinzugefügt und mathematisch falsch: Der zu −π/2 ≈ −1.5708 **nächste** Gitterpunkt ist beim h=1-Gitter (−3,−2,−1,0,1) der Punkt **−2** (Abstand 0.43 < 0.57), nicht −1; beim 0.2-Gitter wäre es **−1.6** (bzw. −1.4), nicht −1.2. Die Zuordnung des Skripts folgt also gerade KEINEM Nächste-Nachbarn-Prinzip (das an anderen Stellen, −0.75→−0.8 und −0.95→−1, sehr wohl verwendet wird) — die Zusammenfassung erfindet eine Begründung, die die Rechnung nicht trägt, und verdeckt damit eine Inkonsistenz des Originals. (Konsequent „nächster Gitterpunkt" gerechnet ergäbe c₁ = |sin(−2)+1| = 0.0907 — der Approximationsfehler aus Kap. 1.)
- **Behebung:** Falsche Begründung entfernen; neutral formulieren („das Skript ordnet −π/2 dem Gitterpunkt −1 bzw. −1.2 zu") und in einer kurzen Anmerkung transparent machen, dass die Zuordnungsregel im Original nicht erklärt wird und vom sonst verwendeten Nächste-Nachbarn-Snapping abweicht. Ggf. als weiteren Errata-Kandidaten dokumentieren.

---

## WICHTIG

### W1 — Vorspann des Skripts (Motto-Zitat S. 3, Introduction S. 7) in der Zusammenfassung nicht abgedeckt
- **Datei/Fundstelle:** `output/zusammenfassung.tex` (Hauptdatei, kein Einleitungsabschnitt); `output/sections/thema_1.tex` Z. 25 (nur Kurzverweis „vgl. Introduction, S. 7").
- **PDF-Referenz:** S. 3 (Zitat „An infinitely accurate approximation is no longer an approximation." — Probably Someone Smart), S. 7 (Introduction: Kursumfang „fundamental concepts, error analysis, problem conditioning, stability, and various numerical techniques…" und Kursversprechen „…machine learning, data science, and engineering contexts").
- **Beschreibung:** Der erste Satz der Introduction ist über das S.-9-Zitat in Thema 1 inhaltlich vorhanden; das Motto-Zitat und der Überblick über Kursinhalte/-ziele fehlen jedoch vollständig. Keine Definition/Formel/Übung betroffen (daher nicht KRITISCH eingestuft), aber für ein eigenständig nutzbares Dokument ist eine kurze Einleitung mit Quellenrahmen didaktisch wertvoll und gehört zum referenzierten Seitenbereich.
- **Behebung:** In `zusammenfassung.tex` vor `\input{sections/thema_1}` einen kurzen Abschnitt „Einleitung (S. 3–7)" mit dem Motto-Zitat und 2–3 Sätzen zum Kursumfang ergänzen.

### W2 — Thema 3: Irreführende Original-Ungleichung „κ ≤ 0.247" unkorrigiert übernommen
- **Datei/Fundstelle:** `output/sections/thema_3.tex`, Z. 77.
- **PDF-Referenz:** S. 31 („Which shows ill-conditioning with κ ≤ 0.247.").
- **Beschreibung:** Die Zusammenfassung übernimmt „κ ≤ 0.247 (so die Formulierung im Original)". Das ist doppelt schief: (a) numerisch falsch — der berechnete Wert ist 0.2474, also gerade nicht ≤ 0.247; (b) konzeptionell verkehrt — für eine Aussage „schlecht konditioniert" wäre eine untere Schranke (κ ≥ …) oder schlicht κ ≈ 0.2474 aussagekräftig, eine obere Schranke belegt keine Schlecht-Konditionierung. Der Hinweis „so die Formulierung im Original" distanziert sich zwar, liefert aber keine korrekte Version — laut Projektpolitik wäre korrigieren + kennzeichnen geboten.
- **Behebung:** Schreiben: „κ ≈ 0.2474 [Korrektur ggü. Original, S. 31: dort ‚κ ≤ 0.247', was weder numerisch (0.2474 > 0.247) noch als Schranke für Schlecht-Konditionierung passt]". Vergleich mit dem gut konditionierten Fall (0.1074–0.1599) beibehalten.

### W3 — Kennzeichnungsdisziplin: mehrere inhaltliche Zusätze ohne [Ergänzung]-Marker
- **Datei/Fundstelle:** u. a. `thema_2.tex` Z. 51–62 (Spalte „Präzision" in der Darstellungs-Tabelle — im PDF, S. 18, stehen nur Beispielwerte; zudem ist „float: 7 Nachkommastellen" ungenau — gemeint sind ≈7 signifikante Dezimalstellen, die hier nur zufällig mit den Nachkommastellen zusammenfallen); `thema_2.tex` Z. 210 (Kausalerklärung zu Figure 8 „— weil 1 + ε im Speicher zu exakt 1 wird und der Nenner zu 0 auslöscht", nicht in der PDF-Caption); `thema_3.tex` Z. 18 („Pointe: Gröbere Diskretisierung ist stabiler — aber … weniger konsistent!").
- **PDF-Referenz:** S. 18, S. 23, S. 26–27.
- **Beschreibung:** Das Dokument verspricht in Legende/Fußnote der Hauptdatei, eigene Zusätze als [Ergänzung] zu markieren, und tut das an vielen Stellen vorbildlich. Die genannten Stellen sind jedoch unmarkierte Zusätze (inhaltlich korrekt, bis auf die Ungenauigkeit „Nachkommastellen"), die ein Leser fälschlich dem Skript zuordnen kann — Traceability-Problem, insbesondere bei einer als Skriptzusammenfassung deklarierten Unterlage.
- **Behebung:** Genannte Stellen mit [Ergänzung] kennzeichnen; in der Tabelle „Präzision" → „≈7 signifikante Dezimalstellen (Beispiel)" bzw. Spalte als Ergänzung ausweisen.

---

## OPTIONAL

### O1 — Fußnoten innerhalb der tcolorboxen werden als Box-interne Minipage-Fußnoten gesetzt
- **Datei/Fundstelle:** `thema_1.tex` Z. 137 (bspbox); `thema_2.tex` Z. 43 (bspbox), Z. 67 (defbox, zwei Fußnoten); Präambel `zusammenfassung.tex`.
- **Beschreibung:** Per Kompiliertest verifiziert: Fußnoten in den Boxen erscheinen mit Buchstabenmarken (a, b) am unteren Boxrand statt nummeriert am Seitenfuß — inkonsistent mit den Fließtext-Fußnoten, Inhalt geht aber nicht verloren.
- **Behebung:** Entweder bewusst so lassen (dokumentieren) oder `\footnotemark`/`\footnotetext`-Paare verwenden bzw. die Quellenangaben aus den Boxen in den Fließtext ziehen.

### O2 — Stil-/Formatinkonsistenz zwischen Thema 3 und Themen 1–2
- **Datei/Fundstelle:** `thema_3.tex` Z. 1 (`\section{Thema 3: Error Analysis (Fehleranalyse) — S.~25--34}` vs. `\section{Enter Numerical Methods (S.~9--16)}` in Thema 1/2); durchgängig `[nosep]` statt `[itemsep=1pt]`; Gedankenstrich „—" statt „--"; `\tag{Gl.~13}` (Thema 3) statt Gleichungsnummern im Fließtext (Themen 1–2); Lernziele in Thema 3 als itemize statt enumerate.
- **Behebung:** Sektionstitel- und Listenformat vereinheitlichen (z. B. überall „Thema n: Titel (S. x–y)").

### O3 — Zwei nicht übernommene Marginalien ohne Fachinhalt
- **Datei/Fundstelle/PDF-Referenz:** (a) S. 27, Randnotiz „Intuitive convergence example with sine, wanted. If you have a better idea … let me know." — Autoren-Aufruf, in `thema_3.tex` nicht erwähnt. (b) S. 23, Marginalientitel „Is double enough?" — in `thema_2.tex` ist die zugehörige Fußnote 7 (Blochinger) übernommen, der Fragetitel selbst nicht.
- **Beschreibung:** Beides Meta-/Titelzeilen ohne eigenständigen Fachinhalt; Vollständigkeit halber dokumentiert.
- **Behebung:** Optional als kurze Klammerbemerkung ergänzen; (b) passt gut als Titelfrage zur Übung 1 in Thema 2.

### O4 — Abbildungen nur textlich referenziert
- **Datei/Fundstelle:** alle drei Themen (Figures 1–13 des Skripts werden beschrieben, nicht reproduziert).
- **Beschreibung:** Für eine Zusammenfassung vertretbar — die Bildinhalte sind jeweils in 1–2 Sätzen korrekt wiedergegeben. Didaktischer Mehrwert wäre eine einfache TikZ-Reproduktion der zentralen Abbildungen (insb. Fig. 8: 1/(1+ε−1), Fig. 12/13: Balkendiagramme h=1 vs. h=0.2), da Thema 3 stark mit diesen Bildern argumentiert.
- **Behebung:** Nice-to-have: 2–3 zentrale Plots als TikZ/pgfplots ergänzen, als [Ergänzung] markiert.

---

## Zusammenfassung der Befunde

| Kategorie | Anzahl |
|---|---|
| KRITISCH | 3 |
| WICHTIG | 3 |
| OPTIONAL | 4 |

**Positivbefund:** Vollständigkeit der Themen 1 und 2 ist sehr gut (alle Definitionen, Formeln Gl. 1–12, beide Beispieltabellen, sämtliche Marginalien, Übungs-/Selbstreflexionsfragen, Teaser und Recaps abgedeckt; alle Rechnungen nachgerechnet korrekt). Thema 3 ist strukturell vollständig (Gl. 13–19, alle Marginalien bis auf O3a, alle 6 Selbstreflexionsfragen), enthält aber die unter K1–K3 beschriebenen fachlichen Mängel im Konsistenz-/Konvergenzteil. Die in der Errata-Liste dokumentierten Korrekturen (0.15853 statt 0.1599; Indexkorrekturen s_{h=1}, f̂₀.₂) sind korrekt umgesetzt und gekennzeichnet. Gleichungs- und Seitenreferenzen: alle geprüft, alle korrekt. Dokument kompiliert fehlerfrei.

*Hinweis: Durch den Kompiliertest liegen ggf. LaTeX-Hilfsdateien (`zusammenfassung.aux/.log/.toc/.out`) im `output/`-Ordner; sie können gelöscht werden.*
# Review Iteration 1 — Teil B (Themen 4–6)

Reviewer: unabhängige Prüfung ausschließlich anhand der Dateien (Original-PDF S. 35–71, errata_original_pdf.md, thema_4/5/6.tex, zusammenfassung.tex). Alle Formeln, Herleitungen und Zahlenwerte wurden eigenständig nachgerechnet; der Seitenabgleich erfolgte lückenlos Seite für Seite.

**Gesamtbild:** Die drei Kapitel sind nahezu vollständig (alle Gl. 20–51, Algorithmen 1–4, Tabellen 2 und 3, alle Beispiele, Übungs-/Selbstreflexionsfragen und praktisch alle Randnotizen sind abgedeckt). Die als [Korrektur ggü. Original] markierten Abweichungen wurden nachgerechnet und sind sämtlich korrekt (S. 37 sin(3.125), S. 38 Gl. 20, S. 44 Newton-Kette, S. 45 Sekanten-Kette, S. 53 f′/f″, S. 64 h/3-Faktor, S. 66 Midpoint n=2, S. 67 T₂ und S₂ — alle verifiziert). Die Didaktik ist gut: Motivation, Boxen, durchgerechnete Beispiele und Merkboxen sind in allen drei Themen vorhanden. Es verbleiben jedoch zwei fachliche Fehler, die unverifiziert aus dem Original übernommen wurden (nicht in der Errata-Liste), sowie einige kleinere Punkte.

---

## KRITISCH (2 Befunde)

### K1. Thema 6: Glättungs-Beispiel S. 59 übernimmt falsche Original-Funktionswerte; Schlussfolgerung dadurch in sich widersprüchlich
- **Datei/Fundstelle:** `output/sections/thema_6.tex`, Beispielbox „Glättung durch Integration bei x = −0.4“ (Z. 67–88).
- **PDF-Referenz:** S. 59 (Original-Fehler, NICHT in `review/errata_original_pdf.md` dokumentiert).
- **Beschreibung:** Die Box übernimmt aus dem PDF f(−0.5) = −1.14973 und f(−0.3) = −0.97720. Eigenständige Nachrechnung mit f(x) = sin(x) + sin(2πx):
  - f(−0.5) = sin(−0.5) + sin(−π) = **−0.47943** (nicht −1.14973),
  - f(−0.3) = sin(−0.3) + sin(−0.6π) = **−1.24658** (nicht −0.97720).
  - Der PDF-Wert −1.14973 ist tatsächlich f(−0.2), und −0.97720 ist f(−0.4) selbst — das Original hat offenbar das Fenster [−0.4, −0.2] gemittelt und die Stützstellen falsch beschriftet.
  - Korrekt für das beschriebene Fenster [−0.5, −0.3]: geglättetes f(−0.4) ≈ (−0.47943 − 1.24658)/2 = **−0.86300** (nicht −1.06347).
  - **Folgewirkung:** Mit den übernommenen Zahlen ist der geglättete Wert (−1.06347) *tiefer* als die Direktauswertung (−0.97720) — das widerspricht direkt der im selben Absatz übernommenen Aussage „Korrektur der lokalen Loss-Landschaft hin zu *höheren* Losses“ / „das Schlagloch wird zugeschüttet“. Mit den korrekten Werten (−0.86300 > −0.97720) stimmt die Aussage.
- **Behebung:** Werte korrigieren (f(−0.5) = −0.47943, f(−0.3) = −1.24658, Integral ≈ −0.17260, geglättet ≈ −0.86300), als „[Korrektur ggü. Original, S. 59]“ kennzeichnen und den neuen Originalfehler in `errata_original_pdf.md` nachtragen. Alternativ zusätzlich erwähnen, dass die PDF-Zahlen dem Fenster [−0.4, −0.2] (Werte f(−0.4), f(−0.2)) entsprechen.

### K2. Thema 4: Tabelle 2 (√2-Newton) — Fehlerwert der Zeile n = 4 ist falsch (Originalfehler unverifiziert übernommen)
- **Datei/Fundstelle:** `output/sections/thema_4.tex`, Beispielbox „Berechnung von √2 mit Newton (Tabelle 2)“ (Z. 165–183), Tabellenzeile „4 & 1.414213562 & 4.5 × 10⁻¹²“.
- **PDF-Referenz:** S. 42, Tabelle 2 (Original-Fehler, NICHT in der Errata-Liste).
- **Beschreibung:** Eigenständige Nachrechnung (Newton auf x² − 2, x₀ = 2): x₄ = 1.4142135623746899, |e₄| = |x₄ − √2| = **1.59 × 10⁻¹²**. Der gedruckte Wert 4.5 × 10⁻¹² ist nachweislich das *Residuum* |f(x₄)| = |x₄² − 2| = 4.51 × 10⁻¹² — inkonsistent mit der Spaltendefinition |eₙ| und mit allen übrigen Zeilen (die |xₙ − √2| enthalten; z. B. n = 3: 2.12 × 10⁻⁶, nicht |f(x₃)| = 6.0 × 10⁻⁶). Nebenbefund: |e₃| ist exakt 2.124 × 10⁻⁶, das gedruckte „2.13 × 10⁻⁶“ ist falsch gerundet (korrekt 2.12 × 10⁻⁶). Die didaktische Kernaussage (Fehlerquadrierung 10⁻³ → 10⁻⁶ → 10⁻¹²) bleibt qualitativ richtig, aber die Zusammenfassung reproduziert hier zwei falsche Zahlen als Fakt — entgegen der Projektpolicy „fachlich korrekte Version verwenden, Abweichung kennzeichnen“.
- **Behebung:** Zeile n = 4 auf |e₄| ≈ 1.6 × 10⁻¹² (und n = 3 auf 2.12 × 10⁻⁶) korrigieren, mit „[Korrektur ggü. Original, S. 42: PDF druckt 4.5 × 10⁻¹², das ist das Residuum |f(x₄)|, nicht |e₄|]“ kennzeichnen; Erratum nachtragen. (Konsistenzcheck: |e₄| ≈ C·e₃² mit C = 1/(2√2) ≈ 0.354: 0.354·(2.12 × 10⁻⁶)² = 1.6 × 10⁻¹² ✓ — die Korrektur demonstriert die quadratische Konvergenz sogar sauberer.)

---

## WICHTIG (3 Befunde)

### W1. Thema 6: Monte-Carlo-Stichprobenvarianz/Standardfehler — Original-Zahlen leicht falsch, unverifiziert übernommen; Box verspricht „vollständige Rechnung“, zeigt sie aber nicht
- **Datei/Fundstelle:** `output/sections/thema_6.tex`, Beispielbox „Monte Carlo von Hand“ (Z. 535–550).
- **PDF-Referenz:** S. 68 (Original-Ungenauigkeit, nicht in der Errata-Liste).
- **Beschreibung:** Mit den vier Samples (f̄ = −0.927228) liefert Gl. (51) eigenständig nachgerechnet: σ_f² = 0.009053/3 = **0.003018** (PDF/Zusammenfassung: 0.003036), σ_f = **0.05493** (statt 0.05512), SE = **0.02747** (statt 0.02756). Abweichung ~0.6 % — klein, aber die Werte sind so nicht aus den angegebenen Samples reproduzierbar. Zudem ist die Passage als „(vollständige Rechnung)“ betitelt, die eigentliche Rechnung (die vier Abweichungsquadrate) fehlt aber — gerade dadurch fällt die Nichtreproduzierbarkeit dem Lernenden auf die Füße.
- **Behebung:** Entweder die korrekten Werte (0.003018 / 0.05493 / 0.02747) mit Korrektur-Marker einsetzen und die vier Abweichungsquadrate (≈ 0.0000030, 0.0052638, 0.0002093, 0.0035770) ausweisen, oder Titelzusatz „vollständige Rechnung“ streichen und Fußnote zur Abweichung ergänzen. Die anschließende [Ergänzung] („SE 0.02756 passt gut zum Fehler 0.02922“) bleibt mit 0.02747 unverändert gültig.

### W2. Thema 6: Simpson-Einzelintervall-Box enthält widersprüchliche h-Konventionen im selben Kasten
- **Datei/Fundstelle:** `output/sections/thema_6.tex`, Satzbox „Herleitung der Simpson-Gewichte über Lagrange-Interpolation“ (Z. 216–245).
- **PDF-Referenz:** S. 63 (die Inkonsistenz stammt aus dem Original, wird aber nicht aufgelöst, sondern mitgeschleppt).
- **Beschreibung:** Die Box behauptet erst „sodass m − a = b − m = h gilt“ (⇒ h = halbe Intervallbreite), präsentiert dann die Formel h/6·[f(a) + 4f(m) + f(b)] und erklärt anschließend „Hier bezeichnet h = b − a die Gesamtbreite“ — beides zugleich kann nicht stimmen. Mit m − a = h wäre die korrekte Formel (2h)/6·[…] = h/3·[…]. Wer h als Gitterweite einsetzt, erhält den halben Wert. Die Merkbox am Kapitelende stellt es zwar richtig („h/6 gehört zur Einzelintervall-Form mit h = b − a“), die Satzbox selbst bleibt aber in sich widersprüchlich.
- **Behebung:** In der Satzbox eine Konvention durchziehen: h := b − a definieren, „m − a = b − m = h“ ersetzen durch „m − a = b − m = h/2“ und das Original-Statement als Konventionswechsel kennzeichnen (z. B. „[Anm.: Das Skript schreibt m − a = b − m = h in der Composite-Konvention, dort lautet die Paar-Formel h/3·…]“).

### W3. Thema 6: Irreführende Original-Formulierung zu Gl. (48) („für N → ∞“) wird unkorrigiert wiedergegeben
- **Datei/Fundstelle:** `output/sections/thema_6.tex`, Satzbox „Eigenschaften des Monte-Carlo-Schätzers“ (Z. 358–365).
- **PDF-Referenz:** S. 65.
- **Beschreibung:** Der Text übernimmt „… erwartungstreu … (das Skript formuliert: für N → ∞)“. Erwartungstreue E[Î_N] = I gilt jedoch für **jedes endliche N**; das „für N → ∞“ des Skripts verwechselt Erwartungstreue mit Konsistenz. Die Zusammenfassung zitiert die Formulierung, ohne sie als irreführend zu markieren — ein Lernender kann daraus mitnehmen, der Schätzer sei nur asymptotisch unverzerrt. (Die [Ergänzung] danach ist korrekt, behebt die Konfusion aber nicht explizit.)
- **Behebung:** Klarstellen, z. B.: „[Anm.: Das ‚für N → ∞‘ des Skripts ist irreführend — Erwartungstreue gilt für jedes N; erst die Aussage Î_N → I (Konsistenz) ist eine N → ∞-Aussage.]“

---

## OPTIONAL (3 Befunde)

### O1. Thema 5: Figure 25 (S. 49) wird nirgends referenziert
- **Datei/Fundstelle:** `output/sections/thema_5.tex`, Beispielbox „Newton auf der Shekel-Funktion ab x₀ = 7.2“ (Z. 94–139).
- **PDF-Referenz:** S. 49, Figure 25 (f′ und f″ der Shekel-Funktion; „second derivative is positive at minima, confirming local curvature“).
- **Beschreibung:** Alle übrigen Abbildungen (14–24, 26–38) sind erwähnt; nur Figure 25 fehlt. Die inhaltliche Aussage (f″ > 0 an Minima) ist anderweitig abgedeckt, der Bildverweis aber nicht.
- **Behebung:** Ein Halbsatz in der Box: „(vgl. Figure 25 [S. 49]: f′ schwarz, f″ grau gestrichelt; f″ > 0 an den Minima)“.

### O2. Thema 6: Figure 37 (S. 65) unreferenziert; PDF-Bildunterschrift ist dort selbst ein Kopierfehler
- **Datei/Fundstelle:** `output/sections/thema_6.tex`, Abschnitt Monte Carlo (Z. 336–355).
- **PDF-Referenz:** S. 65, Figure 37 — die Caption ist wortgleich mit Figure 34 („midpoint rule integrals … bars now touch“), obwohl die Abbildung im MC-Kontext steht (offenbar Copy-Paste-Fehler des Originals).
- **Beschreibung:** Die Zusammenfassung erwähnt Figure 37 nicht; angesichts der defekten Original-Caption ist das verschmerzbar, könnte aber als Errata-Kandidat dokumentiert werden.
- **Behebung:** Optional kurzer Hinweis bzw. Aufnahme in `errata_original_pdf.md` (Rubrik „Geringfügiges“).

### O3. Thema 4: Inkonsistente Rundung innerhalb einer Korrektur-Anmerkung
- **Datei/Fundstelle:** `output/sections/thema_4.tex`, Z. 247: „falschem Zähler 0.432 statt ≈ 0.305 (… wäre f(1.127) ≈ 0.3044 …)“.
- **PDF-Referenz:** S. 44.
- **Beschreibung:** Im selben Satz wird derselbe Wert einmal als ≈ 0.305 und einmal als ≈ 0.3044 angegeben (f(1.127) = 0.30444). Sachlich harmlos, wirkt aber unsauber.
- **Behebung:** Einheitlich „≈ 0.304“ schreiben.

---

## Explizite Negativ-Befunde (geprüft, in Ordnung)

- **Vollständigkeit:** Keine fehlenden Inhalte. Gl. 20–51 sämtlich vorhanden und korrekt nummeriert/paginiert; Algorithmen 1–4 vollständig (inkl. Hinweis auf das „end whilereturn“-Layoutartefakt); Tabellen 2 und 3 vollständig reproduziert; alle Beispiele (Grid Search/Newton an sin, √2, Newton/Sekante an x³−x, Shekel-Newton ab 7.2, Random-Restarts-Rechnung p=0.15, Glättung, Exakt/Midpoint/Trapez/Simpson/MC an ∫sin), alle Übungs- und Selbstreflexionsfragen (4+2 / 6+12 / 9+7) und die relevanten Randnotizen sind abgedeckt. — **keine Befunde** über K1/K2 hinaus.
- **Korrektheit der markierten Korrekturen:** Alle elf einschlägigen [Korrektur ggü. Original]-Stellen in Themen 4–6 nachgerechnet — sämtlich korrekt (u. a. Sekanten-Kette 1.0706→1.0272→1.0026→1.0001 ✓, Newton-Kette 1.1246→1.0181→1.0005 ✓, Midpoint n=2 = −0.966485/0.010036 ✓, T₂ = −0.93644/0.02001 ✓, S₂ = −0.9568/3.4·10⁻⁴ ✓, Shekel f′(7.2)/f″(7.2) inkl. Ableitungsformeln ✓, K = 28.3→29 ✓, P(K=10, p=0.15) = 0.803 ✓, 1−0.9²⁰ ≈ 0.88 ✓).
- **Referenzen:** Seiten-, Gleichungs-, Algorithmen-, Tabellen- und (bis auf O1/O2) Abbildungsverweise stimmen. — **keine Befunde**.
- **Didaktik:** Jedes Thema hat Motivation („The Why“), Lernziele, Definitions-/Satz-/Beispielboxen, mindestens ein vollständig durchgerechnetes Beispiel und eine Merkbox mit Fehlerquellen und Merksätzen; Themen sind ohne Originalvorlesung verständlich. — **keine Befunde** über W2/W3 hinaus.
- **Präambel (`zusammenfassung.tex`):** Boxdefinitionen (defbox/satzbox/bspbox/merkbox), Pakete (amsmath, algorithm/algpseudocode, enumitem, booktabs, tcolorbox[most], hyperref) decken alle in Themen 4–6 verwendeten Konstrukte ab. — **keine Befunde**.

## Empfohlene Nachträge zur Errata-Liste (aus diesem Review)

1. **[S. 59]** Glättungsbeispiel: f(−0.5) und f(−0.3) falsch gedruckt (sind f(−0.2) bzw. f(−0.4)); korrektes geglättetes f(−0.4) ≈ −0.86300 (siehe K1).
2. **[S. 42]** Tabelle 2: |e₄| = 4.5·10⁻¹² ist das Residuum |f(x₄)|; korrekt |e₄| ≈ 1.6·10⁻¹²; |e₃| korrekt 2.12·10⁻⁶ (siehe K2).
3. **[S. 68]** σ_f² = 0.003036 / σ_f = 0.05512 / SE = 0.02756 nicht aus den Samples reproduzierbar; korrekt 0.003018 / 0.05493 / 0.02747 (siehe W1).
4. **[S. 65]** Figure-37-Caption ist Kopie der Figure-34-Caption (Geringfügiges, siehe O2).
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
# Review Iteration 1 — Teil D: Übungsblätter 4–6

Unabhängiger Review ausschließlich anhand der Dateien. Referenz: Original-PDF S. 35–70 (vollständig gelesen) und `review/errata_original_pdf.md`. **Alle Musterlösungen wurden vollständig numerisch nachgerechnet** (Python-Skripte unter `/tmp/review_calc/blatt{4,5,6}.py`).

Geprüfte Dateien:
- `output/uebungen/uebung_04_newton_methods.tex` (8 Aufgaben, 50 P)
- `output/uebungen/uebung_05_global_optimization.tex` (8 Aufgaben, 50 P)
- `output/uebungen/uebung_06_numerical_integration.tex` (8 Aufgaben, 54 P)

---

## KRITISCH

### K1 — Blatt 4, Aufgabe 7(b) (Aufgabentext): fachlich falsche Aussage über die Wurzelabstände
**Datei/Stelle:** `uebung_04_newton_methods.tex`, Aufgabe 7(b) (Zeile 174–175).
**Befund:** Der Aufgabentext behauptet, der Startwert $x_0 = 0.5$ sei „von allen drei Wurzeln höchstens $0.5$ entfernt". Nachrechnung: Abstände von $0.5$ zu den Wurzeln $-1, 0, 1$ sind $1.5$, $0.5$, $0.5$ — die Aussage ist für die Wurzel $-1$ falsch (Abstand $1.5$, nicht $\le 0.5$). Sie widerspricht zudem der eigenen Musterlösung, die korrekt formuliert, Newton springe „zur **entferntesten** Wurzel $-1$" und $x_0=0.5$ liege „genau mittig zwischen den Wurzeln $0$ und $1$".
**Hinweis:** Die eigentliche Rechnung in Aufgabe und Lösung ist korrekt ($f(0.5)=-0.375$, $f'(0.5)=-0.25$, $x_1 = 0.5 - (-0.375)/(-0.25) = -1$ exakt, nachgerechnet ✓); nur die Nebenbemerkung im Aufgabentext ist falsch.
**Behebung:** Formulierung ersetzen durch z. B. „… dass der Startwert $x_0 = 0.5$ — der von den beiden Wurzeln $0$ und $1$ jeweils genau $0.5$ entfernt ist — in einem einzigen Newton-Schritt exakt auf der **entfernten** Wurzel $x=-1$ landet …".

*(Keine weiteren KRITISCH-Befunde: Sämtliche Musterlösungen aller drei Blätter wurden Zwischenschritt für Zwischenschritt nachgerechnet und sind numerisch korrekt; alle Aufgaben sind mit den gegebenen Mitteln lösbar — die Wertetabelle in Blatt 6 deckt alle benötigten $e^x$-Werte ab; keine Lösungsleaks im Aufgabenteil; alle Errata-Korrekturen (Newton-Kette 1.4→1.1246→1.0181→1.0005, Sekante f(1.2)=0.528 / x₂≈1.0706, Gl.-(20)-Layout, f″/f′-Druckfehler S. 53, Composite-Simpson h/3, Midpoint n=2 ≈ −0.966485, T₂ ≈ −0.93644, S₂ ≈ −0.956788) sind korrekt übernommen und als „[Korrektur ggü. Original, S. n]" gekennzeichnet.)*

---

## WICHTIG

### W1 — Blatt 5, Aufgabe 8(d): widersprüchliche Annahmen führen zu zwei verschiedenen vertretbaren Ergebnissen
**Datei/Stelle:** `uebung_05_global_optimization.tex`, Aufgabe 8(d) (Zeile 240–246) und zugehörige Lösung (Zeile 591–602).
**Befund:** Der Aufgabentext kombiniert zwei nicht äquivalente Annahmen: (1) „ein lokaler Optimierer konvergiert stets zum **nächstgelegenen** Fuchsloch" und (2) „die lokalen Maxima liegen näherungsweise bei $x \approx 1.7$ und $x \approx 5.7$". Unter Annahme (1) liegen die Basin-Grenzen an den Mittelpunkten $2$ und $5.5$ → Sprung von $7$ mit $\mathrm{Uniform}(-3,3)$ landet in $[4,10]$, Überlapp mit $(2, 5.5)$ ist $1.5$ → $P = 1.5/6 = 0.25$. Die Musterlösung nutzt dagegen die Maxima als Grenzen → Überlapp $[4, 5.7)$, $P = 1.7/6 \approx 0.283$. Ein Studierender, der Annahme (1) wörtlich nimmt, erhält ein abweichendes, aber konsistentes Ergebnis. (Nachrechnung der echten Maxima von $f'$: $x \approx 1.685$ und $x \approx 5.681$ — die Angabe $\approx 1.7 / 5.7$ ist korrekt; die gradientenbasierten Basins haben tatsächlich ihre Grenzen an den Maxima, d. h. die Lösung ist die fachlich „richtigere" Lesart.)
**Behebung:** „nächstgelegenes Fuchsloch" streichen und ersetzen durch: „ein lokaler Optimierer konvergiert stets in das Minimum desjenigen Basins, in dem er startet; die Basin-Grenzen liegen an den lokalen Maxima $x \approx 1.7$ und $x \approx 5.7$". (Damit zugleich konsistent zur Lösungsaussage in Aufgabe 3(a), dass Basin-Grenzen an lokalen Maxima liegen.)

### W2 — Blatt 6: Themenlücke Lagrange-Interpolation (Gl. 45)
**Datei/Stelle:** `uebung_06_numerical_integration.tex`, gesamtes Blatt.
**Befund:** Das Skript führt Lagrange-Interpolation als eigenes Lernziel („Know about Lagrange interpolation and how it relates to quadrature rules", S. 60) mit Gl. (45) und der Herleitung der Simpson-Gewichte $h/6, 2h/3, h/6$ ein (S. 63). Das Blatt deklariert Abdeckung „(42)–(51)", prüft Gl. (45) aber nirgends; nur Lösung 8(b) erwähnt das quadratische Interpolationspolynom beiläufig. Alle übrigen Kerninhalte (Gl. 42–44, 46–51, Tab. 3, Monte Carlo, Curse of Dimensionality, SGD-Bezug) sind abgedeckt.
**Behebung:** Teilaufgabe ergänzen, z. B. in Aufgabe 2 oder 8: Lagrange-Basispolynome $L_j$ für drei äquidistante Knoten $a, m, b$ aufstellen und durch Integration die Simpson-Gewichte $h/6$ (Endpunkte) und $2h/3$ (Mittelpunkt) verifizieren.

### W3 — Blatt 6, Aufgabe 4(d) vs. Aufgabe 6: inkonsistente $h$-Definition bei Simpson
**Datei/Stelle:** `uebung_06_numerical_integration.tex`, Aufgabe 4(d) (Zeile 90) und Aufgabe 6 (Zeile 105).
**Befund:** Aufgabe 4(d) definiert die Einzel-Simpson-Regel mit $h = b - a = 2$ (Formel $\frac{h}{6}[f(a)+4f(m)+f(b)]$ — so korrekt). Aufgabe 6 bezeichnet denselben Fall dann als „Simpson: $h = 1 \to 0.5$" (Composite-Lesart mit Gitterweite $h=(b-a)/2$). Die Quotientenrechnung selbst ist eindeutig und korrekt (nachgerechnet: $0.031672/0.002154 \approx 14.7 \approx 2^4$), aber der stillschweigende Wechsel der $h$-Konvention kann Studierende verwirren — zumal das Skript an genau dieser Stelle selbst inkonsistent ist (Erratum 7).
**Behebung:** In Aufgabe 6 einen Halbsatz ergänzen: „(die Einzel-Simpson-Regel aus Aufgabe 4(d) wird hier als zusammengesetzte Regel mit $n=2$, Gitterweite $h = 1$ gelesen)".

---

## OPTIONAL (Stil/Rundung; Endergebnisse jeweils korrekt)

### O1 — Blatt 6, Lösung 7(b): letzte Nachkommastelle einzelner quadrierter Abweichungen
Mit den Tabellenwerten ergibt sich $(5.754603-3.409329)^2 = 5.500310$ (Blatt: $5.500308$); je nach Rundungsweg ebenso $1.670115$ statt $1.670114$ und $1.149955$ statt $1.149956$. Abweichungen $\le 2\cdot10^{-6}$, Summe ($12.837295$), Varianz ($4.279098$), $\sigma_f$ ($2.068598$) und SE ($2.068598$) sind korrekt. Behebung: Abweichungen aus den 6-stelligen Tabellenwerten neu runden.

### O2 — Blatt 6, Lösungen 4(d)/5(d): Klammersummen um $10^{-6}$ daneben
$1 + 4\cdot2.718282 + 7.389056 = 19.262184$ (Blatt: $19.262183$); $1+6.594884+5.436564+17.926756+7.389056 = 38.347260$ (Blatt: $38.347261$, entspricht dem ungerundeten Wert). Quotienten $6.420728$ bzw. $6.391210$ stimmen. Behebung: konsistent aus Tabellenwerten summieren.

### O3 — Blatt 6, Lösung 1(b): unklare Formulierung „nahe an der halben Periode pro Halbintervall"
$h/2 = 0.24$ ist $\approx T/4$ (Viertelperiode), nicht „halbe Periode pro Halbintervall"; die Klammerangabe „$h \approx T/2$ in der Nachbar-Mittelung" ist korrekt. Behebung: Formulierung straffen („$h = 0.48 \approx T/2$: benachbarte Auswertungspunkte liegen nahezu gegenphasig").

### O4 — Blatt 5, Lösung 7(b): Zwischenwert-Rundung
„$f(-0.0740) \approx 0.00003 - 0.01094$": korrekt wäre $2\cdot0.074^2 = 0.010952$; Endwert $-0.0109$ stimmt ($f(-0.07397) = -0.010914$). Behebung: Zwischenwert auf $0.01095$ korrigieren.

---

## Positivbefunde (Prüfprotokoll, Auswahl der Nachrechnungen)

- **Blatt 4, A3:** Newton an $x^2-5$, $x_0=3$: $2.3333333 \to 2.2380952 \to 2.2360689$; $f$-, $f'$-Spalten, Fehler $7.639\text{e-}1 / 9.727\text{e-}2 / 2.027\text{e-}3 / 9.18\text{e-}7$ und $C_n = 0.167/0.214/0.223 \to C_\text{theor} = 1/(2\sqrt5)=0.2236$ — alles exakt bestätigt.
- **Blatt 4, A4:** $\ln(1.2)=0.1823216$; Fehler $0.1823216 / 0.0176784 / 0.0023216$ ✓.
- **Blatt 4, A5(c):** Sekante: $x_2=2.2$, $x_3=2.2307692$ ($f=-0.0236686$), $x_4=2.2361111$, $|x_4-\sqrt5|=4.31\text{e-}5$ ✓.
- **Blatt 4, A6/A8:** Verhältnistabelle ($0.25/0.33/0.35/0.99$) ✓; Herleitung deckungsgleich mit Gl. (28)–(33) ✓.
- **Blatt 4, A7(c):** $N(x)=2x^3/(3x^2-1)$, Oszillationspunkte $\pm1/\sqrt5 = \pm0.4472136$, $N(1/\sqrt5)=-1/\sqrt5$ ✓.
- **Blatt 5, A2(c):** $f(4)=-8.6769$, $f(7)=-2.9549$, $f(5.5)=-1.1413$, Sehnenmittel $-5.8159$ ✓.
- **Blatt 5, A4:** $x_1=3.0833$, $x_2=3.0032$ bzw. $x_1=0.9167$, $x_2=0.9968$ ✓.
- **Blatt 5, A5:** $P=0.803$; $K=28.34\to29$; $1-0.8^8=0.832$; $K=13.43\to14$ (Probe $0.956/0.945$ ✓); $K=89.8\to90$, $K=458.2\to459$ ✓.
- **Blatt 5, A6:** $e^{-0.25}=0.779$, $e^{-1}=0.368$, $e^{-5}=0.0067$, $e^{-0.1}=0.905$, $e^{-1.2}=0.301$ ✓.
- **Blatt 5, A7(b):** $f'(0.3)=-1.092$, $f''(0.3)=-2.92$; Standard $x_1=-0.0740$ ($f=-0.0109$, bergauf), $|f''|$-Trick $x_1=0.674$ ($f=-0.7021$, bergab) ✓.
- **Blatt 5, A8(b,c):** $f'(7.2)$-Summanden $0.0052/0.0998/2.2727 \to 2.3778$; $f''(7.2)$-Summanden $-0.0021/-0.0912/7.2314 \to 7.1381$; $x_1 = 6.8669 \approx 6.87$ — deckungsgleich mit Skript S. 49 ✓.
- **Blatt 6, A4/A5:** exakt $6.389056$; $M_1=5.436564$ (Fehler $0.952492$), $T_1=8.389056$ ($2.000000$), $S_1=6.420728$ ($0.031672$); $M_2=6.130410$ ($0.258646$), $T_2=6.912810$ ($0.523754$), $S_4=6.391210$ ($0.002154$) — alle ✓.
- **Blatt 6, A6:** Quotienten $3.68 / 3.82 / 14.7$; Prognose $S_8 \approx 1.3\text{e-}4$ (tatsächlich $1.38\text{e-}4$) ✓.
- **Blatt 6, A7:** $\hat I_4 = 6.818659$ (Fehler $0.429602$), $\bar f = 3.409329$, Var $=4.279098$, $\sigma_f = 2.068598$, SE $=2.068598$, Halbierung bei $N=16$ ✓.
- **Blatt 6, A8(a):** Simpson an $\int_0^1 x^3 = 0.25$ exakt ✓; A3: $10^{20}/10^9$ s $\approx 3.2\cdot10^3$ Jahre, $2^{10^6}$ hat $301\,030$ Stellen ✓.
- **Struktur/Format (alle drei Blätter):** je 8 Aufgaben (Vorgabe 5–8 ✓); Punktsummen verifiziert: Teilpunkte je Aufgabe und Blattsummen stimmen (50/50/54 = ausgewiesene Gesamtsummen); ansteigende Schwierigkeit mit ausgewiesener Staffelung; Lösungen strikt nach `\newpage`; `\refstepcounter`/`\label{auf:n}`/`\ref` korrekt verknüpft; keine Lösungsleaks im Aufgabenteil (die in Blatt 5, A8(c) vorgegebenen $x_2 \approx 7.02$, $x_3 \approx 7.00$ sind bewusste Interpretationsvorgabe, $x_1$ wird nicht verraten).
- **Skript-Treue:** Kap. 4 (Gl. 20/21, Taylor 23–26, quadratische Konvergenz 27–33, Sekante 34, Failure Modes, Algorithmen 1/2) und Kap. 5 (Gl. 35–41, Alg. 3/4, Konvexität, Simulated Annealing, Basins, DL-Bezüge) vollständig abgedeckt; Kap. 6 bis auf Gl. 45 (→ W2) vollständig. Transferaufgaben (Konvexitätsbeweis, Oszillations-Fixpunkt, Simpson-Grad-3-Exaktheit) sind als Transfer gekennzeichnet und konsistent mit Skript/Errata; keine ungekennzeichneten Fremdkonzepte.

**Bilanz: 1 × KRITISCH, 3 × WICHTIG, 4 × OPTIONAL.**
