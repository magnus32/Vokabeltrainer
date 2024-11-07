# Vokabeltrainer

## Beschreibung
Vokabeltrainer ist eine Flask-Anwendung, die es Benutzern ermöglicht, Vokabelblöcke zu erstellen, zu verwalten und zu üben. Die Anwendung verwendet SQLite zur Speicherung der Vokabeln und bietet eine benutzerfreundliche Oberfläche zur Eingabe und Abfrage von Vokabeln.

## Funktionen
- Erstellen, Bearbeiten und Löschen von Vokabelblöcken
- Abfragen von Vokabeln mit Eingabefeldern
- Schnell-Lernen-Funktion zur schnellen Überprüfung des Vokabelwissens
- Speicherung der Vokabeln in einer SQLite-Datenbank

## Installation

### Voraussetzungen
- Python 3.x
- pip (Python-Paketmanager)

### Schritte zur Installation
1. Klonen Sie das Repository:
   ```
   git clone <repository-url>
   cd Vokabeltrainer
   ```

2. Erstellen Sie eine virtuelle Umgebung:
   ```
   python -m venv venv
   ```

3. Aktivieren Sie die virtuelle Umgebung:
   - Auf Windows:
     ```
     venv\Scripts\activate
     ```
   - Auf macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Installieren Sie die Abhängigkeiten:
   ```
   pip install -r requirements.txt
   ```

5. Führen Sie die Migrationen aus, um die Datenbank zu initialisieren:
   ```
   flask db upgrade
   ```

6. Starten Sie die Anwendung:
   ```
   python run.py
   ```

## Nutzung
- Öffnen Sie Ihren Webbrowser und navigieren Sie zu `http://127.0.0.1:5000`.
- Erstellen Sie einen neuen Vokabelblock, indem Sie die erforderlichen Felder ausfüllen.
- Wählen Sie einen Vokabelblock aus, um mit dem Üben zu beginnen.

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der LICENSE-Datei.