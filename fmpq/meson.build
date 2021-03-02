
src_fmpq = files(['add.c', 'add_fmpz.c', 'add_si.c', 'add_small.c', 'add_ui.c', 'addmul.c', 'ball.c', 'canonicalise.c', 'cfrac_bound.c', 'clear_readonly.c', 'cmp.c', 'cmp_fmpz.c', 'cmp_si.c', 'cmp_ui.c', 'dedekind_sum.c', 'dedekind_sum_naive.c', 'div.c', 'div_2exp.c', 'div_fmpz.c', 'farey_neighbors.c', 'fmpz_vector.c', 'fprint.c', 'gcd_cofactors.c', 'get_cfrac.c', 'get_cfrac_helpers.c', 'get_d.c', 'get_mpfr.c', 'get_mpz_frac.c', 'get_str.c', 'harmonic_ui.c', 'height.c', 'height_bits.c', 'init_set_mpz_frac_readonly.c', 'init_set_readonly.c', 'inlines.c', 'inv.c', 'is_canonical.c', 'mat22.c', 'mod_fmpz.c', 'mpq_clear_readonly.c', 'mpq_init_set_readonly.c', 'mul.c', 'mul_2exp.c', 'mul_fmpz.c', 'mul_si.c', 'mul_small.c', 'mul_ui.c', 'next_calkin_wilf.c', 'next_minimal.c', 'next_signed_calkin_wilf.c', 'next_signed_minimal.c', 'pow_fmpz.c', 'pow_si.c', 'randbits.c', 'randtest.c', 'reconstruct_fmpz.c', 'reconstruct_fmpz_2.c', 'reconstruct_fmpz_2_naive.c', 'set_cfrac.c', 'set_fmpz_frac.c', 'set_si.c', 'set_str.c', 'set_ui.c', 'simplest_between.c', 'sub.c', 'sub_fmpz.c', 'sub_si.c', 'sub_ui.c', 'submul.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpq
else
  src_fmpq += generated_headers
  fmpq = static_library(
    'fmpq',
    src_fmpq,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpq
endif
