from flask import Flask, render_template    #imports flask
app = Flask(__name__)                       #this variable tells Flask if we are running the file or importing it as a module (?I have ?s about this.)

@app.route('/')
def portfolio():
    return render_template('portfolio.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)
