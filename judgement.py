from flask import Flask, render_template, redirect, request, session, flash
import model

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03' #copied key from UberMelon_app


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/userlist')
def show_all_user_list():
    user_list = model.session.query(model.User).all()
    # user_page = 
    return render_template("user_list.html", user_list=user_list)

@app.route('/userpage/<int:id>')
def show_single_user(id):
    m = model.session.query(model.Data).filter_by(user_id = id).all()
    movie_list = []
    for rating in m:
        movie_list.append(rating.movie.title)

    return render_template("user_page.html", movie_list=movie_list, user_id = id)

@app.route("/login", methods=['GET'])
def show_login():
    #copied from UberMelon_app
    return render_template("login.html")    

@app.route("/login", methods=['POST'])
def process_login():
    #copied from UberMelon_app
    f = request.form

    user_email = f.get('email')
    user_password = f.get('password')


    user_login =  model.session.query(model.User).filter_by(email = user_email).filter_by(password = user_password).first()

    if not model.session.query(model.User).filter_by(email = user_email).filter_by(password = user_password).first():
        print "invalid e-mail address"
    else:
        session['email'] = user_email
        flash("You are logged in now, yay")

    return redirect('/')

@app.route("/signup", methods = ['GET'])
def show_signup():
    return render_template("signup.html")

@app.route("/signup", methods = ['POST'])
def process_signup():

    f = request.form

    user = model.User(email=f.get("email"), password=f.get("password"), age=f.get("age"), zipcode=f.get("zipcode"))
    model.session.add(user)
    model.session.commit()

    return redirect('/login')



if __name__ == "__main__":
    app.run(debug=True)

