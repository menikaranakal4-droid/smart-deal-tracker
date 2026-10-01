import pandas as pd
from app.storage.storage import load_products


def create_report():
    products = load_products()
    df = pd.DataFrame(products)

    total_products = len(df)

    target_reached = len(
        df[df["status"] == "Target price reached"]
    )

    priced_products = df.dropna(subset=["current_price"])

    if not priced_products.empty:
        average_price = priced_products["current_price"].mean()
        highest_price = priced_products["current_price"].max()
        lowest_price = priced_products["current_price"].min()
    else:
        average_price = None
        highest_price = None
        lowest_price = None

    largest_price_drop = None

    for product in products:
        history = product.get("price_history", [])

        if len(history) >= 2:
            prices = [entry["price"] for entry in history]
            price_drop = max(prices) - min(prices)

            if largest_price_drop is None or price_drop > largest_price_drop:
                largest_price_drop = price_drop

    report = pd.DataFrame([{
        "total_products": total_products,
        "target_reached": target_reached,
        "average_price": average_price,
        "highest_price": highest_price,
        "lowest_price": lowest_price,
        "largest_price_drop": largest_price_drop
    }])

    report.to_csv("data/report_new.csv", index=False)

    return report