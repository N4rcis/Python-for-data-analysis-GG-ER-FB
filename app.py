from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template("host.html")

@app.route('/datav')
def datav():
   return render_template("datav.html")

@app.route('/datam')
def datam():
   return render_template("datam.html")

@app.route('/indivp')
def indivp():
   return render_template("individuals.html")

@app.route('/data_analysis')
def data_analysis():
   return render_template("data_analysis.html")

if __name__ == '__main__':
   app.run()
   
   