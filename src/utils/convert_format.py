def convert_to_number(value: str):
    if isinstance(value, (int, float)):
        return value
    value = value.strip().lower()
    multiplier = 1
    if value.endswith('k'):
        multiplier = 1_000
        value = value[:-1]
    elif value.endswith('m'):
        multiplier = 1_000_000
        value = value[:-1]
    elif value.endswith('b'):
        multiplier = 1_000_000_000
        value = value[:-1]
    elif value.endswith('%'):
        return round(float(value.replace("%",'')),2)  # Convert percentage to float and round to 4 decimal places

    return round(float(value) * multiplier, 2)  # Round to 2 decimal places


def format_number(value):
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f}b"
    elif value >= 1_000_000:
        return f"{value / 1_000_000:.2f}m"
    elif value >= 1_000:
        return f"{value / 1_000:.2f}k"
    else:
        return str(value)