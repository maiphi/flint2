
src_fmpq_mpoly = ['add.c', 'add_fmpq.c', 'cmp.c', 'compose_fmpq_mpoly.c', 'compose_fmpq_mpoly_gen.c', 'compose_fmpq_poly.c', 'derivative.c', 'div.c', 'divides.c', 'divrem.c', 'divrem_ideal.c', 'equal_fmpq.c', 'equal_fmpz.c', 'evaluate_all.c', 'evaluate_one.c', 'fprint_pretty.c', 'gcd.c', 'gcd_cofactors.c', 'geobuckets.c', 'get_coeff_fmpq_fmpz.c', 'get_coeff_fmpq_monomial.c', 'get_coeff_fmpq_ui.c', 'get_coeff_vars_ui.c', 'get_fmpq.c', 'get_str_pretty.c', 'get_term.c', 'get_term_coeff_fmpq.c', 'get_term_exp_fmpz.c', 'get_term_exp_si.c', 'get_term_exp_ui.c', 'get_term_monomial.c', 'get_term_var_exp_si.c', 'get_term_var_exp_ui.c', 'inflate.c', 'inlines.c', 'integral.c', 'is_canonical.c', 'make_monic.c', 'mul.c', 'pow_fmpz.c', 'pow_ui.c', 'push_term_fmpq_fmpz.c', 'push_term_fmpq_ui.c', 'reduce.c', 'repack_bits.c', 'rescale.c', 'scalar_div_fmpq.c', 'scalar_div_fmpz.c', 'scalar_mul_fmpq.c', 'scalar_mul_fmpz.c', 'set_coeff_fmpq_fmpz.c', 'set_coeff_fmpq_monomial.c', 'set_coeff_fmpq_ui.c', 'set_fmpq.c', 'set_fmpz.c', 'set_str_pretty.c', 'set_term_coeff_fmpq.c', 'sub.c', 'sub_fmpq.c', 'term_content.c', 'univar.c']

src_fmpq_mpoly += generated_headers

headers_fmpq_mpoly = files([])

headers += headers_fmpq_mpoly

fmpq_mpoly = static_library(
  'fmpq_mpoly',
  src_fmpq_mpoly,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
