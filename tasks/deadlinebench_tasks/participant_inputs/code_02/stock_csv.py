"""Synthetic DeadlineBench fixture: buggy warehouse stock reconciliation.

Records have sku, quantity, and location fields. Negative quantities are
adjustments, not invalid stock rows. See TASK.md; this is not production code.
"""
import csv
import io


def read_stock(text):
    """Read stock adjustment records from a headered CSV string."""
    lines = text.splitlines()
    if not lines:
        return []
    header = lines[0].split(",")
    records = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = line.split(",")
        row = dict(zip(header, values))
        records.append({"sku": row["sku"], "quantity": int(row["quantity"]),
                        "location": row["location"]})
    return records


def totals(records):
    """Sum each (sku, location) key, keeping keys whose net stock is zero."""
    result = {}
    for row in records:
        key = (row["sku"], row["location"])
        result[key] = row["quantity"]
    return result


def available(records, sku):
    """Sum nonnegative net stock for sku independently at each location."""
    return sum(row["quantity"] for row in records if row["sku"] == sku)


def shortages(records):
    """List sorted (sku, location, positive deficit) tuples for negative nets."""
    return sorted((row["sku"], row["location"], -row["quantity"])
                  for row in records if row["quantity"] < 0)


def write_stock(records):
    """Serialize valid records in their input order as canonical CSV."""
    result = ["sku,quantity,location"]
    for row in records:
        result.append(f'{row["sku"]},{row["quantity"]},{row["location"]}')
    return "\n".join(result)


def transfer(records, sku, source, target, quantity):
    """Return copied records plus two adjustments for a valid stock move."""
    if quantity < 0:
        raise ValueError("negative transfer")
    records.append({"sku": sku, "quantity": -quantity, "location": source})
    records.append({"sku": sku, "quantity": quantity, "location": target})
    return records
