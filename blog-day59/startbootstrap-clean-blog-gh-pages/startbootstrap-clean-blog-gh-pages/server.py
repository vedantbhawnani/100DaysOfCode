from flask import *
import requests
app = Flask(__name__)

r = requests.get("https://api.npoint.io/ba3bab5450d1b16406cd")
data = r.json()

@app.route("/")
@app.route("/index.html")
def landing():
    return render_template("index.html", data = data)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/post.html/<int:num>")
def post(num):
    blog = data[num-1]
    return render_template("post.html", num = num, blog = blog)

@app.route("/form.html")
def forms():
    return render_template('forms.html')

if __name__ == '__main__':
    app.run(debug=True)