RATE_MULTIPLIER = 1.15
DEFAULT_LOG_FILE = "log.txt"


def _validate_data(data):
    """Validate input data and fail fast with clear messages."""
    if data is None:
        raise ValueError("data cannot be None")
    if not isinstance(data, list):
        raise TypeError("data must be a list of numeric values")

    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("all data items must be numeric")


def _calculate_totals(data, rate_multiplier=RATE_MULTIPLIER):
    """Pure transformation: apply multiplier to each value."""
    return [value * rate_multiplier for value in data]


def _format_total_lines(totals):
    """Pure formatting: create user-facing output lines."""
    return [f"Total: {total:.2f}" for total in totals]


def _print_lines(lines):
    for line in lines:
        print(line)


def _append_log(totals, log_file=DEFAULT_LOG_FILE):
    with open(log_file, "a", encoding="utf-8") as file_handle:
        file_handle.write(f"{totals}\n")


def process_data(data):
    """Orchestrate data processing, display, and logging."""
    _validate_data(data)
    totals = _calculate_totals(data)
    lines = _format_total_lines(totals)

    _print_lines(lines)
    _append_log(totals)

    return totals
