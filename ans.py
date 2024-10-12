import time as t
import threading

def conditional_cache(expiry, condition, max_size=5):
    cache = {}
    lock = threading.Lock()

    def decorator(function):
        def wrapper(*args, **kwargs):
            if not condition(*args, **kwargs):
                return None
            
            key = (args, tuple(sorted(kwargs.items())))
            time_now = t.time()

            with lock:
                expired_keys = []
                for k, (val, timestamp) in cache.items():
                    if time_now - timestamp > expiry:
                        expired_keys.append(k)
                
                for k in expired_keys:
                    del cache[k]

                if key in cache:
                    val, timestamp = cache[key]
                    if time_now - timestamp <= expiry:
			cache[key] = (val, t.time())
                        return val

            final_result = function(*args, **kwargs)

            with lock:
                if len(cache) >= max_size:
                    oldest_key = min(cache, key=lambda k: cache[k][1])
                    del cache[oldest_key]
                
                cache[key] = (final_result, t.time())

            return final_result

        return wrapper

    return decorator


def is_positive(x):
    return x > 0


@conditional_cache(expiry=5, condition=is_positive)
def compute_square(x):
    print(f"Computing square of {x}")
    return x * x


print(compute_square(3))
t.sleep(2)
print(compute_square(3))
t.sleep(4)
print(compute_square(3))
print(compute_square(-3))
