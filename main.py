from flask import Flask, render_template,request
from script import assistant_gui


app = Flask(__name__)


@app.route("/")
def load_home():
    return render_template('home.html')


@app.route("/team")
def team():
    return render_template('team.html')



@app.route("/func",methods={'GET','POST'})
def process():
    name =request.form.get('input')
    if name:
        assistant_gui.respond(name.lower())
    else:
        name=assistant_gui.record_audio()
        assistant_gui.respond(name)
    return render_template('home.html')


if __name__ == "__main__":
    app.run()
