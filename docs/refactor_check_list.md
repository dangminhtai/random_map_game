# Project Architecture Refactoring: Checklist

## Phase 1: Planning
- [x] Define directory structure (`core/`, `game/`, `ui/`) <!-- id: 300 -->
- [x] Create this checklist <!-- id: 301 -->

## Phase 2: Core Engine (Logic & Math)
- [x] Create `core/prng.py` and move `MatrixPRNG`, `det2`, `op_det2` from `random_map.py` <!-- id: 310 -->
- [x] Create `core/map_generator.py` and move `generate_map` logic <!-- id: 311 -->

## Phase 3: UI & Presentation (Pygame decoupling)
- [x] Create `ui/constants.py` for Colors, Fonts, Tile sizes, and Emoji mappings <!-- id: 320 -->
- [x] Create `ui/input_box.py` to handle the grid input logic (DRY principle for input fields) <!-- id: 321 -->
- [x] Create `ui/renderer.py` to handle Pygame drawing operations <!-- id: 322 -->

## Phase 4: Game State (Controller/Manager)
- [x] Create `game/state.py` to manage Player Data, Steps, Map Data, and Win/Loss conditions <!-- id: 330 -->
- [x] Create new `main.py` at the root as the single entry point that wires `core`, `game`, and `ui` together <!-- id: 331 -->

## Phase 5: Cleanup & Verification
- [x] Delete old bloated `random_map.py` and `pygame_main.py` <!-- id: 340 -->
- [x] Verify the game runs correctly via `python main.py` <!-- id: 341 -->
