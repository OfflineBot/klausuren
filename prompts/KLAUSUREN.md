# Prompt: Weitere Probeklausuren erstellen (PDF)

> **So benutzt du diesen Prompt:** Starte Claude Code im jeweiligen Fach-Ordner
> (z. B. `analysis_2/`, `numerik/`, `logik/` …) und sage einfach:
> *„Schau dir `../prompts/KLAUSUREN.md` an und führe es aus.“*
> Alle Pfade in diesem Prompt sind **relativ zum aktuellen Fach-Ordner**.
> Folge den Schritten von oben nach unten – ohne Rückfragen, außer es geht gar nicht anders.

---

## ⛔ Sicherheitsregeln (oberste Priorität)

- **Verändere, verschiebe oder lösche KEINE vorhandenen Dateien oder Ordner.** Alle bestehenden
  Materialien werden **nur gelesen**.
- Du darfst **ausschließlich** in deine **eigenen** Unterordner schreiben (bei Bedarf neu anlegen):
  - `output/klausuren/` → die **Probeklausur zum Ausfüllen** (ohne Lösung).
  - `results/klausuren/` → die **Musterlösung / Ergebnisse**.
- Bleibe in diesen beiden Unterordnern. Schreibe in **keine** anderen Ordner (auch nicht in
  `output/aufgaben/`, `output/erklaerung/` o. Ä. – die gehören anderen Prompts) und insbesondere **nicht**
  in den vorhandenen Ordner `probeklausuren/` – dieser wird nur gelesen.
- Wenn die Ordner schon existieren: bestehende Dateien darin **nicht überschreiben**, sondern
  fortlaufend weiternummerieren.

---

## Ziel

Erstelle eine neue, vollständige **Probeklausur** als **PDF zum Ausfüllen** – plus eine separate
**Lösungs-PDF**. Gleicher Aufbau, Umfang, Niveau, gleiche Themenabdeckung, Punkteverteilung und
Zeitvorgabe wie die echte Klausur.

---

## Ablauf

### Schritt 1 – Probeklausuren analysieren (nur lesen)

1. Liste **alle** Dateien in `probeklausuren/` auf und analysiere jede (auch Lösungen) gründlich.
2. Achte auf: **Aufbau/Reihenfolge der Aufgaben, Anzahl der Aufgaben, Punkteverteilung
   (Gesamt + pro Aufgabe), Zeitvorgabe, Aufgabentypen** (Beweis, Rechnung, Multiple Choice,
   Modellierung, Ankreuzen …), **Formulierungsstil** und erlaubte **Hilfsmittel**.
3. Beziehe zusätzliche Übungsklausuren aus `vorlesungs_materialien/` oder `übungen/` mit ein, falls vorhanden.
4. Falls **keine** Probeklausur existiert: ein plausibles Klausurformat aus Stoff und Übungen rekonstruieren
   und das im Output vermerken.

### Schritt 2 – Vorlesungsmaterialien analysieren (nur lesen)

1. Liste **alle** Dateien in `vorlesungs_materialien/` auf und analysiere sie gründlich.
2. Erstelle eine Übersicht über **Themen, Definitionen, Sätze, Formeln, Verfahren** und die **Notation**
   (übernimm sie später 1:1). Ermittle die klausurrelevanten und häufig geprüften Themen.

### Schritt 3 – Weitere Materialien analysieren (nur lesen)

1. Liste **alle** Dateien in `andere_materialien/` auf und analysiere sie gründlich
   (Skripte, Zusammenfassungen, Quizze, Notizen, ZIP-Inhalte, Bilder …) – hier stecken oft Hinweise
   auf Prüfungsschwerpunkte.
2. Ziehe ergänzend `openbook/` heran, **falls** vorhanden.
3. Leeren oder fehlenden Ordner kurz vermerken und überspringen.

### Schritt 4 – Neue Probeklausur entwerfen

- **Gleiche Struktur** wie die echten Probeklausuren (Anzahl Aufgaben, Reihenfolge, Aufgabentypen).
- **Gleiche Gesamtpunktzahl und Punkteverteilung**; jede Aufgabe mit Punktangabe.
- **Zeitvorgabe** übernehmen (falls bekannt).
- **Repräsentative Themenabdeckung** über den klausurrelevanten Stoff – nicht nur ein Thema.
- **Gleiche Notation und Fachsprache** wie in der Vorlesung.
- **Keine Kopien** – eigenständige neue Aufgaben im gleichen Stil und Niveau.
- Eine vollständige, nachvollziehbare **Musterlösung** zu jeder Aufgabe (mit Punktevergabe pro Schritt,
  falls die Originale das so machen).

