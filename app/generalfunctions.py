
from decimal import Decimal


def floating_decimals(f_val, dec):
    prc = "{:."+str(dec)+"f}"

    return Decimal(prc.format(f_val))