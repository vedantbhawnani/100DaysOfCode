from flask import *
import requests
import datetime as dt
app = Flask(__name__)
ager = 'https://api.agify.io?name='
genderize = 'https://api.genderize.io?name='
blog_url = "https://api.npoint.io/8a942e3050fdbe95ca77"

yr = dt.datetime.now().year
r = requests.get(blog_url)
blog_data = r.json()
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/<name>")
def guess_name(name):
    old = requests.get(f"{ager}{name}")
    genders = requests.get(f"{genderize}{name}")
    data = old.json()
    return render_template("guess.html", name = name.title(),age = data['age'], gender = (genders.json())['gender'])

@app.route("/blog")
def blog():
    return render_template("blogs.html", blog_data = blog_data, year = yr)

@app.route("/blog/<int:num>")
def blog1(num):
    return render_template("blog1.html", blog_data = blog_data, year = yr, num = num)

# @app.route("/blog/2")
# def blog2():
#     r = requests.get(blog_url)
#     blog_data = r.json()
#     return render_template("blog2.html", blog_data = blog_data, year = yr)

# @app.route("/blog/3")
# def blog3():
#     r = requests.get(blog_url)
#     blog_data = r.json()
#     return render_template("blog3.html", blog_data = blog_data, year = yr)

if __name__ == '__main__':
    app.run(debug = True)
