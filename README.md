# LinkedIn Tango Solver

A Chrome extension that automatically solves LinkedIn's Tango puzzle directly inside the browser.

The extension extracts the current board state and puzzle constraints from LinkedIn's DOM, solves the puzzle using a backtracking algorithm, and automatically fills the board.

## Features

* Automatically detects the Tango board
* Extracts existing Sun and Moon placements
* Detects equality and opposite constraints
* Solves the puzzle using a backtracking algorithm
* Automatically fills the board on LinkedIn
* Supports both 4×4 and 6×6 boards
* One-click solve from a Chrome extension popup

## How it works

1. Read the current puzzle state from the page.
2. Extract equality (=) and opposite (×) constraints.
3. Apply Tango rules:

   * No three consecutive identical symbols in any row or column.
   * Each row and column must contain an equal number of Suns and Moons.
   * Equality constraints must be satisfied.
   * Opposite constraints must be satisfied.
4. Use recursive backtracking to find a valid solution.
5. Simulate mouse events to fill the puzzle automatically.

## Technologies Used

* JavaScript
* Chrome Extension (Manifest V3)
* DOM Manipulation
* Recursive Backtracking
* Event Simulation

## Installation

1. Clone this repository:

```bash
git clone https://github.com/b0larp3ar/linkedin-tango-solver.git
```

2. Open Chrome and navigate to:

```
chrome://extensions
```

3. Enable **Developer Mode**.

4. Click **Load unpacked**.

5. Select the project folder.

6. Open LinkedIn Tango:

```
https://www.linkedin.com/games/tango/
```

7. Click the extension icon and press **Solve Puzzle**.

## Project Structure

```
linkedin-tango-solver/

manifest.json

main.js

popup.html

popup.css

popup.js
```

## Future Improvements

* [ ] Publish to the Chrome Web Store
* [ ] Add animations while solving
* [ ] Add a "Solved!" notification
* [ ] Improve popup UI
* [ ] Add support for future LinkedIn Tango updates

## Disclaimer

This project is an independent educational project and is not affiliated with, endorsed by, or maintained by LinkedIn.

