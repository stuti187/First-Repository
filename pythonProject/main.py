from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index1.html')
@app.route("/index1.html")
def home1():
    return render_template('index1.html')
@app.route("/contact.html")
def contact():
    return render_template('contact.html')
@app.route("/More.html")
def more():
    return render_template('More.html')

# @app.route("/about")
# def about():
#     return render_template('about.html')
# @app.route("/contact", methods = ['GET', 'POST'])
# def contact():
#     return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True)