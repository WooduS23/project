from .masks import mask_card_number, mask_account_number

def mask_account_card(input_string: str) -> str:
    """
    Принимает на вход строку с типом карты или счета и возвращает замаскированный номер
    """
    parts = input_string.split()
    card_type = " ".join(parts[:-1])
    number = parts[-1]
    if card_type.lower() in ["visa platinum", "maestro", "mastercard", "visa classic", "visa gold"]:
        return f"{card_type} {mask_card_number(number)}"
    elif card_type.lower() == "счет":
        return f"{card_type} {mask_account_number(number)}"
    else:
        return "Неизвестный тип карты или счета"


def get_date(date_string: str) -> str:
    """
    Принимает на вход строку и возвращает дату в формате 'DD.MM.YYYY'.
    """
    year, month, day = date_string.split('-')
    return f"{day}.{month}.{year}"