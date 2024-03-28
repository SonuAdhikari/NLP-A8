from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

# Load the language model
text_generator = pipeline("text-generation", model="distilgpt2")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        prompt = request.form["prompt"]
        generated_text = text_generator(prompt, max_length=50, do_sample=True)[0]["generated_text"]
        return render_template("index.html", prompt=prompt, generated_text=generated_text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
