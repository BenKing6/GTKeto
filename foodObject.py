from datetime import datetime.datetime

# TODO set list of possible size values, sanitise inputs

class FoodObject():
    def __init__(self, title, date, size, quantity, carbs, calories, protein, fat):
        self.title = title
        self.date = date
        self.size = size
        self.quantity = quantity
        self.carbs = carbs
        self.calories = calories
        self.protein = protein
        self.fat = fat