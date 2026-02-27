import pygame
from .constants import COLOR_TEXT, COLOR_DIM

class InputController:
    """Manages multiple input fields and focus state."""
    
    def __init__(self, default_inputs):
        """
        default_inputs: dict of field names and their default string values.
        """
        self.inputs = default_inputs.copy()
        self.input_order = list(self.inputs.keys())
        self.focus_idx = 0

    def get_focused_field(self):
        return self.input_order[self.focus_idx]

    def handle_event(self, event):
        """Processes keyboard events for inputs. Returns True if Enter was pressed."""
        if event.type != pygame.KEYDOWN:
            return False
            
        active_field = self.get_focused_field()
        
        if event.key == pygame.K_RETURN:
            return True
        elif event.key == pygame.K_TAB:
            self.focus_idx = (self.focus_idx + 1) % len(self.input_order)
        elif event.key == pygame.K_BACKSPACE:
            self.inputs[active_field] = self.inputs[active_field][:-1]
        else:
            if event.unicode.isdigit():
                self.inputs[active_field] += event.unicode
                
        return False
        
    def get_color(self, field_name):
        """Returns white if focused, gray otherwise."""
        return (255, 255, 255) if self.get_focused_field() == field_name else COLOR_DIM
