
src_mpoly = files(['bidegree.c', 'bivar_cld_bounds.c', 'cmp_general.c', 'compose_mat.c', 'compression.c', 'ctx_clear.c', 'ctx_init.c', 'ctx_init_rand.c', 'degree.c', 'degrees.c', 'degrees_fit_si.c', 'exp_bits_required.c', 'fill_marks.c', 'gcd_info.c', 'gen_bits_required.c', 'gen_fields.c', 'gen_monomial_offset_shift.c', 'gen_shift_left_right.c', 'get_cmpmask.c', 'get_monomial.c', 'get_monomial_var.c', 'inlines.c', 'is_gen.c', 'is_proved_not_square.c', 'main_variable_split.c', 'max_fields.c', 'min_fields.c', 'monomial_cofactors.c', 'monomial_exists.c', 'monomial_index.c', 'monomial_mul_fmpz.c', 'monomials_cmp.c', 'monomials_deflate.c', 'monomials_deflation.c', 'monomials_inflate.c', 'monomials_inorder_test.c', 'monomials_overflow_test.c', 'monomials_shift_right_ui.c', 'monomials_valid_test.c', 'pack_monomials_tight.c', 'pack_vec.c', 'parse_pretty.c', 'randbits_fmpz.c', 'rbtree.c', 'remove_var_powers.c', 'repack_monomials.c', 'reverse.c', 'search_monomials.c', 'set_monomial.c', 'term_exp_fits.c', 'test_irreducible.c', 'to_from_mpolyl.c', 'total_degree.c', 'unpack_monomials_tight.c', 'unpack_vec.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_mpoly
else
  src_mpoly += generated_headers
  mpoly = static_library(
    'mpoly',
    src_mpoly,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += mpoly
endif
