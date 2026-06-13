# Review Iteration 4 — Teil A (Bestätigungsrunde, gesamtes Dokument)

**Reviewer-Vorgehen:** Unabhängige Bestätigungsprüfung ausschließlich anhand der Dateien (kein Vorwissen über die Entstehung). Geprüft: Original-PDF S. 1–71 vollständig (Read, 4 Blöcke: 1–18, 19–36, 37–54, 55–71), `output/zusammenfassung.tex` (vollständig), alle sechs Dateien `output/sections/thema_1.tex`–`thema_6.tex` (vollständig), `errata_original_pdf.md`, Vorrunden-Berichte `review_iteration_3_teilA.md` und `review_iteration_3_teilB.md`. Seit Iteration 3 geänderte Dateien (Zeitstempel 13:10): `zusammenfassung.tex`, `sections/thema_5.tex`, `errata_original_pdf.md` — diese drei wurden an den geänderten Stellen **voll** geprüft (inkl. unabhängiger Nachrechnung); die unveränderten Sections wurden im Gesamtdurchgang auf Konsistenz und Regressionen durchgesehen, gestützt auf die in den Vorrunden dokumentierten, dort vollständig verifizierten Rechnungen — ergänzt um eigene Stichproben-Nachrechnungen (Python, analytisch + zentrale Differenzenquotienten als Gegenprobe): Shekel-Instanz f″(6.1) = −2.9772, f″(6.0) = −2.6304, f′(7.2) = 2.3778 (Summanden 0.0052/0.0998/2.2727), f″(7.2) = 7.138 (Summanden −0.0021/−0.0912/7.2314), Newton-auf-f′-Kette 6.86689 → 7.01551 → 6.99067; Konsistenz 0.06796, Konvergenz 0.15853, κ(−1,+0.25) = 0.1599, s₀.₂ = 0.4964; Newton x³−x: 1.1246/1.0181/1.0005; Sekante: 1.0706/1.0272/1.0026/1.0001; √2-Tabelle inkl. |e₃| = 2.124·10⁻⁶, |e₄| = 1.595·10⁻¹², Residuum 4.51·10⁻¹²; Glättung −0.47943/−1.24658/−0.17260/−0.86300; Ĩ = −0.9564491424; Midpoint n=1 −0.99749/0.041046, n=2 −0.966485/0.010036; T₂ −0.93644/0.02001; S₂ −0.956788/3.42·10⁻⁴; MC −0.927233/0.029216 (mit gedruckten gerundeten Samples −0.927228/0.02922 reproduziert), σ_f² 0.003018, σ_f 0.05493, SE 0.02747; P = 0.803, K = 28.34 → 29, 1−0.9²⁰ = 0.878. Alle Werte stimmen mit den Materialien und der Errata-Liste überein. Kompiliertest gemäß Vorgabe: `bash /tmp/textest/compile_it4.sh`.

---

## KRITISCH

**Keine Befunde.**

---

## WICHTIG

**Keine Befunde.**

(Insbesondere: Die beiden offenen WICHTIG-Punkte aus Iteration 3 — It.3-A-W1 (Einleitung) und It.3-B-W1 (|f″|-Trick-Steigung) — sind vollständig und ohne Folgefehler behoben; Details unten.)

---

## OPTIONAL (6 Befunde — sämtlich Carry-over bzw. rein informativ, nicht freigaberelevant)

