import re

def parse_receipt_text(text):
    """Parse text from OCR output to extract structured receipt data."""
    lines = text.split("\n")
    items = []
    total_amount = None
    date = None

    price_pattern = re.compile(r"\d+\.\d{2}")
    date_pattern = re.compile(r"\d{2}/\d{2}/\d{4}")

    for line in lines:
        if not date:
            match = date_pattern.search(line)
            if match:
                date = match.group()

        if price_pattern.search(line):
            parts = line.split()
            try:
                price = float(parts[-1].replace("$", ""))
                name = " ".join(parts[:-1])
                items.append({"name": name, "price": price})
            except:
                continue

        if "total" in line.lower() and price_pattern.search(line):
            total_amount = float(price_pattern.search(line).group())

    return {"items": items, "date": date, "total_amount": total_amount}
