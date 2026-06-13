# Prompt: Alle Themen erklären (Lernskript als PDF)

> **So benutzt du diesen Prompt:** Starte Claude Code im jeweiligen Fach-Ordner
> (z. B. `analysis_2/`, `numerik/`, `logik/` …) und sage einfach:
> *„Schau dir `../prompts/ERKLÄRUNG.md` an und führe es aus.“*
> Alle Pfade in diesem Prompt sind **relativ zum aktuellen Fach-Ordner**.
> Folge den Schritten von oben nach unten – ohne Rückfragen, außer es geht gar nicht anders.

---

## ⛔ Sicherheitsregeln (oberste Priorität)

- **Verändere, verschiebe oder lösche KEINE vorhandenen Dateien oder Ordner.** Alle bestehenden
  Materialien werden **nur gelesen**.
- Du darfst **ausschließlich** in deine **eigenen** Unterordner schreiben (bei Bedarf neu anlegen):
  - `output/erklaerung/` → das **Lernskript** und die **Abfragefragen** (zum Ausfüllen).
  - `results/erklaerung/` → die **Abfrage-Lösungen / Ergebnisse**.
- Bleibe in diesen beiden Unterordnern. Schreibe in **keine** anderen Ordner (auch nicht in
  `output/aufgaben/`, `output/klausuren/` o. Ä. – die gehören anderen Prompts) und in keine vorhandenen
  Materialordner.
- Wenn die Ordner schon existieren: bestehende Dateien darin **nicht überschreiben**, sondern
  fortlaufend weiternummerieren.

---

## Ziel

Erstelle ein **vollständiges, gut verständliches Lernskript** als **PDF**, das **alle Themen** des Fachs
erklärt – plus einen **Abfrage-/Quiz-Teil** zum Selbsttesten.

Das Skript soll **erklären, nicht nur auflisten**: jedes Thema mit Intuition, Definition, den wichtigsten
Sätzen/Formeln, einem durchgerechneten Beispiel und typischen Fehlerquellen.

Der Abfrage-Teil soll mir helfen, das Gelernte **aktiv abzufragen** (Frage → selbst überlegen →
Lösung kontrollieren).

---

## Ablauf

### Schritt 1 – Vorlesungsmaterialien analysieren (nur lesen)

1. Liste **alle** Dateien in `vorlesungs_materialien/` auf und analysiere sie gründlich
   (PDF, Folien, Tafelaufschriebe, Bilder, HTML …).
2. Erstelle eine **vollständige Themenliste / Gliederung** in der Reihenfolge der Vorlesung, inkl. der
   zentralen **Definitionen, Sätze, Formeln, Verfahren** und der verwendeten **Notation** (1:1 übernehmen).

### Schritt 2 – Weitere Materialien analysieren (nur lesen)

1. Liste **alle** Dateien in `andere_materialien/` auf und analysiere sie gründlich
   (Skripte, Zusammenfassungen, Quizze, Notizen, ZIP-Inhalte, Bilder …).
2. Ziehe `openbook/` als **vertiefende Quelle** heran, **falls** vorhanden.
3. Sieh dir vorhandene `übungen/` (bzw. `uebungen/`) und `probeklausuren/` an, um zu erkennen, **welche
   Themen besonders prüfungsrelevant** sind und worauf der Fokus liegen sollte.
4. Leeren oder fehlenden Ordner kurz vermerken und überspringen.

### Schritt 3 – Erklärungen ausarbeiten

Arbeite die Gliederung aus Schritt 1 vollständig durch. Für **jedes Thema**:

- **Intuition / Motivation:** Worum geht es, wozu braucht man das? (in einfachen Worten)
- **Definition(en):** präzise, mit der Notation der Vorlesung.
- **Wichtige Sätze / Formeln / Verfahren:** kurz erklärt, wann/wie man sie anwendet.
- **Durchgerechnetes Beispiel:** mindestens eines, Schritt für Schritt.
- **Typische Fehler / Merkhilfen:** worauf man achten muss.
- Querverweise zu verwandten Themen, wo sinnvoll.

Regeln:
- **Decke wirklich alle Themen** des Stoffs ab – nichts auslassen.
- **Gleiche Notation und Fachsprache** wie in der Vorlesung.
- Erkläre **verständlich und vom Einfachen zum Schweren**; lieber ein Beispiel mehr.
- Erfinde keinen Stoff, der nicht in den Materialien vorkommt.

### Schritt 4 – Abfrage-/Quiz-Teil entwerfen

Erstelle zum Selbsttesten einen Satz **Abfragefragen** über **alle** Themen:

- Pro Thema mehrere Fragen, gemischte Art: kurze **Verständnisfragen**, **Definitionen abfragen**,
  kleine **Rechen-/Beweisaufgaben** und einige **Ankreuz-/Wahr-Falsch-Fragen**.