### Schritt 5 – Als PDF erzeugen

Erzeuge **zwei** PDFs in **getrennten** Ordnern:

1. **`output/klausuren/probeklausur_<NN>.pdf`** – die Klausur mit Kopf (**Name**, **Datum**,
   **Bearbeitungszeit**, **Gesamtpunkte**, **Hilfsmittel**) und **großzügigem Platz zum handschriftlichen
   Ausfüllen** nach jeder Aufgabe.
2. **`results/klausuren/probeklausur_<NN>_loesung.pdf`** – die vollständigen Musterlösungen.

`<NN>` ist eine fortlaufende Nummer (`01`, `02`, …); **nie eine vorhandene Datei überschreiben**.

**Vorgehen zur PDF-Erzeugung:**

1. Schreibe das Klausur-Dokument `probeklausur_<NN>.tex` nach `output/klausuren/` und das Lösungs-Dokument
   `probeklausur_<NN>_loesung.tex` nach `results/klausuren/`.
   - `\documentclass[a4paper,11pt]{article}`, `amsmath`, `amssymb`.
   - Umlaute: bei **xelatex** `\usepackage{fontspec}`; bei **pdflatex** `\usepackage[utf8]{inputenc}`,
     `\usepackage[T1]{fontenc}`, `\usepackage[ngerman]{babel}`.
   - Kopf der Klausur mit Feldern Name/Datum und der Tabelle Aufgabe → Punkte (zum Eintragen).
2. **Platz zum Ausfüllen**: nach jeder Aufgabe abhängig von Punkten/Aufwand Leerraum lassen
   (`\vspace{...}`, mehr Platz bei mehr Punkten); bei Multiple-Choice die Ankreuzkästchen einbauen.
3. Kompiliere mit **xelatex** (bevorzugt), sonst **pdflatex**, jeweils in den passenden Ordner:
   `xelatex -interaction=nonstopmode -output-directory=output/klausuren probeklausur_<NN>.tex`
   und `xelatex -interaction=nonstopmode -output-directory=results/klausuren probeklausur_<NN>_loesung.tex`
   (zweimal laufen lassen, falls Referenzen). Bei Fehlern Log lesen, `.tex` korrigieren, neu kompilieren.
4. Mathematik konsequent in LaTeX-Mathematikumgebungen setzen.

### Schritt 6 – Überprüfen (Pflicht)

1. **PDF-Check:** Bestätige, dass `output/klausuren/probeklausur_<NN>.pdf` und
   `results/klausuren/probeklausur_<NN>_loesung.pdf` existieren, fehlerfrei kompiliert wurden und
   Seitenzahl > 0 haben.
2. **Inhaltliche Prüfung:** Rechne **jede** Musterlösung unabhängig nach bzw. überprüfe jeden Beweis.
   Korrigiere Fehler in der `.tex`-Datei und kompiliere neu, bis alle Lösungen korrekt sind.
3. **Format-Check:** Punktesumme stimmt mit der angegebenen Gesamtpunktzahl überein; die Klausur ist in der
   angegebenen Zeit **realistisch lösbar**; jede Aufgabe hat genau eine Lösung; Notation wie in der Vorlesung.

### Schritt 7 – Zusammenfassung ausgeben

Gib am Ende kurz aus: erkanntes Klausurformat (Punkte, Zeit, Aufgabenanzahl), abgedeckte Themen,
erzeugte Dateien (mit Pfad) und das Ergebnis der Überprüfung.

---

## Wichtige Hinweise

- Arbeite **nur** im aktuellen Fach-Ordner; gehe nicht in andere Fächer.
- Erfinde keinen Stoff, der nicht zur Vorlesung passt – im Zweifel an den Materialien orientieren.
- Du darfst Hilfsdateien (`.tex`, `.aux`, `.log`) erzeugen, aber **nur innerhalb von `output/klausuren/`
  und `results/klausuren/`**.
