## Important Note

This game uses the `curses` library for terminal graphics.
It cannot run on Ed. Please run it on your local machine.

⚠️ Do NOT run this in VS Code terminal — the window is too small.
Use the full screen Windows Command Prompt (CMD) or Mac Terminal instead.

## How to Run

### Step 1 — Open full screen terminal
- **Windows** — Press `Win + R`, type `cmd`, press Enter. Then maximise the window fully. and then go the file location and (python3 -m fruit_dash) to run it 
- **Mac** — Open Terminal app and maximise the window fully.

### Step 1 — Clone the repository
```bash
git clone https://github.com/Souravnair07/fruit_dash_project.git
cd fruit_dash_project
```

### Step 2 — Install dependency (Windows only)
```bash
pip install windows-curses
```
Mac and Linux skip this step — curses is built in.

### Step34 — Run the game
```bash
python -m fruit_dash
```

If that doesn't work try:
```bash
python3 -m fruit_dash
```

## Controls

| Key | Action     |
|-----|------------|
| w   | Accelerate |
| s   | Decelerate |
| a   | Move Left  |
| d   | Move Right |
| q   | Quit       |