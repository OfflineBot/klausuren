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
