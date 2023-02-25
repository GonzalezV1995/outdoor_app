from flask_app import app
from flask import render_template, request, redirect, session


@app.route('/')  
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response  
# The "@" decorator associates this route with the function immediately following


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')