- Schwierigkeit mischen (leicht → schwer), nach Themen gruppiert.
- Zu **jeder** Frage eine **kurze, korrekte Lösung** (kommt in den separaten Lösungsteil).
- Geeignet zum aktiven Abfragen: erst die Frage, Lösung erst in der separaten Lösungs-Datei.

### Schritt 5 – Als PDF erzeugen

Erzeuge die PDFs in **getrennten** Ordnern:

1. **`output/erklaerung/erklaerung_<NN>.pdf`** – das vollständige Lernskript.
2. **`output/erklaerung/abfrage_<NN>.pdf`** – die Abfragefragen (mit etwas Platz zum Notieren).
3. **`results/erklaerung/abfrage_<NN>_loesung.pdf`** – die Lösungen zu den Abfragefragen.

`<NN>` ist eine fortlaufende Nummer (`01`, `02`, …); **nie eine vorhandene Datei überschreiben**.

**Vorgehen:**

1. Schreibe `erklaerung_<NN>.tex` und `abfrage_<NN>.tex` nach `output/erklaerung/`, und
   `abfrage_<NN>_loesung.tex` nach `results/erklaerung/`.
   - `\documentclass[a4paper,11pt]{article}`, `amsmath`, `amssymb`, `amsthm`.
   - Umlaute: bei **xelatex** `\usepackage{fontspec}`; bei **pdflatex** `\usepackage[utf8]{inputenc}`,
     `\usepackage[T1]{fontenc}`, `\usepackage[ngerman]{babel}`.
   - **Inhaltsverzeichnis** (`\tableofcontents`) und klare Abschnitte (`\section`/`\subsection`) pro Thema.
   - Definitionen/Sätze/Beispiele optisch hervorheben (z. B. `\theoremstyle` + `\newtheorem` oder Boxen).
2. Kompiliere **jedes** Dokument mit **xelatex** (bevorzugt wegen Umlauten), sonst **pdflatex**, jeweils in
   den passenden Ordner, z. B.:
   `xelatex -interaction=nonstopmode -output-directory=output/erklaerung erklaerung_<NN>.tex`
   und `xelatex -interaction=nonstopmode -output-directory=results/erklaerung abfrage_<NN>_loesung.tex`
   (zweimal laufen lassen wegen Inhaltsverzeichnis). Bei Fehlern Log lesen, `.tex` korrigieren, neu kompilieren.
3. Mathematik konsequent in LaTeX-Mathematikumgebungen setzen.

### Schritt 6 – Überprüfen (Pflicht)

1. **PDF-Check:** Bestätige, dass `output/erklaerung/erklaerung_<NN>.pdf`, `output/erklaerung/abfrage_<NN>.pdf`
   **und** `results/erklaerung/abfrage_<NN>_loesung.pdf` existieren, fehlerfrei kompiliert wurden und
   Seitenzahl > 0 haben; das Inhaltsverzeichnis wurde erzeugt.
2. **Vollständigkeit:** Gleiche die Abschnitte mit deiner Themenliste aus Schritt 1 ab – **kein Thema fehlt**;
   auch der Abfrage-Teil deckt alle Themen ab.
3. **Korrektheit:** Prüfe Definitionen, Formeln, durchgerechnete Beispiele **und alle Abfrage-Lösungen** auf
   Richtigkeit. Korrigiere Fehler in der `.tex`-Datei und kompiliere neu, bis alles stimmt.

### Schritt 7 – Zusammenfassung ausgeben

Gib am Ende kurz aus: die abgedeckten Themen (als Liste), die erzeugten Dateien (mit Pfad), Seitenzahlen,
Anzahl der Abfragefragen und das Ergebnis der Überprüfung.

---

## Wichtige Hinweise

- Arbeite **nur** im aktuellen Fach-Ordner; gehe nicht in andere Fächer.
- **Git-Hinweis:** Die Ordner `output/erklaerung/` und `results/erklaerung/` existieren bereits.
  `output/` wird versioniert (kommt auf GitHub), die **Inhalte** von `results/` sind per `.gitignore`
  ausgenommen und bleiben lokal. Das ändert für dich nichts – schreibe einfach wie oben beschrieben.
- Bei sehr viel Stoff darfst du mehrere PDFs pro Themenblock erzeugen
  (`erklaerung_<NN>_<thema>.pdf`) – immer **nur in `output/erklaerung/`** und ohne Überschreiben.
- Du darfst Hilfsdateien (`.tex`, `.aux`, `.toc`, `.log`) erzeugen, aber **nur innerhalb von
  `output/erklaerung/` und `results/erklaerung/`**.
