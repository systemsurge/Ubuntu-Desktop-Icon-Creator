# Ubuntu Desktop Icon Creator

A lightweight, lightning-fast Python Tkinter GUI utility for Linux that lets you easily browse installed applications and generate native `.desktop` launcher shortcuts directly onto your Desktop folder.

## Features
* **Instant Loading:** Bypasses slow icon-scraping to load your entire application library instantly.
* **Native Integration:** Generates standard, compliant Linux `[Desktop Entry]` shortcuts.
* **Auto-Executable:** Automatically updates permissions (`chmod +x`) so the system trusts the launcher immediately.

## Prerequisites
Most Linux distributions come with Python pre-installed, but you may need to ensure the Tkinter GUI backend is installed:

```bash
# Ubuntu / Debian / Mint
sudo apt-get install python3-tk

## How to Run
1. Clone this repository or download the script file.
2. Mark the file as executable and launch it from your terminal:

```bash
chmod +x "Linux Program Icon Creator.py"
./"Linux Program Icon Creator.py"
