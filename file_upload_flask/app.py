from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
    return render_template('upload.html')


app.run(debug=True)