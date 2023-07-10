from flask import Flask
app = Flask(__name__)



def make_bold(function):
    def new_func():
        return '<b>' + function() + '</b>' 
    new_func.__name__ = function.__name__
    return new_func

def make_emphasis(function):
    def new_func():
        return '<em>' + function() + '</em>' 
    new_func.__name__ = function.__name__
    return new_func


def make_underline(function):
    def new_func():
        return '<u>' + function() + '</u>' 
    new_func.__name__ = function.__name__
    return new_func


@app.route('/')
@make_bold
@make_emphasis 
def main_page():
    return '<h1 style = "text-align: center">GUESS THE NUMBER(1 and 9)</h1>'\
            '<p>para</p>'

if __name__ == '__main__':
    app.run(debug=True)
