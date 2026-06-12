import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def generate_charts(df):

    folder = "static/charts"
    os.makedirs(folder, exist_ok=True)

    # 🔥 CLEAR OLD FILES
    for file in os.listdir(folder):
        os.remove(os.path.join(folder, file))

    chart_files = []

    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:

        plt.figure(figsize=(8,5))
        plt.hist(df[col], bins=10)

        plt.title(f"{col} Distribution")
        plt.xlabel(col)
        plt.ylabel("Frequency")

    # 🔥 FIRST define filename
        filename = f"{col}.png"

    # 🔥 THEN create filepath
        filepath = os.path.join(folder, filename)

        plt.savefig(filepath)
        plt.close()

        chart_files.append(filename)

    return chart_files