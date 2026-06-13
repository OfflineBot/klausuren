# Prompt: Weitere Übungsaufgaben erstellen

> **Verwendung:** Dieses Fenster wurde in einem Fach-Ordner gestartet (z. B. `analysis_2/`, `numerik/`, `logik/` …).
> Alle Pfade in diesem Prompt sind **relativ zum aktuellen Fach-Ordner**.
> Starte, indem du diese Datei liest und den Anweisungen Schritt für Schritt folgst.

---

## Ziel

Erstelle neue, klausurnahe **Übungsaufgaben** für das aktuelle Fach – basierend auf den vorhandenen
Vorlesungsmaterialien und (falls vorhanden) bestehenden Übungsaufgaben.

Die Aufgaben sollen mir beim Lernen für die Klausur helfen: Sie müssen inhaltlich **exakt** zum gelehrten
Stoff passen, im gleichen Schwierigkeitsgrad wie Klausur/Übung liegen und **mit ausführlichen Lösungen** versehen sein.

---

## Ablauf

### Schritt 1 – Vorlesungsmaterialien analysieren

1. Gehe in den Ordner `vorlesungs_materialien/` und liste **alle** Dateien auf.
2. Lies und analysiere die Materialien (PDF, Folien, Tafelaufschriebe, Bilder, HTML …) gründlich.
3. Erstelle dir intern eine Übersicht über:
   - die **Themen / Kapitel** und ihre Reihenfolge,
   - die zentralen **Definitionen, Sätze, Formeln und Verfahren**,
   - die verwendete **Notation** (übernimm sie später 1:1),
   - typische **Aufgabentypen**, die im Stoff vorkommen.

### Schritt 1b – Weitere Materialien analysieren

1. Gehe in den Ordner `andere_materialien/` und liste **alle** Dateien auf. Analysiere sie gründlich
   (Skripte, Zusammenfassungen, Quizze, Notizen, ZIP-Inhalte, Bilder …) – hier stecken oft zusätzliche
   Beispiele, Schwerpunkte und Aufgabentypen.
2. Ziehe ergänzend `openbook/` heran, **falls** dort etwas vorhanden ist.
3. Falls ein Ordner leer ist oder fehlt: kurz vermerken und überspringen.

### Schritt 2 – Bestehende Übungsaufgaben analysieren (falls vorhanden)

1. Prüfe, ob es einen Übungsordner gibt: `übungen/` (alternativ `uebungen/`).
2. Prüfe außerdem `probeklausuren/` auf vorhandene Aufgaben/Klausuren.
3. Falls vorhanden: analysiere diese Aufgaben und achte auf:
   - **Aufgabenformat** (Beweis, Rechenaufgabe, Multiple Choice, Modellierung …),
   - **Schwierigkeitsgrad** und typischen Umfang einer Aufgabe,
   - **Punkteverteilung** und Formulierungsstil,
   - welche Themen **besonders oft** geprüft werden.
4. Falls **keine** Übungsaufgaben existieren: orientiere dich allein an den Vorlesungsmaterialien und an den
   typischen Aufgabentypen des Fachs.

### Schritt 3 – Neue Übungsaufgaben erstellen

Erstelle neue Aufgaben, die sich am erkannten Stil und Niveau orientieren. Halte dich an folgende Regeln:

- **Decke die wichtigsten Themen** des Stoffs ab (nicht nur eines).
- Mische die Schwierigkeitsgrade: **leicht → mittel → schwer** (kennzeichne jede Aufgabe).
- Verwende die **gleiche Notation und Fachsprache** wie in der Vorlesung.
- **Keine Kopien** bestehender Aufgaben – eigenständige, neue Varianten.
- Zu **jeder** Aufgabe gehört eine **vollständige, nachvollziehbare Musterlösung** mit Rechen-/Beweisschritten
  und kurzer Begründung.
- Pro Durchlauf **mindestens 8–12 Aufgaben** (oder mehr, wenn der Stoff es hergibt).

### Schritt 4 – Output schreiben

1. Lege den Ordner `claude_übungsaufgaben/` im aktuellen Fach-Ordner an (falls noch nicht vorhanden).
2. Schreibe die Aufgaben als **Markdown-Datei(en)** dorthin.
   - Pro Themengebiet eine eigene Datei ist erlaubt und erwünscht, z. B.
     `claude_übungsaufgaben/01_<thema>.md`.
   - **Überschreibe keine** bereits vorhandenen Dateien – nummeriere fortlaufend weiter.
3. Verwende pro Datei folgende Struktur:

```markdown
# Übungsaufgaben – <Thema> (<Fach>)

> Quelle der Themen: vorlesungs_materialien/<...>
> Erstellt von Claude · Schwierigkeit gemischt

## Aufgabe 1  ·  [leicht | mittel | schwer]
<Aufgabenstellung>

<details>
<summary>Lösung</summary>

<vollständige Musterlösung mit allen Schritten>

</details>

## Aufgabe 2  ·  [...]
...
```

> Mathematische Ausdrücke in LaTeX (`$...$` bzw. `$$...$$`) setzen.

---

## Wichtige Hinweise

- Arbeite **nur** innerhalb des aktuellen Fach-Ordners; gehe nicht in andere Fächer.
- Wenn ein Ordner leer ist oder fehlt, **überspringe** ihn und vermerke das kurz im Output.
- Erfinde keinen Stoff, der nicht zur Vorlesung passt – im Zweifel an den Materialien orientieren.
- Gib am Ende eine **kurze Zusammenfassung** aus: welche Themen abgedeckt wurden, wie viele Aufgaben
  erstellt wurden und in welche Dateien sie geschrieben wurden.
