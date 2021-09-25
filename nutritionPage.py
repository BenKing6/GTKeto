import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class nutritionPage(Gtk.VBox):
    def __init__(self):
        super().__init__()
        
        self.set_valign(Gtk.Align.START)

        # Nutrition Limit Counters
        self.carbs_bar = Gtk.ProgressBar()
        self.calories_bar = Gtk.ProgressBar()
        self.protein_bar = Gtk.ProgressBar()
        self.fat_bar = Gtk.ProgressBar()
        self.nutrition_bars = [self.carbs_bar, self.calories_bar, self.protein_bar, self.fat_bar]

        self.carbs_bar.set_text("Total Carbs (g)")
        self.calories_bar.set_text("Total Calories (kcal)")
        self.protein_bar.set_text("Total Protein (g)")
        self.fat_bar.set_text("Total Fat (g)")

        for bar in self.nutrition_bars:
            bar.set_show_text(True)
            bar.set_margin_top(5)
            bar.set_margin_bottom(5)
            self.add(bar)



