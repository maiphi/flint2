
src_fmpz_mod_poly = ['add.c', 'add_series.c', 'berlekamp_massey.c', 'clear.c', 'compose_divconquer.c', 'compose_horner.c', 'compose_mod.c', 'compose_mod_brent_kung.c', 'compose_mod_brent_kung_precomp_preinv.c', 'compose_mod_brent_kung_preinv.c', 'compose_mod_brent_kung_vec_preinv.c', 'compose_mod_brent_kung_vec_preinv_threaded.c', 'compose_mod_horner.c', 'derivative.c', 'discriminant.c', 'div_basecase.c', 'div_newton_n_preinv.c', 'div_series.c', 'divrem_basecase.c', 'divrem_divconquer.c', 'divrem_divconquer_recursive.c', 'divrem_f.c', 'divrem_newton_n_preinv.c', 'evaluate_fmpz.c', 'evaluate_fmpz_vec.c', 'evaluate_fmpz_vec_fast.c', 'evaluate_fmpz_vec_iter.c', 'find_distinct_nonzero_roots.c', 'fit_length.c', 'fprint.c', 'fread.c', 'frobenius_power.c', 'frobenius_powers_2exp_clear.c', 'frobenius_powers_2exp_precomp.c', 'frobenius_powers_clear.c', 'frobenius_powers_precomp.c', 'gcd_euclidean.c', 'gcd_euclidean_f.c', 'gcd_hgcd.c', 'gcdinv.c', 'gcdinv_euclidean.c', 'gcdinv_euclidean_f.c', 'gcdinv_f.c', 'get_fmpz_poly.c', 'hgcd.c', 'init.c', 'inlines.c', 'inv_series_newton.c', 'inv_series_newton_f.c', 'invmod.c', 'invmod_f.c', 'make_monic.c', 'make_monic_f.c', 'minpoly_bm.c', 'minpoly_hgcd.c', 'mul.c', 'mullow.c', 'mulmod.c', 'mulmod_preinv.c', 'neg.c', 'normalise.c', 'pow.c', 'pow_trunc.c', 'pow_trunc_binexp.c', 'powers_mod_bsgs_threaded.c', 'powers_mod_naive.c', 'powmod_fmpz_binexp.c', 'powmod_fmpz_binexp_preinv.c', 'powmod_ui_binexp.c', 'powmod_ui_binexp_preinv.c', 'powmod_x_fmpz_preinv.c', 'product_roots_fmpz_vec.c', 'radix.c', 'randtest.c', 'randtest_monic_primitive.c', 'realloc.c', 'rem_basecase.c', 'remove.c', 'resultant_euclidean.c', 'resultant_hgcd.c', 'reverse.c', 'scalar_div_fmpz.c', 'scalar_mul_fmpz.c', 'scalar_mul_ui.c', 'set.c', 'set_coeff_fmpz.c', 'set_coeff_si.c', 'set_coeff_ui.c', 'set_fmpz.c', 'set_fmpz_poly.c', 'set_trunc.c', 'shift_left.c', 'shift_right.c', 'sqr.c', 'sub.c', 'sub_series.c', 'swap.c', 'tree.c', 'xgcd_euclidean.c', 'xgcd_euclidean_f.c', 'xgcd_hgcd.c', 'zero_coeffs.c']

src_fmpz_mod_poly += generated_headers

headers_fmpz_mod_poly = files([])

headers += headers_fmpz_mod_poly

fmpz_mod_poly = static_library(
  'fmpz_mod_poly',
  src_fmpz_mod_poly,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
