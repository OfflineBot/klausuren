# Prompt: Weitere Probeklausuren erstellen

> **Verwendung:** Dieses Fenster wurde in einem Fach-Ordner gestartet (z. B. `analysis_2/`, `numerik/`, `logik/` …).
> Alle Pfade in diesem Prompt sind **relativ zum aktuellen Fach-Ordner**.
> Starte, indem du diese Datei liest und den Anweisungen Schritt für Schritt folgst.

---

## Ziel

Erstelle eine neue, vollständige **Probeklausur** für das aktuelle Fach – basierend auf den vorhandenen
Probeklausuren, den Vorlesungsmaterialien und den weiteren Materialien.

Die Probeklausur soll mich realistisch auf die echte Klausur vorbereiten: gleicher **Aufbau**, gleicher
**Umfang**, gleiches **Niveau** und gleiche **Themenabdeckung** wie die echte Prüfung – inklusive
**Punkteverteilung**, **Zeitvorgabe** und einer separaten **Musterlösung**.

---

## Ablauf

### Schritt 1 – Probeklausuren analysieren

1. Gehe in den Ordner `probeklausuren/` und liste **alle** Dateien auf.
2. Lies und analysiere jede Probeklausur (auch Lösungen, falls vorhanden) gründlich. Achte auf:
   - **Aufbau und Reihenfolge** der Aufgaben,
   - **Anzahl der Aufgaben** und Gesamtumfang,
   - **Punkteverteilung** (Gesamtpunkte, Punkte pro Aufgabe/Teilaufgabe),
   - **Zeitvorgabe** (Bearbeitungsdauer), falls angegeben,
   - **Aufgabentypen** (Beweis, Rechnung, Multiple Choice, Modellierung, Ankreuzen …),
   - **Formulierungsstil** und erlaubte Hilfsmittel.
3. Falls in `vorlesungs_materialien/` oder `übungen/` zusätzliche **Übungsklausuren** liegen, beziehe sie mit ein.
4. Falls **keine** Probeklausur existiert: rekonstruiere ein plausibles Klausurformat aus dem Stoff und den
   Übungsaufgaben und vermerke das im Output.

### Schritt 2 – Vorlesungsmaterialien analysieren

1. Gehe in den Ordner `vorlesungs_materialien/` und liste **alle** Dateien auf.
2. Analysiere sie gründlich und erstelle dir eine Übersicht über **Themen, Definitionen, Sätze, Formeln,
   Verfahren** und die verwendete **Notation** (übernimm sie später 1:1).
3. Ermittle, welche Themen klausurrelevant sind und welche besonders häufig geprüft werden.

### Schritt 3 – Weitere Materialien analysieren

1. Gehe in den Ordner `andere_materialien/` und liste **alle** Dateien auf. Analysiere sie gründlich
   (Skripte, Zusammenfassungen, Quizze, Notizen, ZIP-Inhalte, Bilder …) – hier stecken oft zusätzliche
   Beispiele und Hinweise auf Prüfungsschwerpunkte.
2. Ziehe ergänzend `openbook/` heran, **falls** dort etwas vorhanden ist.
3. Falls ein Ordner leer ist oder fehlt: kurz vermerken und überspringen.

### Schritt 4 – Neue Probeklausur erstellen

Erstelle eine komplette, neue Probeklausur, die dem erkannten Format **so genau wie möglich** entspricht:

- **Gleiche Struktur** wie die echten Probeklausuren (Anzahl Aufgaben, Reihenfolge, Aufgabentypen).
- **Gleiche Gesamtpunktzahl und Punkteverteilung**; jede Aufgabe mit Punktangabe.
- **Zeitvorgabe** übernehmen (falls bekannt) und im Kopf der Klausur angeben.
- **Repräsentative Themenabdeckung** über den klausurrelevanten Stoff – nicht nur ein Thema.
- **Gleiche Notation und Fachsprache** wie in der Vorlesung.
- **Keine Kopien** bestehender Aufgaben – eigenständige, neue Aufgaben im gleichen Stil und Niveau.
- Eine **vollständige, nachvollziehbare Musterlösung** zu jeder Aufgabe (mit Punktevergabe pro Schritt,
  falls in den Originalen so gehandhabt).

### Schritt 5 – Output schreiben

1. Lege den Ordner `claude_probeklausuren/` im aktuellen Fach-Ordner an (falls noch nicht vorhanden).
2. Schreibe pro Durchlauf eine neue Probeklausur als **Markdown-Datei** dorthin.
   - **Überschreibe keine** vorhandenen Dateien – nummeriere fortlaufend, z. B.
     `claude_probeklausuren/Probeklausur_01.md`.
   - Lege die Musterlösung entweder als eigene Datei (`Probeklausur_01_Loesung.md`) an **oder** als
     ausklappbaren Lösungsteil pro Aufgabe – orientiere dich daran, wie die Originale aufgebaut sind.
3. Verwende folgende Grundstruktur:

```markdown
# Probeklausur <Fach> – Nr. <n>

**Bearbeitungszeit:** <z. B. 90 Minuten>   ·   **Gesamtpunkte:** <z. B. 60>
**Hilfsmittel:** <wie im Original>

> Erstellt von Claude · orientiert an probeklausuren/<...>

---

## Aufgabe 1  ·  (<x> Punkte)  ·  <Aufgabentyp>
<Aufgabenstellung>

## Aufgabe 2  ·  (<x> Punkte)
...

---

# Musterlösung
## Lösung Aufgabe 1
<vollständige Lösung mit Punktevergabe>
...
```

> Mathematische Ausdrücke in LaTeX (`$...$` bzw. `$$...$$`) setzen.

---

## Wichtige Hinweise

- Arbeite **nur** innerhalb des aktuellen Fach-Ordners; gehe nicht in andere Fächer.
- Wenn ein Ordner leer ist oder fehlt, **überspringe** ihn und vermerke das kurz im Output.
- Erfinde keinen Stoff, der nicht zur Vorlesung passt – im Zweifel an den Materialien orientieren.
- Achte darauf, dass die Probeklausur in der angegebenen Zeit **realistisch lösbar** ist.
- Gib am Ende eine **kurze Zusammenfassung** aus: welches Klausurformat erkannt wurde (Punkte, Zeit, Aufgabenanzahl),
  welche Themen abgedeckt wurden und in welche Datei(en) geschrieben wurde.
