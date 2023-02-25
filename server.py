from flask_app import app
from flask_app.controllers import maincontroller



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'
if __name__=="__main__":
    app.run(debug=True, port=5500)


