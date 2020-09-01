from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
@app.route('/signup')
def welcome():
    return render_template("signup.html",title='SignUp')


app.run(debug=True)
