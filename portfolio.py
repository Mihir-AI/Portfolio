from flask import Flask,render_template,request,redirect
app=Flask(__name__)

@app.route('/index.html')
def my_home():
    return render_template("index.html")
@app.route('/works.html')
def work():
    return render_template("works.html")
@app.route('/about.html')
def about():
    return render_template("about.html")
@app.route('/contact.html')
def contact():
    return render_template("contact.html")
def write(data):
    with open("database.txt",mode="a") as database:
        email=data["email"]
        message=data["message"]
        subject=data["subject"]
        file=database.write(f"\n {email},{message},{subject}")
@app.route('/submit',methods=["POST","GET"])
def submit_form():
    if request.method=="POST":
        data=request.form.to_dict()
        write(data)
        return "Form Submitted,Thank you"
    else:
         return "Something is wrong"
app.run()
