# Projects

Just for fun

## Risk Engine Example

This repository includes a simple Python script that analyzes a bank statement CSV file and prints basic risk signals. To try it out:

1. Ensure you have Python 3 installed (no external packages are required).
2. Run the script against `sample_bank_statement.csv`:

```bash
python3 risk_engine.py sample_bank_statement.csv
```

You can replace `sample_bank_statement.csv` with your own statement file in the same format (columns: `Date`, `Description`, `Amount`, `Balance`).

## Web UI

You can also try the risk engine in your browser using a small Flask app. First install Flask:

```bash
pip install flask
```

Run the web application:

```bash
python3 app.py
```

Then open <http://localhost:5000> and upload a CSV bank statement. The detected risk signals will be highlighted on the page.
