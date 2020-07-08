from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def ola():
    return render_template('template.html')

app.run(host='0.0.0.0', port=8080)
