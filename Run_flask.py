from flask import *
import os

app = Flask(__name__)
poll_data = {
   'question' : 'What is Your Favorite Season?',
   'fields'   : ['Winter', 'Spring', 'Summer', 'Fall']
}
poll_data1 = {
   'question' : 'How do you commute to work/school?',
   'fields'   : ['Bike', 'Auto', 'Car', 'Walk']
}
filename = 'data.txt'
filename1 = 'data1.txt'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("main.html")


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("main.html")

@app.route('/poll')
def root():
    return render_template('poll.html', data=poll_data)

@app.route('/result')
def show_results():
    vote = request.args.get('field')
    out = open(filename, 'a')
    out.write(vote + '\n')
    out.close()
    votes = {}
    for f in poll_data['fields']:
        votes[f] = 0

    f = open(filename, 'r')
    for line in f:
        vote = line.rstrip("\n")
        votes[vote] += 1

    return render_template('result.html', data=poll_data, votes=votes)

@app.route('/poll1')
def root1():
    return render_template('poll1.html', data=poll_data1)

@app.route('/result1')
def show_results1():
    vote = request.args.get('field')
    out = open(filename1, 'a')
    out.write(vote + '\n')
    out.close()
    votes = {}
    for f in poll_data1['fields']:
        votes[f] = 0

    f = open(filename1, 'r')
    for line in f:
        vote = line.rstrip("\n")
        votes[vote] += 1

    return render_template('result.html', data=poll_data1, votes=votes)


if __name__ == "__main__":
    app.run(debug=True)
