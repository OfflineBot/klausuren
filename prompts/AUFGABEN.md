# Prompt: Weitere Übungsaufgaben erstellen (PDF)

> **So benutzt du diesen Prompt:** Starte Claude Code im jeweiligen Fach-Ordner
> (z. B. `analysis_2/`, `numerik/`, `logik/` …) und sage einfach:
> *„Schau dir `../prompts/AUFGABEN.md` an und führe es aus.“*
> Alle Pfade in diesem Prompt sind **relativ zum aktuellen Fach-Ordner**.
> Folge den Schritten von oben nach unten – ohne Rückfragen, außer es geht gar nicht anders.

---

## ⛔ Sicherheitsregeln (oberste Priorität)

- **Verändere, verschiebe oder lösche KEINE vorhandenen Dateien oder Ordner.** Alle bestehenden
  Materialien werden **nur gelesen**.
- Du darfst **ausschließlich** in deine **eigenen** Unterordner schreiben (bei Bedarf neu anlegen):
  - `output/aufgaben/` → die **Aufgaben zum Ausfüllen** (ohne Lösung).
  - `results/aufgaben/` → die **Lösungen / Ergebnisse**.
- Bleibe in diesen beiden Unterordnern. Schreibe in **keine** anderen Ordner (auch nicht in
  `output/klausuren/`, `output/erklaerung/` o. Ä. – die gehören anderen Prompts) und in keine
  vorhandenen Materialordner (`vorlesungs_materialien/`, `andere_materialien/`, `openbook/`,
  `übungen/`, `probeklausuren/` …).
- Wenn die Ordner schon existieren: bestehende Dateien darin **nicht überschreiben**, sondern
  fortlaufend weiternummerieren.

---

## Ziel

Erstelle neue, klausurnahe **Übungsaufgaben** als **PDF zum Ausfüllen** – plus eine separate
**Lösungs-PDF**. Die Aufgaben müssen exakt zum gelehrten Stoff passen, im Niveau der Übung/Klausur
liegen und vollständig korrekt gelöst sein.

---

## Ablauf

### Schritt 1 – Vorlesungsmaterialien analysieren (nur lesen)

1. Liste **alle** Dateien in `vorlesungs_materialien/` auf und analysiere sie gründlich
   (PDF, Folien, Tafelaufschriebe, Bilder, HTML …).
2. Erstelle dir eine Übersicht über **Themen/Kapitel, Definitionen, Sätze, Formeln, Verfahren**,
   die verwendete **Notation** (übernimm sie später 1:1) und typische **Aufgabentypen**.

### Schritt 2 – Weitere Materialien analysieren (nur lesen)

1. Liste **alle** Dateien in `andere_materialien/` auf und analysiere sie gründlich
   (Skripte, Zusammenfassungen, Quizze, Notizen, ZIP-Inhalte, Bilder …) – hier stecken oft
   zusätzliche Beispiele und Prüfungsschwerpunkte.
2. Ziehe ergänzend `openbook/` heran, **falls** vorhanden.
3. Leeren oder fehlenden Ordner kurz vermerken und überspringen.

### Schritt 3 – Bestehende Übungsaufgaben analysieren (nur lesen, falls vorhanden)

1. Prüfe `übungen/` (alternativ `uebungen/`) und `probeklausuren/` auf vorhandene Aufgaben.
2. Achte auf **Aufgabenformat, Schwierigkeitsgrad, Umfang, Formulierungsstil** und welche Themen
   besonders oft drankommen.
3. Falls keine Übungsaufgaben existieren: allein an den Vorlesungs- und weiteren Materialien orientieren.

### Schritt 4 – Neue Übungsaufgaben entwerfen

- **Mindestens 8–12 Aufgaben** (oder mehr), die die wichtigsten Themen abdecken.
- Schwierigkeit mischen und kennzeichnen: **leicht / mittel / schwer**.
- **Gleiche Notation und Fachsprache** wie in der Vorlesung.
- **Keine Kopien** – eigenständige, neue Varianten.
- Zu **jeder** Aufgabe eine vollständige, nachvollziehbare **Musterlösung** mit allen Schritten.

