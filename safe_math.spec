methods {
    function safe_add(uint256 x, uint256 y) external returns(uint256) envfree;
}


rule safe_add {
    uint256 a; uint256 b;

    mathint cres = a + b; 

    uint256 vres = safe_add@withrevert(a, b);

    if (cres <= max_uint256) {
        assert vres == assert_uint256(cres);
    } else {
        assert lastReverted;
    }
}