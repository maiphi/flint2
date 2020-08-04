
src_fq_nmod_mpoly = files(['add.c', 'add_fq_nmod.c', 'combine_like_terms.c', 'compose_fq_nmod_mpoly.c', 'compose_fq_nmod_mpoly_gen.c', 'compose_fq_nmod_mpoly_geobucket.c', 'compose_fq_nmod_mpoly_horner.c', 'compose_fq_nmod_poly.c', 'compose_mat.c', 'ctx_change_modulus.c', 'ctx_clear.c', 'ctx_init.c', 'ctx_init_rand.c', 'deflate.c', 'deflation.c', 'derivative.c', 'div.c', 'divides.c', 'divides_monagan_pearce.c', 'divrem.c', 'divrem_ideal.c', 'equal.c', 'equal_fq_nmod.c', 'evaluate_all.c', 'evaluate_one.c', 'fit_length.c', 'fprint_pretty.c', 'fq_nmod_embed.c', 'gcd.c', 'gcd_brown.c', 'gcd_cofactors.c', 'gen.c', 'geobuckets.c', 'get_coeff_fq_nmod_fmpz.c', 'get_coeff_fq_nmod_monomial.c', 'get_coeff_fq_nmod_ui.c', 'get_fq_nmod.c', 'get_term.c', 'get_term_coeff_fq_nmod.c', 'get_term_exp_fmpz.c', 'get_term_exp_si.c', 'get_term_exp_ui.c', 'get_term_monomial.c', 'get_term_var_exp_si.c', 'get_term_var_exp_ui.c', 'inflate.c', 'init.c', 'inlines.c', 'is_canonical.c', 'is_fq_nmod.c', 'is_gen.c', 'is_one.c', 'make_monic.c', 'mpolyd.c', 'mpolyn.c', 'mpolyn_gcd_brown.c', 'mpolyu.c', 'mpolyu_divides.c', 'mpolyun.c', 'mul.c', 'mul_johnson.c', 'neg.c', 'one.c', 'pow_fmpz.c', 'pow_rmul.c', 'pow_ui.c', 'push_term_fq_nmod_fmpz.c', 'push_term_fq_nmod_ui.c', 'randtest_bits.c', 'randtest_bound.c', 'randtest_bounds.c', 'realloc.c', 'repack_bits.c', 'reverse.c', 'scalar_mul_fq_nmod.c', 'set.c', 'set_coeff_fq_nmod_fmpz.c', 'set_coeff_fq_nmod_monomial.c', 'set_coeff_fq_nmod_ui.c', 'set_fq_nmod.c', 'set_fq_nmod_gen.c', 'set_str_pretty.c', 'set_term_coeff_fq_nmod.c', 'set_term_exp_fmpz.c', 'set_term_exp_ui.c', 'set_ui.c', 'setform.c', 'sort_terms.c', 'sub.c', 'sub_fq_nmod.c', 'to_from_fq_nmod_poly.c', 'univar.c', 'clear.c', 'cmp.c', 'div_monagan_pearce.c', 'divrem_ideal_monagan_pearce.c', 'divrem_monagan_pearce.c', 'gcd_zippel.c', 'get_coeff_vars_ui.c', 'get_str_pretty.c', 'interp.c', 'mpolyu_gcdp_zippel.c', 'resize.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fq_nmod_mpoly
else
  src_fq_nmod_mpoly += generated_headers
  fq_nmod_mpoly = static_library(
    'fq_nmod_mpoly',
    src_fq_nmod_mpoly,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fq_nmod_mpoly
endif
