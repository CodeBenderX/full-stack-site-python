from flask import Flask, request, render_template

app = Flask(__name__)
#accout database
accounts = []
id_counter = 1

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/form')
def form_page():
    return render_template('form-page.html')

@app.post('/create-account')
def create_account():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    
    global id_counter
    account = {
        'id': id_counter,
        'first_name': first_name,
        'last_name': last_name
    }
    #Create an account
    accounts.append(account)
    id_counter += 1
    return render_template('account-created.html', first_name=first_name, last_name=last_name)

@app.get('/accounts')
def list_accounts():
    return {'accounts': accounts}

if __name__ == '__main__':
    app.run(debug=True)