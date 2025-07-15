from flask import Flask, render_template, request
from persona_builder import get_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    persona_text = None
    error = None

    if request.method == "POST":
        url = request.form.get("profile_url")

        try:
            persona_text = get_response(url)
        except Exception as e:
            error = f"⚠️ Error: {e}"

    return render_template("index.html", persona=persona_text, error=error)

if __name__ == "__main__":
    app.run(debug=True)
