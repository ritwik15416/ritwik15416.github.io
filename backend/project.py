from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm
app=Flask(__name__)
app.config['SECRET_KEY']='7c33c9b6be66139cc21104999b9dae7b'
@app.route('/home')
def home():
    return render_template('home.html',title='Home')
@app.route("/signup",methods=['GET','POSTS'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('signup.html',title='Register',form=form)

app.run(debug=True)
