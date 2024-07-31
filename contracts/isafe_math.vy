#pragma version 0.3.10

@external
@pure
def safe_add(x: int256, y: int256) -> int256:
    return x + y

@external
@pure
def safe_sub(x: int256, y: int256) -> int256:
    return x - y

@external
@pure
def safe_div(x: int256, y: int256) -> int256:
    return x / y

@external
@pure
def safe_mul(x: int256, y: int256) -> int256:
    return x * y

@external
@pure
def safe_modulo(x: int256, y: int256) -> int256:
    return x % y

@external
@pure
def safe_exp_base2(y: int256) -> int256:
    return 2 ** y

@external
@pure
def safe_abs(y: int256) -> int256:
    return abs(y)
