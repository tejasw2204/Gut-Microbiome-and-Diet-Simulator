import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# ------------------------------
# Nutrient and Microbe Mapping
# ------------------------------

# Maps foods to their primary nutrient category
# Categories: carbs, protein, fiber, fat, sugar
nutrients = {
    # Carbohydrates
    "rice": "carbs", "oats": "carbs", "banana": "carbs", "potato": "carbs",
    "sweet potato": "carbs", "bread": "carbs", "pasta": "carbs", "quinoa": "carbs",
    "chapati": "carbs", "poha": "carbs", "idli": "carbs", "dosa": "carbs",
    "corn": "carbs", "noodles": "carbs", "wheat": "carbs",

    # Proteins
    "paneer": "protein", "chicken": "protein", "almonds": "protein",
    "chana dal": "protein", "toor dal": "protein", "salmon": "protein",
    "yogurt": "protein", "milk": "protein", "egg": "protein", "soybeans": "protein",
    "rajma": "protein", "chickpeas": "protein", "moong dal": "protein",
    "fish": "protein", "mutton": "protein", "tofu": "protein", "cheese": "protein",
    "peanuts": "protein",

    # Fiber
    "spinach": "fiber", "apple": "fiber", "blueberries": "fiber",
    "pumpkin": "fiber", "methi": "fiber", "broccoli": "fiber", "carrot": "fiber",
    "cabbage": "fiber", "beans": "fiber", "peas": "fiber", "orange": "fiber",
    "pear": "fiber", "guava": "fiber", "beetroot": "fiber", "okra": "fiber",
    "cauliflower": "fiber", "lettuce": "fiber", "cucumber": "fiber",

    # Fats
    "ghee": "fat", "coconut": "fat", "butter": "fat", "olive oil": "fat",
    "sunflower oil": "fat", "mustard oil": "fat", "groundnut oil": "fat",
    "cashews": "fat", "walnuts": "fat", "avocado": "fat", "seeds": "fat",
    "sesame oil": "fat", "flaxseeds": "fat", "pumpkin seeds": "fat",

    # Sugars / Processed Foods
    "sugar": "sugar", "jaggery": "sugar", "honey": "sugar", "chocolate": "sugar",
    "ice cream": "sugar", "cake": "sugar", "biscuits": "sugar", "cookies": "sugar",
    "cold drink": "sugar", "soft drink": "sugar", "jam": "sugar", "candy": "sugar",
    "doughnut": "sugar", "pastry": "sugar", "milkshake": "sugar"
}

# Each nutrient category supports growth of specific microbes
microbes = {
    "carbs":   ["Bacteroides", "Prevotella"],
    "protein": ["Alistipes", "Bilophila"],
    "fiber":   ["Ruminococcus", "Faecalibacterium"],
    "fat":     ["Firmicutes", "Bacteroides"],
    "sugar":   ["Lactobacillus", "Streptococcus"]
}


# ------------------------------
# Microbe Prediction Logic
# ------------------------------

def predict_microbes(food_list):
    """
    Given a list of foods:
    - Checks each food against the nutrient dictionary
    - Maps the nutrient to its associated microbes
    - Counts how many times each microbe is predicted (relative abundance)
    """
    microbe_counts = {}
    for food in food_list:
        food = food.strip().lower()
        if food in nutrients:
            nutrient = nutrients[food]
            for microbe in microbes[nutrient]:
                microbe_counts[microbe] = microbe_counts.get(microbe, 0) + 1
        else:
            messagebox.showwarning("Unknown Food", f"'{food}' not found in database.")
    return microbe_counts


# ------------------------------
# Visualization: Bar Chart
# ------------------------------

def show_chart(results):
    """
    Plots a bar chart of predicted microbes vs their relative counts.
    Shows a popup if no results are available to plot.
    """
    if not results:
        messagebox.showinfo("No Data", "No microbes predicted to plot.")
        return

    microbes_list = list(results.keys())
    counts = list(results.values())

    plt.figure(figsize=(7, 4))
    bars = plt.bar(microbes_list, counts, color="skyblue", edgecolor="black")
    plt.xlabel("Microbes")
    plt.ylabel("Predicted Abundance (Count)")
    plt.title("Predicted Microbial Abundance")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.show()


# ------------------------------
# Button Click Handler
# ------------------------------

def show_results():
    """
    Reads food input, runs prediction, updates the result label,
    and triggers the bar chart.
    """
    input_text = food_entry.get().strip()
    if not input_text:
        messagebox.showerror("Input Error", "Please enter some foods separated by commas.")
        return

    food_list = [f.strip() for f in input_text.split(",") if f.strip()]
    results = predict_microbes(food_list)

    if not results:
        result_label.config(text="No known foods found. Check your input.")
        return

    result_text = "Predicted Microbes:\n"
    for microbe, count in results.items():
        result_text += f"  {microbe}: {count}\n"

    result_label.config(text=result_text)
    show_chart(results)


# ------------------------------
# GUI Setup
# ------------------------------

window = tk.Tk()
window.title("Gut Microbiome & Diet Simulator")
window.geometry("620x420")
window.resizable(False, False)

tk.Label(
    window,
    text="Gut Microbiome & Diet Simulator",
    font=("Arial", 14, "bold")
).pack(pady=(15, 5))

tk.Label(
    window,
    text="Enter foods consumed (comma-separated):",
    font=("Arial", 11)
).pack(pady=5)

food_entry = tk.Entry(window, width=60, font=("Arial", 11))
food_entry.pack(pady=8)

tk.Button(
    window,
    text="Predict Microbes",
    command=show_results,
    bg="#2c7a2c",
    fg="white",
    font=("Arial", 11),
    padx=10,
    pady=4
).pack(pady=8)

result_label = tk.Label(
    window,
    text="Predicted microbes will appear here.",
    font=("Arial", 11),
    justify="left",
    anchor="w"
)
result_label.pack(pady=15, padx=30, anchor="w")

window.mainloop()
