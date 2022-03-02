import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import pandas as pd

app_dir = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(app_dir, "uploads")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/postyMcpostface', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(path)

        df = pd.read_csv(path)
        return df.to_html()

if __name__ == "__main__":
    app.run(debug=True)