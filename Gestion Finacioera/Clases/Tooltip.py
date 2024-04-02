import tkinter as tk

class Tooltip:
    def __init__(self, widget, text, bg_color="Lavender", fg_color="black"):
        self.widget = widget
        self.text = text
        self.bg_color = bg_color  # Color de fondo del tooltip
        self.fg_color = fg_color  # Color del texto del tooltip
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        
        label = tk.Label(self.tooltip, text=self.text, background=self.bg_color, foreground=self.fg_color)
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