### Schritt 5 – Als PDF erzeugen

Erzeuge **zwei** PDFs in **getrennten** Ordnern:

1. **`output/aufgaben/aufgaben_<NN>.pdf`** – nur die Aufgabenstellungen, **mit großzügigem Platz zum
   handschriftlichen Ausfüllen** nach jeder Aufgabe (siehe unten).
2. **`results/aufgaben/loesungen_<NN>.pdf`** – die vollständigen Musterlösungen.

`<NN>` ist eine fortlaufende Nummer (`01`, `02`, …); **nie eine vorhandene Datei überschreiben**.

**Vorgehen zur PDF-Erzeugung:**

1. Schreibe das Aufgaben-Dokument `aufgaben_<NN>.tex` nach `output/aufgaben/` und das Lösungs-Dokument
   `loesungen_<NN>.tex` nach `results/aufgaben/`.
   - Nutze `\documentclass[a4paper,11pt]{article}`, `amsmath`, `amssymb`.
   - Für Umlaute: bei **xelatex** `\usepackage{fontspec}`; bei **pdflatex** `\usepackage[utf8]{inputenc}`
     und `\usepackage[T1]{fontenc}`, `\usepackage[ngerman]{babel}`.
2. **Platz zum Ausfüllen** im Aufgaben-PDF: nach jeder Aufgabe abhängig vom Aufwand Leerraum lassen,
   z. B. `\vspace{5cm}` bzw. für Rechenaufgaben mehr. Optional Linien zum Schreiben (z. B. via
   `\hrulefill` in Wiederholung). Kopfzeile mit Feldern **Name** und **Datum**.
3. Kompiliere mit **xelatex** (bevorzugt wegen Umlauten), sonst **pdflatex**, jeweils in den passenden Ordner:
   `xelatex -interaction=nonstopmode -output-directory=output/aufgaben aufgaben_<NN>.tex`
   und `xelatex -interaction=nonstopmode -output-directory=results/aufgaben loesungen_<NN>.tex`
   (zweimal laufen lassen, falls Referenzen). Bei Fehlern Log lesen, `.tex` korrigieren, neu kompilieren.
4. Mathematik konsequent in LaTeX-Mathematikumgebungen setzen.

### Schritt 6 – Überprüfen (Pflicht)

1. **PDF-Check:** Bestätige, dass `output/aufgaben/aufgaben_<NN>.pdf` und
   `results/aufgaben/loesungen_<NN>.pdf` existieren und ohne Fehler kompiliert wurden. Prüfe Seitenzahl > 0.
2. **Inhaltliche Prüfung:** Rechne **jede** Musterlösung unabhängig nach bzw. überprüfe jeden Beweis.
   Korrigiere Fehler in der `.tex`-Datei und kompiliere neu, bis alle Lösungen korrekt sind.
3. **Konsistenz:** Jede Aufgabe im Aufgaben-PDF hat genau eine Lösung im Lösungs-PDF; Nummerierung passt;
   Notation entspricht der Vorlesung.

### Schritt 7 – Zusammenfassung ausgeben

Gib am Ende kurz aus: abgedeckte Themen, Anzahl Aufgaben, erzeugte Dateien (mit Pfad) und das Ergebnis
der Überprüfung.

---

## Wichtige Hinweise

- Arbeite **nur** im aktuellen Fach-Ordner; gehe nicht in andere Fächer.
- **Git-Hinweis:** Die Ordner `output/aufgaben/` und `results/aufgaben/` existieren bereits.
  `output/` wird versioniert (kommt auf GitHub), die **Inhalte** von `results/` sind per `.gitignore`
  ausgenommen und bleiben lokal. Das ändert für dich nichts – schreibe einfach wie oben beschrieben.
- Erfinde keinen Stoff, der nicht zur Vorlesung passt – im Zweifel an den Materialien orientieren.
- Du darfst Hilfsdateien (`.tex`, `.aux`, `.log`) erzeugen, aber **nur innerhalb von `output/aufgaben/`
  und `results/aufgaben/`**.
