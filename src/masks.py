def mask_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты и возращает маску номера
    """
    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_card_number


def mask_account_number(account_number: str) -> str:
    """
    Принимает на вход номер счета и возращает маску номера
    """
    masked_account_number = f"**{account_number[-4:]}"
    return masked_account_number
