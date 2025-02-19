import json

from models import Ingredient
from models import Recipe

class DataService:
    @staticmethod
    def save_recipes_to_file(recipes, next_id, filename):
        data = {
            "next_id": next_id,
            "recipes": {
                recipe_id: {
                    "name": recipe.name,
                    "ingredients": [{"name": ing.name, "quantity": ing.quantity} for ing in recipe.ingredients],
                    "steps": recipe.steps,
                    "category": recipe.category,
                    "tags": recipe.tags
                }
                for recipe_id, recipe in recipes.items()
            }
        }

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_recipes_from_file(filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            recipes = {
                int(recipe_id): Recipe(
                    int(recipe_id),
                    recipe_data["name"],
                    [Ingredient(ing["name"], ing["quantity"]) for ing in recipe_data["ingredients"]],
                    recipe_data["steps"],
                    recipe_data["category"],
                    recipe_data["tags"]
                )
                for recipe_id, recipe_data in data["recipes"].items()
            }
            next_id = data["next_id"]
            return recipes, next_id
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return {}, 1