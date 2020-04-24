
src_fq_poly_templates = ['add.c', 'add_series.c', 'clear.c', 'compose.c', 'compose_divconquer.c', 'compose_horner.c', 'compose_mod.c', 'compose_mod_brent_kung.c', 'compose_mod_brent_kung_precomp_preinv.c', 'compose_mod_brent_kung_preinv.c', 'compose_mod_horner.c', 'compose_mod_horner_preinv.c', 'compose_mod_preinv.c', 'deflate.c', 'deflation.c', 'derivative.c', 'div_basecase.c', 'div_newton_n_preinv.c', 'div_series.c', 'divides.c', 'divrem_basecase.c', 'divrem_divconquer.c', 'divrem_divconquer_recursive.c', 'divrem_f.c', 'divrem_newton_n_preinv.c', 'equal.c', 'equal_trunc.c', 'evaluate_fq.c', 'evaluate_fq_vec.c', 'evaluate_fq_vec_fast.c', 'evaluate_fq_vec_iter.c', 'fit_length.c', 'fprint.c', 'fprint_pretty.c', 'gcd.c', 'gcd_euclidean.c', 'gcd_euclidean_f.c', 'gcd_hgcd.c', 'gen.c', 'get_coeff.c', 'get_str.c', 'get_str_pretty.c', 'hamming_weight.c', 'hgcd.c', 'inflate.c', 'init.c', 'inv_series_newton.c', 'make_monic.c', 'mul.c', 'mul_KS.c', 'mul_classical.c', 'mul_reorder.c', 'mulhigh.c', 'mulhigh_classical.c', 'mullow.c', 'mullow_KS.c', 'mullow_classical.c', 'mulmod.c', 'mulmod_preinv.c', 'neg.c', 'normalise.c', 'one.c', 'pow.c', 'powmod_fmpz_binexp.c', 'powmod_fmpz_binexp_preinv.c', 'powmod_fmpz_sliding_preinv.c', 'powmod_ui_binexp.c', 'powmod_ui_binexp_preinv.c', 'powmod_x_fmpz_preinv.c', 'randtest.c', 'randtest_irreducible.c', 'randtest_monic.c', 'realloc.c', 'remove.c', 'reverse.c', 'scalar_addmul_fq.c', 'scalar_div_fq.c', 'scalar_mul_fq.c', 'scalar_submul_fq.c', 'set.c', 'set_coeff.c', 'set_fmpz_mod_poly.c', 'set_fq.c', 'set_nmod_poly.c', 'set_trunc.c', 'shift_left.c', 'shift_right.c', 'sqr.c', 'sqr_KS.c', 'sqr_classical.c', 'sqr_reorder.c', 'sub.c', 'sub_series.c', 'swap.c', 'tree.c', 'truncate.c', 'xgcd_euclidean.c', 'xgcd_euclidean_f.c']

src_fq_poly_templates += generated_headers

headers_fq_poly_templates = files([])

headers += headers_fq_poly_templates

fq_poly_templates = static_library(
  'fq_poly_templates',
  src_fq_poly_templates,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
