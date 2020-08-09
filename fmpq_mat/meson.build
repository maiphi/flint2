
src_fmpq_mat = files(['add.c', 'charpoly.c', 'clear.c', 'concat_horizontal.c', 'concat_vertical.c', 'det.c', 'equal.c', 'get_fmpz_mat.c', 'get_fmpz_mat_colwise.c', 'get_fmpz_mat_entrywise.c', 'get_fmpz_mat_matwise.c', 'get_fmpz_mat_mod_fmpz.c', 'get_fmpz_mat_rowwise.c', 'gso.c', 'hilbert_matrix.c', 'init.c', 'init_set.c', 'inlines.c', 'inv.c', 'is_integral.c', 'is_one.c', 'is_zero.c', 'kronecker_product.c', 'minpoly.c', 'mul.c', 'mul_cleared.c', 'mul_direct.c', 'mul_fmpz_mat.c', 'mul_r_fmpz_mat.c', 'neg.c', 'one.c', 'pivot.c', 'print.c', 'randbits.c', 'randtest.c', 'rref.c', 'rref_classical.c', 'rref_fraction_free.c', 'scalar_div_fmpz.c', 'scalar_mul_fmpq.c', 'scalar_mul_fmpz.c', 'set.c', 'set_fmpz_mat.c', 'set_fmpz_mat_div_fmpz.c', 'set_fmpz_mat_mod_fmpz.c', 'similarity.c', 'solve.c', 'solve_dixon.c', 'solve_fraction_free.c', 'solve_multi_mod.c', 'sub.c', 'swap.c', 'trace.c', 'transpose.c', 'window_clear.c', 'window_init.c', 'zero.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpq_mat
else
  src_fmpq_mat += generated_headers
  fmpq_mat = static_library(
    'fmpq_mat',
    src_fmpq_mat,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpq_mat
endif
