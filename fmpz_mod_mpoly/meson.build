
src_fmpz_mod_mpoly = files(['add.c', 'add_fmpz.c', 'clear.c', 'cmp.c', 'combine_like_terms.c', 'compose_fmpz_mod_mpoly.c', 'compose_fmpz_mod_mpoly_geobucket.c', 'compose_mat.c', 'content_vars.c', 'ctx_clear.c', 'ctx_init.c', 'ctx_init_rand.c', 'deflate.c', 'deflation.c', 'derivative.c', 'div.c', 'div_monagan_pearce.c', 'divides.c', 'divides_dense.c', 'divides_monagan_pearce.c', 'divrem.c', 'divrem_ideal.c', 'divrem_ideal_monagan_pearce.c', 'divrem_monagan_pearce.c', 'equal.c', 'equal_fmpz.c', 'evaluate_all_fmpz.c', 'evaluate_one.c', 'fit_length.c', 'fit_length_fit_bits.c', 'fit_length_reset_bits.c', 'fprint_pretty.c', 'gcd.c', 'gcd_brown.c', 'gcd_cofactors.c', 'gcd_hensel.c', 'gcd_subresultant.c', 'gcd_zippel.c', 'gcd_zippel2.c', 'gen.c', 'geobuckets.c', 'get_coeff_fmpz_fmpz.c', 'get_coeff_fmpz_monomial.c', 'get_coeff_fmpz_ui.c', 'get_coeff_vars_ui.c', 'get_fmpz.c', 'get_set_is_fmpz_mod_poly.c', 'get_set_nmod_mpoly.c', 'get_str_pretty.c', 'get_term.c', 'get_term_coeff_fmpz.c', 'get_term_exp_fmpz.c', 'get_term_exp_si.c', 'get_term_exp_ui.c', 'get_term_monomial.c', 'get_term_var_exp_si.c', 'get_term_var_exp_ui.c', 'inflate.c', 'init.c', 'is_canonical.c', 'is_fmpz.c', 'lead_coeff_vars.c', 'make_monic.c', 'mul.c', 'mul_dense.c', 'mul_johnson.c', 'neg.c', 'pow_fmpz.c', 'pow_rmul.c', 'pow_ui.c', 'push_term_fmpz_fmpz.c', 'push_term_fmpz_ui.c', 'quadratic_root.c', 'randtest_bits.c', 'randtest_bound.c', 'randtest_bounds.c', 'repack_bits.c', 'resize.c', 'scalar_addmul_fmpz.c', 'scalar_mul_fmpz.c', 'set.c', 'set_coeff_fmpz_fmpz.c', 'set_coeff_fmpz_monomial.c', 'set_coeff_fmpz_ui.c', 'set_fmpz.c', 'set_str_pretty.c', 'set_term_coeff_fmpz.c', 'set_term_exp_fmpz.c', 'set_term_exp_ui.c', 'sort_terms.c', 'sqrt_heap.c', 'sub.c', 'sub_fmpz.c', 'term_content.c', 'to_from_nmod_poly.c', 'univar.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz_mod_mpoly
else
  src_fmpz_mod_mpoly += generated_headers
  fmpz_mod_mpoly = static_library(
    'fmpz_mod_mpoly',
    src_fmpz_mod_mpoly,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz_mod_mpoly
endif
