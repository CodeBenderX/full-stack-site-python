from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html', first_name='Julius')

if __name__ == '__main__':
    app.run(debug=True)