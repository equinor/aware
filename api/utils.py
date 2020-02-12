def get_path(event, first_key, *keys):
    value = event.get(first_key, {})
    if keys is None:
        return value
    for key in keys:
        if key in value:
            value = value.get(key, {})
        else:
            return None
    return value