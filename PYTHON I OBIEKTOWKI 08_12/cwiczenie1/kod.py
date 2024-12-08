def multiply (a, b)
    try:
        a = float (a)
        b = float (b)
        return round(a * b, 5)
    except:
        return None