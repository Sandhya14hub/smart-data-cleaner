from flask import Flask, render_template, request
from src.cleaner import clean_data
import os

from src.visualizer import generate_charts
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    filepath = os.path.join("uploads", file.filename)
    file.save(filepath)

    df, report = clean_data(filepath)
    df.to_csv("cleaned/cleaned_file.csv", index=False)

    chart_files = generate_charts(df)

    return render_template(
    "report.html",
    report=report,
    charts=chart_files,
    columns=list(df.columns)
)
    
from flask import send_file

@app.route("/download")
def download():
    return send_file(
        "cleaned/cleaned_file.csv",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)