import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def funkcja():
    print("WSB")

def main():
    funkcja()
    funkcja()
    funkcja()
    funkcja()
    funkcja()
    funkcja()
    funkcja()
    funkcja()
    funkcja()
    funkcja()
    funkcja()
    print(funkcja.num_calls)

if __name__ == '__main__':
    main()