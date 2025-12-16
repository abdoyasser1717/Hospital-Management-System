def input_valid_int(msg, start=1, end=None):
    while True:
        raw = msg
        parts = [p for p in raw.split() if p.isdigit()]
        if not parts:
            print("Invalid input. Must contain an integer.")
            continue
        val = int(parts[0])
        if val < start:
            print(f"Value must be >= {start}")
            continue
        if end is not None and val > end:
            print(f"Value must be <= {end}")
            continue
        return val
if __name__ == '__main__':
    input_valid_int("Enter a number")






