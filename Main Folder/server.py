from flask import Flask,render_template,url_for
app=Flask(__name__)

@app.route('/')
@app.route('/Home/home.html')
def welcome():
    return render_template('/Home/home.html',title='Home')
@app.route('/Contact/contact.html')
def contact():
    return render_template('/Contact/contact.html',title="Contact")
@app.route('/About/about.html')
def about():
    return render_template('/About/about.html',title="About")
@app.route('/Signup/signup.htm')
def signup():
    return render_template('/Signup/signup.htm',title="Sign Up")
@app.route('/Login/login.html')
def login():
    return render_template('/Login/login.html',title="Log In")
app.run(debug=True)