
src_fq_mat_templates = ['add.c', 'charpoly_danilevsky.c', 'clear.c', 'concat_horizontal.c', 'concat_vertical.c', 'equal.c', 'fprint.c', 'init.c', 'init_set.c', 'inv.c', 'is_zero.c', 'lu.c', 'lu_classical.c', 'lu_recursive.c', 'minpoly.c', 'mul.c', 'mul_KS.c', 'mul_classical.c', 'neg.c', 'nullspace.c', 'randops.c', 'randpermdiag.c', 'randrank.c', 'randtest.c', 'randtril.c', 'randtriu.c', 'rank.c', 'reduce_row.c', 'rref.c', 'set.c', 'similarity.c', 'solve.c', 'solve_tril.c', 'solve_tril_classical.c', 'solve_tril_recursive.c', 'solve_triu.c', 'solve_triu_classical.c', 'solve_triu_recursive.c', 'sub.c', 'submul.c', 'swap.c', 'window_clear.c', 'window_init.c', 'zero.c']

src_fq_mat_templates += generated_headers

headers_fq_mat_templates = files([])

headers += headers_fq_mat_templates

fq_mat_templates = static_library(
  'fq_mat_templates',
  src_fq_mat_templates,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
