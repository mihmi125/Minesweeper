# Minesweeper

A classic Minesweeper game implementation built with Python and Pygame. Uncover tiles, avoid mines, and use numerical clues to complete the board!

## Features

- **Interactive Gameplay**: Click to reveal tiles, right-click to place flags
- **Customizable Difficulty**: Choose from preset difficulties or create custom board sizes
- **Quick Presets**: Small (8x8, 12 mines), Medium (12x12, 30 mines), Large (16x16, 60 mines)
- **Manual Tuning**: Fine-tune rows, columns, and mine counts to your preference
- **Win/Loss Detection**: Automatic game-over detection and win condition checking
- **Game Reset**: Press 'R' to reset the current game instantly
- **Main Menu & Settings**: Easy navigation between game and configuration screens

## Requirements

- Python 3.12
- Pygame

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mihmi125/Minesweeper.git
cd Minesweeper
```

2. Install dependencies:
```bash
pip install pygame
```

3. Ensure you have the UI assets in the `ui/assets/` directory (tile images should be included)

## Running the Game

```bash
python main.py
```

The game will start with the main menu. From there, you can:
- Click **PLAY** to start a game
- Click **SETTINGS** to customize board difficulty

## How to Play

| Action | Button |
|--------|--------|
| Reveal Tile | Left Click |
| Place/Remove Flag | Right Click |
| Reset Game | Press 'R' |
| Return to Menu | Press 'ESC' |

### Gameplay Rules

1. **Reveal tiles** by left-clicking on them
2. **Numbers** indicate how many mines are in the 8 adjacent tiles
3. **Empty tiles** mean no adjacent mines - these auto-reveal neighbors
4. **Place flags** on suspected mines using right-click
5. **Win** by revealing all non-mine tiles
6. **Lose** by clicking on a mine (all mines will be revealed)

## Project Structure

```
Minesweeper/
├── main.py              # Entry point for the application
├── config.py            # Game configuration and asset loading
├── core/
│   └── game.py          # Main game loop and state management
├── logic/
│   ├── board.py         # Board logic, mine placement, and game state
│   └── cell.py          # Individual cell representation
├── ui/
│   ├── interface.py     # Game board rendering and input handling
│   ├── menu.py          # Main menu UI
│   ├── settings.py      # Settings/difficulty selection UI
│   └── assets/          # UI tile images
└── README.md            # This file
```

## Configuration

Edit `config.py` to modify:
- **Screen size**: `SCR_WIDTH`, `SCR_HEIGHT` (default: 800x600)
- **Tile size**: `TILE_SIZE` (default: 32px)
- **FPS**: Frame rate (default: 60)

## Game Assets

The game uses sprite tiles located in `ui/assets/`:
- `TileEmpty.png` - Revealed empty tile
- `Tile1.png` through `Tile8.png` - Number tiles
- `TileUnknown.png` - Unrevealed tile
- `TileFlag.png` - Flagged tile
- `TileMine.png` - Revealed mine
- `TileExploded.png` - Exploded mine (on loss)
- `TileNotMine.png` - Incorrectly flagged tile

## Code Architecture

### Core Components

- **Game**: Orchestrates game state and connects UI with logic
- **Board**: Manages tile grid, mine placement, and game rules
- **Cell**: Represents individual tile state
- **Interface**: Renders the game board and handles user input
- **Menu**: Main menu UI
- **Settings**: Difficulty/customization UI

### Key Features

- **Smart neighbor reveal**: Empty tiles automatically reveal adjacent tiles
- **Boundary checking**: Settings prevent invalid board configurations
- **State callbacks**: Clean separation between UI and game logic

## Troubleshooting

**Assets not found**: Ensure the `ui/assets/` folder exists with all required PNG files

**Game won't start**: Check that Pygame is installed: `pip install pygame`

**Window not appearing**: Check if Pygame display mode is supported on your syste

## Creators

**Mihmi125**: Mihkel

**Nurruw-Meowthra**: Siim

