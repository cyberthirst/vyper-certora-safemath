methods {
    function safe_add(uint256 x, uint256 y) external returns(uint256) envfree;
    function safe_sub(uint256 x, uint256 y) external returns(uint256) envfree;
    function safe_div(uint256 x, uint256 y) external returns(uint256) envfree;
    function safe_mul(uint256 x, uint256 y) external returns(uint256) envfree;
}


rule safe_add {
    uint256 a; uint256 b;

    mathint cres = a + b; 

    uint256 vres = safe_add@withrevert(a, b);

    if (cres <= max_uint256) {
        assert vres == assert_uint256(cres);
        assert vres >= a;
        assert vres >= b;
    } else {
        assert lastReverted;
    }
}

rule safe_sub {
    uint256 a; uint256 b;

    mathint cres = a - b; 

    uint256 vres = safe_sub@withrevert(a, b);

    if (cres < 0) {
        assert lastReverted;
    } else {
        assert vres == assert_uint256(cres);
        assert vres <= a;
    }
}

rule safe_div {
    uint256 a; uint256 b;

    uint256 vres = safe_div@withrevert(a, b);

    if (b == 0) {
        assert lastReverted;
    } else {
        mathint cres = a / b;
        assert vres == assert_uint256(cres);
        assert vres <= a;
    }
}

rule safe_mul {
    uint256 a; uint256 b;

    mathint cres = a * b; 

    uint256 vres = safe_mul@withrevert(a, b);

    if (cres <= max_uint256) {
        assert vres == assert_uint256(cres);
        if (a != 0 && b != 0) {
            assert vres >= a;
            assert vres >= b;
        } else {
            assert vres == 0;
        }
    } else {
        assert lastReverted;
    }
}