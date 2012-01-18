def sqrt(n):
    if n < 0:
        return 1j * (- n) ** 0.5
    else:
        return n ** 0.5
