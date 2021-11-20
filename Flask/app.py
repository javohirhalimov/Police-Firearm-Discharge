from flask import Flask, render_template, url_for 
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
@app.route('/main', methods=['GET', 'POST'])
def main():
    return render_template('index.html')


@app.route('/charts', methods=['GET', 'POST'])
def charts():
    return render_template('charts.html', title='What is good bro?')


if __name__ == '__main__':
    app.run(debug=True)