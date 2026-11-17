
def clean_colour_name(name):
    """
    Turns a colour name into a lower-case code.
    """
    if not isinstance(name, str):
        return ""

    return name.strip().lower().replace(' ', '_')


def room_area(text):
    """
    Converts LENGTHxWIDTH into an area in square feet.
    """
    if not isinstance(text, str):
        return 0

    try:
        parts = text.lower().split('x')

        if len(parts) != 2:
            return 0

        length, width = parts

        length = int(length.strip())
        width = int(width.strip())

        if length < 0 or width < 0:
            return 0

        return length * width

    except ValueError:
        return 0


def total_wall_area(text):
    """
    Adds wall areas separated by semicolons.
    """
    if not isinstance(text, str) or not text.strip():
        return 0

    try:
        areas = text.split(';')
        return sum(int(area.strip()) for area in areas)
    except ValueError:
        return 0


def main():
    print("==== Running clean_colour_name ====")
    value = input("Enter a paint colour name (e.g. Ocean Blue): ")
    print("Colour code:", clean_colour_name(value))

    print("\n==== Running room_area ====")
    value = input("Enter room size as LENGTHxWIDTH in feet (e.g. 12x10): ")
    print("Room area (sq ft):", room_area(value))

    print("\n==== Running total_wall_area ====")
    value = input("Enter wall areas separated by ; (e.g. 120;95;110): ")
    print("Total wall area (sq ft):", total_wall_area(value))


if __name__ == "__main__":
    main()
