
src_nmod_mat = ['add.c', 'addmul.c', 'charpoly_danilevsky.c', 'clear.c', 'concat_horizontal.c', 'concat_vertical.c', 'det.c', 'equal.c', 'howell_form.c', 'init.c', 'init_set.c', 'inlines.c', 'inv.c', 'is_zero.c', 'lu.c', 'lu_classical.c', 'lu_recursive.c', 'minpoly.c', 'mul.c', 'mul_classical.c', 'mul_classical_threaded.c', 'mul_strassen.c', 'neg.c', 'nullspace.c', 'one.c', 'pow.c', 'print_pretty.c', 'randfull.c', 'randops.c', 'randpermdiag.c', 'randrank.c', 'randtest.c', 'randtril.c', 'randtriu.c', 'rank.c', 'reduce_row.c', 'rref.c', 'scalar_mul.c', 'scalar_mul_add.c', 'set.c', 'similarity.c', 'solve.c', 'solve_tril.c', 'solve_tril_classical.c', 'solve_tril_recursive.c', 'solve_triu.c', 'solve_triu_classical.c', 'solve_triu_recursive.c', 'solve_vec.c', 'strong_echelon_form.c', 'sub.c', 'submul.c', 'swap.c', 'trace.c', 'transpose.c', 'window_clear.c', 'window_init.c', 'zero.c']

src_nmod_mat += generated_headers

headers_nmod_mat = files([])

headers += headers_nmod_mat

nmod_mat = static_library(
  'nmod_mat',
  src_nmod_mat,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
