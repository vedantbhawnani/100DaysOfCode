import random
from flask import Flask
app = Flask(__name__)

@app.route('/')
def login():
    return '<h1 style = "text-align = center">Guess a number between 1 and 9</h1>'\
           '<img src = "https://media3.giphy.com/media/13RcbHeXlLNysE/giphy.gif?cid=ecf05e473p23vvjxxuv8nein204bxygcvrob1pe4axqfpkho&rid=giphy.gif&ct=g" width="480" height="304" frameBorder="0">'

rand = random.randint(1,9)


@app.route(f'/<guess>')
def game(guess):
    guess = int(guess)
    if guess == rand:
        return '<h1 style = "text-align = center">YOU GOT IT</h1>'\
            '<img src = "https://media0.giphy.com/media/9xt5eMX6WhOhvfWajw/200w.webp?cid=ecf05e475gjerlqafice9dckycc7978z3s3m8wqg4xtiyomc&rid=200w.webp&ct=g" width="480" height="304" frameBorder="0">'
    elif guess < rand:
        return '<h1 style = "text-align = center">CLOSE BUT AIM HIGHER</h1>'\
            '<img src = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDMxMGM0ZGM3NjA3YzM5MDY3YjAxODY1YzUwNmFlOGE3NWYzYzc3MyZjdD1n/cP5li7Un9Ua2OT7i9y/giphy.gif" width="480" height="304" frameBorder="0">'
    elif guess > rand:
        return '<h1 style = "text-align = center">BZZZZ AIM FOR THE MOON NOT THE SUN</h1>'\
            '<img src = "https://media0.giphy.com/media/Wq9RLX06zRg4UM42Qf/giphy.webp?cid=ecf05e47mj97cd15eu49li1cpv0zg2k4h44wumzd5tu0lh2b&rid=giphy.webp&ct=g" width="480" height="304" frameBorder="0">'
    elif 10<guess<0:
        return '<h1 style = "text-align = center">DID YOU EVEN SEE THE GUESSING RANGE</h1>'\
            '<img src = "https://media4.giphy.com/media/zxxXYJqTlpBnO/giphy.gif?cid=ecf05e479iwst5j9on61q2jvj183fkmkn6goo9bmck63hx5i&rid=giphy.gif&ct=g" width="480" height="304" frameBorder="0">'
if __name__ == '__main__':
    app.run(debug=True)