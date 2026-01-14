from flask import Flask, render_template, request
import uuid
import random

app = Flask(__name__)

APPS = [
    "FB_ANDROID",
    "MESSENGER",
    "FB_LITE",
    "ADS_MANAGER",
    "INSTAGRAM",
    "WHATSAPP"
]

def generate_fake_token(prefix):
    return prefix + "_" + uuid.uuid4().hex.upper()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # FAKE MULTI TOKENS
        tokens = {}
        for app_name in APPS:
            tokens[app_name] = generate_fake_token(app_name)

        return render_template(
            "result.html",
            email=email,
            tokens=tokens,
            count=len(tokens)
        )

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
