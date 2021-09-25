import gi
from nutritionPage import nutritionPage
from settingsPage import settingsPage

# GTK 3.0 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
# Libhandy
gi.require_version('Handy', '1') 
from gi.repository import Handy

default_height = 600
default_width = 400

class MainWindow(Handy.Window):
    def __init__(self):
        super().__init__(title="GTKeto")

        # window stuff
        self.set_default_size(default_width, default_height)

        # Main box
        self.box = Gtk.VBox()
        self.add(self.box)

        # Main Stack 
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.box.pack_start(self.stack, True, True, 0)

        # Add nutrition page to Main Stack
        self.nutrition_page = nutritionPage()
        self.stack.add_titled(self.nutrition_page, "nutrition", "Nutrition")

        # Bottom button bar
        self.bottom_bar = Handy.ViewSwitcherBar()
        self.bottom_bar.set_stack(self.stack)
        self.bottom_bar.set_reveal(True)
        self.box.pack_end(self.bottom_bar, False, False, 0)

        # ----- TEST STUFF ------ #
        self.test_label = Gtk.Label("blank")
        self.stack.add_titled(self.test_label, "blank", "blank")
        # ----------------------------- #

        # Add settings page to Main Stack
        self.settings_page = settingsPage()
        self.stack.add_titled(self.settings_page, "settings", "Settings")
 
win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()