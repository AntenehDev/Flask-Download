from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download_file():
    file = 'flask.png'
    return send_file(file,as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)