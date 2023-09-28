import random


def generate_otp() -> str:
    chars = "0123456789"
    code = ""
    for _ in range(6):
        code += random.choice(chars)
    return code
