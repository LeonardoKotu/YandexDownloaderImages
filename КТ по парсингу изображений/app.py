from flask import Flask, render_template, request, send_file
import requests
from io import BytesIO
from parser import parse_images

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parse', methods=['POST'])
def parse():
    category = request.form['category']
    images = parse_images(category)
    return {'images': images}

@app.route('/download')
def download():
    url = request.args.get('url')
    filename = request.args.get('filename')
    
    response = requests.get(url)
    return send_file(
        BytesIO(response.content),
        as_attachment=True,
        download_name=filename
    )

if __name__ == '__main__':
    app.run(debug=True)