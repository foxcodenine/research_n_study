from flask import Flask, render_template, redirect, request

app = Flask(__name__)

app.config["DEBUG"] = True






@app.route('/', methods=['POST', 'GET'])
def index():
    answer = None

    if request.method == 'POST':
        answer = request.form['question']
        return render_template('index.html', answer=answer)

    return render_template(
        'index.html', answer=answer
    )







if __name__ == '__main__':
    app.run()