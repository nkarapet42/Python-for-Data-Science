def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {object.__class__}")
    elif object != object:
        print(f"Cheese: {object} {object.__class__}")
    elif object == 0:
        print(f"Zero: {object} {object.__class__}")
    elif object == "":
        print(f"Empty: {object} {object.__class__}")
    elif object is False:
        print(f"Fake: {object} {object.__class__}")
    else:
        print("Type not Found")
        return 1
    return 0