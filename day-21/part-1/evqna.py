from tool.runners.python import SubmissionPy

from collections import Counter

class EvqnaSubmission(SubmissionPy):
    def parse_food(self, food):
        ingredients = set()
        allergens = []
        found_allergens = False
        for w in food.split():
            if w.startswith('('):
                found_allergens = True
                continue
            if found_allergens:
                allergens.append(w[:-1])    # Ignore , )
            else:
                ingredients.add(w)
        return ingredients, allergens

    def find_safe_ingredients(self, ingredients, allergen_table):
        safe_ingredients = set(ingredients.keys())
        for allergen in allergen_table:
            safe_ingredients.difference_update(allergen_table[allergen])
        return safe_ingredients

    def run(self, s):
        all_ingredients = Counter()
        allergen_table = {}  # {allergen: {compatible_ingredients}}
        for food in s.splitlines():
            ingredients, allergens = self.parse_food(food)
            all_ingredients.update(ingredients)
            for a in allergens:
                if a not in allergen_table:
                    allergen_table[a] = ingredients.copy()
                else:
                    allergen_table[a].intersection_update(ingredients)
        
        safe_ingredients = self.find_safe_ingredients(all_ingredients, allergen_table)
        return sum(all_ingredients[i] for i in safe_ingredients)
