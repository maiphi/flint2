
src_fmpz_mpoly = files(['add.c', 'add_fmpz.c', 'clear.c', 'combine_like_terms.c', 'compose_fmpz_mpoly.c', 'compose_fmpz_mpoly_gen.c', 'compose_fmpz_mpoly_geobucket.c', 'compose_fmpz_mpoly_horner.c', 'compose_fmpz_poly.c', 'compose_mat.c', 'ctx_clear.c', 'ctx_init.c', 'ctx_init_rand.c', 'deflate.c', 'deflation.c', 'derivative.c', 'div.c', 'divides_array.c', 'divides_monagan_pearce.c', 'divrem.c', 'divrem_array.c', 'divrem_ideal.c', 'equal.c', 'equal_fmpz.c', 'equal_si.c', 'equal_ui.c', 'evaluate_all.c', 'evaluate_one.c', 'fit_length.c', 'fprint_pretty.c', 'gen.c', 'geobuckets.c', 'get_coeff_fmpz_fmpz.c', 'get_coeff_fmpz_monomial.c', 'get_coeff_fmpz_ui.c', 'get_coeff_si_fmpz.c', 'get_coeff_si_ui.c', 'get_coeff_ui_fmpz.c', 'get_coeff_ui_ui.c', 'get_fmpz.c', 'get_term.c', 'get_term_coeff_fmpz.c', 'get_term_exp_fmpz.c', 'get_term_exp_si.c', 'get_term_exp_ui.c', 'get_term_monomial.c', 'get_term_var_exp_si.c', 'get_term_var_exp_ui.c', 'inflate.c', 'init.c', 'inlines.c', 'integral.c', 'interp.c', 'is_canonical.c', 'is_fmpz.c', 'is_gen.c', 'mpolyd.c', 'mpolyu_divides.c', 'mul_array.c', 'mul_dense.c', 'mul_johnson.c', 'neg.c', 'parse_pretty.c', 'pow_fmpz.c', 'pow_fps.c', 'pow_ui.c', 'push_term_fmpz_fmpz.c', 'push_term_fmpz_ui.c', 'quasidiv.c', 'quasidivrem.c', 'quasidivrem_ideal.c', 'randtest_bits.c', 'randtest_bound.c', 'randtest_bounds.c', 'realloc.c', 'repack_bits.c', 'reverse.c', 'scalar_divexact_fmpz.c', 'scalar_divides_fmpz.c', 'scalar_mul_fmpz.c', 'select_exps.c', 'set.c', 'set_coeff_fmpz_fmpz.c', 'set_coeff_fmpz_monomial.c', 'set_coeff_fmpz_ui.c', 'set_coeff_si_fmpz.c', 'set_coeff_si_ui.c', 'set_coeff_ui_fmpz.c', 'set_coeff_ui_ui.c', 'set_fmpz.c', 'set_si.c', 'set_term_coeff_fmpz.c', 'set_term_exp_fmpz.c', 'set_term_exp_ui.c', 'set_ui.c', 'sort_terms.c', 'sub.c', 'sub_fmpz.c', 'term_content.c', 'to_from_fmpz_poly.c', 'univar.c', 'cmp.c', 'div_monagan_pearce.c', 'divides.c', 'divides_heap_threaded.c', 'divrem_ideal_monagan_pearce.c', 'divrem_monagan_pearce.c', 'gcd.c', 'gcd_berlekamp_massey.c', 'gcd_berlekamp_massey_threaded.c', 'gcd_brown.c', 'gcd_brown_threaded.c', 'gcd_cofactors.c', 'gcd_zippel.c', 'get_coeff_vars_ui.c', 'get_str_pretty.c', 'mpolyu.c', 'mpolyu_divides_threaded.c', 'mul.c', 'mul_array_threaded.c', 'mul_heap_threaded.c', 'quasidiv_heap.c', 'quasidivrem_heap.c', 'quasidivrem_ideal_heap.c', 'resize.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz_mpoly
else
  src_fmpz_mpoly += generated_headers
  fmpz_mpoly = static_library(
    'fmpz_mpoly',
    src_fmpz_mpoly,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz_mpoly
endif
