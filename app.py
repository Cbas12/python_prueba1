from flask import Flask, request, render_template

app = Flask(__name__, template_folder='/path/to/template/folder')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        op = request.form['operator']
        if op == 'add':
            result = num1 + num2
        elif op == 'subtract':
            result = num1 - num2
        elif op == 'multiply':
            result = num1 * num2
        elif op == 'divide':
            result = num1 / num2
        return render_template('index.html', result=result)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
