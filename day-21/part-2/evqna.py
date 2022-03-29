from tool.runners.python import SubmissionPy

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

    def build_allergen_table(self, all_foods):
        A = {}  # {allergen: {compatible_ingredients}}
        all_ingredients = set()
        for food in all_foods:
            ingredients, allergens = self.parse_food(food)
            all_ingredients.update(ingredients)
            for a in allergens:
                if a not in A:
                    A[a] = ingredients.copy()
                else:
                    A[a].intersection_update(ingredients)
        return A
    
    def find_allergens(self, allergen_table):
        allergens = {}
        N = len(allergen_table)
        while len(allergens) < N:
            for allergen, ingredients in allergen_table.items():
                if len(ingredients) == 1:
                    ingredient = next(iter(ingredients))
                    allergens[allergen] = ingredient
                    for a in allergen_table:
                        allergen_table[a].discard(ingredient)
        return allergens
    
    def dangerous_ingredients_list(self, allergen_map):
        return ','.join(v for _, v in sorted(allergen_map.items()))

    def run(self, s):
        allergen_table = self.build_allergen_table(s.splitlines())
        allergens = self.find_allergens(allergen_table)
        return self.dangerous_ingredients_list(allergens)
