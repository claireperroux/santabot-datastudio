from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        code = request.form.get('code1') + request.form.get('code2') + request.form.get('code3') + request.form.get('code4')
        if code == "0000":
            message = "IA désactivée"
        else:
            message = "Échec ! Essayez à nouveau"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
