# Offene Themen — Matrizen / Fortgeschrittene Lineare Algebra

> Stand: Juni 2026. Alles, was du **noch nicht sicher** kannst — als Checkliste.
> Legende: `[ ]` offen · `[~]` in Arbeit (Lernblatt liegt vor, noch nicht bestätigt) · `[x]` sitzt.

---

## A) Grundlagen — noch festigen (lernblatt-2 deckt das ab)

Auf lernblatt-1 falsch oder leer; lernblatt-2 erklärt es gezielt. Nach dem Ausfüllen + Check werden die zu `[x]`.

- [~] **Eigenwerte & Eigenvektoren** — charakteristische Gleichung `det(A−λE)=0`, Eigenvektor lösen (war ganz leer)
- [~] **Diagonalisierung A=SDS⁻¹ & Potenz Aᵏ** — über Eigenwerte/-vektoren (war leer)
- [~] **Gram-Schmidt → QR** — Norm `‖a‖=√(a₁²+a₂²)`, Projektion (Frage: „woher kommt die 5?")
- [~] **Definitheit klassifizieren** — auf **Vorzeichen von a** achten, nicht nur Determinante (B/C falsch)
- [~] **Konzept-Fakten** — Spektralsatz (symmetrisch ⇒ diagonalisierbar), `AAᵀ`/`AᵀA` immer symmetrisch
- [~] **Orthogonale Matrizen** — `det Q=±1` (Drehung/Spiegelung) & Längenerhalt rechnen
- [~] **Vier Unterräume** — Dimensionen (`dim N = n−r` usw.) & Nullraum-Basis (RZSF kannst du)
- [~] **det(cA) = cⁿ·det A** — der Exponent (du hattest `det(3A)=3·5` statt `3³·5`)

---

## B) Noch gar nicht behandelt — kommt in lernblatt-3 / 4

Diese Aufbau-Themen brauchen erst sicheres Fundament (Eigenwerte + Orthogonalität).

- [ ] **SVD** (Singulärwertzerlegung) — volle & reduzierte Form, `A = UΣVᵀ`, Singulärwerte aus `AᵀA`
- [ ] **Spektralzerlegung 3×3** — `A = QΛQᵀ` für symmetrische Matrizen, volle Rechnung
- [ ] **Cholesky-Zerlegung** — `A = LLᵀ` für symmetrisch positiv definite Matrizen
- [ ] **Pseudoinverse & Ausgleichsrechnung** — `A⁺ = (AᵀA)⁻¹Aᵀ`, überbestimmte Systeme bestmöglich lösen
- [ ] **Lineare Regression & Deutung** — Designmatrix, Normalengleichung, R² und p-Wert interpretieren
- [ ] **PCA (Hauptkomponentenanalyse)** — Daten zentrieren, Kovarianzmatrix, erste Hauptkomponente, Varianzanteil
- [ ] **LoRA / beste Rang-k-Näherung** — `A_k = Σ σᵢ uᵢ vᵢᵀ`, Approximationsfehler, Speicherersparnis
- [ ] **Hyperebene, Abstand & Margin-Classifier** — Normalenvektor, Abstand Punkt–Ebene, trennende Ebene, Margin
- [ ] **Innere Produkte & Mahalanobis-Abstand** — `⟨x,y⟩=xᵀAy`, Norm bzgl. A, `√(xᵀΣ⁻¹x)`
- [ ] **Untervektorraum-Test** — Kriterien: `0∈U`, abgeschlossen unter + und ·
- [ ] **LU mit Zeilentausch (PA=LU)** — Permutationsmatrix, warum Pivot 0 ein Problem ist
- [ ] **Finite Differenzen — die vier Matrizen** — `K, T, B, C`; welche invertierbar/positiv definit/singulär
- [ ] **Beweise** — `(AB)⁻¹ = B⁻¹A⁻¹` und `(Aᵀ)⁻¹ = (A⁻¹)ᵀ`

---

## ✅ Schon sicher (zum Vergleich — kommt nicht mehr dran)

Lösbarkeit LGS / Gauß · Sarrus-Determinante & Spur · 2×2-Inverse · RZSF/Rang · CR-Zerlegung (mechanisch) ·
det-Grundregeln (`det AB`, `det A⁻¹`, `det Aᵀ`, `det Aᵏ`)
