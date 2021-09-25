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
        self.nutrition_bars = [self.carbs_bar, self.calories_bar, self.protein_bar, self.fat_bar]

        self.carbs_bar.set_text("Total Carbs (g)")
        self.calories_bar.set_text("Total Calories (kcal)")
        self.protein_bar.set_text("Total Protein (g)")
        self.fat_bar.set_text("Total Fat (g)")

        for bar in self.nutrition_bars:
            bar.set_show_text(True)
            bar.set_margin_top(5)
            bar.set_margin_left(5)
            bar.set_margin_right(5)
            bar.set_margin_bottom(5)
            self.pack_start(bar, False, False, 0)

        # Food list
        self.food_list_label = Gtk.Label("Today's Food:")
        self.food_list_label.set_margin_bottom(5)
        self.pack_start(self.food_list_label, False, False, 0)
        self.food_list = Gtk.ListBox()
        self.food_list.set_hexpand(True)
        self.pack_start(self.food_list, True, True, 0)

        # New food button
        self.new_food_button = Gtk.Button("Add New Food")
        self.new_food_button.set_valign(Gtk.Align.END)
        self.new_food_button.set_margin_top(5)
        self.new_food_button.set_margin_left(5)
        self.new_food_button.set_margin_right(5)
        self.new_food_button.set_margin_bottom(5)
        self.pack_end(self.new_food_button, False, False, 0)

