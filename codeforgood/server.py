from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/bigsick')
def bigsick():
	btn1 = open('information/Conscious_big_sick/Conscious_big_sick.txt', 'r+').read()
	return render_template('bigsick.html', test=btn1)


@app.route('/littlesick')
def littlesick():
	btn2 = open('information/Conscious_little_sick/Conscious_little_sick.txt', 'r+').read()
	return render_template('littlesick.html', test1=btn2)



@app.route('/breathing')
def breathing():
	btn3 = open('information/Unconscious_breathing/Unconscious_breathing.txt', 'r+').read()
	return render_template('breathing.html', test2=btn3)


@app.route('/notbreathing')
def notbreathing():
	btn4 = open('information/Unconscious_not_breathing/Unconscious_not_breathing.txt', 'r+').read()
	return render_template('notbreathing.html', test3=btn4)

@app.route('/explore)
def explore():
	return render_template(explore.html')
	
if __name__ == "__main__":
    app.run(debug=True)
