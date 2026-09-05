# Minesweeper Game (Python / Tkinter)

A desktop implementation of the classic **Minesweeper** game developed in Python using the `Tkinter` GUI toolkit. The application features customizable board dimensions, dynamic mine placement, recursive flood-fill tile reveals, and full game-state management.

---

## 🎮 Game Overview

Players navigate a hidden grid to reveal safe tiles while avoiding concealed landmines, using numerical clues indicating adjacent mine counts.

### Key Features
- **Configurable Grid & Difficulty:** Define custom board dimensions ($N 	imes N$) and mine counts dynamically upon startup via CLI prompt.
- **Randomized Mine Generation:** Mines are distributed uniformly across the grid using `random.sample` to prevent overlapping placements.
- **Neighbor Calculation:** Pre-computes 8-directional adjacent mine counts for each cell to optimize runtime responsiveness.
- **Recursive Reveal (Flood Fill):** Clicking a tile with zero adjacent mines automatically and recursively unveils neighboring safe tiles.
- **Flagging Mechanism:** Right-click to place or remove a flag (`F` indicator) on suspected mines to prevent accidental clicks.
- **Win / Loss Validation:**
  - **Game Over:** Triggering a mine exposes all hidden mine positions (`B` highlighted in red) and displays a game-over dialog.
  - **Victory:** Automatically verifies when all non-mine tiles have been safely cleared and displays a congratulations notice.

---

## 🕹️ Controls

| Action | Control | Description |
| :--- | :--- | :--- |
| **Reveal Tile** | `Left Click` (Primary) | Uncovers the selected cell. Recursively reveals surrounding empty cells if neighbor count is 0. |
| **Toggle Flag** | `Right Click` (`<Button-3>`) | Marks/unmarks a tile with an **"F"** on a yellow background to prevent detonating. |

---

## 🏗️ Architecture & Class Design

The codebase adheres to Object-Oriented Programming (OOP) principles, separating domain state from UI rendering:

1. **`Cell` Class:**
   - Encapsulates individual cell attributes: `is_bomb`, `is_revealed`, `is_flagged`, and `neighbor_bombs`.

2. **`Board` Class:**
   - Manages the $N 	imes N$ matrix of `Cell` objects.
   - Handles algorithmic placement of mines (`place_bombs`) using mathematical 1D-to-2D index mapping (`divmod`).
   - Calculates 8-way neighbor proximity counts (`calculate_neighbors`).

3. **`Minesweeper` Class (GUI & Logic Controller):**
   - Initializes the main `Tk` window and dynamically builds a grid layout of button widgets.
   - Binds UI interactions (`<Button-1>`, `<Button-3>`) to event handlers.
   - Implements recursive cascade clearing (`reveal_recursive`) for rapid terrain discovery.
   - Validates game termination states (`check_win`, `show_mines`).

---

## 📁 Project Structure

```text
.
├── main.py            # Complete application source code (domain logic & Tkinter GUI)
├── .gitignore         # Ignores Python cache and virtual environment files
└── README.md          # Project documentation
```

---

## 🚀 How to Run the Game

### Prerequisites
- **Python 3.8+** installed on your system.
- `Tkinter` (standard library included by default on Windows and macOS).
  - *Linux users (Ubuntu/Debian) only:* If Tkinter is not pre-installed, install it via:
    ```bash
    sudo apt-get update && sudo apt-get install python3-tk
    ```

---

### Step-by-Step Execution

1. **Open a terminal / command prompt** and navigate to the project directory:
   ```bash
   cd path/to/project
   ```

2. **Run the script:**
   ```bash
   python main.py
   ```

3. **Configure the game parameters in the terminal:**
   When prompted, enter your desired grid size and mine density:
   ```text
   Enter the size of the board: 8
   Enter the number of bombs: 10
   ```
   *The Tkinter graphical game window will launch immediately with your specified grid layout.*

---

## 👩‍💻 Author

- **Moriya Malkiel**
