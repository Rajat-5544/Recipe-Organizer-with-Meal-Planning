# Recipe-Organizer-with-Meal-Planning

## Project Overview

This project implements a CLI-based Recipe Organizer with Meal Planning. It allows users to add, edit, and delete recipes, plan meals for the week, search for recipes, and generate shopping lists.

## Features

1. Add, edit, view, and delete recipes

2. Plan meals for different days

3. Search recipes by category, tag, or ingredient

4. Generate a shopping list based on the meal plan

5. Data persistence using JSON files

## Project Structure

The project follows a clean, object-oriented design pattern with a structured code organization:

1. Models (models/)

This folder contains the entity classes, each with properties, constructors, getters, and setters. These classes do not contain any business logic.

    Ingredient: Represents an ingredient with a name and quantity.

    Recipe: Represents a recipe with an ID, name, ingredients, steps, category, and tags.

    MealPlan: Represents a meal plan for a specific day with a corresponding recipe.

2. Services (services/)

This folder contains the core business logic of the application.

RecipeService: Handles recipe creation, editing, deletion, and searching.

MealPlanService: Manages meal planning and generates the shopping list.

DataService: Provides methods to save and load recipes from a JSON file.

3. Main (main.py)

The main file contains the user interface logic. It handles user input, invokes the necessary service methods, and displays output to the user.
