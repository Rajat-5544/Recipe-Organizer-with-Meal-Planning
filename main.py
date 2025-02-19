from services import RecipeService
from services import MealPlanService
from services import DataService
from models import Ingredient

def main():
    filename = "recipes.json"
    recipes, next_id = DataService.load_recipes_from_file(filename)
    recipe_service = RecipeService()
    recipe_service.recipes = recipes
    recipe_service.next_id = next_id
    meal_plan_service = MealPlanService()

    while True:
        print("\n" + "="*40)
        print("Recipe Organizer and Meal Planner")
        print("="*40 + "\n")
        print("1. Add Recipe")
        print("2. Plan Meal")
        print("3. Manage Recipes")
        print("4. Search Recipes")
        print("5. Generate Shopping List")
        print("6. Show Meal Plan")
        print("7. Exit")
        print("\n" + "="*40 + "\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n" + "="*40)
            print("**** Add Recipe ****")
            print("="*40 + "\n")
            name = input("Enter recipe name: ")
            ingredients = []
            while True:
                ing_name = input("Ingredient name (or 'done' to finish): ")
                if ing_name.lower() == 'done':
                    break
                quantity = input("Enter quantity(in grams or 0.00 if not defined): ")
                ingredients.append(Ingredient(ing_name, quantity))
            steps = []
            i = 1
            while True:
                in_step = input(f"Enter cooking step {i} (or 'done' to finish): ")
                if in_step.lower() == 'done':
                    break
                steps.append(in_step)
                i += 1
            category = input("Enter category (e.g., Breakfast, Dinner): ")
            tags = input("Enter dietary tags (comma-separated): ").split(",")
            try:
                recipe = recipe_service.add_recipe(name, ingredients, steps, category, tags)
                print("\n" + "="*40 + "\n")
                print(f"Recipe '{recipe.get_name()}' added successfully.")
            except ValueError as e:
                print("\n" + "="*40 + "\n")
                print(e)

        elif choice == "2":
            day = input("Enter day of the week: ")
            recipe_id = input("Enter recipe ID to assign: ")
            try:
                recipe_id = int(recipe_id)
                recipe = recipe_service.get_recipe_by_id(recipe_id)
                if recipe:
                    try:
                        meal_plan_service.add_meal(day, recipe)
                        print(f"Meal for {day} planned successfully.")
                    except ValueError as e:
                        print(e)
                else:
                    print("Recipe ID not found.")
            except ValueError:
                print("Invalid Recipe ID.")

        elif choice == "3":
            print("\n" + "="*40)
            print("**** Manage Recipes ****")
            print("="*40 + "\n")
            print("1. View Recipes")
            print("2. Edit Recipe")
            print("3. Delete Recipe")
            manage_choice = input("Enter your choice (1/2/3): ")

            if manage_choice == "1":
                print("\nAvailable Recipes:")
                print("="*40 + "\n")
                for recipe_id, recipe in recipe_service.recipes.items():
                    print(f"{recipe_id}: {recipe.get_name()} - {recipe.get_category()}")
                print()
                recipe_id = input("Enter recipe ID to view recipe: ")
                try:
                    recipe_id = int(recipe_id)
                    recipe = recipe_service.get_recipe_by_id(recipe_id)
                    print(f"\n{recipe}")
                except ValueError:
                    print("Invalid Recipe ID.")

            elif manage_choice == "2":
                recipe_id = input("Enter recipe ID to edit: ")
                try:
                    recipe_id = int(recipe_id)
                    recipe = recipe_service.get_recipe_by_id(recipe_id)
                    if recipe:
                        print("\nEditing Recipe:")
                        name = input(f"Enter new name (current: {recipe.get_name()}): ")
                        ingredients = []
                        while True:
                            ing_name = input("Ingredient name (or 'done' to finish): ")
                            if ing_name.lower() == 'done':
                                break
                            quantity = input("Enter quantity (in grams or 0.00 if not defined): ")
                            ingredients.append(Ingredient(ing_name, quantity))
                        steps = []
                        i = 1
                        while True:
                            in_step = input(f"Enter cooking step {i} (or 'done' to finish): ")
                            if in_step.lower() == 'done':
                                break
                            steps.append(in_step)
                            i += 1
                        category = input(f"Enter new category (current: {recipe.get_category()}): ")
                        tags = input(f"Enter new dietary tags (current: {', '.join(recipe.tags)}): ").split(",")
                        try:
                            recipe_service.edit_recipe(recipe_id, name, ingredients, steps, category, tags)
                            print(f"Recipe '{recipe.get_name()}' updated successfully.")
                        except ValueError as e:
                            print(e)
                    else:
                        print("Recipe ID not found.")
                except ValueError:
                    print("Invalid Recipe ID.")

            elif manage_choice == "3":
                recipe_id = input("Enter recipe ID to delete: ")
                try:
                    recipe_id = int(recipe_id)
                    recipe_service.delete_recipe(recipe_id)
                    print(f"Recipe with ID {recipe_id} deleted successfully.")
                except ValueError:
                    print("Invalid Recipe ID.")

        elif choice == "4":
            print("\n" + "="*40)
            print("**** Search Recipes ****")
            print("="*40 + "\n")
            print("Search by:")
            print("1. Category")
            print("2. Dietary Tags")
            print("3. Ingredient")
            search_choice = input("Enter search choice (1/2/3): ")

            if search_choice == "1":
                category = input("Enter category to search for: ")
                results = recipe_service.search_recipes(category=category)
                if results:
                    print(f"\nFound {len(results)} recipes in category '{category}':")
                    for recipe in results:
                        print(f"{recipe.get_name()} - {recipe.get_category()}")
                else:
                    print(f"No recipes found in category '{category}'.")

            elif search_choice == "2":
                tag = input("Enter dietary tag to search for: ")
                results = recipe_service.search_recipes(tag=tag)
                if results:
                    print(f"\nFound {len(results)} recipes with tag '{tag}':")
                    for recipe in results:
                        print(f"{recipe.get_name()} - {recipe.get_category()}")
                else:
                    print(f"No recipes found with tag '{tag}'.")

            elif search_choice == "3":
                ingredient = input("Enter ingredient to search for: ")
                results = recipe_service.search_recipes(ingredient=ingredient)
                if results:
                    print(f"\nFound {len(results)} recipes with ingredient '{ingredient}':")
                    for recipe in results:
                        print(f"{recipe.get_name()} - {recipe.get_category()}")
                else:
                    print(f"No recipes found with ingredient '{ingredient}'.")
            else:
                print("Invalid choice.")

        elif choice == "5":
            shopping_list = meal_plan_service.generate_shopping_list()
            print("\nShopping List:")
            for item, quantity in shopping_list.items():
                print(f"{item}: {quantity}")

        elif choice == "6":
            meal_plan = meal_plan_service.get_meal_plan()
            if meal_plan:
                print("\nMeal Plan:")
                for day, recipe_name in meal_plan.items():
                    print(f"{day.capitalize()}: {recipe_name}")
            else:
                print("No meals planned yet.")

        elif choice == "7":
            print("\n" + "="*40)
            DataService.save_recipes_to_file(recipe_service.recipes, recipe_service.next_id, filename)
            print("Exiting program.")
            print(f"Recipes saved to {filename}")
            break

        else:
            print("Invalid choice. Please try again.")

    print("="*40 + "\n")

if __name__ == "__main__":
    main()