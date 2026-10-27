
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    courses = ["Python Programming", "Java Programming", "Web Development", "Data Science"]
    return render_template("index.html", courses=courses)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    course = request.form.get("course", "").strip()

    courses = ["Python Programming", "Java Programming", "Web Development", "Data Science"]

# Course Registration System - Jenkins CI Test

    if not name or not email or course not in courses:
        return render_template(
            "index.html",
            courses=courses,
            error="Please enter your name and email, and choose one of the available courses.",
            name=name,
            email=email,
            selected_course=course,
        ), 400

    return render_template(
        "success.html",
        name=name,
        course=course
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)
