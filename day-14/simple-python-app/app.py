from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Application launch page "\n" Congratulations on hosting your first containerized application! "\n" Application programming language "\n" Python "\n" Cloud provider "\n" AWS cloud "\n" Containerization tool "\n" Docker'

if __name__ == '__main__':
    app.run()




