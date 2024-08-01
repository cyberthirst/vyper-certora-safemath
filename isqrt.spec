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

rule isqrt_perfect_square {
    uint256 x;
    require x * x <= to_mathint(MAX_UINT256());

    uint256 result = isqrt_(assert_uint256(x * x));
    assert result == x, "The square root of a perfect square should be exact";
}