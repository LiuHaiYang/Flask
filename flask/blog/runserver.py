from blog import app
@app.route('/')
def hello_world():
    return 'Hello Python'

if __name__ == '__main__':
    app.run(debug=True)