# gut-microbiome-diet-simulator

An interactive educational tool that maps your diet to predicted gut microbial activity — built with Python, Tkinter, and Matplotlib.

---

## About

This project was developed as part of the M.Sc. Bioinformatics (Part II) curriculum at **Guru Nanak Khalsa College of Arts, Science & Commerce (Autonomous)**, Academic Year 2025–2026.

---

## What It Does

You type in foods you've eaten, and the simulator predicts which gut microbes are likely to thrive based on the nutrient content of those foods. Results appear as a text summary and a bar chart.

```
User inputs foods → Food-to-Nutrient mapping → Nutrient-to-Microbe mapping → Prediction + Bar Chart
```

### Nutrient → Microbe Mapping

| Nutrient Category | Predicted Microbes |
|---|---|
| Carbohydrates | *Bacteroides*, *Prevotella* |
| Protein | *Alistipes*, *Bilophila* |
| Fiber | *Ruminococcus*, *Faecalibacterium* |
| Fat | *Firmicutes*, *Bacteroides* |
| Sugar / Processed | *Lactobacillus*, *Streptococcus* |

---

## Screenshots

**Mixed diet input (rice, paneer, spinach):**

![Fig 01 – Basic output](screenshots/fig01_basic_output.png)

**After matplotlib installed — chart visualization active:**

![Fig 02 – Visualization enabled](screenshots/fig02_visualization_enabled.png)

**Bar chart for carbohydrate-rich foods:**

![Fig 03 – Carb chart](screenshots/fig03_carb_barchart.png)

**Output for protein-rich foods (almonds, yogurt, milk):**

![Fig 04 – Protein output](screenshots/fig04_protein_output.png)

**Bar chart for protein-rich foods:**

![Fig 05 – Protein chart](screenshots/fig05_protein_barchart.png)

**Output for fat-rich foods (ghee, coconut, apple, blueberries):**

![Fig 06 – Fat output](screenshots/fig06_fat_output.png)

**Bar chart for fat-rich foods:**

![Fig 07 – Fat chart](screenshots/fig07_fat_barchart.png)

**Error — unknown food entered ('cocunut' typo):**

![Fig 08 – Error popup](screenshots/fig08_error_unknown_food.png)

---

## Setup

### Requirements
- Python 3.x
- `tkinter` (bundled with most Python installations)
- `matplotlib`

### Install matplotlib

```bash
pip install matplotlib
```

### Run

```bash
python gut_microbiome_simulator.py
```

---

## How to Use

1. Launch the app.
2. Type food items separated by commas — e.g. `rice, paneer, spinach, ghee`
3. Click **Predict Microbes**.
4. The predicted microbes appear in the window, and a bar chart pops up.

### Food examples by category

**Carbs:** rice, chapati, oats, banana, idli, dosa, poha, bread  
**Protein:** paneer, chicken, egg, rajma, moong dal, tofu, yogurt, milk  
**Fiber:** spinach, apple, broccoli, carrot, guava, peas, beetroot  
**Fat:** ghee, coconut, butter, walnuts, flaxseeds, avocado  
**Sugar/Processed:** honey, jaggery, chocolate, cake, soft drink, biscuits  

---

## Limitations

- Predefined food-nutrient-microbe database only — not personalized.
- Does not use real sequencing data or clinical nutrition profiles.
- Foods absent from the database trigger a warning and are skipped.
- For educational purposes only — not medical or dietary advice.

---

## Future Prospects

- Expand the food database to cover global and regional cuisines.
- Integrate real microbiome datasets (e.g. Human Microbiome Project) for biologically grounded predictions.
- Add machine learning models for personalized gut health analysis.
- Provide dietary recommendations based on the predicted microbial profile.
- Deploy as a web or mobile app for wider accessibility.
- Add multi-language support for diverse user groups.

---

## References

1. Ross, F. C. (2024). The interplay between diet and the gut microbiome. *Nature Reviews Microbiology*, 22(6), 671–686.
2. Zhang, P. et al. (2022). Influence of foods and nutrition on the gut microbiome. *PMC*.
3. Singh, R. K. et al. (2017). Influence of diet on the gut microbiome and implications for human health. *Journal of Translational Medicine*.
4. Ortiz, J. P. M. et al. (2021). Enabling rational gut microbiome manipulations by simulation. *PMC*.
5. Sanz, Y. et al. (2025). The gut microbiome connects nutrition and human health. *Nature Reviews*.

---

## Note

This is a simplified model built for learning purposes. It is not clinically validated and should not be used for medical decisions.
