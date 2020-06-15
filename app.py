from flask import Flask, request, redirect, render_template, url_for, jsonify
import algorithm


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print("Incoming...")
        print(request.get_json(force=True))
        beg_pos = request.json.get("to")
        end_pos = request.json.get("from")
        return 'OK', 200

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)