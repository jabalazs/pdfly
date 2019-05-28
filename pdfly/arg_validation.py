def validate_page_numbers(from_page, to_page):
    if not isinstance(from_page, int) or not isinstance(to_page, int):
        raise ValueError("Page numbers must be integers")
    elif from_page < 0 or to_page < 0:
        raise ValueError("Page numbers must be positive integers")
    elif (from_page > to_page) and to_page != 0:
        raise ValueError(
            "First page number must be smaller than last page number"
        )
    return
