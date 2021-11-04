import timeit


def time_test(loops):
    def func_wrapper(func):
        def wrapper(*args, **kwargs):
            start_time = timeit.default_timer()
            for _ in range(loops - 1):
                func(*args, **kwargs)
            result = func(*args, **kwargs)
            stop_time = timeit.default_timer() - start_time
            print(f'Function operation time {func.__name__}: ' + str((stop_time) * 1000 / loops) + 'ms')
            return result
        return wrapper
    return func_wrapper