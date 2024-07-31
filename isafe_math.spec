definition MAX_INT256() returns mathint = 57896044618658097711785492504343953926634992332820282019728792003956564819967;
definition MIN_INT256() returns mathint = -57896044618658097711785492504343953926634992332820282019728792003956564819968;
definition ABS(int256 x) returns mathint = x < 0 ? -x : x;
// remainder = get_sign(x) * (abs(x) % abs(y))
definition REM(int256 x, int256 y) returns mathint = x < 0 ? -1 * (ABS(x) % ABS(y)) : ABS(x) % ABS(y);

methods {
    function safe_add(int256 x, int256 y) external returns(int256) envfree;
    function safe_sub(int256 x, int256 y) external returns(int256) envfree;
    function safe_div(int256 x, int256 y) external returns(int256) envfree;
    function safe_mul(int256 x, int256 y) external returns(int256) envfree;
    function safe_modulo(int256 x, int256 y) external returns(int256) envfree;
    function safe_exp_base2(int256 y) external returns(int256) envfree;
    function safe_abs(int256 y) external returns(int256) envfree;
}


rule safe_add {
    int256 a; int256 b;

    mathint cres = a + b; 

    int256 vres = safe_add@withrevert(a, b);

    if (cres >= MIN_INT256() && cres <= MAX_INT256()) {
        assert vres == assert_int256(cres);
    } else {
        assert lastReverted;
    }
}

rule safe_sub {
    int256 a; int256 b;

    mathint cres = a - b; 

    int256 vres = safe_sub@withrevert(a, b);

    if (cres >= MIN_INT256() && cres <= MAX_INT256()) {
        assert vres == assert_int256(cres);
    } else {
        assert lastReverted;
    }
}


rule safe_div {
    int256 a; int256 b;

     int256 vres = safe_div@withrevert(a, b);

    if (b != 0 && (a != assert_int256(MIN_INT256()) || b != -1)) {
        mathint cres = a / b;
        mathint remainder = a % b;
        mathint adjusted_cres = 
            (cres == 0) ? 0 :  // If the result is 0, don't adjust
            ((a < 0 && b > 0 && remainder != 0) || (a > 0 && b < 0 && remainder != 0)) ? 
                cres + 1 : cres;
        
        assert vres == assert_int256(adjusted_cres);
    } else {
        assert lastReverted;
    }
}

/*
rule safe_mul {
    int256 a; int256 b;

    mathint cres = a * b; 

    int256 vres = safe_mul@withrevert(a, b);

    if (cres >= MIN_INT256() && cres <= MAX_INT256()) {
        assert vres == assert_int256(cres);
    } else {
        assert lastReverted;
    }
}
*/


rule safe_mod {
    int256 a; int256 b;

    int256 vres = safe_modulo@withrevert(a, b);

    if (b != 0) {
        mathint cres = REM(a, b);
        assert vres == assert_int256(cres);
    } else {
        assert lastReverted;
    }
}


rule safe_exp_base2 {
    int256 b;

    require b >= 0;

    mathint cres = 1 << assert_uint256(b); 

    int256 vres = safe_exp_base2@withrevert(b);

    if (cres >= MIN_INT256() && cres <= MAX_INT256()) {
        assert vres == assert_int256(cres);
    } else {
        assert lastReverted;
    }
}

rule safe_abs {
    int256 b;

    require b >= 0;

    int256 vres = safe_abs@withrevert(b);

    if (b != assert_int256(MIN_INT256())) {
        mathint cres = ABS(b);
        assert vres == assert_int256(cres);
    } else {
        assert lastReverted;
    }
}

/*
function power(uint256 base, uint256 exp) returns uint256 {
    uint256 i, result = 1;
    for (i = 0; i < exp; i++)
        result *= base;
    return result;
}

rule safe_exp_general {
    uint256 base, exp;

    mathint cres = power(base, exp);

    uint256 vres = safe_exp_base2@withrevert(b);

    if (cres <= max_uint256) {
        assert vres == assert_uint256(cres);
    } else {
        assert lastReverted;
    }
}
*/