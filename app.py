from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from risk_engine import parse_transactions, analyze

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    signals = None
    if request.method == 'POST':
        if 'statement' not in request.files:
            return render_template('index.html', error='No file part')
        file = request.files['statement']
        if file.filename == '':
            return render_template('index.html', error='No selected file')
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        transactions = parse_transactions(path)
        signals = analyze(transactions)
    return render_template('index.html', signals=signals)

if __name__ == '__main__':
    app.run(debug=True)
