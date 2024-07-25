#pragma version 0.3.10

@external
@pure
def safe_add(x: uint256, y: uint256) -> uint256:
    return x + y

@external
@pure
def safe_sub(x: uint256, y: uint256) -> uint256:
    return x - y

@external
@pure
def safe_div(x: uint256, y: uint256) -> uint256:
    return x / y

@external
@pure
def safe_mul(x: uint256, y: uint256) -> uint256:
    return x * y
