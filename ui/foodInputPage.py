import gi

# GTK 3.0 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
# Libhandy
gi.require_version('Handy', '1') 
from gi.repository import Handy

class FoodInputPage(Gtk.VBox):
    def __init__(self):
        super().__init__()

        self.data_ready = False
        self.cancelled = False

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
        self.size_field = Gtk.Entry() # TODO limited options using some GTK input thingy, load values from FoodObject
        self.pack_start(self.size_box, False, False, 5)
        
        # Quantity of "Size" eaten
        self.quantity_box = Gtk.HBox()
        self.quantity_label = Gtk.Label("Quantity:")
        self.quantity_box.pack_start(self.quantity_label, False, False, 5)
        self.quantity_field = Gtk.Entry() # TODO limited options, number wheel
        self.pack_start(self.quantity_box, False, False, 5)

        # Calories per "Size"
        self.calories_box = Gtk.HBox()
        self.calories_label = Gtk.Label("Calories:")
        self.calories_box.pack_start(self.calories_label, False, False, 5)
        self.calories_field = Gtk.Entry()
        self.calories_box.pack_end(self.calories_field, True, True, 5)
        self.pack_start(self.calories_box, False, False, 5)

        # Button box
        self.button_box = Gtk.HBox()
        self.pack_start(self.button_box, False, False, 5)

        # Confirm button
        self.confirm_button = Gtk.Button("Confirm new food")
        self.confirm_button.connect("clicked", self.confirm_pressed)
        self.confirm_button.set_margin_left(5)
        self.confirm_button.set_margin_right(2.5)
        self.button_box.pack_start(self.confirm_button, True, True, 5)

        # Cancel button
        self.cancel_button = Gtk.Button("Cancel")
        self.cancel_button.set_margin_left(2.5)
        self.cancel_button.set_margin_right(5)
        self.button_box.pack_end(self.cancel_button, True, True, 5)

    def clear_all(self):
        self.data_ready = False
        self.cancelled = False

        self.title_field.set_text("")
        self.date_field.set_text("")
        self.size_field.set_text("")
        self.quantity_field.set_text("")
        self.calories_field.set_text("")

    def confirm_pressed(self, button):
        # TODO put field data into FoodObject
        self.data_ready = True

    def cancel_pressed(self, button):
        self.cancelled = True

    @property
    def get_data_ready(self):
        return self.data_ready

    @property
    def get_cancelled(self):
        return self.cancelled