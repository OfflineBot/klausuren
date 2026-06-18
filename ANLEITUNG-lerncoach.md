# Anleitung: Mathe-Lerncoach mit reMarkable

So läuft die iterative Lernschleife (Erklärung → Beispiel → Übung → Korrektur → nächstes Blatt)
zusammen mit dem reMarkable. Gilt für jeden Fach-Ordner unter `klausuren/` (matrizen, analysis_2, …).

## Der Ablauf in Kürze

```
Claude baut  lernblatt-N.pdf   (Light Mode: Erklärung + vorgerechnetes Beispiel + Übung mit Karo-Feld)
      │
      ▼
PDF liegt auf dem reMarkable (Ordner des Fachs) → du füllst die Karo-Felder per Stift aus
      │
      ▼
du sagst:  „überprüf lernblatt-N"
      │
      ▼
Claude lädt deine ausgefüllte Version vom reMarkable, bewertet jede Aufgabe
(richtig / teilweise / falsch / nicht versucht) und gibt eine Übersicht
      │
      ▼
Claude baut  lernblatt-(N+1).pdf  — NUR für deine Lücken (Beherrschtes fällt weg,
Schweres wird ausführlicher). Von vorne.
```

## Wichtige Eckdaten

- **Fach-Ordner:** z. B. `klausuren/matrizen/`. Quellmaterial liegt in `vorlesungs_materialien/`,
  `openbook/`, `andere_materialien/`, `übungen/`. Anmerkungen/Wünsche in `anmerkung/anmerkung.md`.
- **Design:** Light Mode (heller Hintergrund, dunkler Text) — **bewusst entgegen** der Vorgaben in
  `LERN-PROMPT.md` / `prompts/AUFGABEN.md` (die Dark Mode wollen). Karo-Felder zum Schreiben.
- **Dateinamen:** Vom Skill erzeugte Dateien tragen `dont` im Namen (`lernblatt-dont-N.tex/.pdf`).
  Auf dem reMarkable heißen sie sauber `lernblatt-N.pdf`.
- **Kompilieren:** `pdflatex -interaction=nonstopmode lernblatt-dont-N.tex` (zweimal), dann
  `.aux/.log/.out` löschen.

## reMarkable: Verbindung & Dateitransfer

- **Modell/IP:** reMarkable 2 (Firmware 3.25.1.1), per USB unter **`10.11.99.1`**, root-SSH **passwortlos**
  (Key ist hinterlegt). Dokumente/Metadaten unter `/home/root/.local/share/remarkable/xochitl/`.
- **Hochladen** (PDF → reMarkable):
  ```bash
  curl -F "file=@lernblatt-dont-N.pdf;type=application/pdf" "http://10.11.99.1/upload"
  ```
  Landet im Hauptverzeichnis. In den Fach-Ordner verschieben: in `<uuid>.metadata` das Feld
  `"parent"` auf die Ordner-UUID setzen und `systemctl restart xochitl`.
  (Ordner „matritzen" = `edb82810-d275-4de4-bf34-f1ba966edf55`.)
- **Ausgefüllte Version herunterladen** (mit eingebrannten Stiftnotizen):
  ```bash
  curl -k "http://10.11.99.1/download/<uuid>/placeholder" -o ausgefuellt.pdf
  ```
  Dann seitenweise als PNG rendern (`pdftoppm -r 110 -png ausgefuellt.pdf seite`) und lesen.
- **Ausfüllen** geht direkt auf dem reMarkable (Stift) oder am PC in **Xournal++**
  (PDF öffnen, schreiben, als PDF exportieren).

## reMarkable-Bildschirm live am PC ansehen (optional)

- **Tool:** goMarkableStream-Binary liegt unter `/home/root/gomarkablestream`.
- **Starten:**
  ```bash
  ssh root@10.11.99.1 'setsid sh -c "export RK_COMPRESSION=false; nohup /home/root/gomarkablestream -unsafe > /home/root/gms.log 2>&1" </dev/null &'
  ```
- **Ansehen:** Browser → `https://10.11.99.1:2001` (Self-Signed-Zertifikat akzeptieren).
  Login trotz `-unsafe`: **`admin` / `password`**.
- **Stoppen:** `ssh root@10.11.99.1 'for p in $(pgrep gomarkablestream); do kill "$p"; done'`
- **Caveats:** Der Stream ist **kein Autostart** → stirbt bei jedem reMarkable-Neustart, dann neu starten.
  Auf Firmware 3.25.1.1 kann das Bild einen Offset-Fehler zeigen (halbe Breite verschoben, Streifen oben);
  ein frischer Start nach Reboot ist meist sauber. Farben im Stream ≠ Graustufen am Gerät (bauartbedingt).

## Was sagen, um die Schleife weiterzudrehen

- „**überprüf lernblatt-N**" → Auswertung + nächstes Blatt.
- „**erstelle das nächste übungsblatt**" → direkt das nächste Blatt (z. B. nach erneutem Ausfüllen).
- Wünsche/Ausschlüsse in `anmerkung/anmerkung.md` eintragen (Abschnitte „Kommt nicht dran",
  „Zusätzlich", „Anmerkung") — die haben Vorrang.
```
