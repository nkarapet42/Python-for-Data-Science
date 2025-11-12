def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    if object_type in [list, tuple, set, dict]:
        print(f"{type(object).__name__.capitalize()} : {object.__class__}")
    elif object_type is str:
        print(f"{object} is in the kitchen : {object.__class__}")
    else:
        print("Type not found")
    return 42