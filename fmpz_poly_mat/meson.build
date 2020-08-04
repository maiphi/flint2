
src_fmpz_poly_mat = files(['add.c', 'clear.c', 'concat_horizontal.c', 'concat_vertical.c', 'det.c', 'det_fflu.c', 'det_interpolate.c', 'equal.c', 'evaluate_fmpz.c', 'fflu.c', 'find_pivot_any.c', 'find_pivot_partial.c', 'init.c', 'init_set.c', 'inlines.c', 'inv.c', 'is_one.c', 'is_zero.c', 'max_bits.c', 'max_length.c', 'mul.c', 'mul_KS.c', 'mul_classical.c', 'mullow.c', 'neg.c', 'nullspace.c', 'one.c', 'pow.c', 'pow_trunc.c', 'print.c', 'prod.c', 'randtest.c', 'randtest_sparse.c', 'randtest_unsigned.c', 'rank.c', 'rref.c', 'scalar_mul_fmpz.c', 'scalar_mul_fmpz_poly.c', 'set.c', 'solve.c', 'solve_fflu.c', 'solve_fflu_precomp.c', 'sqr.c', 'sqr_KS.c', 'sqr_classical.c', 'sqrlow.c', 'sub.c', 'swap.c', 'trace.c', 'transpose.c', 'truncate.c', 'window_clear.c', 'window_init.c', 'zero.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz_poly_mat
else
  src_fmpz_poly_mat += generated_headers
  fmpz_poly_mat = static_library(
    'fmpz_poly_mat',
    src_fmpz_poly_mat,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz_poly_mat
endif
