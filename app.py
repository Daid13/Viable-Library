from flask import (
    Flask,
    make_response,
    session,
    redirect,
    render_template,
    request,
    url_for,
)
from viablelibrary import ViableLibrary

app = Flask(__name__)
def create_values(lib):
    books=[["Return of the King","The finale to the epic, genre defining work by J.R.R. Tolkien."],
           ["Foundation", "The Galactic Empire is dying but Hari Seldon's Psychohistory predicts a better future."],
           ["Artemis Fowl", "Teenage criminal mastermind begins to pray on the fay, but does he bite off more than he chew?"]]
    for b in books:
        lib.add_book(b[0],b[1])


lib=ViableLibrary()
create_values(lib)

@app.route('/')
def start():
    return render_template("start.html")

@app.route("/input/", methods=["GET"])
def input():
    inp = request.args.get(
        "input"
    ) 
    if inp=="login":
        render_template("login.html")
    else:
        render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if lib.login(request.form["email"],request.form["password"]):
            return redirect(url_for('main'))
        else:
            error = 'Invalid Credentials. Please try again.'
            
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET','POST'])
def register():
    error = None
    if request.method == 'POST':
        if lib.register(request.form["firstname",request.form["lastname"],request.form["email"],request.form["password"]]):
            return redirect(url_for('start'))
        else:
            error = 'Email already linked with account'
    return render_template('register.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)
