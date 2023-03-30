import datetime
from flask import Flask, render_template, request
from database import db

app = Flask(__name__)
# Author: DAN YU
# Description: add secret key encrypt session data
app.secret_key = b'F\x1c!Bg\xee\xfa\xe30\x00\xfa3\x97\x9c<a'

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        db.entries.insert_one({"content": entry_content, "date": formatted_date})

    entries_with_date = [
        (entry["content"], entry["date"], datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")) for
        entry in db.entries.find({})]
    return render_template("home.html", entries=entries_with_date)


# add user sign up
from routes.login import signup_bp
from routes.login import login_bp

app.register_blueprint(signup_bp)
app.register_blueprint(login_bp)

if __name__ == "__main__":
    app.run(debug=True)
