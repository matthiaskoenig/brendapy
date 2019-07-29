
def is_ec_number(ec):
    """Tests if given string 'ec' is EC number.

    :param ec: ec string
    :return: True if EC number, False otherwise
    """
    ec = ec.strip().split(".")
    for number in ec:
        if not number.isdigit():
            return False
    return True
