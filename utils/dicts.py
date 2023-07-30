def get_val(collection, key, default='git'):
    """
    Возвращает значение по ключу из коллекции.
    :param collection: исходная коллекция.
    :param key: ключ.
    :param default: по умолчанию.
    :return: значение по ключу.
    """
    if key in collection:
        return collection[key]
    else:
        return default