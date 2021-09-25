import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class nutritionPage(Gtk.VBox):
    def __init__(self):
        super().__init__()
        
        # Nutrition Limit Counters
        self.carbs_bar = Gtk.ProgressBar()
        self.calories_bar = Gtk.ProgressBar()
        self.protein_bar = Gtk.ProgressBar()
        self.fat_bar = Gtk.ProgressBar()

        self.carbs_bar.set_show_text(True)
        self.calories_bar.set_show_text(True)
        self.protein_bar.set_show_text(True)
        self.fat_bar.set_show_text(True)

        self.carbs_bar.set_text("Total Carbs (g)")
        self.calories_bar.set_text("Total Calories (kcal)")
        self.protein_bar.set_text("Total Protein (g)")
        self.fat_bar.set_text("Total Fat (g)")

        self.add(self.carbs_bar)
        self.add(self.calories_bar)
        self.add(self.protein_bar)
        self.add(self.fat_bar)