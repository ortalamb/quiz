from flask import Flask, request, redirect, url_for, render_template
from question import Question

questions = ["""\
What color are flowers?
    (a) Blue1
    (b) Red1
    (c) bhhh1 
    (d) njnj1""",

"""\
What is the ans?
    (a) Blue2
    (b) Red1
    (c) bhhh1
    (d) njnj1""",

"""\
Who is the prime?
  (a) Blue3
  (b) Red1
  (c) bhhh1
  (d) njnj1""",
  
"""\
What are hggy?
 (a) Blue4
 (b) Red1
 (c) bhhh1
 (d) njnj1"""]

answers=['a','b','c','a']

queries = [Question(question, answer) for question, answer in zip(questions, answers)]


app = Flask(__name__)

@app.route('/')

def form():
    result = f"""<body style="background-color:powderblue;">
            <form action="/submit" method="post">"""
    for i, question in enumerate(questions):
            result += f"""
            <h1>Question # {i+1}</h1>
            <pre>{question}</pre>
            <form action="/submit" method="post">
            <label for="ans{i}">Your answer is:</label><br>
            <input type="text" id="ans{i}" name="ans{i}" value=""><br><br>
            """
    result+=f"""<input type="submit" value="Submit">
            </form>"""

    return result
    # return render_template('main.html', q = questions)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    print(data)
    score = 0
    for i,ans in enumerate(answers):
        if ans == data[f"""ans{i}"""]:
            score += 1
    return f""" <h1 style="background-color:Orange;">Your score is {score} / {len(answers)}</h1>"""

from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


if __name__ == '__main__':
 app.run(debug=True)