from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/about")
def about():
    return  render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/vid_upload")
def vid_upload():
    return render_template("vid_upload.html")


if __name__ == '__main__':
    app.run(debug="True")
