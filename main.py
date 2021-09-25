import gi
from nutritionPage import nutritionPage

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

default_height = 600
default_width = 400

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="DietApp")

        # window stuff
        self.set_default_size(default_width, default_height)
        
        # Main box
        self.box = Gtk.VBox()
        self.add(self.box)

        # Main Stack 
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.box.add(self.stack)

        # Add Nutrition Page to Main Stack
        self.nutrition_page = nutritionPage()
        self.stack.add_titled(self.nutrition_page, "nutrition", "Nutrition")

        # Bottom button bar
        self.bottom_bar = Gtk.StackSwitcher(homogeneous=True)
        self.bottom_bar.set_stack(self.stack)
        self.bottom_bar.set_halign(Gtk.Align.CENTER)
        self.box.add(self.bottom_bar)

        # ----- TEST STUFF ------ #
        self.test_label = Gtk.Label("test")
        self.test_label2 = Gtk.Label("test2")
        self.stack.add(self.test_label)
        self.stack.add(self.test_label2)
        # ----------------------------- #
 
win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()