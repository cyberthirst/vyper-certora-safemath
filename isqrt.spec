methods {
    function isqrt_(uint256 y) external returns(uint256) envfree;
}

definition MAX_UINT256() returns uint256 = 115792089237316195423570985008687907853269984665640564039457584007913129639935;


rule result_is_max_half_maxuint256 {
    uint256 y;

    uint256 result = isqrt_(y);

    assert to_mathint(result) <= to_mathint(MAX_UINT256()) / 2, "The result should not exceed half of MAX_UINT256";
}

rule result_square_check {
    uint256 y;

    uint256 result = isqrt_(y);

    assert to_mathint(result) * to_mathint(result) <= to_mathint(y), "The square of the result should not exceed the input";
}


rule result_square_check2{
    uint256 y;

    uint256 result = isqrt_(y);

    assert (to_mathint(result) + 1) * (to_mathint(result) + 1) > to_mathint(y), "The square of the (result + 1) should exceed the input";
}

rule isqrt_monotonicity {
    uint256 x; uint256 y;
    require x < y;

    uint256 result_x = isqrt_(x);
    uint256 result_y = isqrt_(y);

    assert result_x <= result_y, "The square root function should be monotonically increasing";
}

rule isqrt_zero {
    uint256 result = isqrt_(0);
    assert result == 0, "The square root of 0 should be 0";
}

rule isqrt_one {
    uint256 result = isqrt_(1);
    assert result == 1, "The square root of 1 should be 1";
}

/* TIMEOUT
rule isqrt_perfect_square {
    uint256 x;
    require x * x <= to_mathint(MAX_UINT256());

    uint256 result = isqrt_(assert_uint256(x * x));
    assert result == x, "The square root of a perfect square should be exact";
}
*/

rule isqrt_multiplication {
    uint256 a; uint256 b;
    require a * b <= to_mathint(MAX_UINT256());
    uint256 sqrt_product = isqrt_(assert_uint256(a * b));
    uint256 product_sqrts = assert_uint256(isqrt_(a) * isqrt_(b));
    assert sqrt_product >= product_sqrts, "sqrt(a*b) >= sqrt(a) * sqrt(b)";
}

rule isqrt_addition {
    uint256 a; uint256 b;
    require a + b <= to_mathint(MAX_UINT256());
    uint256 sqrt_sum = isqrt_(assert_uint256(a + b));
    uint256 sum_sqrts = assert_uint256(isqrt_(a) + isqrt_(b));
    assert sqrt_sum <= sum_sqrts, "sqrt(a+b) <= sqrt(a) + sqrt(b)";
}

rule isqrt_continuity {
    uint256 x; uint256 y;
    require x < y;
    uint256 sqrt_x = isqrt_(x);
    uint256 sqrt_y = isqrt_(y);
    assert assert_uint256(sqrt_y - sqrt_x) <= isqrt_(assert_uint256(y - x)), "sqrt(y) - sqrt(x) <= sqrt(y - x)";
}

rule isqrt_geometric_mean {
    uint256 a; uint256 b;
    require (a + b) / 2 <= to_mathint(MAX_UINT256());
    require a * b <= to_mathint(MAX_UINT256());
    uint256 arithmetic_mean = assert_uint256((a + b) / 2);
    uint256 geometric_mean = isqrt_(assert_uint256(a * b));
    assert geometric_mean <= isqrt_(arithmetic_mean), "Geometric mean <= sqrt(arithmetic mean)";
}