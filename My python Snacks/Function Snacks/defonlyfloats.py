def only_floats(a, b):
    if isinstance(a, float) and isinstance(b, float):
        return 2

    elif isinstance(a, float) or isinstance(b, float):
        return 1
    else:
        return 0
