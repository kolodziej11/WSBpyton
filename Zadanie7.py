from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*arg, **kwargs):
        print('Dekorator')
        return func(*arg,**kwargs)
    return wrapper

@decorator
def funkcja():
    return 0
def main():
    print(funkcja.__name__)
    funkcja()
if __name__ == '__main__':
    main()
