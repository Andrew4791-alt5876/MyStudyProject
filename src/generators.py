def filter_by_currency(transactions, code):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == code:
            yield transaction
        else:
            yield {}


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction["description"]





usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
