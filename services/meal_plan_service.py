from models import MealPlan

class MealPlanService:
    def __init__(self):
        self.meal_plans = {}

    def add_meal(self, day, recipe):
        if day.lower() in self.meal_plans:
            raise ValueError(f"Meal already planned for {day}.")
        self.meal_plans[day.lower()] = MealPlan(day, recipe)

    def get_meal_plan(self):
        return {day: plan.recipe.name for day, plan in self.meal_plans.items()}

    def generate_shopping_list(self):
        shopping_list = {}
        for plan in self.meal_plans.values():
            for ingredient in plan.recipe.ingredients:
                if ingredient.name in shopping_list:
                    shopping_list[ingredient.name] += float(ingredient.quantity)
                else:
                    shopping_list[ingredient.name] = float(ingredient.quantity)
        return shopping_list
