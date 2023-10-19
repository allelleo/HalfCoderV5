def override(func):
    def _wrapper(*args, **kwargs):
        func(*args, **kwargs) 
    return _wrapper