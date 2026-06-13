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
