class DatabaseMeta(type):
    _instance = None  # esto es estatico

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)

        return cls._instance
