
src_fmpq_poly = files(['add.c', 'add_series.c', 'asin_series.c', 'asinh_series.c', 'atan_series.c', 'atanh_series.c', 'canonicalise.c', 'clear.c', 'cmp.c', 'compose.c', 'compose_series.c', 'compose_series_brent_kung.c', 'compose_series_horner.c', 'content.c', 'cos_series.c', 'cosh_series.c', 'debug.c', 'derivative.c', 'div.c', 'div_series.c', 'divrem.c', 'equal.c', 'equal_trunc.c', 'evaluate_fmpq.c', 'evaluate_fmpz.c', 'evaluate_mpq.c', 'evaluate_mpz.c', 'exp_series.c', 'fit_length.c', 'fprint.c', 'fprint_pretty.c', 'fread.c', 'gcd.c', 'gegenbauer_c.c', 'get_coeff_fmpq.c', 'get_coeff_mpq.c', 'get_nmod_poly.c', 'get_slice.c', 'get_str.c', 'get_str_pretty.c', 'init.c', 'inlines.c', 'integral.c', 'interpolate_fmpz_vec.c', 'inv.c', 'inv_series_newton.c', 'invsqrt_series.c', 'is_canonical.c', 'is_monic.c', 'is_squarefree.c', 'laguerre_l.c', 'lcm.c', 'legendre_p.c', 'log_series.c', 'make_monic.c', 'mul.c', 'mullow.c', 'neg.c', 'normalise.c', 'pow.c', 'pow_trunc.c', 'power_sums.c', 'power_sums_to_poly.c', 'powers_clear.c', 'powers_precompute.c', 'primitive_part.c', 'randtest.c', 'realloc.c', 'rem.c', 'rem_powers_precomp.c', 'rescale.c', 'resultant.c', 'resultant_modular_div.c', 'reverse.c', 'revert_series.c', 'revert_series_lagrange.c', 'revert_series_lagrange_fast.c', 'revert_series_newton.c', 'scalar_div_fmpq.c', 'scalar_div_fmpz.c', 'scalar_div_mpq.c', 'scalar_div_mpz.c', 'scalar_div_si.c', 'scalar_div_ui.c', 'scalar_mul_fmpq.c', 'scalar_mul_fmpz.c', 'scalar_mul_mpq.c', 'scalar_mul_mpz.c', 'scalar_mul_si.c', 'scalar_mul_ui.c', 'set.c', 'set_array_mpq.c', 'set_coeff_fmpq.c', 'set_coeff_fmpz.c', 'set_coeff_mpq.c', 'set_coeff_mpz.c', 'set_coeff_si.c', 'set_coeff_ui.c', 'set_fmpq.c', 'set_fmpz.c', 'set_fmpz_poly.c', 'set_length.c', 'set_mpq.c', 'set_mpz.c', 'set_nmod_poly.c', 'set_si.c', 'set_str.c', 'set_trunc.c', 'set_ui.c', 'shift_left.c', 'shift_right.c', 'sin_cos_series.c', 'sin_series.c', 'sinh_series.c', 'sqrt_series.c', 'sub.c', 'sub_series.c', 'swap.c', 'tan_series.c', 'tanh_series.c', 'xgcd.c', 'zero.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpq_poly
else
  src_fmpq_poly += generated_headers
  fmpq_poly = static_library(
    'fmpq_poly',
    src_fmpq_poly,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpq_poly
endif
