from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.utils import read_json_file

if __name__ == '__main__':
    # Проверка masks
    get_mask_card_number(7000792289606361)
    get_mask_account(7365410843013587430)

    # Проверка utils
    read_json_file("data/operations.json")
