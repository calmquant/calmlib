from functools import wraps
import inspect


def autocast_args(fail_on_errors=True):
    def cast_arg(arg, arg_sig, func_name):
        try:
            if arg_sig.annotation is not inspect._empty:
                return arg_sig.annotation(arg)
        except Exception as e:
            if fail_on_errors:
                raise TypeError(
                    f"Failed to cast argument {arg_sig.name} of funciton {func_name} to type {arg_sig.annotation}")
        return arg

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            signature = inspect.signature(func)
            casted_args = []
            args = [cast_arg(arg, arg_sig, func.__name__) for arg, arg_sig in zip(args, signature.parameters.values())]
            kwargs = {key: cast_arg(val, signature.parameters[key], func.__name__) for key, val in kwargs.items()}

            return func(*args, **kwargs)

        return wrapper

    return decorator
