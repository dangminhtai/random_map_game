# Seed Explorer: Implementation Checklist

## Phase 1: Planning & Setup
- [ ] Finalize `requirements.md` <!-- id: 10 -->
- [ ] Initialize `check_list.md` <!-- id: 11 -->
- [ ] Project directory structure verification <!-- id: 12 -->

## Phase 2: Engine Development
- [ ] Integrate/Refactor `SimplePRNG` from `random_map.py` <!-- id: 20 -->
- [ ] Enhance `generate_map` to include Treasure (`X`) and Player (`P`) starting position <!-- id: 21 -->
- [ ] Implement collision detection logic <!-- id: 22 -->

## Phase 3: Game Loop
- [ ] Implement keyboard input handling (non-blocking if possible, or simple `input()`) <!-- id: 30 -->
- [ ] Create the main game loop (Render -> Input -> Update) <!-- id: 31 -->
- [ ] Add coordinate-based movement system <!-- id: 32 -->

## Phase 4: UI/UX & Polish
- [ ] Add start screen with Seed input <!-- id: 40 -->
- [ ] Improve map rendering (ANSI colors if possible) <!-- id: 41 -->
- [ ] Implement Win/Loss screens <!-- id: 42 -->

## Phase 5: Verification & Testing
- [ ] Verify seed reproducibility (same seed = same map) <!-- id: 50 -->
- [ ] Test boundary collisions (can't walk off map) <!-- id: 51 -->
- [ ] Test win/loss triggers <!-- id: 52 -->
