from flask import Flask, request, render_template
from reg import classifier
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def classifierA():
    if request.method == "POST":
        val = int(request.form.get("nm"))
        out = classifier(val)
        return render_template("login.html",out="The Predicted Salary Is:"+ str(round(out[0])))

    return render_template("login.html",out="")

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port = 8080)

if __name__ == "__main__":
    app.run(debug=True)
