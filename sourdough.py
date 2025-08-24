def sourdough_recipe(flour, hydration=70, starter_pct=20, salt_pct=2):
    water = flour * (hydration / 100)
    starter = flour * (starter_pct / 100)
    salt = flour * (salt_pct / 100)
    total = flour + water + starter + salt
    
    return {
        "Flour (g)": flour,
        "Water (g)": round(water, 1),
        "Starter (g)": round(starter, 1),
        "Salt (g)": round(salt, 1),
        "Total Dough (g)": round(total, 1)
    }

    print(sourdough_recipe(500))  

