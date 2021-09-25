import gi

# GTK 3.0 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
# Libhandy
gi.require_version('Handy', '1') 
from gi.repository import Handy

class FoodInputPage(Gtk.VBox):
    def __init__(self):
        super().__init__(foodObject)

        # Food name / title
        self.title_box = Gtk.HBox()
        self.title_label = Gtk.Label("Name:")
        self.title_box.pack_start(self.title_label, False, False, 5)
        self.title_field = Gtk.Entry()
        self.title_box.pack_end(self.title_field, True, True, 5)
        self.pack_start(self.title_box, False, False, 5)

        # Date eaten
        self.date_box = Gtk.HBox()
        self.date_label = Gtk.Label("Date:")
        self.date_box.pack_start(self.date_label, False, False, 5)
        self.date_field = Gtk.Entry()
        self.date_box.pack_end(self.date_field, True, True, 5)
        self.pack_start(self.date_box, False, False, 5)
         
        # Unit of size
        self.size_box = Gtk.HBox()
        self.size_label = Gtk.Label("Unit of Size:")
        self.size_box.pack_start(self.size_label, False, False, 5)
        # self.size_field = Gtk # TODO limited options using some GTK input thingy, load values from FoodObject
        self.pack_start(self.size_box, False, False, 5)
        
        # Quantity of "Size" eaten
        self.quantity_box = Gtk.HBox()
        self.quantity_label = Gtk.Label("Quantity:")
        self.quantity_box.pack_start(self.quantity_label, False, False, 5)
        # self.quantity_field = Gtk # TODO limited options, number wheel
        self.pack_start(self.quantity_box, False, False, 5)

        # Calories per "Size"
        self.calories_box = Gtk.HBox()
        self.calories_label = Gtk.Label("Calories:")
        self.calories_box.pack_start(self.calories_label, False, False, 5)
        self.calories_field = Gtk.Entry()
        self.calories_box.pack_end(self.calories_field, True, True, 5)
        self.pack_start(self.calories_box, False, False, 5)