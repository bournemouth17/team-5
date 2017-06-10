from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

# Conscious_big_sick
@app.route('/bigsick')
def bigsick():
	btn1 = open('information/Conscious_big_sick.txt', 'r+').read()
	return render_template('bigsick.html', test=btn1)

# Conscious_big_sick
@app.route('/littlesick')
def littlesick():
	btn2 = open('information/Conscious_little_sick.txt', 'r+').read()
	return render_template('littlesick.html', test=btn2)


# Conscious_big_sick
@app.route('/breathing')
def breathing():
	btn3 = open('information/Unconscious_breathing.txt', 'r+').read()
	return render_template('breathing.html', test=btn3)

# Conscious_big_sick
@app.route('/notbreathing')
def notbreathing():
	btn4 = open('information/Unconscious_not_breathing.txt', 'r+').read()
	return render_template('notbreathing.html', test=btn4)


if __name__ == "__main__":
    app.run(debug=True)

