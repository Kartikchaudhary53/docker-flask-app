from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask inside Docker 🚀"

@app.route('/about')
def about():
    return "This is a Docker + Flask CI/CD project"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# final update
