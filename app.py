from flask import Flask, request, redirect, render_template, url_for, jsonify
import agent


app = Flask(__name__)
ai = agent.Agent(depth=5)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print("Incoming...")
        print(request.get_json(force=True))
        beg_pos = request.json.get("from")
        end_pos = request.json.get("to")
        print(beg_pos, end_pos, type(beg_pos), type(end_pos))
        ai_move = ai.add_move(beg_pos, end_pos)

        return str(ai_move), 200
    else:
        ai.reset_board()
        return render_template("index.html")

if __name__ == "__main__":
    app.run()