from flask import app
from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models.user import User
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/user', methods=["POST"])
def register():
    if not User.validate_registration(request.form):
        (print(request.form))
        return redirect('/')

    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'city' : request.form['city'],
        'state' : request.form['state'],
        'password' : bcrypt.generate_password_hash(request.form['password'])
    }

    userId=User.save(data)
    session['userId'] = userId
    return redirect ('/dashboard')

@app.route('/dashboard')
def dashboard():
    
    if 'userId' not in session:
        
        return redirect('/')
    print(session['userId'])
    data = {
        "id": session['userId']

    }
    user=User.getById(data)

    return render_template('dashboard.html',user=user)


@app.route('/login', methods=['POST'])
def login():
        if not User.validate_login(request.form):
            # flash("Invalid Email","login")
            return redirect('/')
        # if not bcrypt.check_password_hash(registration.password,request.form['password']):
        #     flash('invalid email or password', 'login')
        #     return redirect('/')
        userId=User.getByEmail(request.form)
        # print("controller" +registrationId ['email'])
        session['userId']=userId ['id']
        return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
