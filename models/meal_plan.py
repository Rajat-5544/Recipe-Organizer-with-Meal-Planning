class MealPlan:
    def __init__(self, day, recipe):
        self.day = day
        self.recipe = recipe

    def get_day(self):
        return self.day

    def set_day(self, day):
        self.day = day

    def get_recipe(self):
        return self.recipe

    def set_recipe(self, recipe):
        self.recipe = recipe

    def __str__(self):
        return f"{self.day}: {self.recipe.name}"