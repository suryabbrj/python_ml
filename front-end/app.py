from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/after', methods=['GET', 'POST'])
def after():
    file = request.files['file1']

    file.save('static/file.jpg')

    return render_template('predict.html')


if __name__ == "__main__":
    app.run(debug=True)