1. **Thema 6, Z. 466/477:** Midpoint-n=1-Fehler als `0.04104` wiedergegeben (originalgetreu); exakt 0.041046 → korrekt gerundet 0.04105. In der Errata-Liste inzwischen dokumentiert ([S. 66], Rubrik Geringfügiges); im Text bewusst belassen — vertretbar (Carry-over It.3-B-O1).
2. **Thema 5, Z. 106–107:** Formulierung der Rundungs-Anmerkung zu f′(7.2) („Die drei Summanden ergeben arithmetisch 2.375; das PDF rundet zulässig auf 2.38") bleibt leicht missverständlich; exakt ist f′(7.2) = 2.3778 → 2.38 (Carry-over It.3-B-O2; faktisch korrekt).
3. **Thema 2, Z. 211:** „knapp unterhalb des double-precision-Epsilons" — 3·10⁻¹⁷ liegt Faktor ≈ 7 unter ε_mach; präziser wäre der Bezug auf ε_mach/2 ≈ 1.1·10⁻¹⁶ (Carry-over It.3-A-O1; sachlich nicht falsch, da auf der log-Achse der Figur argumentiert wird).
4. **Box-Fußnoten** (thema_1 Z. 137, thema_2 Z. 43/68): Fußnoten innerhalb von tcolorboxen erscheinen am Boxrand statt am Seitenfuß; kein Inhaltsverlust (Carry-over It.1–3).
5. **Format-/Stilinkonsistenzen** (thema_3: `[nosep]`, Gedankenstriche, `\tag{Gl.~n}`; Figures 1–38 nur textlich beschrieben, keine TikZ-Reproduktionen) — rein kosmetisch (Carry-over It.1–3).
6. **Build-Hinweis (neu dokumentiert, kein Mangel):** Der Log enthält 12 benigne hyperref-Warnungen „Token not allowed in a PDF string" — Ursache ist Mathematik in zwei Subsection-Titeln (thema_4 Z. 231: $f(x)=x^3-x$; thema_6 Z. 447: $\int\sin(x)dx$); hyperref entfernt die Mathe-Tokens nur aus den PDF-Bookmarks, Dokumentinhalt und ToC sind korrekt. Beide Stellen sind seit Iteration 3 unverändert — **keine Regression** der It.-3-Fixes. Optionaler Fix: `\texorpdfstring{}{}`.

---

## Behebungsstatus der Iteration-3-Auflagen (3/3 umgesetzt, vollständig verifiziert)

| Auflage (It. 3) | Status | Verifikation in dieser Runde |
|---|---|---|
| **(a) It.3-A-W1 — Einleitung, Kursversprechen-Satz** (`zusammenfassung.tex`, Z. 58) | **BEHOBEN** | Der Satz lautet jetzt: „Das Kursversprechen: Der Kurs vermittelt alles Nötige, um mit numerischen Methoden sicher umzugehen (‚everything you need to know to become proficient') und sie in Machine Learning, Data Science und Ingenieursanwendungen (machine learning, data science, and engineering contexts) gewinnbringend einzusetzen." — gegen PDF S. 7 wortgenau abgeglichen: deckungsgleich mit „This course will teach you everything you need to know to become proficient with numerical methods, and how to put them to good use in machine learning, data science, and engineering contexts." ✓. Die zuvor monierte „proficiency"-Dimension ist jetzt enthalten ✓. Der frühere unmarkierte Relativsatz ist als eigener Satz ausgegliedert und korrekt gekennzeichnet: „[Ergänzung: In diesen Feldern beruht praktisch jede Berechnung — vom Training neuronaler Netze bis zur Simulation — auf numerischen Approximationen.]" ✓ (inhaltlich durch S. 9 gedeckt: „training models … simulating complex systems"). Kein Folgefehler. |
| **(b) It.3-B-W1 — thema_5, \|f″\|-Trick-Box, Steigungswert** (`thema_5.tex`, Z. 365–369) | **BEHOBEN** | Neuer Text: „Die Tangente an f′ hat dort Steigung f″(6.1) ≈ −2.98 [Korrektur ggü. Original, S. 54: Die Captions von Fig. 27/28 drucken ≈ ∓2.66 — das ist f″ bei x ≈ 6.0 (f″(6.0) ≈ −2.63); bei x = 6.1 ist f″ ≈ −2.98]; der Ersatz f″ → \|f″\| klappt die Steigung auf ≈ +2.98 um". **Eigene Nachrechnung an der Shekel-Instanz** f(x) = −1/((x−0)²+0.7) − 1.7/((x−4)²+0.2) − 1.1/((x−7)²+0.4) (analytisch über die im Skript/Material angegebene f″-Formel, gegengeprüft per zentralem Differenzenquotienten h = 10⁻⁶): **f″(6.1) = −2.97720 ≈ −2.98 ✓**; f″(6.0) = −2.63041 ≈ −2.63 ✓; der PDF-Wert −2.66 entspricht x ≈ 6.01, die Zuordnung „x ≈ 6.0" im Korrektur-Marker ist zutreffend ✓. Vorzeichenlogik (−2.98 → +2.98 durch \|f″\|) korrekt ✓. Kennzeichnung entspricht exakt der Projektpolicy. Kein Folgefehler; umgebende Box (Gl. 41, DL-Hoffnungen, Denkfrage) unverändert korrekt. |
| **(c) Errata-Nachträge** (`errata_original_pdf.md`) | **BEHOBEN** | Beide von It. 3 Teil B empfohlenen Nachträge vorhanden und fachlich korrekt: „[S. 54] Captions Fig. 27/28: ‚slope ≈ ∓2.66' am Punkt x = 6.1 — tatsächlich f″(6.1) ≈ −2.977 ≈ −2.98; der Wert −2.66 entspricht x ≈ 6.0 (f″(6.0) ≈ −2.63)" ✓ (Werte nachgerechnet, s. o.) sowie „[S. 66] Midpoint-n=1-Fehler: exakt 0.041046 → korrekt gerundet 0.04105 (PDF druckt 0.04104)" ✓ (nachgerechnet: 0.0410458). Beide korrekt in der Rubrik „Rundungen/Geringfügiges" einsortiert. |

**Regressionscheck:** Beide Textänderungen sind lokal begrenzt (ein Satz in der Einleitung; zwei Zeilen in der |f″|-Trick-Box). Alle umgebenden Inhalte erneut gegen das PDF geprüft (Einleitung vollständig gegen S. 3–7; thema_5 vollständig gegen S. 47–56) — keine neuen Abweichungen, keine beschädigten Marker, keine Zahlendreher. Die unveränderten Sections (thema_1–4, thema_6) wurden im Gesamtdurchgang gegengelesen; sämtliche [Korrektur]-Kennzeichnungen decken sich weiterhin mit der Errata-Liste (Errata 1–15 sämtlich korrekt umgesetzt und gekennzeichnet), alle Stichproben-Nachrechnungen (siehe Kopf) bestanden. Iteration-1/2/3-Fixes intakt (u. a. Konsistenz-/Konvergenzbox thema_3, Tabelle 2, Sekanten-/Newton-Ketten, Glättungsbox, T₂/S₂/MC-Boxen, Gl.-47/48-Anmerkungen, Simpson-h-Konvention, x₃ = 6.9907-Anmerkung).

## Kompiliertest (It. 4, gemäß Vorgabe)

- Skript `/tmp/textest/compile_it4.sh` erstellt und mit exakt `bash /tmp/textest/compile_it4.sh` ausgeführt.
- Ergebnis: zweifacher pdflatex-Lauf erfolgreich; `grep -cE '^!' zusammenfassung.log` → **0 Fehler**; Log: „Output written on zusammenfassung.pdf (**61 pages**, 724302 bytes)"; alle Referenzen aufgelöst (keine „undefined"-Meldungen). Einzige Log-Auffälligkeit: die 12 benignen hyperref-Bookmark-Warnungen (siehe OPTIONAL Nr. 6, vorbestehend).

## Zusammenfassung der Befunde

| Kategorie | Anzahl |
|---|---|
| KRITISCH | 0 |
| WICHTIG | 0 |
| OPTIONAL | 6 (5 bekannte Carry-over + 1 informativer Build-Hinweis) |

**Positivbefund:** Vollständigkeit gegen PDF S. 1–71 lückenlos (Motto, Introduction, Gl. 1–51, Algorithmen 1–4, Tabellen 1–3, Figures 1–38 textlich, alle Rand-/Fußnoten inkl. abgebrochener Sätze S. 13/55 als [Anm.] dokumentiert, alle Übungs-/Selbstreflexionsfragen, Recaps, Teaser, Index-Kapitelstand). Kennzeichnungspolicy ([Korrektur ggü. Original, S. n] / [Ergänzung] / [Anm.] / [sic]) jetzt durchgängig ohne Ausnahme eingehalten — der letzte unmarkierte Zusatz (Einleitung) ist beseitigt, der letzte unverifiziert übernommene Originalwert (−2.66) ist korrigiert und markiert. Didaktik (Boxen-Systematik, „In eigenen Worten", Merkboxen, Querbezüge Kap. 1→6) konsistent.

---

## Freigabe-Urteil

**JA — Freigabe ohne Auflagen erteilt.** Die Zusammenfassung ist frei von KRITISCH- und WICHTIG-Befunden. Alle drei Auflagen aus Iteration 3 sind korrekt, vollständig und policy-konform umgesetzt (jeweils unabhängig nachgerechnet bzw. wortgenau gegen das Original-PDF verifiziert); es gibt keine Regressionen. Die sechs OPTIONAL-Punkte sind kosmetischer bzw. dokumentarischer Natur und stehen einer Veröffentlichung nicht entgegen.

*Hinweis: Durch den Kompiliertest wurden die LaTeX-Hilfsdateien (`zusammenfassung.aux/.log/.toc/.pdf`) im `output/`-Ordner aktualisiert; Kompilierskript unter `/tmp/textest/compile_it4.sh`, Verifikationsrechnungen inline per Python ausgeführt.*
