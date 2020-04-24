
src_fq_nmod_mpoly = ['add.c', 'add_fq_nmod.c', 'clear.c', 'cmp.c', 'combine_like_terms.c', 'compose_fq_nmod_mpoly.c', 'compose_fq_nmod_mpoly_gen.c', 'compose_fq_nmod_mpoly_geobucket.c', 'compose_fq_nmod_mpoly_horner.c', 'compose_fq_nmod_poly.c', 'compose_mat.c', 'ctx_change_modulus.c', 'ctx_clear.c', 'ctx_init.c', 'ctx_init_rand.c', 'deflate.c', 'deflation.c', 'derivative.c', 'div.c', 'div_monagan_pearce.c', 'divides.c', 'divides_monagan_pearce.c', 'divrem.c', 'divrem_ideal.c', 'divrem_ideal_monagan_pearce.c', 'divrem_monagan_pearce.c', 'equal.c', 'equal_fq_nmod.c', 'evaluate_all.c', 'evaluate_one.c', 'fit_length.c', 'fprint_pretty.c', 'fq_nmod_embed.c', 'gcd.c', 'gcd_brown.c', 'gcd_cofactors.c', 'gcd_zippel.c', 'gen.c', 'geobuckets.c', 'get_coeff_fq_nmod_fmpz.c', 'get_coeff_fq_nmod_monomial.c', 'get_coeff_fq_nmod_ui.c', 'get_coeff_vars_ui.c', 'get_fq_nmod.c', 'get_str_pretty.c', 'get_term.c', 'get_term_coeff_fq_nmod.c', 'get_term_exp_fmpz.c', 'get_term_exp_si.c', 'get_term_exp_ui.c', 'get_term_monomial.c', 'get_term_var_exp_si.c', 'get_term_var_exp_ui.c', 'inflate.c', 'init.c', 'inlines.c', 'interp.c', 'is_canonical.c', 'is_fq_nmod.c', 'is_gen.c', 'is_one.c', 'make_monic.c', 'mpolyd.c', 'mpolyn.c', 'mpolyn_gcd_brown.c', 'mpolyu.c', 'mpolyu_divides.c', 'mpolyu_gcdp_zippel.c', 'mpolyun.c', 'mul.c', 'mul_johnson.c', 'neg.c', 'one.c', 'pow_fmpz.c', 'pow_rmul.c', 'pow_ui.c', 'push_term_fq_nmod_fmpz.c', 'push_term_fq_nmod_ui.c', 'randtest_bits.c', 'randtest_bound.c', 'randtest_bounds.c', 'realloc.c', 'repack_bits.c', 'resize.c', 'reverse.c', 'scalar_mul_fq_nmod.c', 'set.c', 'set_coeff_fq_nmod_fmpz.c', 'set_coeff_fq_nmod_monomial.c', 'set_coeff_fq_nmod_ui.c', 'set_fq_nmod.c', 'set_fq_nmod_gen.c', 'set_str_pretty.c', 'set_term_coeff_fq_nmod.c', 'set_term_exp_fmpz.c', 'set_term_exp_ui.c', 'set_ui.c', 'setform.c', 'sort_terms.c', 'sub.c', 'sub_fq_nmod.c', 'to_from_fq_nmod_poly.c', 'univar.c']

src_fq_nmod_mpoly += generated_headers

headers_fq_nmod_mpoly = files([])

headers += headers_fq_nmod_mpoly

fq_nmod_mpoly = static_library(
  'fq_nmod_mpoly',
  src_fq_nmod_mpoly,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
