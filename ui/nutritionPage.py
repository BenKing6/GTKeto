import gi
from ui.foodInputPage import FoodInputPage


# GTK 3.0 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
# Libhandy
gi.require_version('Handy', '1') 
from gi.repository import Handy

food_list = []

class nutritionPage(Gtk.Stack):
    def __init__(self):
        super().__init__()

        self.main_box = Gtk.VBox()
        self.add(self.main_box)

        # Nutrition Limit Counters
        self.carbs_box = Gtk.HBox()
        self.carbs_bar = Gtk.ProgressBar()
        self.carbs_bar.set_show_text(True)
        self.carbs_bar.set_text("Total Carbs (g)")
        self.carbs_label = Gtk.Label("0 / 10")
        self.carbs_box.pack_start(self.carbs_bar, True, True, 5)
        self.carbs_box.pack_end(self.carbs_label, False, False, 5)

        self.calories_box = Gtk.HBox()
        self.calories_bar = Gtk.ProgressBar()
        self.calories_bar.set_show_text(True)
        self.calories_bar.set_text("Total Calories (kcal)")
        self.calories_label = Gtk.Label("0 / 10")
        self.calories_box.pack_start(self.calories_bar, True, True, 5)
        self.calories_box.pack_end(self.calories_label, False, False, 5)
        
        self.protein_box = Gtk.HBox()
        self.protein_bar = Gtk.ProgressBar()
        self.protein_bar.set_show_text(True)
        self.protein_bar.set_text("Total Protein (g)")
        self.protein_label = Gtk.Label("0 / 10")
        self.protein_box.pack_start(self.protein_bar, True, True, 5)
        self.protein_box.pack_end(self.protein_label, False, False, 5)

        self.fat_box = Gtk.HBox()
        self.fat_bar = Gtk.ProgressBar()
        self.fat_bar.set_show_text(True)
        self.fat_bar.set_text("Total Fat (g)")
        self.fat_label = Gtk.Label("0 / 10")
        self.fat_box.pack_start(self.fat_bar, True, True, 5)
        self.fat_box.pack_end(self.fat_label, False, False, 5)
        
        self.nutrition_bars = [self.carbs_box, self.calories_box, self.protein_box, self.fat_box]

        for item in self.nutrition_bars:
            item.set_margin_top(5)
            item.set_margin_bottom(5)
            self.main_box.pack_start(item, False, False, 0)

        # Food list
        self.food_list_label = Gtk.Label("Today's Food:")
        self.food_list_label.set_margin_bottom(5)
        self.main_box.pack_start(self.food_list_label, False, False, 0)
        self.food_list = Gtk.ListBox()
        self.food_list.set_hexpand(True)
        self.main_box.pack_start(self.food_list, True, True, 0)

        # New food button
        self.new_food_button = Gtk.Button("Add New Food")
        self.new_food_button.connect("clicked", self.add_new_food)
        self.new_food_button.set_valign(Gtk.Align.END)
        self.new_food_button.set_margin_top(5)
        self.new_food_button.set_margin_left(5)
        self.new_food_button.set_margin_right(5)
        self.new_food_button.set_margin_bottom(5)
        self.main_box.pack_end(self.new_food_button, False, False, 0)

    # New Food Button pressed
    def add_new_food(self, button):
        food_page = FoodInputPage()
        self.remove(self.main_box)
        self.add(food_page)