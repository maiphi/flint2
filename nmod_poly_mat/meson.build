
src_nmod_poly_mat = files(['add.c', 'concat_horizontal.c', 'concat_vertical.c', 'det.c', 'det_fflu.c', 'det_interpolate.c', 'equal.c', 'evaluate_nmod.c', 'fflu.c', 'find_pivot_any.c', 'find_pivot_partial.c', 'init_set.c', 'inlines.c', 'inv.c', 'is_one.c', 'is_zero.c', 'max_length.c', 'mul.c', 'mul_KS.c', 'mul_classical.c', 'mul_interpolate.c', 'neg.c', 'nullspace.c', 'one.c', 'pow.c', 'print.c', 'randtest.c', 'randtest_sparse.c', 'rank.c', 'rref.c', 'scalar_mul_nmod.c', 'scalar_mul_nmod_poly.c', 'set.c', 'solve.c', 'solve_fflu_precomp.c', 'sqr.c', 'sqr_KS.c', 'sqr_classical.c', 'sqr_interpolate.c', 'sub.c', 'swap.c', 'trace.c', 'zero.c', 'clear.c', 'init.c', 'solve_fflu.c', 'window_clear.c', 'window_init.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_nmod_poly_mat
else
  src_nmod_poly_mat += generated_headers
  nmod_poly_mat = static_library(
    'nmod_poly_mat',
    src_nmod_poly_mat,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += nmod_poly_mat
endif
