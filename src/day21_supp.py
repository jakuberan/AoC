def update_allergens(allerg, allergens, allergens_all):
    """
    Function for allergen list update
    """
    if len(allergens_all[allerg]) > 1 or allerg in allergens.keys():
        return
    else:
        ingredient = allergens_all[allerg]
        allergens[allerg] = ingredient

        # Update overall allergen list
        for allg in allergens_all.keys():
            if ingredient[0] in allergens_all[allg] and allg != allerg:
                allergens_all[allg] = list(set(allergens_all[allg]) - set(ingredient))
                update_allergens(allg, allergens, allergens_all)
