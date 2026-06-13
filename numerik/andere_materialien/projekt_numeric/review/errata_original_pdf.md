# Errata des Original-PDFs (vom Orchestrator durch Nachlesen verifiziert)

Diese Liste dokumentiert Stellen, an denen das Original-Skript („Numerical Methods", Schutera, Stand 2026-05-06, explizit „unfinished lecture notes") nachweislich Fehler enthält. Vorgehen in allen erzeugten Materialien: **fachlich korrekte Version verwenden, Abweichung vom Original als „[Korrektur ggü. Original, S. n]" kennzeichnen.** Diese Liste ist die verbindliche Referenz für Synthese, Zusammenfassung, Übungsblätter und Reviews.

## Verifizierte Originalfehler (Rechnung/Inhalt)

1. **[S. 32] Konvergenzrechnung, beide Fälle:** PDF druckt Endwert `= 0.1599`; korrekt ist |−0.84147 − (−1)| = **0.15853** (beide Fälle h=1 und h=0.2). Zudem fehlen in den Umformungsketten die Relationszeichen (Layout), und im h=0.2-Block steht einmal fälschlich f̂₁(−1.2) statt f̂₀.₂(−1.2).
2. **[S. 31] Stabilitätsrechnung h=1:** Indexwechsel s_{h=1,x=−1} → s_{h=1,x=0} innerhalb derselben Rechnung; gemeint ist durchgängig derselbe Fall (x̃ = x + 0.25, x = −1). Ergebnis s ≈ 0 ist korrekt.
3. **[S. 37] Newton an sin(x), x₂-Schritt:** PDF druckt `0.0008/−0.9999`; tatsächlich sin(3.125) ≈ **0.01659**, cos(3.125) ≈ −0.99986. Damit x₂ = 3.125 − 0.01659/(−0.99986) ≈ 3.125 + 0.0166 ≈ **3.1416** ✓ (Endergebnis stimmt, Zwischenwert nicht).
4. **[S. 38] Gl. (20):** Layoutfehler — „+ f(xₙ)" ist hinter die Nebenbedingung gerutscht. Korrekt: f(x) ≈ **f(xₙ) + f′(xₙ)·(x − xₙ)** für x nahe xₙ. (Bestätigt durch die Folgezeile 0 = f(xₙ) + f′(xₙ)(x_{n+1} − xₙ).)
5. **[S. 45] Sekanten-Handrechnung an f(x) = x³ − x, x₀=1.2, x₁=1.4:** Mehrere falsche Zahlenwerte. Korrekt: f(1.2) = **0.528** (PDF: 0.128), f(1.4) = **1.344** (PDF: 0.744). Korrekte Iteration: x₂ = 1.4 − 1.344·(0.2/0.816) ≈ **1.0706**; weitere Schritte entsprechend neu zu rechnen. Die PDF-Kette (1.159, 1.011) beruht auf den falschen Werten. Methodik (Gl. 34) ist korrekt.
6. **[S. 53] „Newton's method finds points where f″(x) = 0":** Druckfehler — Newton auf f′ findet Punkte mit **f′(x) = 0** (Extremstellen); der anschließende Second-Derivative-Test klassifiziert sie über f″. 
7. **[S. 64] Composite Simpson:** In der Herleitung steht pro Teilintervall-Paar der Faktor h/6; korrekt ist bei Gitterweite h und Paarbreite 2h der Faktor **2h/6 = h/3** pro Paar. Die Endformel h/3·[f(x₀) + 4Σ_{i ungerade} f(xᵢ) + 2Σ_{i gerade} f(xᵢ) + f(xₙ)] ist korrekt; nur die Zwischenzeilen sind inkonsistent.
8. **[S. 66] Mittelpunktsregel n=2:** PDF: Î ≈ −0.927228, Fehler 0.02922. Korrekt: Î = 0.5·[sin(−1.75) + sin(−1.25)] = 0.5·(−1.932971) ≈ **−0.966485**, Fehler |Ĩ − Î| ≈ **0.010036**. (Qualitative Aussage „Fehler sinkt mit n" bleibt richtig.)

9. **[S. 44] Newton-Handrechnung an f(x) = x³ − x, x₀ = 1.4:** Mehrere falsche Zwischenwerte. Korrekt: x₁ = 1.4 − 1.344/4.88 ≈ **1.1246** (PDF: 1.127); x₂-Zähler f(x₁) ≈ **0.297** (PDF: 0.432), damit x₂ ≈ **1.0181** (PDF: 0.976); x₃ ≈ **1.0005** (PDF: 1.014). (Selbstkonsistente Kette aus x₁ = 1.1246; die zunächst notierten Werte 1.0186/1.0009 entstanden aus Weiterrechnung mit dem PDF-gerundeten x₁ = 1.127.) Die korrekte Newton-Folge konvergiert monoton von oben gegen die Wurzel x = 1; die PDF-Kette springt fälschlich unter 1. Methodik korrekt. (Vom Orchestrator nachgerechnet; vom Thema-4-Autor unabhängig gefunden.)

10. **[S. 67] Trapezregel T₂:** PDF druckt T₂ ≈ −0.927228 (identisch mit dem Midpoint-n=2-/MC-Wert — offenbar Kopierfehler). Die eigene gedruckte Formel ergibt 0.25·[−0.90930 + 2(−0.99749) + (−0.84147)] = 0.25·(−3.74575) ≈ **−0.93644**, Fehler |Ĩ − T₂| ≈ **0.02001**. Damit ist auch die Aussage „The error is the same as the midpoint rule with n = 2" hinfällig (sie beruht auf zwei falschen Werten).
11. **[S. 67] Simpson S₂:** PDF druckt S₂ ≈ −0.9564491424 (= exakter Integralwert) und Fehler ≈ 0 („Simpson's rule is exact for this particular integral"). Die eigene Formel ergibt (1/6)·[−0.90930 + 4(−0.99749) + (−0.84147)] = (1/6)·(−5.74073) ≈ **−0.956788**, Fehler ≈ **3.4·10⁻⁴** — sehr klein, aber nicht null. Simpson ist exakt für Polynome bis Grad 3, nicht für sin(x); die qualitative Aussage (deutlich genauer als Midpoint/Trapez) bleibt richtig.
    - Folgeänderung [S. 68]: „which is the same as the midpoint method" (MC-Fehler 0.02922 vs. Midpoint) beruht auf dem falschen Midpoint-Wert aus Erratum 8; der MC-Wert −0.927228 und Fehler 0.02922 selbst sind korrekt.

12. **[S. 32] Konsistenzrechnung h=0.2:** PDF nutzt f̂₀.₂(−1.2) = −0.94898; das ist sin(−1.25), aber −1.25 ist kein Gitterpunkt des h=0.2-Gitters. Korrekt: f̂₀.₂(−1.2) = sin(−1.2) = **−0.93204**, damit c₀.₂ ≥ |−0.93204 − (−1)| = **0.06796** (PDF: 0.05102). Die qualitative Aussage „Consistency improves with smaller step sizes" bleibt richtig (0.06796 < 0.15853). (Von Review-Iteration 1 gefunden, vom Orchestrator gegen S. 32 verifiziert.)

13. **[S. 59] Glättungsbeispiel an f(x) = sin(x) + sin(2πx), x = −0.4:** PDF setzt f(−0.5) = −1.14973 und f(−0.3) = −0.97720 ein — das sind tatsächlich f(−0.2) bzw. f(−0.4). Korrekt: f(−0.5) = sin(−0.5) + sin(−π) = **−0.47943**, f(−0.3) = sin(−0.3) + sin(−0.6π) = **−1.24658**; damit geglättet f(−0.4) ≈ (−0.47943 − 1.24658)/2 = **−0.86300** (PDF: −1.06347) und h·f(−0.4) ≈ **−0.17260** (PDF: −0.11285). Mit den korrekten Werten wird die Skript-Aussage „correction towards higher losses" (−0.86300 > −0.97720) erst konsistent; mit den PDF-Werten widerspräche das Ergebnis ihr. Gl. (43) selbst (f(−0.4) = −0.97720) ist korrekt. (Von Review-Iteration 1 gefunden, vom Orchestrator gegen S. 59 verifiziert.)
14. **[S. 42] Tabelle 2 (Newton für √2, x₀ = 2):** Zeile n=4: PDF druckt |e₄| = 4.5×10⁻¹² — das ist das Residuum |x₄² − 2|, nicht der Fehler |x₄ − √2| ≈ **1.6×10⁻¹²** (Spaltendefinition!). Zudem Zeile n=3: korrekt |e₃| = **2.12×10⁻⁶** (PDF: 2.13×10⁻⁶). Übrige Zeilen korrekt. (Von Review-Iteration 1 gefunden, vom Orchestrator gegen S. 42 verifiziert.)
15. **[S. 68] Monte-Carlo-Stichprobenvarianz:** Aus den vier Samples folgt σ_f² ≈ **0.003018**, σ_f ≈ **0.05493**, SE ≈ **0.02747** (PDF: 0.003036/0.05512/0.02756 — aus gerundeten Zwischenwerten entstanden, ~0.6 % daneben). Korrekte Werte verwenden, Abweichungsquadrate zeigen.

## Rundungen / Geringfügiges (kein Handlungsbedarf, ggf. Fußnote)

- **[S. 65, Gl. 48]** „unbiased … for the number of N → ∞": begrifflich unsauber — Erwartungstreue gilt für jedes endliche N; N → ∞ betrifft Konsistenz/Konvergenz. In Materialien mit klarstellender Anmerkung wiedergeben.
- **[S. 65, Gl. 47]** PDF druckt links „I =" — gemeint ist der Schätzer Î_N (das exakte Integral I ist Gl. 46; Gl. 48 verwendet selbst Î_N). Mit Anmerkung wiedergeben.
- **[S. 49]** Shekel-Newton: x₃ exakt ≈ 6.9907 (PDF rundet 7.00) — Minimum liegt durch Foxhole-Termüberlappung knapp unter 7.
- **[S. 36]** Grid Search: f(2.5) korrekt gerundet 0.598 (sin(2.5) = 0.598472; PDF: 0.599).
- **[S. 67]** Monte-Carlo-Samples: sin(−1.95) = −0.9289597 → −0.92896 (PDF: −0.92895; Folgewerte konsistent mit dem gedruckten Wert).
- **[S. 54]** Captions Fig. 27/28: „slope ≈ ∓2.66" am Punkt x = 6.1 — tatsächlich f″(6.1) ≈ −2.977 ≈ −2.98; der Wert −2.66 entspricht x ≈ 6.0 (f″(6.0) ≈ −2.63). Markerposition und Steigungswert sind im Original inkonsistent gepaart. (Vom Orchestrator nachgerechnet.)
- **[S. 66]** Midpoint-n=1-Fehler: exakt 0.041046 → korrekt gerundet 0.04105 (PDF druckt 0.04104, abgeschnitten statt gerundet).

- **[S. 31]** „Which shows ill-conditioning with κ ≤ 0.247": Der berechnete Maximalwert ist 0.2474, also ist „≤ 0.247" numerisch unsauber (korrekt: κ ≈ 0.2474 bzw. ≤ 0.25); zudem belegt eine obere Schranke allein keine schlechte Konditionierung. In Materialien: κ ≈ 0.2474 verwenden, kurz anmerken.

- **[S. 49]** f′(7.2): Summanden ergeben 2.375, PDF rundet auf 2.38 — zulässige Rundung.
- **[S. 59]** „destructive inference" → gemeint „interference".
- Diverse Tippfehler: „Excercises", „Newton-Rhapson" (als Name historisch erklärt, Schreibweise „Raphson"), „understnad", „Conditiioning", „Intgration", „inifinitely", „independant", „end whilereturn" (Algorithmen-Layoutartefakt).

## Offene Fragen an den Nutzer (am Ende berichten)

- [S. 13] Eine Randnotiz bricht mitten im Satz ab („in a sense that it ."). Inhalt nicht rekonstruierbar — im Material weggelassen, da kein vollständiger Gedanke.
- [S. 55] Abgebrochener Satz bei „Noise and landscape engineering" / „mini-batches," sowie Fußnotenrest „foxhole.2" — Inhalt nur teilweise rekonstruierbar.
- [S. 70] Das Skript verweist auf ein Folgekapitel (Stabilität numerischer Methoden), das im PDF nicht enthalten ist — Materialien decken daher nur Kap. 1–6 ab.
