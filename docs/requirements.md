# Seed Explorer: Game Requirements

## 1. Overview
Seed Explorer is a terminal-based exploration game where the world is procedurally generated using a Pseudo-Random Number Generator (PRNG). Players use a numeric seed to explore unique maps, find treasure, and avoid obstacles.

## 2. Core Mechanics

### 2.1 Map Generation
- Use the `SimplePRNG` (LCG algorithm) to generate a 2D grid.
- Map Tiles:
    - `~` (Water): Impassable or lethal.
    - `T` (Forest): Passable but might slow down or hide items.
    - `.` (Land): Normal traversable terrain.
    - `P` (Player): Current player position.
    - `X` (Treasure): The goal of the game.

### 2.2 Movement
- WSAD or Arrow keys for top-down movement (Up, Down, Left, Right).
- Collision detection for map boundaries and impassable tiles (Water).

### 2.3 Winning/Losing Conditions
- **Win**: Reach the Treasure `X`.
- **Loss**: Fall into Water `~` or (optional) run out of energy/steps.

## 3. Technical Requirements
- **Language**: Python 3.x.
- **Engine**: Terminal-based (standard print).
- **PRNG**: Custom `SimplePRNG` class to ensure reproducibility across different machines using the same seed.

## 4. User Interface
- Input prompt for the Seed at the start.
- Visual map display updated after every move.
- Status display (Current Seed, Coordinates, Steps taken).

## 5. Future Enhancements
- Fog of War (only reveal nearby tiles).
- Multiple levels with increasing difficulty.
- Enemies or NPCs moving based on the same seed.
