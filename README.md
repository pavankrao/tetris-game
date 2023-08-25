# Python Tetris game

Tetris tile-matching puzzle video game made in Python3

![ScreenShot](https://raw.githubusercontent.com/pavankrao/tetris-game/main/screenshots/game.png)

**Controls**
- Move     - ← ↓ →
- Drop     - ↓
- Rotate   - ↑
- Restart New Game - ↓

**Points**
- **1** for each block move
- **100** for each line cleared


#### Play on Linux

1. Install tool to build package `pip install pyinstaller`

2. Build the game `python3 -m PyInstaller main.py --onefile`

3. Move game file relative to game resources (sound files) by doing `mv dist/main .`

4. Run the game by doing `./main` and enjoy :)