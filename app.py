from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
import backend
from os import environ
import threading, webbrowser

app = Flask(__name__)
Bootstrap(app)


def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)


@app.route('/loading', methods=['GET', 'POST'])
def newquestion():
    return redirect(redirect_url())

# this is the home screen where you can select the general university course of study
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/choose', methods=['GET', 'POST'])
def practice():
    return render_template('computing.html')

# this is the page where you've already chosen the course, and are presented with a list of modules
@app.route('/<course>', methods=['GET', 'POST'])
def coursechoice(course):
    return render_template(
        'computing.html',
        course=course)


@app.route('/<course>/<subject>', methods=['GET', 'POST'])
def setcuecard(course, subject):
    coursename = course
    sheetname = subject + "CC.xlsx"
    question, answer = backend.showcard(sheetname)
    return render_template(
        'gamescreen.html',
        subject=subject,
        question=question,
        answer=answer,
        coursename=coursename
    )


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down. Please close this window.'


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    url = "http://127.0.0.1:{0}".format(PORT)

    threading.Timer(1.25, lambda: webbrowser.open(url)).start()
    app.run(HOST, PORT, debug=False)
