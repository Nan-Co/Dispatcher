import functools

def dispatcher(func):
    
    registry = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            key = kwargs.get("key")
            targetfunc = registry[key]
        except KeyError:
            pass
        else:
            del kwargs["key"]
            return targetfunc(*args, **kwargs)
        
        return func(*args, **kwargs)

    def register(value):
        def wrap(func):
            if value in register:
                raise ValueError("@dispatcher:%s is repeated registration value"%value)
            registry[value] = func
            return func
        return wrap
    
    def registerall(values):
        def wrap(func):
            for value in values:
                if value in registry:
                    raise ValueError("@dispatcher:%s is repeated registration value"%value)
                registry[value] = func
            return func
        return wrap

    wrapper.register = register
    wrapper.registerall = registerall
    return wrapper