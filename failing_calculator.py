def average_ratios(numbers):
    """Return average of 100/x for non-zero numeric inputs."""
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    if not numbers:
        raise ValueError("numbers cannot be empty")

    non_zero_numbers = []
    for value in numbers:
        if not isinstance(value, (int, float)):
            raise TypeError("all items in numbers must be numeric")
        if value != 0:
            non_zero_numbers.append(value)

    if not non_zero_numbers:
        raise ValueError("numbers must contain at least one non-zero value")

    total = 0
    for value in non_zero_numbers:
        total += 100 / value

    return total / len(non_zero_numbers)


if __name__ == "__main__":
    try:
        print(average_ratios([10, 5, 0]))
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
