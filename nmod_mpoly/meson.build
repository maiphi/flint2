
src_nmod_mpoly = ['add.c', 'add_ui.c', 'clear.c', 'cmp.c', 'combine_like_terms.c', 'compose_mat.c', 'compose_nmod_mpoly.c', 'compose_nmod_mpoly_gen.c', 'compose_nmod_mpoly_geobucket.c', 'compose_nmod_mpoly_horner.c', 'compose_nmod_poly.c', 'ctx_clear.c', 'ctx_init.c', 'ctx_init_rand.c', 'deflate.c', 'deflation.c', 'derivative.c', 'div.c', 'div_monagan_pearce.c', 'divides.c', 'divides_dense.c', 'divides_heap_threaded.c', 'divides_monagan_pearce.c', 'divrem.c', 'divrem_ideal.c', 'divrem_ideal_monagan_pearce.c', 'divrem_monagan_pearce.c', 'equal.c', 'equal_ui.c', 'evaluate_all.c', 'evaluate_one.c', 'fit_length.c', 'fprint_pretty.c', 'gcd.c', 'gcd_brown.c', 'gcd_brown_threaded.c', 'gcd_cofactors.c', 'gcd_zippel.c', 'gen.c', 'geobuckets.c', 'get_coeff_ui_fmpz.c', 'get_coeff_ui_monomial.c', 'get_coeff_ui_ui.c', 'get_coeff_vars_ui.c', 'get_str_pretty.c', 'get_term.c', 'get_term_coeff_ui.c', 'get_term_exp_fmpz.c', 'get_term_exp_si.c', 'get_term_exp_ui.c', 'get_term_monomial.c', 'get_term_ui_fmpz.c', 'get_term_ui_ui.c', 'get_term_var_exp_si.c', 'get_term_var_exp_ui.c', 'get_ui.c', 'inflate.c', 'init.c', 'inlines.c', 'interp.c', 'is_canonical.c', 'is_gen.c', 'is_ui.c', 'make_monic.c', 'mpolyd.c', 'mpolyn.c', 'mpolyn_divides_threaded.c', 'mpolyn_gcd_brown.c', 'mpolyu.c', 'mpolyu_divides.c', 'mpolyu_gcdp_zippel.c', 'mpolyun.c', 'mpolyun_divides.c', 'mul.c', 'mul_array.c', 'mul_array_threaded.c', 'mul_dense.c', 'mul_heap_threaded.c', 'mul_johnson.c', 'neg.c', 'pow_fmpz.c', 'pow_rmul.c', 'pow_ui.c', 'push_term_ui_fmpz.c', 'push_term_ui_ui.c', 'randtest_bits.c', 'randtest_bound.c', 'randtest_bounds.c', 'realloc.c', 'repack_bits.c', 'resize.c', 'reverse.c', 'scalar_mul_ui.c', 'set.c', 'set_coeff_ui_fmpz.c', 'set_coeff_ui_monomial.c', 'set_coeff_ui_ui.c', 'set_str_pretty.c', 'set_term_coeff_ui.c', 'set_term_exp_fmpz.c', 'set_term_exp_ui.c', 'set_term_ui.c', 'set_term_ui_fmpz.c', 'set_term_ui_ui.c', 'set_ui.c', 'setform.c', 'sort_terms.c', 'stack.c', 'sub.c', 'sub_ui.c', 'term_content.c', 'to_from_nmod_poly.c', 'univar.c']

src_nmod_mpoly += generated_headers

headers_nmod_mpoly = files([])

headers += headers_nmod_mpoly

nmod_mpoly = static_library(
  'nmod_mpoly',
  src_nmod_mpoly,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
