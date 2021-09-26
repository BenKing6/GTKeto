import gi

# GTK 3.0 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
# Libhandy
gi.require_version('Handy', '1') 
from gi.repository import Handy

class SettingsPage(Handy.PreferencesPage):
    def __init__(self):
        super().__init__()
        