from models import Recipe

class RecipeService:
    def __init__(self):
        self.recipes = {}
        self.next_id = 1

    def add_recipe(self, name, ingredients, steps, category, tags):
        if any(r.name == name for r in self.recipes.values()):
            raise ValueError("Recipe with the same name already exists.")
        recipe = Recipe(self.next_id, name, ingredients, steps, category, tags)
        self.recipes[self.next_id] = recipe
        self.next_id += 1
        return recipe

    def get_recipe_by_id(self, recipe_id):
        recipe = self.recipes.get(recipe_id)
        if not recipe:
            raise ValueError("Recipe not found.")
        return recipe

    def search_recipes(self, category=None, tag=None, ingredient=None):
        results = self.recipes.values()
        if category:
            results = [r for r in results if r.category == category]
        if tag:
            results = [r for r in results if tag in r.tags]
        if ingredient:
            results = [r for r in results if any(ing.name == ingredient for ing in r.ingredients)]
        return list(results)

    def edit_recipe(self, recipe_id, name=None, ingredients=None, steps=None, category=None, tags=None):
        recipe = self.get_recipe_by_id(recipe_id)
        if not recipe:
            raise ValueError("Recipe not found.")
        if name:
            recipe.name = name
        if ingredients:
            recipe.ingredients = ingredients
        if steps:
            recipe.steps = steps
        if category:
            recipe.category = category
        if tags:
            recipe.tags = tags

    def delete_recipe(self, recipe_id):
        if recipe_id in self.recipes:
            del self.recipes[recipe_id]
        else:
            raise ValueError("Recipe not found.")
        
    def print_all_recipes(self):
        for key in self.recipes:
            print(self.recipes[key])