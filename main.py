def calculate_shares(amount):
    shares = {
        "VOOG": 40,
        "V00": 25,
        "VTI": 20,
        "VHT": 15,
    }

    fees = 0
    total = 0
    print(f"{'Name':{' '}^{6}} | {'Per(%)':{' '}^{6}} | {'Value ($)':{' '}^{20}} | {'Tax ($)':{' '}^{20}} | "
          f"{'VAT ($)':{' '}^{20}}")
    for key, val in shares.items():
        realValue = amount * (val / 100)
        # tax = realValue * 0.01
        tax = 0.5
        valueAfterTax = realValue - tax
        total += valueAfterTax
        fees += tax
        print(f"{key:{' '}^{6}} | {val:{' '}^{6}} | {realValue:{' '}^{20}} | {tax:{' '}^{20}} | "
              f"{valueAfterTax:{' '}^{20}}")

    return total, fees


if __name__ == '__main__':
    print(calculate_shares(103.30))
