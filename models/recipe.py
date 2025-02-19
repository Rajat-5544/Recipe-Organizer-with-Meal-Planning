class Recipe:
    def __init__(self, recipe_id, name, ingredients, steps, category, tags):
        self.recipe_id = recipe_id
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.category = category
        self.tags = tags

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_ingredients(self):
        return self.ingredients

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients

    def get_steps(self):
        return self.steps

    def set_steps(self, steps):
        self.steps = steps

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def get_tags(self):
        return self.tags
    
    def add_tag(self, new_tag):
        self.tags.append(new_tag)

    def set_tags(self, tags):
        self.tags = tags

    def __str__(self):
        ingredients_str = ", ".join(str(ing) for ing in self.ingredients)
        steps_str = "\n".join(f"{i+1}. {step}" for i, step in enumerate(self.steps))
        tags_str = ", ".join(self.tags)
        return (f"Recipe ID: {self.recipe_id}\nName: {self.name}\nCategory: {self.category}\n"
                f"Tags: {tags_str}\nIngredients: {ingredients_str}\nSteps:\n{steps_str}")