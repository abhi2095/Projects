import csv
import sys

LARGE_TRANSACTION_THRESHOLD = 1000.0


def parse_transactions(path):
    """Load transactions from a CSV file."""
    transactions = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                amount = float(row.get("Amount", 0))
            except ValueError:
                continue
            try:
                balance = float(row.get("Balance", 0))
            except ValueError:
                balance = 0
            transactions.append({
                "date": row.get("Date"),
                "description": row.get("Description", ""),
                "amount": amount,
                "balance": balance,
            })
    return transactions


def analyze(transactions):
    risk_signals = []

    # Negative balance days
    negative_days = [t for t in transactions if t["balance"] < 0]
    if negative_days:
        risk_signals.append(
            f"Account had negative balance on {len(negative_days)} days"
        )

    # Large transactions
    large = [t for t in transactions if abs(t["amount"]) >= LARGE_TRANSACTION_THRESHOLD]
    for t in large:
        risk_signals.append(
            f"Large transaction {t['amount']:.2f} on {t['date']} ({t['description']})"
        )

    # Count cash/ATM withdrawals
    atm = [t for t in transactions if "ATM" in t["description"].upper() or "CASH" in t["description"].upper()]
    if atm:
        risk_signals.append(f"ATM/cash withdrawals: {len(atm)}")

    # Withdrawal to deposit ratio
    deposits = sum(t["amount"] for t in transactions if t["amount"] > 0)
    withdrawals = -sum(t["amount"] for t in transactions if t["amount"] < 0)
    if deposits:
        ratio = withdrawals / deposits
        risk_signals.append(f"Withdrawal to deposit ratio: {ratio:.2f}")

    return risk_signals


def main(path):
    transactions = parse_transactions(path)
    signals = analyze(transactions)
    print("Risk signals:")
    for s in signals:
        print("-", s)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 risk_engine.py <statement.csv>")
        sys.exit(1)
    main(sys.argv[1])
