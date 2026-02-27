# Matrix PRNG Integration: Checklist

## Phase 1: Planning & Setup
- [x] Create `matrix_prng_check_list.md` <!-- id: 200 -->
- [x] Research seed-to-matrix derivation (how to turn 1 integer into a 2x2 matrix) <!-- id: 201 -->

## Phase 2: Engine Development
- [x] Implement `MatrixPRNG` class in `random_map.py` <!-- id: 210 -->
    - [x] `det2(matrix)` helper
    - [x] `op_det2(matrix)` helper
    - [x] `next()` method using the recursive determinant logic
- [x] Add `MOD = 594` or similar configurable modulus <!-- id: 211 -->

## Phase 3: Integration
- [x] Update `generate_map` to use `MatrixPRNG` instead of `SimplePRNG` <!-- id: 220 -->
- [x] Adjust coordinate normalization (mapping `0-MOD` to `0.0-1.0`) <!-- id: 221 -->

## Phase 4: UI/UX Consistency
- [x] Ensure `main.py` (Console) still works with the new logic <!-- id: 230 -->
- [x] Ensure `pygame_main.py` (GUI) handles the new seed logic correctly <!-- id: 231 -->
- [/] Implement multi-field input for Matrix (m00-m11) and MOD <!-- id: 232 -->

## Phase 5: Verification & Testing
- [x] Compare output consistency with user's provided snippet <!-- id: 240 -->
- [x] Test map variation (ensure different seeds produce different-looking maps) <!-- id: 241 -->
- [ ] Verify custom matrix parameters generate expected maps <!-- id: 242 -->
